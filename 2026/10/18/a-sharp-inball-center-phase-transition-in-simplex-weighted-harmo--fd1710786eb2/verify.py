"""Standalone numerical/exact-combinatorial sanity checks for a simplex-weighted harmonic polytope.
Runs without internet and without any project-specific dependencies.
Analytic theorem and boundary proofs are in the accompanying mathematical note.
"""
import itertools
import math
from fractions import Fraction

def facets(n):
    for a in range(n):
        for b in range(n):
            if a+b==0 or a+b>n: continue
            if a+b==n and (a==0 or b==0): continue
            X = a*(n-a)+b*(n-b)
            yield a,b,X

def distance(n,lam,a,b,X):
    return (X/2 + lam*(1-(a+b)/n)) / math.sqrt(X/n)

def exact_slack(n,lam,a,b):
    s,t=n-a,n-b
    mu=Fraction(n+1,2)+lam/n
    return mu*(s+t)-Fraction(s*(s+1)+t*(t+1),2)-lam

def test():
    total=0
    for n in range(3,16):
        c=(math.sqrt(2)-1)/2
        star=n*(n-1)*c
        R=math.sqrt(n*(n-1)/2)
        typA={(n-1,0),(0,n-1)}
        typB={(1,n-1),(n-1,1)}
        for lam in [Fraction(1,7),Fraction(1,1),star*.5,star*.999,star,star*1.001,star*3,star*25]:
            d=[(distance(n,float(lam),a,b,X),a,b) for a,b,X in facets(n)]
            best=min(t[0] for t in d)
            formula=min(math.sqrt(n*(n-1))/2+float(lam)/math.sqrt(n*(n-1)),R)
            assert math.isclose(best, formula, rel_tol=2e-12,abs_tol=2e-12),(n,lam,best,formula)
            expected = typA if float(lam)<star-1e-12 else (typB if float(lam)>star+1e-12 else typA|typB)
            ties={(a,b) for dis,a,b in d if abs(dis-best)<1e-9}
            assert ties==expected,(n,lam,expected,ties)
            total+=len(d)
        for a,b,X in facets(n):
            for lam in (Fraction(1,2),Fraction(7,4)):
                assert exact_slack(n,lam,a,b) == Fraction(X,2)+lam*(1-Fraction(a+b,n))
                total+=1
    # Concrete support-point test independent of facet H description:
    # for arbitrary objectives, a product-permutohedron minimizer is obtained by
    # assigning ranks 1..n from smallest to largest objective; the simplex
    # minimizer chooses a coordinate with minimal pairwise-sum objective.
    from random import Random
    rng=Random(720221)
    for n in range(3,7):
        permutations=list(itertools.permutations(range(1,n+1)))
        for lam in (.2,1.7,7.5):
            for j in range(32):
                objx=[rng.uniform(-1,1) for _ in range(n)]
                objy=[rng.uniform(-1,1) for _ in range(n)]
                # minimizing objectives assign higher ranks to more negative coefficients
                px=tuple(sorted(range(n), key=lambda i:objx[i],reverse=True))
                py=tuple(sorted(range(n), key=lambda i:objy[i],reverse=True))
                xx=[0]*n; yy=[0]*n
                for k,i in enumerate(px):xx[i]=k+1
                for k,i in enumerate(py):yy[i]=k+1
                k=min(range(n),key=lambda i:objx[i]+objy[i])
                xx[k]+=lam; yy[k]+=lam
                attained=sum(objx[i]*xx[i]+objy[i]*yy[i] for i in range(n))
                # check permutations independently and the diagonal simplex vertices
                brute=min(sum(objx[i]*p[i]+objy[i]*q[i] for i in range(n)) for p in permutations for q in permutations)
                brute+=lam*min(objx[i]+objy[i] for i in range(n))
                assert math.isclose(attained,brute,rel_tol=1e-12,abs_tol=1e-12)
                total+=1
    print('VERIFY_OK',total)

if __name__=='__main__':test()
