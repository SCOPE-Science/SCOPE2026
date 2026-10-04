
def ed_degree(ds):
    xs=[d-1 for d in ds]
    D=1
    for d in ds:
        D*=d
    T=sum(xs)
    h2=sum(xs[i]*xs[j] for i in range(len(xs)) for j in range(i,len(xs)))
    return D*(1+T+h2)

def balanced(c,S):
    k,r=divmod(S,c)
    assert k>=2
    return (k,)*(c-r)+(k+1,)*r

def extreme(c,S):
    return (2,)*(c-1)+(S-2*c+2,)

def balancing_neighbors(ds):
    ds=list(ds)
    out=[]
    n=len(ds)
    for i in range(n):
        for j in range(n):
            if ds[j]-ds[i]>=2:
                e=ds.copy()
                e[i]+=1
                e[j]-=1
                if min(e)>=2:
                    out.append(tuple(sorted(e)))
    return set(out)

def partitions_sum(c,S):
    def rec(k,rem,lo,pref):
        if k==1:
            if rem>=lo:
                yield tuple(pref+[rem])
            return
        for v in range(lo,rem//k+1):
            yield from rec(k-1,rem-v,v,pref+[v])
    yield from rec(c,S,2,[])

family_checks=0
move_checks=0
fixed_sum_checks=0
for c in range(2,7):
    for S in range(2*c,4*c+1):
        fam=list(partitions_sum(c,S))
        vals={ds:ed_degree(ds) for ds in fam}
        lo=min(vals.values())
        hi=max(vals.values())
        mins=[ds for ds,v in vals.items() if v==lo]
        maxs=[ds for ds,v in vals.items() if v==hi]
        assert mins==[extreme(c,S)], (c,S,mins,extreme(c,S))
        assert maxs==[balanced(c,S)], (c,S,maxs,balanced(c,S))
        for ds in fam:
            v=vals[ds]
            for nb in balancing_neighbors(ds):
                assert ed_degree(nb)>v, (ds,nb,v,ed_degree(nb))
                move_checks+=1
        family_checks+=len(fam)
        fixed_sum_checks+=1

assert family_checks==425
assert fixed_sum_checks==45
assert move_checks==933
assert ed_degree((2,2,8))==2432
assert ed_degree((3,4,5))==3900
assert ed_degree((4,4,4))==4096
print('VERIFY_OK', fixed_sum_checks, family_checks, move_checks)
