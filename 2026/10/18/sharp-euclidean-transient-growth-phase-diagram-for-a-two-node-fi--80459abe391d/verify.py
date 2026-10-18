#!/usr/bin/env python3
"""Exact-arithmetic checks for the two-interior-node heat FEM phase diagram.

No external packages or external files are required.
"""
from fractions import Fraction as Q
from random import Random

checks = 0

def check(ok, message):
    global checks
    if not ok:
        raise AssertionError(message)
    checks += 1

def mmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def inverse(A):
    d = det(A)
    return [[A[1][1]/d, -A[0][1]/d], [-A[1][0]/d, A[0][0]/d]]

def assembly(u, v):
    # Independently assemble the two 2x2 interior blocks from the 3 elements,
    # whose nodal indices are 0,1,2,3. Zero boundary values at 0 and 3.
    h = [u, Q(1), v]
    mass = [[Q(0), Q(0)], [Q(0), Q(0)]]
    stiffness = [[Q(0), Q(0)], [Q(0), Q(0)]]
    for e, length in enumerate(h):
        for a in (0,1):
            for b in (0,1):
                ia, ib = e+a, e+b
                if ia in (1,2) and ib in (1,2):
                    mloc=length*Q(2 if a==b else 1,6)
                    kloc=Q(1 if a==b else -1)/length
                    mass[ia-1][ib-1]+=mloc
                    stiffness[ia-1][ib-1]+=kloc
    return mass, stiffness

def analytic(u, v):
    d = 4*u*v+4*u+4*v+3
    X = 2*u*v+3*u+2*v+2
    Y = 2*u*v+2*u+3*v+2
    Z = 2*u*u*v+2*u*v*v+6*u*v+u+v
    H = [[6*X/(u*d), -3*Z/(u*v*d)],[-3*Z/(u*v*d), 6*Y/(v*d)]]
    Delta = 4*u*v*X*Y-Z*Z
    return H, Delta, d

def poly(r):
    return 4*r**4-44*r**3-79*r**2-62*r+1

r=Random(271828)
parameters = [(Q(a,b),Q(c,d)) for a in (1,2,3,4,11,20,100) for b in (1,3,8)
              for c in (1,2,3,11,20) for d in (1,2,7)]
for _ in range(1200):
    parameters.append((Q(r.randrange(1,300),r.randrange(1,300)),
                       Q(r.randrange(1,300),r.randrange(1,300))))
for u,v in parameters:
    M,K=assembly(u,v)
    check(M[0][0]>0 and det(M)>0,'mass SPD')
    check(K[0][0]>0 and det(K)>0,'stiffness SPD')
    B=mmul(inverse(M),K)
    H=[[ (B[i][j]+B[j][i])/2 for j in range(2)] for i in range(2)]
    Ha,Delta,d=analytic(u,v)
    check(H==Ha,f'assemble-versus-formula u={u} v={v}')
    check(det(H)==9*Delta/(u*u*v*v*d*d),'det identity')
    check(H[0][0]>0 and H[1][1]>0,'positive H diagonal')
    check(B[0][1]<0 and B[1][0]<0,'positivity generator')
    check((Delta>=0)==(det(H)>=0),'phase identity')

for q in [Q(1,10_000),Q(1,1000),Q(1,100),Q(1,50),Q(1,10),Q(1),Q(10),Q(20),Q(100)]:
    _,D,d=analytic(Q(1),q)
    check(D==-poly(q),'one-parameter quartic reduction')

# Rational root enclosures; Descartes' sign rule and IVT supply global uniqueness.
check(poly(Q('0.01580'))>0 and poly(Q('0.01582'))<0,'lower root bracket')
check(poly(Q('12.6570'))<0 and poly(Q('12.6571'))>0,'upper root bracket')
check(poly(Q(1))<0,'central contractive region')

M,K=assembly(Q(1),Q(20))
B=mmul(inverse(M),K)
A=[[-x for x in row] for row in B]
H=[[(A[i][j]+A[j][i])/2 for j in range(2)] for i in range(2)]
w=[Q(1),Q(3)]
vHv=sum(w[i]*H[i][j]*w[j] for i in range(2) for j in range(2))
check(vHv==Q(921,1670),'strictly positive witness quadratic form')
check(2*vHv==Q(921,835),'Euclidean norm square derivative')

M,K=assembly(Q(1),Q(1,100))
B=mmul(inverse(M),K)
A=[[-x for x in row] for row in B]
H=[[(A[i][j]+A[j][i])/2 for j in range(2)] for i in range(2)]
w=[Q(1),Q(1,10)]
check(sum(w[i]*H[i][j]*w[j] for i in range(2) for j in range(2))==Q(453,295),
      'bounded-mass-contrast positive-data witness')

# Exact leading coefficient for r -> 0:
# limit r H_B = [[0,-3/7],[-3/7,24/7]] and det asymptotics.
for n in (4,6,8):
    q=Q(1,10**n)
    H,_,_=analytic(Q(1),q)
    # Rational error bounded O(r) in each entry from the derived formulas.
    target=[[Q(0),-Q(3,7)],[-Q(3,7),Q(24,7)]]
    check(all(abs(q*H[i][j]-target[i][j])<100*q for i in range(2) for j in range(2)),
          'small-element limiting symmetric operator')

print('PASS', checks, 'exact-rational checks')
