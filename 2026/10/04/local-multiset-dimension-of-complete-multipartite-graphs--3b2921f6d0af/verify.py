import itertools, math
def partitions(n,r,lo=1):
    if r==0:
        if n==0: yield ()
        return
    for x in range(lo,n+1):
        if n-x < x*(r-1): break
        for q in partitions(n-x,r-1,x): yield (x,)+q
def labels(parts):
    out=[]
    for i,a in enumerate(parts): out += [i]*a
    return out
def rep(v,mask,lab):
    vals=[]
    for w in range(len(lab)):
        if mask>>w & 1: vals.append(0 if v==w else (2 if lab[v]==lab[w] else 1))
    return tuple(sorted(vals))
def local_ok(mask,lab):
    n=len(lab)
    return all(rep(u,mask,lab)!=rep(v,mask,lab)
               for u in range(n) for v in range(u+1,n) if lab[u]!=lab[v])
def profile(mask,parts):
    lab=labels(parts); w=[0]*len(parts)
    for v,p in enumerate(lab):
        if mask>>v & 1: w[p]+=1
    return tuple(w)
def criterion(w):
    pos=[x for x in w if x>0]
    return len(pos)==len(set(pos)) and sum(x==0 for x in w)<=1
def finite_condition(parts):
    a=sorted(parts)
    return all(a[i]>=i for i in range(1,len(a)))
def dim_formula(parts):
    r=len(parts)
    return r*(r-1)//2 if finite_condition(parts) else None
def basis_count(parts):
    r=len(parts); total=0
    for perm in itertools.permutations(range(r)):
        ways=1
        for i,c in enumerate(perm):
            if c>parts[i]: ways=0; break
            ways*=math.comb(parts[i],c)
        total+=ways
    return total
types=subsets=finite_types=basis_checks=0
for N in range(2,10):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            lab=labels(parts); valid=[]; minsz=None
            for mask in range(1<<N):
                subsets+=1
                got=local_ok(mask,lab)
                assert got==criterion(profile(mask,parts))
                if got:
                    valid.append(mask)
                    s=mask.bit_count()
                    minsz=s if minsz is None else min(minsz,s)
            d=dim_formula(parts)
            assert minsz==d
            if d is not None:
                finite_types+=1
                assert sum(m.bit_count()==d for m in valid)==basis_count(parts)
                basis_checks+=1
            types+=1
print("VERIFY_OK")
print("multipartite_types_checked =",types)
print("vertex_subsets_checked =",subsets)
print("finite_types_checked =",finite_types)
print("basis_count_checks =",basis_checks)
print("orders = 2..9")
