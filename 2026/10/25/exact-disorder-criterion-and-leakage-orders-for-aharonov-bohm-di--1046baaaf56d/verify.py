#!/usr/bin/env python3
"""Reproducible numerical checks for weighted diamond-chain caging.

Only finite periodic matrices are tested. The infinite-chain statements
are justified analytically in RESULT.md, not by these experiments.
"""
import numpy as np
from numpy.linalg import norm, eigvalsh
from scipy.linalg import expm
import sympy as sp

RNG = np.random.default_rng(417028)


def example(n):
    assert n >= 4
    l = (RNG.uniform(.3, 1.8, (n, 2)) * np.exp(1j * RNG.uniform(-3, 3, (n, 2))))
    r = np.column_stack((-np.conj(l[:, 1]), np.conj(l[:, 0]))) * (
        RNG.uniform(.3, 1.9, n) * np.exp(1j * RNG.uniform(-3, 3, n)))[:, None]
    eps = RNG.uniform(-1.7, 1.7, n)
    v = RNG.uniform(-1.8, 1.8, n)
    return l, r, eps, v


def model(l, r, eps, v, asym=None):
    n = len(v)
    H = np.zeros((3*n, 3*n), dtype=complex)
    for j in range(n):
        H[j,j] = v[j]
        for k in range(2):
            arm = n + 2*j + k
            H[arm,arm] = eps[j] if asym is None else (eps[j] + asym[j,k])
            H[arm,j] = l[j,k]
            H[arm,(j+1)%n] = r[j,k]
            H[j,arm] = np.conj(l[j,k])
            H[(j+1)%n,arm] = np.conj(r[j,k])
    return H


def unitary(l,r):
    n = len(l)
    U = np.zeros((3*n,3*n),complex)
    for j in range(n):
        U[j,3*j] = 1
        U[n+2*((j-1)%n):n+2*((j-1)%n)+2,3*j+1] = r[(j-1)%n]/norm(r[(j-1)%n])
        U[n+2*j:n+2*j+2,3*j+2] = l[j]/norm(l[j])
    return U


def leading(H, i, j, order):
    # Coefficient in the matrix-exponential Taylor series
    from math import factorial
    return ((-1j)**order/factorial(order)) * np.linalg.matrix_power(H,order)[i,j]


# A symbolic four-site transfer calculation independently checks the
# first two potentially nonzero hub-to-hub Taylor coefficients.
a,b,eu,ed,xu,xd,yu,yd,Xu,Xd,Yu,Yd = sp.symbols(
    'a b eu ed xu xd yu yd Xu Xd Yu Yd')
Z=sp.Matrix([[a,Xu,Xd,0],
             [xu,eu,0,yu],
             [xd,0,ed,yd],
             [0,Yu,Yd,b]])
S = Yu*xu+Yd*xd
assert sp.expand((Z**2)[3,0]-S)==0
assert sp.expand((Z**3)[3,0]-(a+b)*S-(eu*Yu*xu+ed*Yd*xd))==0

stats = {'balanced_blocks':0,'balanced_spectra':0,'balanced_dynamics':0,
         'flux_breaking':0,'potential_breaking':0,'special_examples':0,'symbolic_identities':2,'time_asymptotics':0}
for trial in range(650):
    n = int(RNG.integers(4,10))
    l,r,eps,v = example(n)
    H = model(l,r,eps,v)
    U = unitary(l,r)
    if norm(U.conj().T@U-np.eye(3*n),ord=np.inf)>3e-13:
        raise AssertionError('nonunitary basis')
    B = U.conj().T@H@U
    target = np.zeros_like(B)
    for j in range(n):
        left = norm(r[(j-1)%n]); right = norm(l[j])
        target[3*j:3*j+3,3*j:3*j+3] = [
            [v[j],left,right],
            [left,eps[(j-1)%n],0],
            [right,0,eps[j]],
        ]
    assert norm(B-target,ord=np.inf)<4e-13
    stats['balanced_blocks']+=1
    assert np.allclose(eigvalsh(H),eigvalsh(target),rtol=2e-12,atol=2e-12)
    stats['balanced_spectra']+=1
    j=int(RNG.integers(n))
    z=expm(-1j*H*float(RNG.uniform(.1,3)) )[:,j]
    supported = {j,n+2*j,n+2*j+1,n+2*((j-1)%n),n+2*((j-1)%n)+1}
    assert norm(z[[k for k in range(3*n) if k not in supported]])<4e-13
    stats['balanced_dynamics']+=1
    # Generic hopping detuning produces an order-t^2 cross-hub amplitude.
    r2=r.copy(); r2[j,0] *= (1+float(RNG.uniform(.08,.5)))
    HB=model(l,r2,eps,v)
    a=(j+1)%n
    S=np.vdot(r2[j],l[j])
    assert abs(S)>1e-4
    assert abs(leading(HB,a,j,2)+S/2)<1e-12
    stats['flux_breaking']+=1
    # Equal arm on-sites broken on a single arm, but flux remains balanced.
    asym=np.zeros((n,2)); asym[j,0]=float(RNG.uniform(.2,1.2))
    HD=model(l,r,eps,v,asym)
    assert abs(leading(HD,a,j,2))<2e-13
    pred=np.conj(r[j,0])*l[j,0]*asym[j,0]
    assert abs(leading(HD,a,j,3)-1j*pred/6)<1e-12
    stats['potential_breaking']+=1
    if trial<125:
        t=0.015
        pH=abs(expm(-1j*HB*t)[a,j])**2
        pD=abs(expm(-1j*HD*t)[a,j])**2
        assert abs(pH / ((abs(S)**2/4)*t**4)-1)<0.12
        assert abs(pD / ((abs(pred)**2/36)*t**6)-1)<0.12
        stats['time_asymptotics']+=1

# Closed-form fixed example verifies coexistence of strong nonuniformity and perfect caging.
n=5
l=np.tile(np.array([1+1j,2-1j]),(n,1))
r=np.tile(np.array([-2-1j,1-1j]),(n,1))  # orthogonality checked explicitly
assert abs(np.vdot(r[0],l[0]))<1e-14
v=np.array([-2.,1.,0.,-1.,2.]); eps=np.array([1.,-2.,3.,.5,-.5]);
H=model(l,r,eps,v)
U=unitary(l,r)
B=U.conj().T@H@U
assert max(abs(B[i,j]) for i in range(3*n) for j in range(3*n) if i//3 !=j//3)<1e-13
expected=[]
for j in range(n):
    expected.extend(eigvalsh(np.array([
        [v[j],norm(r[(j-1)%n]),norm(l[j])],
        [norm(r[(j-1)%n]),eps[(j-1)%n],0],
        [norm(l[j]),0,eps[j]]])))
assert np.allclose(eigvalsh(H),sorted(expected),atol=2e-12)
stats['special_examples']+=1
print(stats)
print('TOTAL_ASSERTION_GROUPS=',sum(stats.values()))
