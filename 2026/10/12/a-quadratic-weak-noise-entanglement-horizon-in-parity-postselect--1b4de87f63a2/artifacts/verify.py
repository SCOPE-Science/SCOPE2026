"""Independent finite arithmetic and small-system checks for the double-rail graph-state crossover."""
import itertools
import math
import numpy as np
import sympy as sp

BITS = np.array([[(s >> j) & 1 for j in range(4)] for s in range(16)], dtype=int)
D = np.array([[sum((int(BITS[s, i] * BITS[t, j]) ^ int(BITS[s, i+2] * BITS[t, j+2]))
                   for i in range(2) for j in range(2)) for t in range(16)] for s in range(16)], dtype=int)
PARITY = np.bitwise_xor.reduce(BITS, axis=1)
PROJ = [np.diag((PARITY == b).astype(float)) for b in (0, 1)]

def transfer(p):
    return (2*p - 1.) ** D

def boundary(a, aprime, p):
    return np.array([(2*p-1.) ** sum((int(a*bits[i]) ^ int(aprime*bits[i+2])) for i in range(2))
                     for bits in BITS], dtype=float)

def transfer_state(n, p):
    assert n >= 2 and n % 2 == 0 and 0 <= p <= 1
    T = transfer(p)
    scale = 64.*(1.-6.*p+24.*p*p) if p<.15 else 64.
    A = {}
    for da, db in itertools.product((0, 1), repeat=2):
        A[da, db] = np.linalg.matrix_power(PROJ[db] @ T @ PROJ[da] @ T @ PROJ[db] / scale, n//2-1)
    rho = np.zeros((4,4), dtype=float)
    for a,b,ap,bp in itertools.product((0,1), repeat=4):
        da,db=a^ap,b^bp
        rho[2*a+b,2*ap+bp] = (boundary(a,ap,p) @ PROJ[db] @ A[da,db] @ T @ PROJ[da] @ boundary(b,bp,p))
    return rho/np.trace(rho)

# Exact Taylor coefficients. This verifies the *whole 16-state* finite identities,
# not an extrapolation from a finite-range or finite-time simulation.
t0 = sp.Matrix(16,16,lambda i,j:int((-1)**D[i,j]))
t1 = sp.Matrix(16,16,lambda i,j:int((-1)**D[i,j]*(-2*D[i,j])))
t2 = sp.Matrix(16,16,lambda i,j:int((-1)**D[i,j]*(2*D[i,j]*(D[i,j]-1))))
S = [sp.diag(*[int(PARITY[i]==b) for i in range(16)]) for b in (0,1)]
expected = {(0,0):1536, (0,1):1280, (1,0):1280, (1,1):1088}
for da,db in itertools.product((0,1),repeat=2):
    P,Q=S[da],S[db]
    a0=Q*t0*P*t0*Q
    a1=Q*(t0*P*t1+t1*P*t0)*Q
    a2=Q*(t2*P*t0+t0*P*t2+t1*P*t1)*Q
    E=a0/64
    assert E*E==E and sp.trace(E)==1
    assert sp.trace(E*a1)==-384
    lam2=sp.trace(E*a2)+sp.trace(E*a1*(Q-E)*a1)/64
    assert lam2==expected[da,db],(da,db,lam2)

for a,b,ap,bp in itertools.product((0,1),repeat=4):
    x=sp.Matrix([(-1)**sum((a*int(bits[i]))^(ap*int(bits[i+2])) for i in range(2)) for bits in BITS])
    y=sp.Matrix([(-1)**sum((b*int(bits[i]))^(bp*int(bits[i+2])) for i in range(2)) for bits in BITS])
    assert (x.T*S[b^bp]*t0*S[a^ap]*y)[0]==64*(-1)**(a*b+ap*bp)

# Direct independent physical circuit: average every one of 256 possible failed-CZ
# patterns and all four accepted X-outcome records for two layers.
EDGES=[(0,1),(0,2),(1,3),(1,4),(2,3),(2,4),(3,5),(4,5)]
V=np.array([[(s>>i)&1 for i in range(6)] for s in range(64)])
EP=np.array([V[:,i]*V[:,j] for i,j in EDGES],dtype=int)
for p in (0., .12, .37, 1.):
    physical=np.zeros((4,4),float)
    for mask in range(256):
        e=np.array([(mask>>k)&1 for k in range(8)], dtype=int)
        w=(1-p)**int(e.sum())*p**int(8-e.sum())
        if w==0:continue
        signs=(-1.)**(e@EP)
        for r1,r2 in itertools.product((0,1),repeat=2):
            amps=np.zeros(4)
            for k,site in enumerate(V):
                a,b=int(site[0]),int(site[5]); y=int(site[1]+site[2]);z=int(site[3]+site[4])
                outcome=(-1.)**(r1*y+r2*z+r2*a+r1*b)
                amps[2*a+b]+=signs[k]*outcome
            physical+=w*np.outer(amps,amps)
    physical/=np.trace(physical)
    assert np.max(np.abs(physical-transfer_state(2,p)))<2.e-13

def limiting_state(c):
    u,v=math.exp(-2*c),math.exp(-3.5*c)
    return np.array([[(-1.)**(a*b+ap*bp)*([1.,u,v][(a!=ap)+(b!=bp)])/4
                       for ap,bp in itertools.product((0,1),repeat=2)]
                      for a,b in itertools.product((0,1),repeat=2)])

for c in (.1, .32, .6, 1.0):
    lim=limiting_state(c)
    assert abs(np.trace(lim)-1)<1e-13
    n=2*round(c/(2*.002**2))
    test=transfer_state(n,.002)
    assert np.max(np.abs(test-lim))<.002
    pt=np.array([[lim[(i//2)*2+j%2,(j//2)*2+i%2] for j in range(4)] for i in range(4)])
    negativity=max(0.,-min(np.linalg.eigvalsh(pt)))
    expected_neg=max(0.,(2*math.exp(-2*c)+math.exp(-3.5*c)-1)/4)
    assert abs(negativity-expected_neg)<1e-12

import scipy.optimize
cutoff=scipy.optimize.brentq(lambda c:2*math.exp(-2*c)+math.exp(-3.5*c)-1,.1,1.)
assert .4<cutoff<.6
print('VERIFY_OK 4 exact Taylor sectors, 16 exact boundary identities, 4096 weighted physical branches over 4 noise levels, 4 scaling limits, negativity, cutoff',format(cutoff,'.12f'))
