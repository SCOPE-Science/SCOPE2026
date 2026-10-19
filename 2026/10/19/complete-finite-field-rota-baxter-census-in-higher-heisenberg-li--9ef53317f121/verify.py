#!/usr/bin/env python3
"""Finite-field checks for weight-arbitrary Lie Rota--Baxter operators on Heisenberg algebras.

Use: python3 verify.py. No external Python dependencies.
"""
from itertools import product
from math import prod
from random import Random


def add(x, y, q):
    return x ^ y if q == 4 else (x + y) % q


def neg(x, q):
    return x if q == 4 else (-x) % q


def mul(x, y, q):
    if q != 4:
        return (x * y) % q
    out = 0
    for i in range(2):
        if (x >> i) & 1:
            for j in range(2):
                if (y >> j) & 1:
                    out ^= 1 << (i+j)
    if out & 8:
        out ^= 0b1110   # alpha^3 = alpha^2+alpha, from alpha^2+alpha+1=0
    if out & 4:
        out ^= 0b111
    return out


def sub(x, y, q):
    return add(x, neg(y, q), q)


def symp(x, y, q):
    assert len(x) == len(y) and len(x) % 2 == 0
    s=0
    for i in range(0, len(x), 2):
        s=add(s,sub(mul(x[i],y[i+1],q),mul(x[i+1],y[i],q),q),q)
    return s


def mat_vec(A, x, q):
    return [sum_field((mul(a,v,q) for a,v in zip(row,x)),q) for row in A]


def sum_field(it,q):
    val=0
    for x in it: val=add(val,x,q)
    return val


def rb_identity(A, b, a, c, q, lam=0):
    m=len(A)
    # R(x+tz) = Ax+t a + (b.x+c t)z.
    def R(x):
        v=x[:m]
        z=x[m]
        y=mat_vec(A,v,q)
        return [add(y[i],mul(z,a[i],q),q) for i in range(m)]+[add(sum_field((mul(b[i],v[i],q) for i in range(m)),q),mul(c,z,q),q)]
    E=[[int(i==j) for j in range(m+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(i+1,m+1):
            x,y=R(E[i]),R(E[j])
            omega=symp(E[i][:m],E[j][:m],q)
            lhs=[0]*m+[symp(x[:m],y[:m],q)]
            lhs=[add(lhs[k],mul(mul(lam,omega,q),R(E[m])[k],q),q) for k in range(m+1)]
            tau=add(symp(x[:m],E[j][:m],q),symp(E[i][:m],y[:m],q),q)
            rhs=R([0]*m+[tau])
            if lhs != rhs:
                return False
    return True


def predicted(A, a, c, q, lam=0):
    m=len(A)
    if any(a):
        return False
    E=[[int(i==j) for j in range(m)] for i in range(m)]
    cols=[mat_vec(A,e,q) for e in E]
    for i in range(m):
        for j in range(i+1,m):
            lhs=symp(cols[i],cols[j],q)
            tau=add(symp(cols[i],E[j],q),symp(E[i],cols[j],q),q)
            lhs=add(lhs,mul(mul(lam,c,q),symp(E[i],E[j],q),q),q)
            if lhs!=mul(c,tau,q):
                return False
    return True


def sp_order(n,q):
    return q**(n*n)*prod(q**(2*j)-1 for j in range(1,n+1))


def isotropic_subspaces(n,r,q):
    return (prod(q**(2*n-i)-q**i for i in range(r))//
            prod(q**r-q**i for i in range(r)))


def surjections(d,r,q):
    return prod(q**d-q**i for i in range(r))


def branch_counts(n,q):
    return [isotropic_subspaces(n,r,q)*surjections(2*n,r,q) for r in range(n+1)]


def rank(M,q):
    M=[row[:] for row in M]
    p=0
    for j in range(len(M[0])):
        k=next((k for k in range(p,len(M)) if M[k][j]),None)
        if k is None: continue
        M[p],M[k]=M[k],M[p]
        inv=next(t for t in range(1,q) if mul(t,M[p][j],q)==1)
        M[p]=[mul(inv,v,q) for v in M[p]]
        for i in range(len(M)):
            if i!=p and M[i][j]:
                z=M[i][j]
                M[i]=[sub(v,mul(z,u,q),q) for v,u in zip(M[i],M[p])]
        p+=1
        if p==len(M):break
    return p


def exhaustive_three_dimensional(q,lam):
    total=0
    by_c=[0]*q
    for tup in product(range(q), repeat=9):
        A=[[tup[0],tup[1]],[tup[2],tup[3]]]
        b=[tup[4],tup[5]]
        a=[tup[6],tup[7]]
        c=tup[8]
        direct=rb_identity(A,b,a,c,q,lam)
        alg=predicted(A,a,c,q,lam)
        assert direct==alg,(q,tup,direct,alg)
        if direct:
            total+=1
            by_c[c]+=1
    singular=1 if lam==0 else 2
    expected=q*q*(singular*sum(branch_counts(1,q))+(q-singular)*sp_order(1,q))
    assert total==expected,(q,total,expected)
    assert by_c[0]==q*q*sum(branch_counts(1,q))
    for c in range(1,q):
        expected_c=q*q*(sum(branch_counts(1,q)) if c==lam else sp_order(1,q))
        assert by_c[c]==expected_c,(q,lam,c,by_c,expected_c)
    print('EXHAUSTIVE_DIM3',q,lam,total,by_c)


def four_dimensional_projection_binary():
    q=2
    m=4
    E=[[int(i==j) for j in range(m)] for i in range(m)]
    zero_by_rank=[0,0,0]
    nonzero=0
    unit_lambda_by_rank=[0,0,0]
    for bits in range(1<<(m*m)):
        A=[[((bits>>(i*m+j))&1) for j in range(m)] for i in range(m)]
        for c in (0,1):
            alg=predicted(A,[0]*m,c,q,0)
            if alg:
                if c==0:
                    r=rank(A,q)
                    assert r<=2
                    zero_by_rank[r]+=1
                else:
                    nonzero+=1
    expected=branch_counts(2,2)
    assert zero_by_rank==expected,(zero_by_rank,expected)
    assert nonzero==sp_order(2,2)
    total=(sum(zero_by_rank)+nonzero)*(q**m)
    assert total==65536
    # In characteristic two, lambda=1 makes BOTH c=0 and c=1 isotropic.
    for bits in range(1<<(m*m)):
        A=[[((bits>>(i*m+j))&1) for j in range(m)] for i in range(m)]
        c=1
        if predicted(A,[0]*m,c,q,1):
            B=[[A[i][j]^(i==j) for j in range(m)] for i in range(m)]
            unit_lambda_by_rank[rank(B,q)]+=1
    assert unit_lambda_by_rank==expected
    assert (sum(zero_by_rank)+sum(unit_lambda_by_rank))*(q**m)==108032
    print('COMPLETE_DIM5_Q2',zero_by_rank,nonzero,total,'WEIGHT1',unit_lambda_by_rank,108032)


def random_higher_dimensional():
    rng=Random(0xA51E)
    for n,q in ((2,3),(2,5),(3,2)):
        m=2*n
        for z in range(2500):
            A=[[rng.randrange(q) for _ in range(m)] for _ in range(m)]
            a=[rng.randrange(q) for _ in range(m)]
            b=[rng.randrange(q) for _ in range(m)]
            c=rng.randrange(q)
            lam=rng.randrange(q)
            assert rb_identity(A,b,a,c,q,lam)==(not any(a) and predicted(A,a,c,q,lam))
        print('RANDOM_DIM',2*n+1,'Q',q,'2500')

if __name__=='__main__':
    for q in (2,3,4):
        for lam in (range(q) if q<4 else (0,1)): exhaustive_three_dimensional(q,lam)
    four_dimensional_projection_binary()
    random_higher_dimensional()
    for q in (2,3,4,5):
        for n in (1,2,3):
            a=branch_counts(n,q)
            assert len(a)==n+1 and a[0]==1
            for lam in range(q):
                singular=1 if lam==0 else 2
                total=q**(2*n)*(singular*sum(a)+(q-singular)*sp_order(n,q))
                assert total>0
                print('THEORETICAL_COUNT',q,n,lam,total)
    print('ALL_HEISENBERG_RB_CHECKS_PASSED')
