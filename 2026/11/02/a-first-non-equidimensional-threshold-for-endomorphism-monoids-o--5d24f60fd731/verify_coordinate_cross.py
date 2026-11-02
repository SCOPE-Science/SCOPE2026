"""Standalone finite-field checks of endomorphism loci of truncated coordinate crosses."""
from itertools import product
from math import factorial
import random


def field(q):
    if q == 4:
        def add(a,b): return a ^ b
        def mul(a,b):
            out=0
            while b:
                if b&1: out ^= a
                b >>= 1
                a <<= 1
                if a&4: a ^= 7  # x^2+x+1
            return out
        return add,mul
    assert q in (2,3,5)
    return lambda a,b:(a+b)%q,lambda a,b:(a*b)%q


def product_zero(u,v,d,add,mul):
    """Independent multiplication in t*k[t]/(t^d)."""
    w=[0]*d
    for i,x in enumerate(u,1):
        for j,y in enumerate(v,1):
            if i+j<d:
                w[i+j]=add(w[i+j],mul(x,y))
    return all(z==0 for z in w)


def is_row_valid(row,n,d,add,mul):
    polys=[[row[(j-1)*n+i] for j in range(1,d)] for i in range(n)]
    return all(product_zero(polys[i],polys[j],d,add,mul)
               for i in range(n) for j in range(i+1,n))


def has_component_cover(row,n,d):
    if d==2:
        return True
    a=row[:n]
    if d==3:
        return sum(z!=0 for z in a)<=1
    b=row[n:2*n]
    if all(z==0 for z in a):
        return True
    return any(a[i]!=0 and all(a[j]==b[j]==0 for j in range(n) if j!=i)
               for i in range(n))


def formula(n,d,q):
    if d==2:return q**(n*n)
    if d==3:return (q**n*(1+n*(q-1)))**n
    assert d==4
    return (q**(2*n)+n*(q-1)*q**(n+1))**n


def check_row(n,d,q):
    add,mul=field(q)
    cnt=0
    for row in product(range(q),repeat=n*(d-1)):
        good=is_row_valid(row,n,d,add,mul)
        cover=has_component_cover(row,n,d)
        assert good==cover,(n,d,q,row,good,cover)
        cnt += good
    assert cnt**n==formula(n,d,q),(n,d,q,cnt)
    print('ROW',n,d,q,cnt,'MONOID',cnt**n)
    return cnt


def rank_mod(a,n,q):
    add,mul=field(q)
    mat=[list(a[i*n:(i+1)*n]) for i in range(n)]
    rank=0
    for c in range(n):
        p=next((j for j in range(rank,n) if mat[j][c]),None)
        if p is None:continue
        mat[rank],mat[p]=mat[p],mat[rank]
        inv=next(z for z in range(1,q) if mul(z,mat[rank][c])==1)
        mat[rank]=[mul(inv,t) for t in mat[rank]]
        for j in range(n):
            if j!=rank and mat[j][c]:
                t=mat[j][c]
                # characteristic 2 subtraction equals addition, otherwise additive inverse needed
                for h in range(c,n):
                    v=mul(t,mat[rank][h]); neg=v if q==4 or q==2 else (-v)%q
                    mat[j][h]=add(mat[j][h],neg)
        rank+=1
    return rank


def check_global(n,d,q,exhaustive=False,samples=5000):
    add,mul=field(q)
    rng=random.Random(314159+n*100+d*10+q)
    rows=product(range(q),repeat=n*n*(d-1)) if exhaustive else (
        tuple(rng.randrange(q) for _ in range(n*n*(d-1))) for _ in range(samples))
    good=0;units=0; seen=0
    for flat in rows:
        seen+=1
        # Data grouped first by output branch, then by coefficient degree.
        branches=[flat[j*n*(d-1):(j+1)*n*(d-1)] for j in range(n)]
        valid=all(is_row_valid(row,n,d,add,mul) for row in branches)
        if valid:
            good+=1
            a=tuple(branches[j][i] for j in range(n) for i in range(n))
            if rank_mod(a,n,q)==n:units+=1
    if exhaustive:
        assert good==formula(n,d,q),(n,d,q,good,formula(n,d,q))
        if d==4:
            auto=factorial(n)*(q-1)**n*q**(n*(n+1))
        elif d==3:
            auto=factorial(n)*(q-1)**n*q**(n*n)
        else:
            auto=1
            for i in range(n):auto*=q**n-q**i
        assert units==auto,(n,d,q,units,auto)
    print('GLOBAL',n,d,q,seen,good,units,'EXHAUSTIVE' if exhaustive else 'SAMPLE')


def main():
    cases=[(2,2,2),(2,2,3),(3,2,2),
           (2,3,2),(2,3,3),(2,3,4),(3,3,2),
           (2,4,2),(2,4,3),(2,4,4),(3,4,2),(3,4,3),(4,4,2)]
    for n,d,q in cases:check_row(n,d,q)
    check_global(2,4,2,True)
    check_global(2,3,2,True)
    check_global(2,2,3,True)
    for n,d,q in [(2,4,3),(2,4,4),(3,4,2),(3,4,3),(3,3,2)]:
        check_global(n,d,q,samples=5000)
    print('COORDINATE_CROSS_ENDOMORPHISM_GEOMETRY_OK',len(cases),'ROW_CASES','3_GLOBAL_EXHAUSTIVE','5_GLOBAL_SAMPLES')

if __name__=='__main__':main()
