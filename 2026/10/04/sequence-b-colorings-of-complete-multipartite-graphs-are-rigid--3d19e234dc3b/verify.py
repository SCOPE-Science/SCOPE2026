from itertools import product

def build_graph(parts):
    part_of=[]
    for i,n in enumerate(parts):
        part_of += [i]*n
    N=len(part_of)
    adj=[[False]*N for _ in range(N)]
    for u in range(N):
        for v in range(u+1,N):
            if part_of[u]!=part_of[v]:
                adj[u][v]=adj[v][u]=True
    return part_of,adj

def proper(col,adj):
    N=len(col)
    return all(not adj[u][v] or col[u]!=col[v] for u in range(N) for v in range(u+1,N))

def cdv_counts(col,adj,k):
    N=len(col)
    out=[0]*k
    for v in range(N):
        seen={col[v]}
        for u in range(N):
            if adj[v][u]: seen.add(col[u])
        if len(seen)==k:
            out[col[v]]+=1
    return out

def is_b(col,adj,k):
    return all(x>0 for x in cdv_counts(col,adj,k))

def part_monochromatic(col,part_of,r):
    vals=[]
    for p in range(r):
        cs={col[v] for v,q in enumerate(part_of) if q==p}
        vals.append(cs)
    return all(len(s)==1 for s in vals) and len({next(iter(s)) for s in vals})==r

def weak_desc_tuples(r,maxv):
    def rec(pref,last):
        if len(pref)==r:
            yield tuple(pref); return
        for x in range(last,0,-1):
            yield from rec(pref+[x],x)
    yield from rec([],maxv)

def formula_count(parts,S):
    ns=sorted(parts,reverse=True)
    ss=tuple(sorted(S,reverse=True))
    if len(ss)!=len(ns): return 0
    ans=1
    for i,s in enumerate(ss, start=1):
        c=sum(n>=s for n in ns)
        ans*=max(0,c-i+1)
    return ans

def brute_labeled_realizations(parts,S):
    r=len(parts); part_of,adj=build_graph(parts); N=len(part_of); k=r
    total=0
    for col in product(range(k), repeat=N):
        if set(col)!=set(range(k)) or not proper(col,adj):
            continue
        counts=cdv_counts(col,adj,k)
        if all(counts[i]>=S[i] for i in range(k)):
            total+=1
    return total

graphs=proper_count=b_count=seq_tests=0
for r in range(2,5):
    # sorted part sizes, total order <= 6
    for parts in product(range(1,4), repeat=r):
        if tuple(sorted(parts,reverse=True))!=parts or sum(parts)>6:
            continue
        graphs+=1
        part_of,adj=build_graph(parts); N=len(part_of)
        for k in range(1,N+1):
            for col in product(range(k), repeat=N):
                if set(col)!=set(range(k)) or not proper(col,adj):
                    continue
                proper_count+=1
                if is_b(col,adj,k):
                    b_count+=1
                    assert k==r, (parts,k,col)
                    assert part_monochromatic(col,part_of,r), (parts,k,col)
                    counts=sorted(cdv_counts(col,adj,k),reverse=True)
                    assert counts==sorted(parts,reverse=True), (parts,counts)
        maxv=max(parts)+1
        for S in weak_desc_tuples(r,maxv):
            seq_tests+=1
            brute=brute_labeled_realizations(parts,S)
            form=formula_count(parts,S)
            assert brute==form, (parts,S,brute,form)
            ns=sorted(parts,reverse=True)
            coord=all(S[i]<=ns[i] for i in range(r))
            assert (brute>0)==coord, (parts,S,brute,coord)
print(f"ALL CHECKS PASSED; graphs={graphs}; proper_colorings={proper_count}; b_colorings={b_count}; sequence_tests={seq_tests}")
