#!/usr/bin/env python3
import math
import numpy as np

sx=np.array([[0,1],[1,0]],complex)
sy=np.array([[0,-1j],[1j,0]],complex)
sz=np.array([[1,0],[0,-1]],complex)
I=np.eye(2,dtype=complex)
paulis=(sx,sy,sz)
YY=np.kron(sy,sy)

def op(a,b,c):
    return np.kron(np.kron(a,b),c)

def hamiltonian(J,J1):
    H=np.zeros((8,8),complex)
    for s in paulis:
        H += J1*(op(s,s,I)+op(s,I,s)) + J*op(I,s,s)
    return H

def thermal_state(J,J1,T):
    w,v=np.linalg.eigh(hamiltonian(J,J1))
    p=np.exp(-(w-w.min())/T)
    rho=(v*p)@v.conj().T
    return rho/np.trace(rho)

def trace_spin3(rho):
    R=rho.reshape(2,2,2,2,2,2)
    return np.einsum('abcdec->abde',R).reshape(4,4)

def concurrence(rho):
    vals=np.linalg.eigvals(rho@YY@rho.conj()@YY).real
    s=np.sort(np.sqrt(np.maximum(vals,0.0)))[::-1]
    return max(0.0,float(s[0]-s[1]-s[2]-s[3]))

def formula(J,J1,T):
    A=math.exp((4*J1-J)/T)
    B=math.exp(3*J/T)
    C=math.exp(-(2*J1+J)/T)
    Z=2*A+2*B+4*C
    return max(0.0,(A-B-4*C)/Z)

def F(u,r):
    # Stable enough for the tested ranges.
    return math.exp(6*u)-math.exp((2+4*r)*u)-4

def ucrit(r):
    lo=0.0; hi=1.0
    while F(hi,r)<0:
        hi*=2
    for _ in range(120):
        mid=(lo+hi)/2
        if F(mid,r)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

def lambertw_pos(x):
    w=math.log(x)
    if x>math.e:
        w-=math.log(w)
    for _ in range(30):
        ew=math.exp(w)
        f=w*ew-x
        den=ew*(w+1)-(w+2)*f/(2*w+2)
        nw=w-f/den
        if abs(nw-w)<1e-15*max(1,abs(nw)):
            return nw
        w=nw
    return w

def cubic_root():
    lo,hi=1.0,2.0
    for _ in range(120):
        z=(lo+hi)/2
        if z**3-z-4>0: hi=z
        else: lo=z
    return (lo+hi)/2

def main():
    matrix_checks=0
    for J,J1 in [(1.0,1.2),(1.0,2.0),(0.5,3.0),(-1.0,0.2),(-1.0,1.0),(-2.0,0.7)]:
        assert J/J1<1
        for T in (0.25,0.6,1.1,2.0):
            direct=concurrence(trace_spin3(thermal_state(J,J1,T)))
            closed=formula(J,J1,T)
            assert abs(direct-closed)<5e-10,(J,J1,T,direct,closed)
            matrix_checks+=1

    rs=(-2.0,-0.5,0.0,0.2,0.5,0.8,0.95)
    roots=[ucrit(r) for r in rs]
    assert all(roots[i]<roots[i+1] for i in range(len(roots)-1))
    for r,u in zip(rs,roots):
        assert abs(F(u,r))<2e-9

    z0=cubic_root()
    assert abs(z0**3-z0-4)<2e-14
    alpha=2/math.log(z0)
    beta=alpha*z0/(z0+6)
    assert abs(alpha-3.41448)<4e-6

    correction_ratios=[]
    for r in (0.08,0.04,0.02,0.01):
        t=1/ucrit(r)
        residual=t-(alpha-beta*r)
        correction_ratios.append(abs(residual)/(r*r))
    assert max(correction_ratios)<0.5

    endpoint=[]
    for delta in (0.03,0.01,0.003,0.001):
        t=1/ucrit(1-delta)
        approx=6/lambertw_pos(6/delta)
        endpoint.append(t/approx)
    assert abs(endpoint[-1]-1)<4e-4
    assert abs(endpoint[-1]-1)<abs(endpoint[0]-1)

    print('VERIFY_OK')
    print('direct_density_matrix_checks =',matrix_checks)
    print('universal_root_cases =',len(rs))
    print('alpha =',format(alpha,'.15f'))
    print('beta =',format(beta,'.15f'))
    print('activation_ratio =',format(endpoint[-1],'.15f'))
    print('max_scaled_strong_impurity_remainder =',format(max(correction_ratios),'.15f'))

if __name__=='__main__':
    main()
