#!/usr/bin/env python3
import math
import numpy as np

sx=np.array([[0,1],[1,0]],complex)
sy=np.array([[0,-1j],[1j,0]],complex)
sz=np.array([[1,0],[0,-1]],complex)
I2=np.eye(2,dtype=complex)
I8=np.eye(8,dtype=complex)
YY=np.kron(sy,sy)

def one(A,i):
    ops=[A if k==i else I2 for k in range(3)]
    out=ops[0]
    for op in ops[1:]:
        out=np.kron(out,op)
    return out

def two(A,i,B,j):
    ops=[]
    for k in range(3):
        if k==i:
            ops.append(A)
        elif k==j:
            ops.append(B)
        else:
            ops.append(I2)
    out=ops[0]
    for op in ops[1:]:
        out=np.kron(out,op)
    return out

def hamiltonian(J,B):
    H=np.zeros((8,8),complex)
    for i,j in ((0,1),(1,2),(2,0)):
        H += (J/2)*(two(sx,i,sx,j)+two(sy,i,sy,j)+two(sz,i,sz,j)-I8)
    for i in range(3):
        H -= B*one(sz,i)
    return H

def reduced_pair(J,B,T):
    E,V=np.linalg.eigh(hamiltonian(J,B))
    w=np.exp(-(E-E.min())/T)
    rho=(V*w)@V.conj().T
    rho/=w.sum()
    r=rho.reshape(2,2,2,2,2,2)
    return np.trace(r,axis1=2,axis2=5).reshape(4,4)

def wootters(rho):
    ev=np.linalg.eigvals(rho@YY@rho.conj()@YY)
    vals=np.sort(np.sqrt(np.maximum(ev.real,0.0)))[::-1]
    return max(0.0,float(vals[0]-vals[1]-vals[2]-vals[3]))

def source_formula(J,B,T):
    x=J/T
    q=math.exp(3*x)
    b=abs(B)/T
    A=2*q+1
    u=1.5*math.exp(3*b)+0.5*A*math.exp(b)
    v=1.5*math.exp(-3*b)+0.5*A*math.exp(-b)
    y=-(q-1)*math.cosh(b)
    Z=2*math.cosh(3*b)+2*A*math.cosh(b)
    return max(4*(abs(y)-math.sqrt(u*v))/(3*Z),0.0)

def activation(J,T):
    q=math.exp(3*J/T)
    q0=4+3*math.sqrt(2)
    if q<=q0:
        return None
    R=(q+2)**2/(q*q-8*q-2)
    return 0.5*T*math.acosh(R)

def main():
    direct_checks=0
    for T in (0.35,0.7,1.0,1.3):
        for B in (0.0,0.3,0.8,1.5,2.0,3.0):
            cd=wootters(reduced_pair(1.0,B,T))
            cf=source_formula(1.0,B,T)
            assert abs(cd-cf)<3e-10,(T,B,cd,cf)
            direct_checks+=1

    q0=4+3*math.sqrt(2)
    Tstar=3/math.log(q0)
    assert activation(1.0,Tstar*1.01) is None
    threshold_checks=0
    for T in (0.4,0.8,1.2):
        bs=activation(1.0,T)
        assert bs is not None
        below=source_formula(1.0,0.999*bs,T)
        above=source_formula(1.0,1.001*bs,T)
        assert below==0.0 and above>0.0
        threshold_checks+=1

    activation_ratios=[]
    for T in (0.4,0.3,0.2):
        bs=activation(1.0,T)
        asym=math.sqrt(6)*T*math.exp(-1.5/T)
        activation_ratios.append(bs/asym)
    assert abs(activation_ratios[-1]-1)<2e-5

    scaling_errors=[]
    T=0.08
    for s in (-2.0,-1.0,0.0,1.0,2.0):
        c=source_formula(1.0,1.5+s*T,T)
        target=2/(3*(2+math.exp(2*s)))
        scaling_errors.append(abs(c-target))
    assert max(scaling_errors)<5e-7

    arrhenius_ratios=[]
    T=0.04
    for B in (1.7,2.0,2.5):
        c=source_formula(1.0,B,T)
        asym=(2/3)*math.exp(-2*(B-1.5)/T)
        arrhenius_ratios.append(c/asym)
    assert max(abs(r-1) for r in arrhenius_ratios)<1e-3

    print("VERIFY_OK")
    print("direct_density_matrix_checks =",direct_checks)
    print("activation_threshold_checks =",threshold_checks)
    print("activation_ratio_last =",activation_ratios[-1])
    print("max_scaling_profile_error =",max(scaling_errors))
    print("arrhenius_ratio_min =",min(arrhenius_ratios))

if __name__=="__main__":
    main()
