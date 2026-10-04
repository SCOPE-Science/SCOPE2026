#!/usr/bin/env python3
import math
import numpy as np

def graph(N):
    A=np.ones((N,N),dtype=float)-np.eye(N)
    m=N//2
    for i in range(m):
        A[i,i+m]=0.0
        A[i+m,i]=0.0
    return A

def direct_amp(N,t):
    A=graph(N)
    w,v=np.linalg.eigh(A)
    U=(v*np.exp(-1j*w*t))@v.conj().T
    return U[N//2,0]

def closed_amp(N,t):
    return -0.5+(0.5-1.0/N)*np.exp(2j*t)+(1.0/N)*np.exp(-1j*(N-2)*t)

def deficit(N,t):
    m=N//2
    return ((m-1)/m)*math.cos(t)**2+(1/m)*math.cos((m-1)*t)**2+((m-1)/(m*m))*math.sin(m*t)**2

def main():
    formula_checks=0
    optimum_checks=0
    deficit_checks=0
    for N in (6,10,14,18,22,30,50):
        assert N%4==2
        for t in (0.137,0.731,1.111,math.pi/2,2.317):
            a=direct_amp(N,t)
            b=closed_amp(N,t)
            assert abs(a-b)<2e-11,(N,t,a,b)
            assert abs((1-abs(b)**2)-deficit(N,t))<2e-12
            formula_checks+=1
            deficit_checks+=1

        target=math.cos(math.pi/N)**2
        for t in (math.pi/2-math.pi/N,math.pi/2+math.pi/N):
            assert abs(abs(direct_amp(N,t))**2-target)<2e-11
            optimum_checks+=1

        source=(1-2/N)**2
        assert abs(abs(direct_amp(N,math.pi/2))**2-source)<2e-11
        assert source<target

        grid=np.linspace(0,math.pi,200001)
        vals=np.abs(-0.5+(0.5-1/N)*np.exp(2j*grid)+(1/N)*np.exp(-1j*(N-2)*grid))**2
        assert vals.max()<=target+2e-9
        assert target-vals.max()<2e-9

    print("VERIFY_OK")
    print("direct_formula_checks =",formula_checks)
    print("deficit_identity_checks =",deficit_checks)
    print("optimal_time_checks =",optimum_checks)
    print("N6_optimum =",math.cos(math.pi/6)**2)
    print("N50_optimum =",math.cos(math.pi/50)**2)

if __name__=="__main__":
    main()
