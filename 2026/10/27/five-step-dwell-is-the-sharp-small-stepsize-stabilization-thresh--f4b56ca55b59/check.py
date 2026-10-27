#!/usr/bin/env python3
"""Independent exact polynomial and numerical checks for the switched reflected recurrence."""
import cmath
import numpy as np

def add(p,q):
    r=[0]*(max(len(p),len(q)))
    for i,v in enumerate(p): r[i]+=v
    for i,v in enumerate(q): r[i]+=v
    return r

def mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,v in enumerate(p):
        for j,w in enumerate(q): r[i+j]+=v*w
    return r

def scale(p,k): return [k*v for v in p]

def conj(p):return [v.conjugate() for v in p]

def norm(p): return mul(p,conj(p))

def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def trace(m):
    # u_0 = 0, u_1 = 1; u_(j+1) = (1-2ia)u_j + ia u_(j-1)
    u0=[0j];u1=[1+0j]
    seq=[u0,u1]
    for j in range(1,m+1):
        seq.append(add(mul([1,-2j],seq[-1]),mul([0,1j],seq[-2])))
    return trim(add(norm(seq[m+1]),[0,0]+norm(seq[m-1])))

def p_at_one(m):
    t=trace(m)
    p=add([1],scale(t,-1))
    return trim(add(p,[0]*(2*m)+[1]))

expected={
  1:[0,-3],
  2:[0,-2,-15],
  3:[0,-1,-4,-63],
  4:[0,0,-2,0,-255],
}
for m in range(1,5):
    coeff=trim(p_at_one(m))
    assert all(abs(z.imag)<1e-10 for z in coeff)
    ev=expected[m]
    # Expected indexing is in a^2, not in a.
    dense=[0]*(2*(len(ev)-1)+1)
    for j,v in enumerate(ev):dense[2*j]=v
    assert len(coeff)==len(dense) and all(abs(x-y)<1e-10 for x,y in zip(coeff,dense)),(m,coeff,dense)
for m in range(2,21):
    t=trace(m)
    assert abs(t[0]-1)<1e-10
    assert abs(t[2]-(4-m))<1e-10,(m,t[2])

def transfer(sign,a):
    return np.array([[1-2j*sign*a,1j*sign*a],[1,0]],dtype=complex)

def spectral_radius(a,m):
    M=np.linalg.matrix_power(transfer(-1,a),m)@np.linalg.matrix_power(transfer(1,a),m)
    t=sum(v*a**k for k,v in enumerate(trace(m)))
    assert abs(M.trace()-t)<5e-7
    assert abs(np.linalg.det(M)-a**(2*m))<5e-7
    return max(abs(v) for v in np.linalg.eigvals(M))
for a in [0.001,0.01,0.03]:
    for m in range(1,13):
        rho=spectral_radius(a,m)
        assert (rho>1+1e-13 if m<=4 else rho<1-1e-13),(a,m,rho)
print('PASS: exact four short-dwell polynomials; trace coefficients m=2..20; 36 Floquet checks.')
