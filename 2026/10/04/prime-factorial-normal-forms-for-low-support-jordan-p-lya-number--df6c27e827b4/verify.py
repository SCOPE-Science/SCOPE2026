#!/usr/bin/env python3
from math import factorial

PRIMES=[2,3,5,7,11,13]

def vp(n,p):
    s=0
    while n:
        n//=p
        s+=n
    return s

def det_int(a):
    # Bareiss exact determinant.
    a=[row[:] for row in a]
    n=len(a)
    sign=1
    prev=1
    for k in range(n-1):
        if a[k][k]==0:
            for i in range(k+1,n):
                if a[i][k]:
                    a[k],a[i]=a[i],a[k]
                    sign=-sign
                    break
            else:
                return 0
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                a[i][j]=(a[i][j]*pivot-a[i][k]*a[k][j])//prev
        prev=pivot
    return sign*a[-1][-1]

def solve_upper_unit(A,b):
    n=len(A)
    x=[0]*n
    for i in range(n-1,-1,-1):
        s=b[i]-sum(A[i][j]*x[j] for j in range(i+1,n))
        assert A[i][i]==1 and s==int(s)
        x[i]=s
    return x

def semigroup(gens,bound):
    vals={1}
    for g in gens:
        old=sorted(vals)
        out=set(vals)
        for v in old:
            z=v*g
            while z<=bound:
                out.add(z)
                z*=g
        vals=out
    return vals

def main():
    ids=[
        (4, [(2,2),(3,1)]),
        (6, [(3,1),(5,1)]),
        (8, [(2,3),(7,1)]),
        (9, [(2,1),(3,2),(7,1)]),
        (10,[(3,1),(5,1),(7,1)]),
        (12,[(2,1),(3,1),(11,1)]),
    ]
    for m,fac in ids:
        rhs=1
        for p,e in fac:
            rhs*=factorial(p)**e
        assert factorial(m)==rhs, (m,factorial(m),rhs)

    for r in range(1,6):
        ps=PRIMES[:r]
        A=[[vp(pj if False else pi, pj) for pi in []] for pj in []]  # unused guard against accidental conventions
        A=[[vp(factorial(pi),pj) if False else 0 for pi in ps] for pj in ps]
        # vp above expects the integer itself; compute direct integer valuations here.
        A=[]
        for pj in ps:
            row=[]
            for pi in ps:
                z=factorial(pi); c=0
                while z%pj==0:
                    z//=pj; c+=1
                row.append(c)
            A.append(row)
        assert det_int(A)==1, (r,A,det_int(A))

    ps=PRIMES
    A=[]
    for pj in ps:
        row=[]
        for pi in ps:
            z=factorial(pi); c=0
            while z%pj==0:
                z//=pj; c+=1
            row.append(c)
        A.append(row)
    b=[]
    for pj in ps:
        z=factorial(14); c=0
        while z%pj==0:
            z//=pj; c+=1
        b.append(c)
    coords=solve_upper_unit(A,b)
    assert coords==[1,-1,-1,1,0,1], coords
    assert factorial(14)*factorial(3)*factorial(5)==factorial(2)*factorial(7)*factorial(13)

    bound=10_000_000_000
    all_gens=[factorial(m) for m in range(2,13)]
    prime_gens=[factorial(p) for p in [2,3,5,7,11]]
    s_all=semigroup(all_gens,bound)
    s_prime=semigroup(prime_gens,bound)
    assert s_all==s_prime
    strata={}
    for p in [2,3,5,7,11]:
        count=0
        for n in s_prime:
            if n==1:
                continue
            x=n; lp=None
            for q in [2,3,5,7,11]:
                if x%q==0:
                    lp=q
            if lp==p:
                count+=1
        strata[p]=count
    ss=','.join(f'{p}:{strata[p]}' for p in [2,3,5,7,11])
    cc=','.join(map(str,coords))
    print(f'VERIFY_OK bound={bound} semigroup_size={len(s_prime)} strata={ss} coord14={cc}')

if __name__=='__main__':
    main()
