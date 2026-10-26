#!/usr/bin/env python3
"""Exact algebraic verification for a planar semidissipative Runge--Kutta benchmark."""
import sympy as sp

h, t = sp.symbols('h t', real=True)
L = sp.Matrix([[-1, -1], [1, 0]])
checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def equal(a, b):
    check(sp.simplify(a-b) == 0, 'polynomial identity')

R = {}
B = {}
for p in (2, 3, 4):
    R[p] = sp.eye(2)
    for k in range(1, p + 1):
        R[p] += (h*L)**k / sp.factorial(k)
    B[p] = R[p].T*R[p] - sp.eye(2)
    check(R[p].shape == (2,2), 'matrix dimension')

E = h**5-3*h**4+3*h**3-6*h**2+36*h-72
C = (h-1)**3-5
G = h**3-6*h**2+18*h-24
F3 = h**5-3*h**3-24*h**2+72*h-72
Q = h**4-2*h**3+48
F4 = h**7-4*h**6+4*h**5-96*h**2+576*h-1152
P = h**5-8*h**3-48*h**2+288*h-384

equal(B[2][0,0],h*(h-2)*(h*h-2*h+4)/4)
equal(B[2][1,1],h**3*(h-2)/2)
equal(B[2].det(),h**4*(h-2)**2*(h*h+4)/16)
equal(B[3][0,0],h*F3/36)
equal(B[3][1,1],h**3*G/36)
equal(B[3].det(),h**4*C*E/1296)
equal(B[4][1,1],h**3*P/576)
equal(B[4].det(),h**4*(h-2)*Q*F4/331776)
equal(E.subs(h,2+t),t**5+7*t**4+19*t**3+20*t**2+32*t-16)
equal(F3.subs(h,2+t),t**5+10*t**4+37*t**3+38*t**2+20*t-16)
equal(G,(h-2)**3+6*(h-2)-4)
equal(sp.diff(G,h),3*(h-2)**2+6)
equal(sp.diff(E,h),h*h*(5*h*h-12*h+9)+36-12*h)
equal(F4,h**5*(h-2)**2-96*((h-3)**2+3))
equal(F4.subs(h,3+t),t**7+17*t**6+121*t**5+465*t**4+1035*t**3+1227*t**2+891*t-45)
equal(P,h**3*(h*h-8)+48*(1-(h-3)**2))
equal(P.subs(h,3+t),t**5+15*t**4+82*t**3+150*t**2+189*t+75)
check(E.subs(h,2)==-16,'root lower bracket')
check(E.subs(h,sp.Rational(5,2))==sp.Rational(251,32),'root upper bracket')
check(G.subs(h,sp.Rational(5,2))==-sp.Rational(7,8),'G bracket')
check(F3.subs(h,sp.Rational(5,2))==sp.Rational(281,32),'F3 bracket')
check(F4.subs(h,3)==-45,'F4 initial sign')
check(sp.factor(B[2].subs(h,2)) == sp.zeros(2),'RK2 boundary')
check(sp.simplify(R[3].subs(h,2)-sp.eye(2)/3)==sp.zeros(2),'RK3 interior')
check(sp.simplify(R[4].subs(h,2)-sp.Matrix([[-1,-2],[2,1]])/3)==sp.zeros(2),'RK4 boundary')

q=sp.Rational(9,4)
check(B[3][1,1].subs(h,q)==-sp.Rational(12879,16384),'rational RK3 diag')
check(B[3].det().subs(h,q)==sp.Rational(103915305,268435456),'rational RK3 det')
check(B[4].det().subs(h,q)==-sp.Rational(5845760259183,17592186044416),'rational RK4 det')
check(sp.trace(R[4].subs(h,q))==-sp.Rational(107,2048),'rational RK4 trace')
check(R[4].det().subs(h,q)==sp.Rational(1949353,4194304),'rational RK4 spectral modulus')
check(sp.trace(R[4].subs(h,q))**2 < 4*R[4].det().subs(h,q),'complex conjugate spectrum')
check(R[4].det().subs(h,q) < 1,'stable spectral radius')

# Extra rational spot checks, not replacements for the analytic half-line proof.
for j in range(1,32):
    hh=sp.Rational(j,16)
    for p in (2,3,4):
        Bb=B[p].subs(h,hh)
        check(Bb[1,1]<0 and Bb.det()>0, 'strictly contractive rational step')
for j in range(1,17):
    hh=2+sp.Rational(j,64)
    Bb3=B[3].subs(h,hh)
    Bb4=B[4].subs(h,hh)
    check(Bb3[1,1]<0 and Bb3.det()>0,'RK3 beyond RK4 cutoff')
    check(Bb4.det()<0,'RK4 beyond own cutoff')
for j in range(1,8):
    hh=sp.Rational(5,2)+sp.Rational(j,2)
    for p in (2,3,4):
        Bb=B[p].subs(h,hh)
        check(not (Bb[1,1]<=0 and Bb[0,0]<=0 and Bb.det()>=0),'eventual no contractivity')
print(f'PASS: {checks} exact symbolic or rational assertions')
