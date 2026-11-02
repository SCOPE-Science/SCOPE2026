"""Standalone exact enumeration and identity checks for bilinear Fourier fourth moments.

Run with Python 3 standard library. Public mathematical reproducibility only.
"""
from itertools import product
from collections import Counter
from math import factorial

def score(q,seq):
    """Exact sum of pairwise squared complex row correlations, integer for q=2,3."""
    # Normalized first row 1. Types (u,v) in Z/qZ.
    vals=[]
    for selector in (lambda a,b:a, lambda a,b:b, lambda a,b:(a-b)%q):
        c=Counter(selector(a,b) for a,b in seq)
        if q==2:
            x=c[0]-c[1]
            vals.append(x*x)
        elif q==3:
            x,y,z=c[0],c[1],c[2]
            vals.append(x*x+y*y+z*z-x*y-x*z-y*z)
        else:raise ValueError(q)
    return sum(vals)

def predicted(q,n):
    if q==2:return (n%4)*(4-n%4)
    if q==3:return 3*(n%3!=0)

def brute(q,n):
    types=list(product(range(q),repeat=2))
    best=100000000000; count=0; witness=None
    for seq in product(types,repeat=n):
        s=score(q,seq)
        if s<best:best,count,witness=s,1,seq
        elif s==best:count+=1
    return best,count,witness

def predicted_count_binary(n):
    t,r=divmod(n,4)
    from math import comb
    return comb(4,r)*factorial(n)//(factorial(t+1)**r*factorial(t)**(4-r))

def direct_moment(q,seq):
    # Direct enumeration of all additive energy coincidences in Z^(3+n) with coefficient tuples.
    n=len(seq)
    edges=[]
    for j,(u,v) in enumerate(seq):
        for i,k in enumerate((0,u,v)):
            expo=tuple(1 if a==i else 0 for a in range(3))+tuple(1 if b==j else 0 for b in range(n))
            edges.append((expo,k))
    sums={}
    for ea,ka in edges:
        for eb,kb in edges:
            ex=tuple(x+y for x,y in zip(ea,eb))
            sums.setdefault(ex,[]).append((ka+kb)%q)
    # Count root-of-unity algebra: in q=2,3, squared norms exact integer.
    def norm_sq(powers):
        c=Counter(powers)
        if q==2:return (c[0]-c[1])**2
        if q==3:
            x,y,z=[c[i] for i in range(3)]
            return x*x+y*y+z*z-x*y-x*z-y*z
    return sum(norm_sq(v) for v in sums.values())

def construct(q,n):
    if q==2:
        types=list(product(range(2),repeat=2))
        return tuple(types[j%4] for j in range(n))
    else:
        return tuple((j%3,2*(j%3)%3) for j in range(n))

def main():
    checks=0
    for q,n_max in [(2,7),(3,5)]:
        for n in range(3,n_max+1):
            s,count,seq=brute(q,n)
            expected=predicted(q,n)
            assert s==expected, (q,n,s,expected)
            checks+=1
            if q==2:
                assert count==predicted_count_binary(n),(q,n,count)
                checks+=1
            assert score(q,construct(q,n))==expected,(q,n,'construct')
            checks+=1
            assert direct_moment(q,seq)==18*n*n-15*n+4*s,(q,n,'moment',direct_moment(q,seq))
            checks+=1
            print('verified exact census',q,n,'minimum',s,'minimizers',count)
    for q in (2,3):
        for n in range(3,121):
            a=construct(q,n)
            assert score(q,a)==predicted(q,n),(q,n)
            checks+=1
    for n in (3,4,5,6):
        for q in (2,3):
            a=construct(q,n)
            assert direct_moment(q,a)==18*n*n-15*n+4*score(q,a)
            checks+=1
    print('PASS',checks,'independent exact assertions; complete enumeration up to binary n=7 and ternary n=5')
if __name__=='__main__':main()
