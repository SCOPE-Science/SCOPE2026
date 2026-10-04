#!/usr/bin/env python3
import math
import numpy as np

sx=np.array([[0,1],[1,0]],complex)
sy=np.array([[0,-1j],[1j,0]],complex)
sz=np.array([[1,0],[0,-1]],complex)
I=np.eye(2,dtype=complex)
paulis=[I,sx,sy,sz]

phi_p=np.array([1,0,0,1],complex)/math.sqrt(2)
phi_m=np.array([1,0,0,-1],complex)/math.sqrt(2)
psi_p=np.array([0,1,1,0],complex)/math.sqrt(2)
psi_m=np.array([0,1,-1,0],complex)/math.sqrt(2)
bells=[psi_m,phi_m,phi_p,psi_p]
projectors=[np.outer(v,v.conj()) for v in bells]

def hamiltonian(J,D):
    return (J/2)*(np.kron(sx,sx)+np.kron(sy,sy)+np.kron(sz,sz)
                  +D*(np.kron(sx,sy)-np.kron(sy,sx)))

def thermal_state(J,D,T):
    w,v=np.linalg.eigh(hamiltonian(J,D))
    p=np.exp(-(w-w.min())/T)
    rho=(v*p)@v.conj().T
    return rho/np.trace(rho)

def wootters(rho):
    YY=np.kron(sy,sy)
    ev=np.linalg.eigvals(rho@YY@rho.conj()@YY)
    vals=np.sort(np.sqrt(np.maximum(ev.real,0)))[::-1]
    return max(0.0,float(vals[0]-vals[1]-vals[2]-vals[3]))

def direct_output(J,D,T,theta,phase):
    rho=thermal_state(J,D,T)
    probs=[float(np.trace(P@rho).real) for P in projectors]
    psi=np.array([0,
                  np.exp(1j*phase)*math.sin(theta/2),
                  math.cos(theta/2),
                  0],complex)
    rin=np.outer(psi,psi.conj())
    rout=np.zeros((4,4),complex)
    for i,pi in enumerate(probs):
        for j,pj in enumerate(probs):
            U=np.kron(paulis[i],paulis[j])
            rout += pi*pj*(U@rin@U.conj().T)
    return wootters(rout)

def corrected(J,D,T,Cin):
    x=J/T
    s=math.sqrt(1+D*D)
    y=x*s
    Z=2*math.exp(-x/2)*(1+math.exp(x)*math.cosh(y))
    raw=4*(Cin*math.exp(x)*math.sinh(y)**2-2*s*s*math.cosh(y))/(Z*Z*s*s)
    return max(raw,0.0)

def printed(J,D,T,Cin):
    return corrected(J,D,T,Cin)/2

def main():
    direct_checks=0
    factor_checks=0
    for J in (-1.4,-0.7,0.6,1.3):
        for D in (0.0,0.4,1.2,3.0,5.0):
            for T in (0.3,0.8,1.5):
                for theta in (0.25,0.8,1.4,2.2):
                    phase=0.37
                    Cin=math.sin(theta)
                    cdir=direct_output(J,D,T,theta,phase)
                    cc=corrected(J,D,T,Cin)
                    assert abs(cdir-cc)<3e-10,(J,D,T,theta,cdir,cc)
                    direct_checks+=1
                    if cc>1e-9:
                        assert abs(cdir-2*printed(J,D,T,Cin))<3e-10
                        factor_checks+=1

    # Eventual strong-D revival: examples are zero at moderate D but positive later.
    examples=[
        (1.0,1.0,0.5,3.0,5.0),
        (-1.0,0.5,1.0,2.0,5.0),
        (-1.0,1.0,1.0,3.0,8.0),
    ]
    for J,T,Cin,Dzero,Dpos in examples:
        assert corrected(J,Dzero,T,Cin)==0.0
        assert corrected(J,Dpos,T,Cin)>0.0

    # Algebraic tail.
    tail_checks=0
    for J,T,Cin in [(1.0,0.7,0.3),(-1.0,0.4,0.8),(1.6,1.2,1.0)]:
        errs=[]
        for D in (8.0,12.0,18.0):
            ratio=D*D*corrected(J,D,T,Cin)/Cin
            errs.append(abs(ratio-1))
        assert errs[-1]<errs[0]
        assert errs[-1]<0.01
        tail_checks+=1

    print("VERIFY_OK")
    print("direct_density_matrix_checks =",direct_checks)
    print("positive_factor_two_checks =",factor_checks)
    print("strong_DM_revival_examples =",len(examples))
    print("strong_DM_tail_cases =",tail_checks)
    print("example_D2_ratio =",18.0**2*corrected(1.6,18.0,1.2,1.0))

if __name__=="__main__":
    main()
