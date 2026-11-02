"""Exact rational checks for spherical harmonic Gram spectra on the A4 root orbit.
The analytic all-degree bounds are in RESULT.md; finite tests here are corroborating.
"""
from fractions import Fraction
from itertools import combinations

EDGES=list(combinations(range(5),2))
N=len(EDGES)

def U(k,x):
    if k==0:return Fraction(1)
    a,b=Fraction(1),2*x
    for _ in range(2,k+1):a,b=b,2*x*b-a
    return b

def dot(e,f):
    a,b=e; c,d=f
    return Fraction((a==c)-(a==d)-(b==c)+(b==d),2)

def matmul(A,B):
    return [[sum(A[i][t]*B[t][j] for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def check(k):
    gram=[[U(k,dot(e,f))/Fraction(k+1) for f in EDGES] for e in EDGES]
    a=U(k,Fraction(1,2))/Fraction(k+1)
    b=U(k,Fraction(0))/Fraction(k+1)
    if k%2:
        l1=1+3*a; l2=1-2*a
        mult=[4,6]; vals=[l1,l2]
        # Signed incidence B has Gram eigenvalues 5 (multiplicity 4) and 0 (multiplicity 6)
        B=[[int(e[0]==i)-int(e[1]==i) for e in EDGES] for i in range(5)]
        BTB=matmul(list(zip(*B)),B)
        proj=[[Fraction(BTB[i][j],5) for j in range(N)] for i in range(N)]
        expected=[[l1*proj[i][j]+l2*(int(i==j)-proj[i][j]) for j in range(N)] for i in range(N)]
    else:
        l0=1+6*a+3*b;l1=1+a-2*b;l2=1-2*a+b
        vals=[l0,l1,l2]; mult=[1,4,5]
        # P0=J/10; P1=(incidence^T incidence-4J/5)/3, P2=I-P0-P1.
        inc=[[int(i in e) for e in EDGES] for i in range(5)]
        C=matmul(list(zip(*inc)),inc)
        P0=[[Fraction(1,10) for j in range(N)] for i in range(N)]
        # C eigen 8 on constant, 3 on standard, 0 on shape(3,2).
        P1=[[(Fraction(C[i][j])-8*P0[i][j])/3 for j in range(N)] for i in range(N)]
        P2=[[Fraction(int(i==j))-P0[i][j]-P1[i][j] for j in range(N)] for i in range(N)]
        expected=[[l0*P0[i][j]+l1*P1[i][j]+l2*P2[i][j] for j in range(N)] for i in range(N)]
    assert gram==expected,(k,'matrix spectrum disagreement')
    assert sum(mult)==10
    assert all(v>=0 for v in vals)
    if k>=3:
        assert all(v>0 for v in vals)
        assert min(vals)>=Fraction(2,11)
        assert max(vals)<=Fraction(22,13)
        assert max(vals)/min(vals)<=6
        assert (max(vals)/min(vals)==6)==(k in (3,10))
    if k==0:assert vals==[10,0,0]
    if k==1:assert vals==[Fraction(5,2),0]
    if k==2:assert vals==[0,Fraction(5,3),Fraction(2,3)]
    return vals,mult

if __name__=='__main__':
    for k in range(0,301):
        v,m=check(k)
        if k in (0,1,2,3,4,5,6,7,8,9,10,11,12):print(k,v,m)
    print('A4_HARMONIC_EXACT_CHECK_OK 301 degrees; all 10x10 entries and spectral constraints')
