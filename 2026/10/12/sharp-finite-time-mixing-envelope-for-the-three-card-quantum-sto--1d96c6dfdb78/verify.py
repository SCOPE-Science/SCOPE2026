#!/usr/bin/env python3
"""Reconstruct the six-state quantum stochastic walk and its sharp control envelope.

Only Python's standard library is used. This script tests finite instances;
proof of the continuum optimum and asymptotics is in RESULT.md.
"""
import cmath
import itertools
import math
from fractions import Fraction

PERMS=list(itertools.permutations(range(3)))
POS={p:j for j,p in enumerate(PERMS)}
E=POS[(0,1,2)]
N=len(PERMS)


def compose(a,b):
    return tuple(a[b[j]] for j in range(3))


def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(N)) for j in range(N)] for i in range(N)]


def ident():
    return [[int(i==j) for j in range(N)] for i in range(N)]


def transpose_matrix(a):
    return [[a[j][i] for j in range(N)] for i in range(N)]


def matrix_norm(a):
    return max(abs(a[i][j]) for i in range(N) for j in range(N))


trans=[]
for a in PERMS:
    if sum(a[j]!=j for j in range(3))==2:
        trans.append(a)
assert len(trans)==3
H=[[0.0]*N for _ in range(N)]
for g in range(N):
    for t in trans:
        H[POS[compose(t,PERMS[g])]][g]+=1/3
H2=mul(H,H)
I=ident()
PP=[[0.5*(H2[i][j]+H[i][j]) for j in range(N)] for i in range(N)]
PM=[[0.5*(H2[i][j]-H[i][j]) for j in range(N)] for i in range(N)]
P0=[[I[i][j]-H2[i][j] for j in range(N)] for i in range(N)]
check_count=0
for P in (PP,PM,P0):
    assert matrix_norm([[mul(P,P)[i][j]-P[i][j] for j in range(N)] for i in range(N)])<1e-12
    check_count+=1
assert matrix_norm([[PP[i][j]+PM[i][j]+P0[i][j]-I[i][j] for j in range(N)] for i in range(N)])<1e-12
check_count+=1


def direct_p(x,theta):
    # Matrix propagation of the classical kernel and the unitary walk, independently
    # of character formulas used in the proof.
    classical=[PP[j][E]+x*x*PM[j][E]+x*P0[j][E] for j in range(N)]
    U=[[cmath.exp(-1j*theta)*PP[g][h]+cmath.exp(1j*theta)*PM[g][h]+P0[g][h]
        for h in range(N)] for g in range(N)]
    return [sum(abs(U[g][h])**2*classical[h] for h in range(N)) for g in range(N)]


def formula_p(x,c):
    xi=x*x*(1+2*c*c)/3
    eta=x*(1+2*c)/3
    answer=[]
    for p in PERMS:
        if p==(0,1,2): answer.append((1+xi+4*eta)/6)
        elif sum(p[k]!=k for k in range(3))==2: answer.append((1-xi)/6)
        else: answer.append((1+xi-2*eta)/6)
    return answer


def tv(x,c):
    xi=x*x*(1+2*c*c)/3
    eta=x*(1+2*c)/3
    return (abs(xi+4*eta)+3*xi+2*abs(xi-2*eta))/12


def star(x):
    return (2-math.sqrt(4+4*x-2*x*x))/(2*x)


for x in (.0001,.04,.2,.5,.9,.999):
    for theta in (-10.0,-2.5,-math.pi/2,0,1.0,math.pi,7.21):
        p=direct_p(x,theta)
        q=formula_p(x,math.cos(theta))
        assert max(abs(a-b) for a,b in zip(p,q))<2e-13
        assert abs(sum(p)-1)<2e-13
        assert abs(.5*sum(abs(z-1/6) for z in p)-tv(x,math.cos(theta)))<2e-13
        check_count+=3
    c=star(x)
    assert -0.5<c<0
    assert abs(x*(1+2*c)/3-x*x*(1+2*c*c)/6)<3e-14
    m=tv(x,c)
    assert abs(m-x*x*(1+2*c*c)/6)<3e-14
    for j in range(3001):
        cj=-1+2*j/3000
        assert tv(x,cj)>m-1e-13
        check_count+=1
    check_count+=3

# Exact rational arithmetic verifies the class-mode formulas (no floating rounding).
for x in (Fraction(1,3),Fraction(2,5),Fraction(3,4)):
    for c in (Fraction(-1),Fraction(-2,3),Fraction(0),Fraction(1,5),Fraction(1)):
        p=formula_p(x,c)
        assert sum(p)==1
        assert all(z>=0 for z in p)
        assert sum(abs(z-Fraction(1,6)) for z in p)/2==tv(x,c)
        check_count+=3

for x in (1e-4,1e-5,1e-6):
    c=star(x)
    m=tv(x,c)
    assert abs(m/x**2-1/4)<0.01
    assert abs((m/((x*x+4*x)/6))/x-3/8)<0.01
    check_count+=2

print(f'VERIFY_OK {check_count} six_state_checks, sharp_envelope and asymptotic_ratio')
