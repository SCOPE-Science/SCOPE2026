"""Independent semantic checker using finite Heyting implication on upsets."""
from itertools import product

def ordered_upsets(sizes):
    n=sum(sizes); offs=[]; k=0
    for a in sizes:
        offs.append(tuple(range(k,k+a)));k+=a
    upper=[]
    for i,lev in enumerate(offs):
        for x in lev:upper.append(frozenset((y for j in range(i+1) for y in (offs[j] if j<i else (x,)))))
    sets=[frozenset(u for u in range(n) if mask>>u&1) for mask in range(1<<n)]
    return upper,[s for s in sets if all(upper[x]<=s for x in s)]

def check(sizes):
    ups,opens=ordered_upsets(sizes);n=sum(sizes)
    def imp(a,b):return frozenset(x for x in range(n) if not(ups[x]&a-b))
    openset=set(opens)
    for f in product(range(n),repeat=n):
        pm=all({f[y] for y in ups[x]}==ups[f[x]] for x in range(n))
        image=lambda u:frozenset(x for x in range(n) if f[x] in u)
        alg=all(imp(image(u),image(v))==image(imp(u,v)) for u in opens for v in opens)
        alg &= all(image(u) in openset for u in opens)
        assert pm==alg,(sizes,f,pm,alg)
    print('ALGEBRA_OK',sizes,'maps',n**n,'upsets',len(opens))
if __name__=='__main__':
    for ss in [(2,2),(2,3),(3,2)]:check(ss)
