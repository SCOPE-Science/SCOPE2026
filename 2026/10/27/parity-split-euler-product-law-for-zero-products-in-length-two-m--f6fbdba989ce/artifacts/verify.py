"""Independent finite checks for the zero-product Smith profile theorem.

Run using Python 3 standard library: python verify.py
This validates direct matrix products for small rings, explicit kernel
cardinalities, exact Smith-stratum formulas, and finite-product limits.
"""
from collections import Counter
from itertools import product
from math import prod
from random import Random


def gbin(n, k, q):
    if k < 0 or k > n:
        return 0
    num, den = 1, 1
    for j in range(k):
        num *= q ** (n-j) - 1
        den *= q ** (k-j) - 1
    assert num % den == 0
    return num // den


def gl(k, q):
    return prod(q ** k - q ** j for j in range(k))


def rankcount(s, k, q):
    return gbin(s, k, q) ** 2 * gl(k, q)


def smith_count(n, a, b, q):
    if a < 0 or b < 0 or a+b > n:
        return 0
    return rankcount(n, a, q) * q ** (2*n*a-a*a) * rankcount(n-a, b, q)


def paircount(n, a, b, q):
    return smith_count(n, a, b, q) * q ** (n*(2*n-2*a-b))


def mul(u, v, mode, p):
    if mode == 'duals':
        a,b = u%p,u//p
        c,d = v%p,v//p
        return (a*c)%p+p*((a*d+b*c)%p)
    return u*v%(p*p)


def add(u, v, mode, p):
    if mode == 'duals':
        return ((u%p+v%p)%p)+p*((u//p+v//p)%p)
    return (u+v)%(p*p)


def matvec(A, x, mode, p):
    n=len(x)
    z=[]
    for i in range(n):
        s=0
        for j in range(n):
            s=add(s,mul(A[n*i+j],x[j],mode,p),mode,p)
        z.append(s)
    return tuple(z)


def matproduct_zero(A,B,n,mode,p):
    for i in range(n):
        for j in range(n):
            z=0
            for k in range(n):
                z=add(z,mul(A[n*i+k],B[n*k+j],mode,p),mode,p)
            if z!=0:
                return False
    return True


def residue_rank(A,n,p):
    a = [[A[i*n+j]%p for j in range(n)] for i in range(n)]
    r=0
    for j in range(n):
        pivot=next((i for i in range(r,n) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        factor=pow(a[r][j],-1,p)
        a[r]=[v*factor%p for v in a[r]]
        for i in range(n):
            if i!=r:
                t=a[i][j]
                a[i]=[(a[i][k]-t*a[r][k])%p for k in range(n)]
        r+=1
    return r


def direct_kernel_size(A,n,mode,p):
    z=(0,)*n
    return sum(matvec(A,x,mode,p)==z for x in product(range(p*p),repeat=n))


def direct_small(mode,p,n):
    q=p
    hist=Counter();ann_pairs=0
    cells=list(product(range(q*q),repeat=n*n))
    for A in cells:
        a=residue_rank(A,n,p)
        K=direct_kernel_size(A,n,mode,p)
        e=0; t=K
        while t%p==0 and t>1:
            e+=1;t//=p
        assert t==1
        b=2*(n-a)-e
        assert 0<=b<=n-a,(mode,p,n,A,a,b,K)
        hist[(a,b)]+=1
        ann_pairs += K**n
    for a in range(n+1):
        for b in range(n-a+1):
            assert hist[(a,b)]==smith_count(n,a,b,p),(
                mode,p,n,a,b,hist[(a,b)],smith_count(n,a,b,p))
    assert ann_pairs==sum(paircount(n,a,b,p)
                          for a in range(n+1) for b in range(n-a+1))
    if n==2 and p==2:
        actual=sum(matproduct_zero(A,B,n,mode,p) for A in cells for B in cells)
        assert actual==ann_pairs,(mode,actual,ann_pairs)
    return ann_pairs,dict(sorted(hist.items()))


def phi(t,q):
    return prod(1-q**(-j) for j in range(1,t+1))


def finite_scaled_weight(n,a,b,q):
    c=n-a-b
    if c<0:return 0.0
    h=a-c
    return q**(-(h*h+b*b)/2) * phi(n,q)**2/(phi(a,q)*phi(b,q)*phi(c,q)**2)


def limit_scaled_weight(h,b,q):
    return q**(-(h*h+b*b)/2)/phi(120,q)/phi(b,q)


def limit_total(parity,q):
    return sum(limit_scaled_weight(h,b,q)
               for b in range(20) for h in range(-30,31)
               if (h+b)%2==parity)


def sample_larger_matrices():
    rng=Random(73819)
    for mode in ('mod','duals'):
        for _ in range(220):
            n=3;p=2
            A=tuple(rng.randrange(4) for __ in range(n*n))
            a=residue_rank(A,n,p)
            K=direct_kernel_size(A,n,mode,p)
            e=0;t=K
            while t>1 and t%p==0:
                e+=1;t//=p
            assert t==1
            b=2*(n-a)-e
            assert 0<=b<=n-a,(mode,A,a,b,K)
            assert K==p**(2*n-2*a-b)
    print('SAMPLED_3_BY_3_KERNELS_OK')


def euler_product_constant(q,parity):
    t=1/q
    plus=prod(1+t**(j-0.5) for j in range(1,120))
    minus=prod(1-t**(j-0.5) for j in range(1,120))
    return (plus**3+(-1)**parity*minus**3)/2


def main():
    for q in (2,3,4,5,7):
        for n in range(0,8):
            assert sum(smith_count(n,a,b,q) for a in range(n+1)
                       for b in range(n-a+1))==q**(2*n*n)
    print('MATRIX_TYPE_NORMALIZATIONS_OK')
    for mode,p,n in [('duals',2,1),('mod',2,1),('duals',2,2),
                      ('mod',2,2),('duals',3,2),('mod',3,2)]:
        total,hist=direct_small(mode,p,n)
        print('DIRECT',mode,p,n,total,hist)
    sample_larger_matrices()
    for q in (2,3,4,5):
        for parity in (0,1):
            lim=limit_total(parity,q)
            closed=euler_product_constant(q,parity)
            assert abs(lim-closed)<1e-10,(q,parity,lim,closed)
            vals=[]
            for n in (12+parity,20+parity,30+parity):
                value=sum(finite_scaled_weight(n,a,b,q)
                          for a in range(n+1) for b in range(n-a+1))
                vals.append(value)
            assert abs(vals[-1]-lim)/lim < 0.0007,(q,parity,vals,lim)
            print('LIMIT',q,parity,round(lim,10),
                  [round(v,9) for v in vals])
    print('VERIFY_OK')

if __name__=='__main__':main()
