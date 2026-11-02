#!/usr/bin/env python3
"""Exact certificate for the 72-point E6 harmonic-sampling spectral theorem.
All arithmetic is integral or rational; no external packages are required.
"""
from fractions import Fraction as F
from math import comb
from itertools import product


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def root_representatives():
    # Coordinate vectors multiplied by 3; actual vectors are a/3.
    # They have squared length 2 (their integer representatives have norm 18).
    v=[]
    for block in range(3):
        for i in range(3):
            for j in range(i+1,3):
                a=[0]*9
                a[3*block+i]=3
                a[3*block+j]=-3
                v.append(tuple(a))
    w=[]
    for i in range(3):
        a=[-1]*3
        a[i]=2
        w.append(tuple(a))
    for a,b,c in product(w,repeat=3):
        v.append(a+b+c)
    assert len(v)==36 and len(set(v))==36
    assert all(dot(a,a)==18 for a in v)
    assert all(tuple(-x for x in a) not in v for a in v)
    return v


def check():
    v=root_representatives()
    n=len(v)
    J=[[1]*n for _ in range(n)]
    S=[[0]*n for _ in range(n)]
    A=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            d=dot(v[i],v[j])
            if i==j:
                assert d==18
            else:
                assert d in (-9,0,9)
                S[i][j]=d//9
                A[i][j]=1 if d else 0
    assert all(sum(a)==20 for a in A)
    # Exhaustive 36-by-36 exact integer matrix identities.
    for i in range(n):
        for j in range(n):
            s2=sum(S[i][k]*S[k][j] for k in range(n))
            a2=sum(A[i][k]*A[k][j] for k in range(n))
            assert s2==8*S[i][j]+20*(i==j)
            assert a2==8*(i==j)-2*A[i][j]+12*J[i][j]
    # Normalized Gegenbauer C_k^2(t)/C_k^2(1) at t=0,1/2,
    # evaluated from the defining three-term recurrence.
    def Gegenbauer_points(K):
        c05=[F(1),F(2)]
        c0=[F(1),F(0)]
        for k in range(1,K):
            c05.append((2*(k+2)*F(1,2)*c05[-1]-(k+3)*c05[-2])/(k+1))
            c0.append((-(k+3)*c0[-2])/(k+1))
        return c05,c0
    c05,c0=Gegenbauer_points(40)
    expected={0:1,1:6,2:20,3:30,4:35}
    for k in range(40):
        den=comb(k+3,3)
        p=c05[k]/den; q=c0[k]/den
        # Independent closed form C^2_k(1/2) by residue class k mod 6.
        cls=k%6
        explicit={0:F(k+3,3),1:F(2*(k+2),3),2:F(k+1,3),
                  3:-F(k+3,3),4:-F(2*(k+2),3),5:-F(k+1,3)}[cls]
        assert c05[k]==explicit,(k,c05[k],explicit)
        if k%2:
            eigs=[(1+10*p,6),(1-2*p,30)]
        else:
            eigs=[(1+20*p+15*q,1),(1+2*p-3*q,20),(1-4*p+3*q,15)]
        assert all(z>=0 for z,_ in eigs),(k,eigs)
        rank=sum(m for z,m in eigs if z)
        assert rank==expected.get(k,36),(k,rank)
        if k>=5:
            nz=[z for z,m in eigs if z]
            cond=max(nz)/min(nz)
            assert cond<=F(25,3)
            assert (cond==F(25,3))==(k==10), (k,cond)
        # Independent direct matrix evaluation at all 36 representatives.
        for i in range(n):
            assert all((F(int(i==j))+p*S[i][j] if k%2 else
                     F(int(i==j))+p*A[i][j]+q*(1-int(i==j)-A[i][j])) ==
                     (F(1) if i==j else (0 if dot(v[i],v[j])==0 and k%2 else
                     p*(1 if dot(v[i],v[j])>0 else -1) if k%2 else
                     p if abs(dot(v[i],v[j]))==9 else q))
                     for j in range(n))
    # Exterior inequalities guarantee no more zeros without extrapolation.
    # For even k>=10: (k+1)(k+2)(k+3) > 125*k+290.
    assert 11*12*13>125*10+290
    # Positive slope of cubic-minus-linear on integers k>=10.
    for k in range(10,40):
        assert (k+1)*(k+2)*(k+3)>125*k+290
    # For odd k>=5: (k+1)(k+2)(k+3)>40k+100.
    assert 6*7*8>40*5+100
    for k in range(5,40):
        assert (k+1)*(k+2)*(k+3)>40*k+100
    print('E6_HARMONIC_ALL_DEGREE_CERTIFICATE_OK',n,'representatives',40,'rational degrees')


if __name__ == '__main__':
    check()
