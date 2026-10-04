#!/usr/bin/env python3
import math
import cmath

def mm(A,B):
    n=len(A); m=len(B); p=len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]

def madd(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mscale(a,A):
    return [[a*x for x in row] for row in A]

def eye(n):
    return [[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]

def maxerr(A,B):
    return max(abs(A[i][j]-B[i][j]) for i in range(len(A)) for j in range(len(A[0])))

def mv(A,v):
    return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]

def dotc(v,w):
    return sum(v[i].conjugate()*w[i] for i in range(len(v)))

def exp_series(M,t,terms=180):
    n=len(M)
    X=eye(n)
    term=eye(n)
    for k in range(1,terms):
        term=mscale((-1j*t)/k, mm(term,M))
        X=madd(X,term)
        if max(abs(z) for row in term for z in row)<1e-16:
            break
    return X

def reduced(n,delta):
    g=2*math.sqrt(2*(n-2))
    e=delta/2
    M=[[0.0,e,g],[e,0.0,0.0],[g,0.0,0.0]]
    Om=0.5*math.sqrt(32*(n-2)+delta*delta)
    return M,Om

def exp_closed(M,Om,t):
    I=eye(3)
    M2=mm(M,M)
    return madd(madd(I,mscale(-1j*math.sin(Om*t)/Om,M)),
                mscale((math.cos(Om*t)-1)/(Om*Om),M2))

def fidelity_formula(n,delta,t):
    Om=0.5*math.sqrt(32*(n-2)+delta*delta)
    a=16*(n-2)/(32*(n-2)+delta*delta)
    return (a*(1-math.cos(Om*t)))**2

def fmax(n,delta):
    return (32*(n-2)/(32*(n-2)+delta*delta))**2

def main():
    cubic_checks=0
    exponential_checks=0
    probability_checks=0
    maximum_checks=0

    vi=[1/math.sqrt(2),1/math.sqrt(2),0.0]
    vj=[1/math.sqrt(2),-1/math.sqrt(2),0.0]

    for n in (4,5,9,20,60):
        for delta in (-7.0,-1.25,0.0,0.6,4.0):
            M,Om=reduced(n,delta)
            M3=mm(mm(M,M),M)
            assert maxerr(M3,mscale(Om*Om,M))<2e-11
            cubic_checks+=1

            # Moderate times keep the direct Taylor sum numerically stable.
            for t in (0.07,0.19,0.41):
                U1=exp_closed(M,Om,t)
                U2=exp_series(M,t)
                assert maxerr(U1,U2)<3e-11
                exponential_checks+=1
                amp=dotc(vj,mv(U1,vi))
                fd=abs(amp)**2
                ff=fidelity_formula(n,delta,t)
                assert abs(fd-ff)<3e-12
                probability_checks+=1

            tstar=math.pi/Om
            assert abs(fidelity_formula(n,delta,tstar)-fmax(n,delta))<2e-13
            for frac in (0.13,0.47,0.83,1.22,1.71):
                assert fidelity_formula(n,delta,frac*tstar)<=fmax(n,delta)+1e-13
            maximum_checks+=1

    # Exact target-fidelity boundary.
    target_checks=0
    for n in (4,10,100):
        for eta in (0.5,0.9,0.99):
            bound=math.sqrt(32*(n-2)*(eta**(-0.5)-1))
            assert abs(fmax(n,bound)-eta)<3e-13
            assert fmax(n,0.99*bound)>=eta
            assert fmax(n,1.01*bound)<eta
            target_checks+=1

    # Fixed-error asymptotic.
    delta=3.0
    ratios=[]
    for n in (100,500,2500,12000):
        lead=delta*delta/(16*(n-2))
        ratios.append((1-fmax(n,delta))/lead)
    assert abs(ratios[-1]-1)<abs(ratios[0]-1)
    assert abs(ratios[-1]-1)<5e-5

    # Natural delta=c sqrt(n) scaling.
    c=2.5
    limit=(32/(32+c*c))**2
    vals=[]
    for n in (100,1000,10000,100000):
        vals.append(fmax(n,c*math.sqrt(n)))
    assert abs(vals[-1]-limit)<abs(vals[0]-limit)
    assert abs(vals[-1]-limit)<3e-5

    print("VERIFY_OK")
    print("cubic_identity_checks =",cubic_checks)
    print("independent_exponential_checks =",exponential_checks)
    print("probability_formula_checks =",probability_checks)
    print("global_maximum_checks =",maximum_checks)
    print("target_fidelity_boundary_checks =",target_checks)
    print("fixed_error_ratio =",ratios[-1])
    print("scaled_error_limit_error =",abs(vals[-1]-limit))

if __name__=="__main__":
    main()
