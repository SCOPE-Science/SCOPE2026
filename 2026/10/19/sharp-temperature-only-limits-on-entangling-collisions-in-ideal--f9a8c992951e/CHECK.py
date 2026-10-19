#!/usr/bin/env python3
"""Reproducibility checks for the two-qubit thermal collision entanglement theorem.

Requires only the Python 3 standard library. Each quantum collision is
independently implemented by 4x4 matrix multiplication, rather than by
reusing the concurrence recurrence.
"""
from fractions import Fraction as F
from math import ceil, log, sqrt
from itertools import product

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def threshold(p, h, protocol):
    r = p if protocol == '+' else (1-p)
    return 2*r/(sqrt(1+4*h*(1-h))-1+2*r)

def count(p, h, protocol):
    z = threshold(p,h,protocol)
    return ceil(log(z)/log(h))

def entanglement_polynomial(p,h,k,protocol):
    r = p if protocol == '+' else 1-p
    x = 1-r
    z = h**(k-1)
    return h*(1-h)*z*z-r*(1-z)*(r+x*z)

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(4))
             for j in range(4)] for i in range(4)]

def adj(a):
    return [[a[j][i].conjugate() for j in range(4)] for i in range(4)]

def collision(q,p,c,s,protocol):
    # Basis: |system,ancilla> = 00,01,10,11.
    v=[(1-q)*(1-p),(1-q)*p,q*(1-p),q*p]
    rho=[[complex(v[i]) if i==j else 0j for j in range(4)] for i in range(4)]
    U=[[1+0j if i==j else 0j for j in range(4)] for i in range(4)]
    a,b=(0,3) if protocol=='+' else (1,2)
    U[a][a]=U[b][b]=complex(c)
    U[a][b]=U[b][a]=-1j*float(s)
    M=mm(mm(U,rho),adj(U))
    q_new=(M[2][2]+M[3][3]).real
    w=abs(M[a][b])
    inert=(1,2) if protocol=='+' else (0,3)
    # Negative partial transpose iff |offdiag|^2>product of inert diagonals.
    d=(M[inert[0]][inert[0]]*M[inert[1]][inert[1]]).real-w*w
    return q_new,d,M

for p in (F(1,100),F(1,10),F(2,5),F(1,2),F(4,5)):
    for c,s in ((F(3,5),F(4,5)),(F(4,5),F(3,5)),
                (F(5,13),F(12,13)),(F(12,13),F(5,13))):
        h=c*c
        for protocol in ('+','-'):
            N=count(float(p),float(h),protocol)
            r=p if protocol=='+' else 1-p
            check(1<=N<=ceil(1/float(r)), 'sharp uniform cap')
            # Exact rational sign at every relevant collision.
            for k in range(1,N+5):
                P=entanglement_polynomial(p,h,k,protocol)
                check((P>0)==(k<=N),f'polynomial cutoff p={p} h={h} {protocol} k={k}')
                q=(1-p if protocol=='+' else p)*(1-h**(k-1))
                q_new,d,M=collision(float(q),float(p),c,s,protocol)
                predicted_q=(1-p if protocol=='+' else p)*(1-h**k)
                check(abs(q_new-float(predicted_q))<3e-13,'system population recurrence')
                check((d < -1e-13) == (P > 0) or abs(d)<1e-13,
                      'matrix partial-transpose test')
                check(abs(sum(M[j][j].real for j in range(4))-1)<1e-13,'trace')
                check(max(abs(M[i][j]-M[j][i].conjugate())
                          for i in range(4) for j in range(4))<1e-13,'Hermiticity')

# Sharpness: as the angle approaches zero, the exact cutoff reaches the cap.
for p in (F(1,10),F(1,5),F(2,5),F(1,2),F(4,5)):
    h=(F(999999,1000000))**2
    for protocol in ('+','-'):
        r=float(p if protocol=='+' else 1-p)
        check(count(float(p),float(h),protocol)==ceil(1/r), 'uniform cap sharpness')

# A cold bath has long anti-thermalizing lifetime and <= 2 ordinary events.
for p in (0.1,0.01,0.001):
    check(count(p,0.5,'-')<=2,'ordinary thermal bound')
    check(count(p,0.5,'+')>count(p,0.5,'-'),'protocol separation')

# Exactly zero bath excitation: the ordinary protocol is stationary and
# unentangling, whereas the pair-creation protocol has positive concurrence
# at every finite collision for any interaction angle in (0, pi/2).
for c,s in ((0.6,0.8),(0.8,0.6)):
    q=0.
    for k in range(1,15):
        q_new,d,_=collision(q,0.,c,s,'+')
        check(d<0.,'cold anti-protocol remains entangled')
        q=q_new
    q=0.
    for k in range(1,15):
        q_new,d,_=collision(q,0.,c,s,'-')
        check(abs(q_new)<1e-15 and abs(d)<1e-15,'cold ordinary protocol inert')
        q=q_new

print(f'PASS: {checks} independent exact-rational and matrix assertions')
