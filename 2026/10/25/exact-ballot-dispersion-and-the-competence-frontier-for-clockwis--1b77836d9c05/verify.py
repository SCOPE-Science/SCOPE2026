"""Exact finite checks for cyclic forward-delegation ballot weights.
Run: python3 check.py (Python 3.9+ standard library)."""
from fractions import Fraction
from itertools import product
from math import comb

def ballot_data(direct):
    n=len(direct)
    if not any(direct):
        return [0]*n
    weights=[0]*n
    for start in range(n):
        j=start
        for _ in range(n):
            if direct[j]:
                weights[j]+=1
                break
            j=(j+1)%n
    return weights

def polynomial_from_compositions(n,q,p):
    r=1-q
    out={0:r**n}
    for k in range(1,n+1):
        # enumerate positive cyclic gap compositions of n into k parts
        def compositions(total,parts):
            if parts==1:
                yield (total,)
            else:
                for a in range(1,total-parts+2):
                    for tail in compositions(total-a,parts-1):
                        yield (a,)+tail
        for gaps in compositions(n,k):
            poly={0:Fraction(1)}
            for gap in gaps:
                nextpoly={}
                for count,pr in poly.items():
                    nextpoly[count]=nextpoly.get(count,Fraction(0))+pr*(1-p)
                    nextpoly[count+gap]=nextpoly.get(count+gap,Fraction(0))+pr*p
                poly=nextpoly
            factor=Fraction(n,k)*q**k*r**(n-k)
            for count,pr in poly.items():
                out[count]=out.get(count,Fraction(0))+factor*pr
    return out

def polynomial_brute(n,q,p):
    r=1-q
    out={}
    Q=Fraction(0)
    for ds in product((0,1),repeat=n):
        k=sum(ds)
        weight_pattern=q**k*r**(n-k)
        w=ballot_data(ds)
        Q+=weight_pattern*sum(v*v for v in w)
        direct_indices=[i for i,v in enumerate(w) if v]
        for successes in product((0,1),repeat=len(direct_indices)):
            s=sum(w[j]*v for j,v in zip(direct_indices,successes))
            pc=p**sum(successes)*(1-p)**(len(successes)-sum(successes))
            out[s]=out.get(s,Fraction(0))+weight_pattern*pc
    return out,Q

def exact_Q(n,q):
    r=1-q
    return n*(Fraction(2)-q)/q-n*(2*n-1+Fraction(2)/q)*r**n

if __name__=='__main__':
    checked=0
    for q,p in [(Fraction(1,2),Fraction(1,2)),(Fraction(2,5),Fraction(3,5)),(Fraction(3,4),Fraction(5,7))]:
        for n in range(2,10):
            brute,Q=polynomial_brute(n,q,p)
            formula=polynomial_from_compositions(n,q,p)
            assert all(formula.get(j,0)==brute.get(j,0) for j in range(n+1)),(n,q,p,formula,brute)
            assert Q==exact_Q(n,q),(n,q,Q,exact_Q(n,q))
            assert sum(brute.values())==1
            checked+=1
    print('PASS: {} complete rational joint-action-and-signal enumeration instances, n=2..9'.format(checked))
    for n in [2,3,5,8]:
        print('n={}, q=1/2, E[sum weights squared]={}'.format(n,exact_Q(n,Fraction(1,2))))
