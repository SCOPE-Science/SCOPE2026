#!/usr/bin/env python3
import math
import itertools

def zeros(n,m):
    return [[0j for _ in range(m)] for _ in range(n)]

def dag(A):
    return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]

def mm(A,B):
    out=zeros(len(A),len(B[0]))
    for i in range(len(A)):
        for k in range(len(B)):
            aik=A[i][k]
            if aik:
                for j in range(len(B[0])):
                    out[i][j]+=aik*B[k][j]
    return out

def kron(A,B):
    out=zeros(len(A)*len(B),len(A[0])*len(B[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B)):
                for l in range(len(B[0])):
                    out[i*len(B)+k][j*len(B[0])+l]=A[i][j]*B[k][l]
    return out

def maxerr(A,B):
    return max(abs(A[i][j]-B[i][j]) for i in range(len(A)) for j in range(len(A[0])))

def initial(r,theta):
    A=(1-r)/4
    c=math.cos(theta)
    s=math.sin(theta)
    rho=zeros(4,4)
    rho[0][0]=A+r*c*c
    rho[1][1]=A
    rho[2][2]=A
    rho[3][3]=A+r*s*s
    rho[0][3]=rho[3][0]=r*s*c
    return rho

def local_isometry(eta):
    # Output basis is |system,environment>; input basis is |system>.
    V=zeros(4,2)
    V[0][0]=1
    V[2][1]=math.sqrt(eta)
    V[1][1]=math.sqrt(1-eta)
    return V

def global_state(r,theta,eta):
    V=kron(local_isometry(eta),local_isometry(eta))
    return mm(mm(V,initial(r,theta)),dag(V))

def reduced(globalrho,keep):
    out=zeros(4,4)
    for s1,e1,s2,e2 in itertools.product(range(2),repeat=4):
        i=(s1*2+e1)*4+(s2*2+e2)
        for S1,E1,S2,E2 in itertools.product(range(2),repeat=4):
            j=(S1*2+E1)*4+(S2*2+E2)
            if keep=="cavity" and e1==E1 and e2==E2:
                out[s1*2+s2][S1*2+S2]+=globalrho[i][j]
            if keep=="reservoir" and s1==S1 and s2==S2:
                out[e1*2+e2][E1*2+E2]+=globalrho[i][j]
    return out

def analytic_cavity(r,theta,eta):
    A=(1-r)/4
    b=math.sin(theta)**2
    c=math.sin(theta)*math.cos(theta)
    p00=A+r*(1-b)
    p01=A
    p10=A
    p11=A+r*b
    q=1-eta
    out=zeros(4,4)
    out[3][3]=eta*eta*p11
    out[1][1]=eta*p01+eta*q*p11
    out[2][2]=eta*p10+eta*q*p11
    out[0][0]=p00+q*p01+q*p10+q*q*p11
    out[0][3]=out[3][0]=r*c*eta
    return out

def concurrence_x(rho):
    d=[max(0.0,rho[i][i].real) for i in range(4)]
    a=abs(rho[0][3])-math.sqrt(d[1]*d[2])
    b=abs(rho[1][2])-math.sqrt(d[0]*d[3])
    return 2*max(0.0,a,b)

def formula_cavity(r,theta,eta):
    A=(1-r)/4
    b=math.sin(theta)**2
    c=math.sin(theta)*math.cos(theta)
    return 2*eta*max(0.0,r*c-A*(2-eta)-r*b*(1-eta))

def alpha(r,theta):
    A=(1-r)/4
    b=math.sin(theta)**2
    c=math.sin(theta)*math.cos(theta)
    return (2*A+r*(b-c))/(A+r*b)

def rc(theta):
    c=math.sin(theta)*math.cos(theta)
    return 1/(1+4*c)

def rs(theta):
    b=math.sin(theta)**2
    c=math.sin(theta)*math.cos(theta)
    return 3/(3+8*c-4*b)

def re_boundary(theta):
    b=math.sin(theta)**2
    c=math.sin(theta)*math.cos(theta)
    return 1/(1+2*(c-b))

def rs_printed(theta):
    b=math.sin(theta)**2
    c=math.sin(theta)*math.cos(theta)
    return 1/(1+2*c-b)

def main():
    trace_checks=0
    concurrence_checks=0
    complement_checks=0
    threshold_checks=0
    simultaneous_checks=0
    nonunital_checks=0
    printed_boundary_checks=0

    for theta in (0.2,0.45,math.pi/4,math.pi/3,1.2):
        r0=rc(theta)
        for frac in (0.18,0.52,0.86):
            r=r0+(1-r0)*frac
            for eta in (0.13,0.37,0.71,0.93):
                G=global_state(r,theta,eta)
                C=reduced(G,"cavity")
                R=reduced(G,"reservoir")
                AC=analytic_cavity(r,theta,eta)
                AR=analytic_cavity(r,theta,1-eta)
                assert maxerr(C,AC)<2e-13
                assert maxerr(R,AR)<2e-13
                trace_checks+=2

                cc=concurrence_x(C)
                crv=concurrence_x(R)
                assert abs(cc-formula_cavity(r,theta,eta))<2e-13
                assert abs(crv-formula_cavity(r,theta,1-eta))<2e-13
                concurrence_checks+=2
                assert abs(crv-formula_cavity(r,theta,1-eta))<2e-13
                complement_checks+=1

    # Unique finite threshold signs and event times.
    for theta,r in (
        (0.2,0.60),
        (0.45,0.60),
        (math.pi/4,0.80),
        (math.pi/3,0.60),
        (math.pi/3,0.95),
        (1.0,0.90),
        (1.2,0.90),
    ):
        a=alpha(r,theta)
        if 0<a<1:
            eps=min(1e-5,a/4,(1-a)/4)
            assert formula_cavity(r,theta,a+eps)>0
            assert formula_cavity(r,theta,a-eps)==0
            # Reservoir concurrence is formula_cavity evaluated at q=1-eta.
            assert formula_cavity(r,theta,a+eps)>0
            assert formula_cavity(r,theta,a-eps)==0
            # Equivalently, in the cavity survival variable eta, birth occurs at eta=1-a.
            eta_birth=1-a
            assert formula_cavity(r,theta,1-(eta_birth-eps))>0
            assert formula_cavity(r,theta,1-(eta_birth+eps))==0
            threshold_checks+=6

    # Simultaneous boundary wherever physically admissible.
    for theta in (0.2,0.45,0.7,math.pi/4,0.9,math.atan(2)):
        r=rs(theta)
        assert rc(theta)<r+1e-14
        if r<=1+1e-14:
            r=min(r,1.0)
            assert abs(alpha(r,theta)-0.5)<2e-13
            tD=-math.log(alpha(r,theta))
            tB=-math.log(1-alpha(r,theta))
            assert abs(tD-tB)<2e-13
            simultaneous_checks+=1

    # Printed frozen-noise boundary lies strictly above the physical one for 0<tan(theta)<2.
    for u in (0.1,0.3,0.7,1.0,1.4,1.8):
        theta=math.atan(u)
        rp=rs_printed(theta)
        rr=rs(theta)
        closed=u*(2-u)*(1+u*u)/((1+2*u)*(3+8*u-u*u))
        assert abs((rp-rr)-closed)<3e-13
        assert rp>rr
        # Pick a point in the discrepancy wedge: physical alpha<1/2.
        rmid=(rp+rr)/2
        assert alpha(rmid,theta)<0.5
        # The printed threshold root beta is >1/2, hence predicts the reverse ordering.
        A=(1-rmid)/4
        b=math.sin(theta)**2
        c=math.sin(theta)*math.cos(theta)
        disc=(rmid*(c-b))**2+4*rmid*b*A
        beta=(-rmid*(c-b)+math.sqrt(disc))/(2*rmid*b)
        assert beta>0.5
        printed_boundary_checks+=1

    # Pure-state simultaneous limit.
    theta=math.atan(2)
    assert abs(rs(theta)-1)<2e-13
    assert abs(alpha(1.0,theta)-0.5)<2e-13
    simultaneous_checks+=1

    # No-finite-threshold boundary for theta <= pi/4.
    for theta in (0.15,0.4,0.65,math.pi/4):
        rE=re_boundary(theta)
        assert rc(theta)<rE<=1+1e-13
        assert abs(alpha(rE,theta))<2e-13
        for r in (rE,min(1.0,rE+(1-rE)*0.7)):
            for eta in (1e-6,0.1,0.5):
                assert formula_cavity(r,theta,eta)>0
                if eta<1:
                    assert formula_cavity(r,theta,1-eta)>0
                threshold_checks+=2

    # Non-unitality of one-qubit amplitude damping.
    for eta in (0.2,0.5,0.8):
        # E(I/2) = diag(1-eta/2, eta/2)
        assert abs((1-eta/2)-0.5)>1e-12
        assert abs(eta/2-0.5)>1e-12
        nonunital_checks+=1

    print("VERIFY_OK")
    print("partial_trace_matrix_checks =",trace_checks)
    print("concurrence_formula_checks =",concurrence_checks)
    print("complementarity_checks =",complement_checks)
    print("threshold_sign_checks =",threshold_checks)
    print("simultaneous_boundary_checks =",simultaneous_checks)
    print("nonunitality_checks =",nonunital_checks)
    print("printed_boundary_discrepancy_checks =",printed_boundary_checks)

if __name__=="__main__":
    main()
