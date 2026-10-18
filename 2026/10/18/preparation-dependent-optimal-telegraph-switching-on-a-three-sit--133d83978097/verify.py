"""Independent checks for the three-site telegraph-hopping population theorem.

Usage: python verify.py  (requires numpy, scipy, sympy)
"""
import numpy as np
from scipy.linalg import expm, eigvals
from scipy.optimize import brentq
from sympy import symbols, factor, discriminant


def reduced(a, lam):
    # population p1,p2,p3; weighted coherences c12,c23,D13
    return np.array([
        [0, 0, 0, 2*a, 0, 0],
        [0, 0, 0, -2*a, 2*a, 0],
        [0, 0, 0, 0, -2*a, 0],
        [-a, a, 0, -2*lam, 0, -a],
        [0, -a, a, 0, -2*lam, a],
        [0, 0, 0, a, -a, -4*lam],
    ], dtype=float)


def dense(a,lam):
    E=np.eye(3); states=[(-1,-1),(-1,1),(1,-1),(1,1)]
    big=np.zeros((36,36),dtype=complex)
    for k,(u,v) in enumerate(states):
        H=np.array([[0,a*u,0],[a*u,0,a*v],[0,a*v,0]])
        big[9*k:9*k+9,9*k:9*k+9]=-1j*(np.kron(E,H)-np.kron(H.T,E))-2*lam*np.eye(9)
        for st in [(-u,v),(u,-v)]:
            h=states.index(st)
            big[9*k:9*k+9,9*h:9*h+9]+=lam*np.eye(9)
    return big


checks=0
for a in [.7,1.5]:
    for lam in [.1,.65,1.41,2.31,5.2]:
        M=reduced(a,lam); L=dense(a,lam)
        for initial in [0,1,2]:
            state=np.zeros(36,complex)
            rho=np.zeros((3,3));rho[initial,initial]=.25
            for j in range(4):state[9*j:9*j+9]=rho.reshape(-1,order='F')
            v=np.zeros(6);v[initial]=1
            for t in [.2,.9,3.1]:
                out=expm(L*t)@state
                dens=np.array([out[9*j:9*j+9].reshape(3,3,order='F') for j in range(4)]).sum(axis=0)
                red=expm(M*t)@v
                assert np.max(np.abs(np.diag(dens)-red[:3]))<2e-12
                assert np.max(np.abs(dens-dens.conj().T))<2e-12
                assert abs(np.trace(dens)-1)<2e-12
                checks+=1
        # analytic characteristic factors, tested against reduced matrix
        roots=np.concatenate(([0],np.roots([1,2*lam,2*a*a]),np.roots([1,6*lam,8*lam**2+8*a*a,24*a*a*lam])))
        spec=eigvals(M)
        assert max(min(abs(x-y) for y in spec) for x in roots)<2e-8
        checks+=1

z,l,a=symbols('z l a',real=True)
p=z**3+6*l*z**2+(8*l*l+8*a*a)*z+24*a*a*l
assert factor(discriminant(p,z)+64*(32*a**6-21*a**4*l**2+24*a**2*l**4-4*l**6))==0
crit=brentq(lambda x:32-21*x*x+24*x**4-4*x**6,2,3,xtol=1e-14)
max_c=2*crit-np.sqrt((4*crit**2-8)/3)
assert abs(crit-2.3008118172002835)<2e-13
assert abs(max_c-2.505998025926741)<2e-13
for x in np.concatenate((np.linspace(.05,crit-.005,110),np.linspace(crit+.005,12,110))):
    rr=np.roots([1,6*x,8*x*x+8,24*x]);gap=-max(r.real for r in rr)
    assert gap<max_c+1e-10
    qr=np.roots([1,2*x,2]);qgap=-max(r.real for r in qr)
    assert qgap+1e-8<gap
print(f'VERIFY_OK dense_populations={checks} cubic_gap_grid=220 critical_rate={crit:.12f} center_gap={max_c:.12f} end_gap={np.sqrt(2):.12f}')
