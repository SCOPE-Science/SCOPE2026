"""Independent finite-field checks for two adjacent complete-intersection exponents."""
from itertools import product
from random import Random
from math import prod


def monomials(d,n):
    return list(product(range(n),repeat=d))


def algebra(d,n,p):
    mon=monomials(d,n); ix={m:i for i,m in enumerate(mon)}
    mul=[[ix.get(tuple(a[i]+b[i] for i in range(d)),-1) if max(a[i]+b[i] for i in range(d)) < n else -1 for b in mon] for a in mon]
    one=ix[(0,)*d]; linear=[ix[tuple(int(i==j) for i in range(d))] for j in range(d)]
    def times(a,b):
        ans=[0]*len(mon)
        for i,ai in enumerate(a):
            if ai:
                for j,bj in enumerate(b):
                    k=mul[i][j]
                    if k>=0 and bj: ans[k]=(ans[k]+ai*bj)%p
        return tuple(ans)
    def power(a,h):
        v=[0]*len(mon); v[one]=1; v=tuple(v)
        for _ in range(h):v=times(v,a)
        return v
    return mon,one,linear,power


def exact(d,n,p):
    mon,one,linear,power=algebra(d,n,p)
    # all elements in maximal ideal (constant=0)
    by_linear={}
    for coeff in product(range(p),repeat=len(mon)-1):
        a=list(coeff); a.insert(one,0); a=tuple(a)
        if any(power(a,n)): continue
        v=tuple(a[j] for j in linear)
        by_linear[v]=by_linear.get(v,0)+1
    if d==2:
        total=sum(c*by_linear.get((w[0],w[1]),0) for v,c in by_linear.items() for w in product(range(p),repeat=2) if (v[0]*w[1]-v[1]*w[0])%p)
        expect= (p*p-1)*(p*p-p)*p**(2*(n*n-3)) if n==p else 2*(p-1)**2*p**(2*((n-1)*n-1))
        assert total==expect,(d,n,p,total,expect)
        print('EXACT_AUT',d,n,p,total,len(by_linear))
        return
    # d>=3: verify number of valid images per row and admissible tangent vectors only
    vals=set(by_linear.values()); assert len(vals)==1,(d,n,p,vals)
    if n==p:
        assert len(by_linear)==p**d,('tangent image count',len(by_linear))
        assert next(iter(vals))==p**(n**d-1-d)
    else:
        assert len(by_linear)==d*(p-1)
        assert next(iter(vals))==p**((n-1)*n**(d-1)-1)
    print('EXACT_ROWS',d,n,p,len(by_linear),next(iter(vals)))


def sampled(d,n,p,cases=400):
    mon,one,linear,power=algebra(d,n,p)
    rng=Random(42715+d*100+n*10+p)
    for _ in range(cases):
        a=tuple(0 if k==one else rng.randrange(p) for k in range(len(mon)))
        v=[a[i] for i in linear]
        if n==p:
            assert not any(power(a,n))
        elif n==p+1:
            nz=[i for i,x in enumerate(v) if x]
            if len(nz)==1:
                chosen=nz[0]
                allow=all(not a[k] for k,m in enumerate(mon) if m[chosen]==0)
                assert (not any(power(a,n)))==allow, ('sample',d,n,p,nz,a)
    print('SAMPLED',d,n,p,cases)

if __name__=='__main__':
    exact(2,2,2)
    exact(2,3,2)
    exact(2,3,3)
    exact(3,2,2)
    sampled(3,3,2,800)
    sampled(2,4,3,800)
    sampled(3,4,3,400)
    print('VERIFY_OK prime-power and successor monomial complete intersections')
