import itertools

def partitions(n,r,lo=1):
    if r==0:
        if n==0: yield ()
        return
    for x in range(lo,n+1):
        if n-x < x*(r-1): break
        for q in partitions(n-x,r-1,x):
            yield (x,)+q

def labels(parts):
    out=[]
    for i,a in enumerate(parts): out += [i]*a
    return out

def is_zero_forcing(mask,L):
    n=len(L)
    blue=mask
    while True:
        if blue == (1<<n)-1:
            return True
        forced=None
        for u in range(n):
            if not ((blue>>u)&1): continue
            whites=[v for v in range(n) if not ((blue>>v)&1) and L[v]!=L[u]]
            if len(whites)==1:
                forced=whites[0]
                break
        if forced is None:
            return False
        blue |= 1<<forced

def minimal_zero_forcing(mask,L):
    if not is_zero_forcing(mask,L): return False
    for v in range(len(L)):
        if (mask>>v)&1 and is_zero_forcing(mask & ~(1<<v), L):
            return False
    return True

def predicted_minimal(parts,L):
    n=sum(parts)
    # Complete graph.
    if all(a==1 for a in parts):
        return sorted(((1<<n)-1) ^ (1<<x) for x in range(n))
    singleton={i for i,a in enumerate(parts) if a==1}
    out=[]
    for x,y in itertools.combinations(range(n),2):
        if L[x]!=L[y] and not (L[x] in singleton and L[y] in singleton):
            out.append(((1<<n)-1) ^ (1<<x) ^ (1<<y))
    return sorted(out)

types=subsets=0
for n in range(2,11):
    for r in range(2,n+1):
        for parts in partitions(n,r):
            L=labels(parts)
            actual=[]
            for mask in range(1<<n):
                subsets += 1
                if minimal_zero_forcing(mask,L):
                    actual.append(mask)
            pred=predicted_minimal(parts,L)
            assert sorted(actual)==pred,(parts, actual, pred)
            sizes={m.bit_count() for m in actual}
            assert len(sizes)==1,(parts,sizes)
            z=min(m.bit_count() for m in actual)
            assert z==(n-1 if all(a==1 for a in parts) else n-2),(parts,z)
            # count formula and irrelevant vertices
            q=sum(a==1 for a in parts)
            if all(a==1 for a in parts):
                cnt=n
                irr=[]
            else:
                cnt=sum(parts[i]*parts[j] for i in range(r) for j in range(i+1,r))-q*(q-1)//2
                irr=[v for v in range(n) if all(not((m>>v)&1) for m in actual)]
                p=tuple(sorted(parts))
                if len(p)==2 and p[0]==1:
                    # the unique singleton is irrelevant
                    singleton_part=parts.index(1)
                    predicted_irr=[v for v,a in enumerate(L) if a==singleton_part]
                else:
                    predicted_irr=[]
                assert irr==predicted_irr,(parts,irr,predicted_irr)
            assert len(actual)==cnt,(parts,len(actual),cnt)
            types += 1

print("VERIFY_OK")
print("multipartite_types_checked =",types)
print("vertex_subsets_checked =",subsets)
print("orders = 2..10")
print("all minimal-zero-forcing-set classifications matched")
print("all well-forced decisions matched")
print("all count formulas and irrelevant-vertex classifications matched")
