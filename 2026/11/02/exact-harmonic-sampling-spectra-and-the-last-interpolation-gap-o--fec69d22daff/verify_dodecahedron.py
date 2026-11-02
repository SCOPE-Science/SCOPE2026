#!/usr/bin/env python3
"""Exact arithmetic verification of dodecahedral harmonic-sampling ranks.

Only the standard library is required. The global theorem uses, in addition,
the analytic all-degree Legendre estimate proved in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def q(a=0, b=0):
    return (F(a), F(b))  # a+b*sqrt(5)


def add(x, y):
    return (x[0]+y[0], x[1]+y[1])


def mul(x, y):
    return (x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0])


def neg(x):
    return (-x[0], -x[1])


def neg_vec(v):
    return tuple(neg(c) for c in v)


def dot(v, w):
    z=q()
    for x, y in zip(v, w):
        z=add(z, mul(x, y))
    return z


def matrix_product(X, Y):
    m=len(X)
    return [[sum(X[i][k]*Y[k][j] for k in range(m)) for j in range(m)] for i in range(m)]


def main():
    phi=q(F(1, 2),F(1, 2))
    phi_inv=q(F(-1, 2),F(1, 2))
    pts=[]
    for sg in product((-1, 1), repeat=3):
        pts.append(tuple(q(t) for t in sg))
    for cyc in range(3):
        for s,t in product((-1,1),repeat=2):
            v=(q(), mul(q(s),phi_inv), mul(q(t),phi))
            pts.append(v[-cyc:]+v[:-cyc] if cyc else v)
    assert len(pts)==len(set(pts))==20
    assert all(dot(v,v)==q(3) for v in pts)
    assert all(neg_vec(v) in pts for v in pts)
    reps=[]
    for v in pts:
        if v not in reps and neg_vec(v) not in reps:
            reps.append(v)
    assert len(reps)==10

    A=[[0]*10 for _ in range(10)]
    B=[[0]*10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            z=dot(reps[i],reps[j])
            if i==j:
                assert z==q(3)
            elif z==q(1): A[i][j]=1
            elif z==q(-1): A[i][j]=-1
            elif z==q(0,1): B[i][j]=1
            elif z==q(0,-1): B[i][j]=-1
            else:
                raise AssertionError(f'unexpected unnormalised dot product: {z}')
    eye=[[int(i==j) for j in range(10)] for i in range(10)]
    ones=[[1]*10 for _ in range(10)]
    C=[[abs(v) for v in row] for row in B]
    assert all(sum(row)==3 for row in C)
    assert matrix_product(C,C)==[[2*eye[i][j]-C[i][j]+1 for j in range(10)] for i in range(10)]
    assert matrix_product(B,B)==[[A[i][j]+3*eye[i][j] for j in range(10)] for i in range(10)]
    assert matrix_product(matrix_product(B,B),B)==[[5*B[i][j] for j in range(10)] for i in range(10)]

    # A_k = 3^k P_k(1/3);
    # B_k = 3^k P_k(sqrt(5)/3) / (sqrt(5) if k is odd else 1).
    aa=[F(1),F(1)]; bb=[F(1),F(1)]
    for k in range(1,186):
        aa.append(((2*k+1)*aa[k]-9*k*aa[k-1])/(k+1))
        bb.append(((5 if k%2 else 1)*(2*k+1)*bb[k]-9*k*bb[k-1])/(k+1))
    exceptional={0:1,1:3,2:5,3:7,4:9,5:6,8:9,14:9}
    zeros=[]
    for k in range(186):
        scale=3**k
        if k%2==0:
            num=(scale+6*aa[k]+3*bb[k],scale-2*aa[k]+bb[k],scale+aa[k]-2*bb[k])
            mult=(1,5,4)
        else:
            num=(scale-3*aa[k],scale+2*aa[k]+5*bb[k],scale+2*aa[k]-5*bb[k])
            mult=(4,3,3)
        assert all(t>=0 for t in num), (k,num)
        rank=sum(m for m,v in zip(mult,num) if v>0)
        assert rank==exceptional.get(k,10), (k,rank)
        if rank<10:
            zeros.append((k,rank,tuple(i for i,v in enumerate(num) if v==0)))
    assert [z[0] for z in zeros]==[0,1,2,3,4,5,8,14]
    # The elementary integral estimate bounds 6|a_k|+3|b_k|
    # by (9 sqrt(pi)/2)(1+1/sqrt(2)) / sqrt(k).
    # Use pi<22/7 and 1/sqrt(2)<7072/10000, by rational arithmetic.
    c_squared_upper=F(81,4)*F(22,7)*(1+F(7072,10000))**2
    assert c_squared_upper < 186
    assert F(7072,10000)**2 > F(1,2)
    # Sanity check for direct scalar P_k at rational 1/3.
    assert aa[2]==-3 and aa[5]==81
    assert bb[2]==3 and bb[3]==-1
    print('DODECAHEDRAL_SAMPLING_EXACT_CHECK_OK')
    print('vertices=20 antipodal_pairs=10')
    print('signed_Petersen_identities=3')
    print('all_degree_ranks_checked=0..185')
    print('exceptional_ranks='+repr(zeros))
    print('analytic_full_rank_from_degree=186')
    print('legendre_bound_squared_upper='+str(c_squared_upper))

if __name__=='__main__':
    main()
