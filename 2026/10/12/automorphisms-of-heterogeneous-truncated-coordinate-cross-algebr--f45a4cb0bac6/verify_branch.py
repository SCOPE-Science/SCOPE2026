"""Independent exhaustive tests for automorphisms of heterogeneous truncated coordinate-cross algebras."""
from itertools import product

def brute(p, ds):
    if len(ds)!=2: raise ValueError('two-branch exhaustive test')
    basis=[(i,j) for i,d in enumerate(ds) for j in range(1,d)]
    n=len(basis); m=p**n
    vecs=list(product(range(p),repeat=n))
    zero=(0,)*n
    idx={a:i for i,a in enumerate(basis)}
    def mul(a,b):
        r=[0]*n
        for t,(i,j) in enumerate(basis):
            if not a[t]:continue
            for u,(i2,j2) in enumerate(basis):
                if i==i2 and j+j2 < ds[i]:
                    r[idx[(i,j+j2)]]=(r[idx[(i,j+j2)]]+a[t]*b[u])%p
        return tuple(r)
    def power(a,k):
        if k<2: return a
        b=mul(a,a)
        for _ in range(3,k+1):b=mul(b,a)
        return b
    linear=[(v[idx[(0,1)]],v[idx[(1,1)]]) for v in vecs]
    nil=[ [i for i,v in enumerate(vecs) if power(v,d)==zero] for d in ds]
    # Exclude pairs of degree-one rank <2 before multiplying.
    accepted=0
    for i in nil[0]:
        a,b=linear[i]
        for j in nil[1]:
            c,d=linear[j]
            if (a*d-b*c)%p and mul(vecs[i],vecs[j])==zero:accepted+=1
    return accepted

def expected(p,ds):
    assert len(ds)>=2 and min(ds)>=3 and len(set(ds))>1
    from collections import Counter
    from math import factorial
    mult=1
    for k in Counter(ds).values(): mult*=factorial(k)
    return mult*(p-1)**len(ds)*p**(sum(d-2 for d in ds)+len(ds)*(len(ds)-1))

if __name__=='__main__':
    tested=0
    for p,ds in [(2,(3,4)),(2,(3,5)),(2,(4,5)),(3,(3,4))]:
        actual=brute(p,ds); correct=expected(p,ds)
        assert actual==correct,(p,ds,actual,correct)
        print('EXACT',p,ds,actual)
        tested+=1
    assert expected(2,(3,3,4))==2**(1+1+2+6)*2
    print('EXHAUSTIVE_CASES',tested,'VERIFY_OK')
