"""Exact finite tests for the cyclic-round conflict distribution theorem.
Only stdlib. No external files or services. Tests are finite corroboration, not a proof.
"""
import itertools, math, random
from collections import Counter
from fractions import Fraction

R=random.Random(26022043)

def law(n,q,hist):
    ans=Counter()
    for shifts in itertools.product(range(n),repeat=q):
        z=sum(h[(shifts[b]-shifts[a])%n] for (a,b),h in hist.items())
        ans[z]+=1
    return ans

def mean_variance(dist,den):
    mean=sum(k*v for k,v in dist.items())*Fraction(1,den)
    var=sum((k-mean)**2*v for k,v in dist.items())*Fraction(1,den)
    return mean,var

def formulas(n,hist):
    em=Fraction(0); var=Fraction(0)
    for a in hist.values():
        sm=sum(a)
        em+=Fraction(sm,n)
        var+=Fraction(sum(x*x for x in a),n)-Fraction(sm*sm,n*n)
    return em,var

def connected_forest(edges,vertices):
    p=list(range(vertices))
    def root(x):
        while x!=p[x]: x=p[x]
        return x
    for u,v in edges:
        a,b=root(u),root(v)
        if a==b:return False
        p[a]=b
    return True

def minmax(n,E):
    q,r=divmod(E,n)
    vmin=Fraction(r*(n-r),n*n)
    vmax=Fraction(q*n*n+r*r,n)-Fraction(E*E,n*n)
    return vmin,vmax

tests=0
for n in range(2,5):
    for E in range(n*n+1):
        vals=[]
        for xs in itertools.product(range(n+1),repeat=n):
            if sum(xs)==E:
                x=Fraction(sum(v*v for v in xs),n)-Fraction(E*E,n*n)
                vals.append(x)
        assert vals
        assert min(vals)==minmax(n,E)[0]
        assert max(vals)==minmax(n,E)[1]
        tests+=1
for n in range(2,5):
    for q in range(2,5):
        all_edges=list(itertools.combinations(range(q),2))
        for rep in range(140):
            hist={e:[R.randint(0,n) for _ in range(n)] for e in all_edges if R.random()<.78}
            d=law(n,q,hist)
            ex,var=mean_variance(d,n**q)
            fex,fvar=formulas(n,hist)
            assert (ex,var)==(fex,fvar),(n,q,hist,ex,var,fex,fvar)
            if connected_forest(hist,q):
                prod={0:1}
                for h in hist.values():
                    nextd=Counter()
                    for s,c in prod.items():
                        for x in h: nextd[s+x]+=c
                    prod=nextd
                # one uniformly chosen difference per edge, n^(q-|E|) shift fibers
                assert d==Counter({z:v*n**(q-len(hist)) for z,v in prod.items()}),(n,q,hist,d,prod)
            tests+=1
# Pairwise independence of distinct block-pair differences, including cycles.
for n in range(2,6):
    q=4
    pairs=list(itertools.combinations(range(q),2))
    ss=list(itertools.product(range(n),repeat=q))
    for e,f in itertools.combinations(pairs,2):
        counts=Counter(((s[e[1]]-s[e[0]])%n,(s[f[1]]-s[f[0]])%n) for s in ss)
        assert all(counts[a,b]==n**(q-2) for a in range(n) for b in range(n))
        tests+=1
# Non-independence on one 3-cycle of rounds.
triangle={(0,1):[1,0],(1,2):[1,0],(0,2):[1,0]}
assert law(2,3,triangle)==Counter({1:6,3:2})
assert formulas(2,triangle)==(Fraction(3,2),Fraction(3,4))
tests+=1
print('VERIFICATION_OK',tests,'exact checks; triangle distribution',dict(law(2,3,triangle)))
