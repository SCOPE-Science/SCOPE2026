#!/usr/bin/env python3
"""Exact-rational reproducibility checks for even-degree E8 root-line harmonic sampling.
Only Python standard library is required. The unrestricted theorem is proved analytically.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb

def root_lines():
    roots=[]
    for i,j in combinations(range(8),2):
        for a,b in product((-2,2),repeat=2):
            v=[0]*8;v[i]=a;v[j]=b;roots.append(tuple(v))
    for v in product((-1,1),repeat=8):
        if sum(x<0 for x in v)%2 == 0:
            roots.append(v)
    assert len(roots)==240 and len(set(roots))==240
    roots={r if next(x for x in r if x)!=-abs(next(x for x in r if x)) else tuple(-x for x in r) for r in roots}
    assert len(roots)==120
    return sorted(roots)

def dot(x,y):return sum(a*b for a,b in zip(x,y))

def p(l,t):
    # Gegenbauer C_l^(3)(t): C_0=1, C_1=6t,
    # l*C_l=2(l+2)*t*C_{l-1}-(l+4)*C_{l-2}
    if l==0:return Q(1)
    if l==1:return 6*t
    a,b=Q(1),6*t
    for m in range(2,l+1):
        a,b=b,(2*(m+2)*t*b-(m+4)*a)/m
    return b

def three_values(l):
    assert l%2==0
    k=l//2; q,r=divmod(l,3)
    a=comb(l+5,5)
    c=(-1)**k*comb(k+2,2)
    b=(-1)**q*(q+1 if r==0 else 3*comb(q+2,2))
    assert (p(l,Q(1)),p(l,Q(1,2)),p(l,Q(0)))==(a,b,c)
    return a,b,c

def eigenvalues(l):
    a,b,c=three_values(l)
    return (Q(a+63*c+56*b,a),Q(a+3*c-4*b,a),Q(a-9*c+8*b,a))

def checks():
    roots=root_lines()
    A=[[int(i!=j and dot(u,v)==0) for j,v in enumerate(roots)] for i,u in enumerate(roots)]
    assert all(dot(x,x)==8 for x in roots)
    assert {abs(dot(roots[i],roots[j])) for i in range(120) for j in range(i+1,120)}=={0,4}
    assert all(sum(row)==63 for row in A)
    # The graph relation entails all spectral assertions, without numerical eigenvalue fitting.
    for i in range(120):
        for j in range(120):
            overlap=sum(A[i][k]*A[k][j] for k in range(120))
            assert overlap == (63 if i==j else (30 if A[i][j] else 36))
    patterns={0:(120,0,0),2:(0,0,Q(24,7)),4:(0,Q(10,7),0),
              6:(0,Q(10,11),Q(96,77)),
              8:(Q(360,143),Q(140,143),Q(144,143)),
              10:(0,Q(1020,1001),Q(984,1001)),
              12:(Q(294,221),Q(1563,1547),Q(1494,1547))}
    for l,expected in patterns.items():
        assert eigenvalues(l)==expected,(l,eigenvalues(l),expected)
    for l in range(0,102,2):
        a,b,c=three_values(l); ll=eigenvalues(l)
        assert ll[0]+84*ll[1]+35*ll[2]==120
        assert all(q>=0 for q in ll)
        # Independent direct root-inner-product evaluation for selected harmonic degrees.
        if l in (0,2,4,6,8,10,12,14,20,30,40,60,100):
            x=[Q((i*7)%17-8) for i in range(120)]
            sx=sum(x)
            Ax=[sum(A[i][j]*x[j] for j in range(120)) for i in range(120)]
            values={d:p(l,Q(d,8)) for d in (-8,-4,0,4,8)}
            for i in range(120):
                direct=sum(values[dot(roots[i],roots[j])]*x[j] for j in range(120))/a
                formula=((a-b)*x[i]+(c-b)*Ax[i]+b*sx)/a
                assert direct==formula
        if l>=12:
            k=l//2
            bound=Q(63*(k+1)*(k+2),2)+Q(56*(2*k+6)*(2*k+3),6)
            assert a>bound and all(q>0 for q in ll)
            d=(k-6)*(4*k**4+54*k**3+409*k**2+1534*k+5335)+28560
            assert 15*(Q(a)-bound)==d
    # Independently exercise the exact Moore--Penrose interpolation image:
    x=[Q((i*11)%23-11) for i in range(120)]
    sx=sum(x)
    Ax=[sum(A[i][j]*x[j] for j in range(120)) for i in range(120)]
    z0=[sx/Q(120)]*120
    z3=[(Ax[i]+9*x[i]-72*z0[i])/12 for i in range(120)]
    zm=[x[i]-z0[i]-z3[i] for i in range(120)]
    for l in (0,2,4,6,8,10,12,14,20):
        a,b,c=three_values(l)
        eig=eigenvalues(l)
        blocks=(z0,z3,zm)
        feasible=[sum(blocks[j][i] for j in range(3) if eig[j]>0) for i in range(120)]
        coeff=[sum(blocks[j][i]/eig[j] for j in range(3) if eig[j]>0) for i in range(120)]
        sc=sum(coeff)
        Ac=[sum(A[i][j]*coeff[j] for j in range(120)) for i in range(120)]
        computed=[((a-b)*coeff[i]+(c-b)*Ac[i]+b*sc)/a for i in range(120)]
        assert computed==feasible
        if l in (8,12,14,20):assert feasible==x
        if l in (6,10):assert sum(feasible)==0
    print('PASS: 240 roots/120 lines, exact SRG parameters, selected direct kernels,')
    print('      symbolic point values, low-degree ranks and all-degree positivity bound.')

if __name__=='__main__':checks()
