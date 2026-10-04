#!/usr/bin/env python3
import math
import cmath
import numpy as np

def norm(v):
    return math.sqrt(float(np.vdot(v,v).real))

def corrected_branches(alpha,beta,x):
    y=math.sqrt(1-x*x)
    s=math.sqrt(2)
    return [
        np.array([alpha*y,beta*x],complex)/s,
        np.array([alpha*x,-beta*y],complex)/s,
        np.array([beta*x,alpha*y],complex)/s,
        np.array([-beta*y,alpha*x],complex)/s,
    ]

def corrected_total(alpha,beta,x):
    y=math.sqrt(1-x*x)
    # basis vectors on Alice's two qubits in computational order 00,01,10,11
    psi_m=np.array([0,x,-y,0],complex)
    psi_p=np.array([0,y,x,0],complex)
    phi_m=np.array([x,0,0,-y],complex)
    phi_p=np.array([y,0,0,x],complex)
    basis=[psi_p,psi_m,phi_p,phi_m]
    branches=corrected_branches(alpha,beta,x)
    out=np.zeros(8,complex)
    for b,v in zip(basis,branches):
        out += np.kron(b,v)
    return out

def original_total(alpha,beta):
    # input qubit 1 times shared (|01>+|10>)/sqrt2 on qubits 2,3
    inp=np.array([alpha,beta],complex)
    bell=np.array([0,1,1,0],complex)/math.sqrt(2)
    return np.kron(inp,bell)

def main():
    identity_checks=0
    singular_checks=0
    kraus_checks=0
    branch_success_checks=0
    printed_incompleteness_checks=0

    states=[
        (1+0j,0+0j),
        (0+0j,1+0j),
        (1/math.sqrt(2),1j/math.sqrt(2)),
        (math.sqrt(0.3),cmath.exp(0.37j)*math.sqrt(0.7)),
    ]
    xs=[1/math.sqrt(2),0.76,0.83,0.91,0.98]

    for alpha,beta in states:
        z=math.sqrt(abs(alpha)**2+abs(beta)**2)
        alpha,beta=alpha/z,beta/z
        for x in xs:
            y=math.sqrt(1-x*x)
            lhs=original_total(alpha,beta)
            rhs=corrected_total(alpha,beta,x)
            assert np.max(np.abs(lhs-rhs)) < 2e-13
            identity_checks += 1

            for D in (
                np.diag([x,y])/math.sqrt(2),
                np.diag([y,x])/math.sqrt(2),
            ):
                sv=np.linalg.svd(D,compute_uv=False)
                assert abs(max(sv)-x/math.sqrt(2))<2e-13
                assert abs(min(sv)-y/math.sqrt(2))<2e-13
                singular_checks += 1

            if y>0:
                Ks=np.diag([y/x,1.0])
                Kf=np.diag([math.sqrt(max(0,1-y*y/(x*x))),0.0])
                assert np.max(np.abs(Ks.conj().T@Ks+Kf.conj().T@Kf-np.eye(2)))<2e-13
                kraus_checks += 1
                D=np.diag([x,y])/math.sqrt(2)
                target=np.array([alpha,beta],complex)
                out=Ks@(D@target)
                assert np.max(np.abs(out-(y/math.sqrt(2))*target))<2e-13
                assert abs(float(np.vdot(out,out).real)-y*y/2)<2e-13
                branch_success_checks += 1

                r=y/x
                A1=np.diag([r,1.0])
                A2=np.diag([1-r,0.0])
                defect=np.max(np.abs(A1.conj().T@A1+A2.conj().T@A2-np.eye(2)))
                if 1e-12 < r < 1-1e-12:
                    assert defect>1e-6
                    printed_incompleteness_checks += 1

    # Endpoint and total success law.
    assert abs(2*(1-(1/math.sqrt(2))**2)-1)<2e-13
    for x in (0.75,0.8,0.9,0.99,0.9999):
        y=math.sqrt(1-x*x)
        total=4*(y*y/2)
        assert abs(total-2*(1-x*x))<2e-13
    assert 2*(1-0.999999**2) < 5e-6

    # Branchwise optimality checked numerically by the required operator norm.
    optimality_checks=0
    for x in (0.76,0.83,0.91,0.98):
        y=math.sqrt(1-x*x)
        D=np.diag([x,y])/math.sqrt(2)
        c=y/math.sqrt(2)
        K=c*np.linalg.inv(D)
        assert np.linalg.norm(K,2)<=1+2e-13
        c_bad=c*(1+1e-5)
        K_bad=c_bad*np.linalg.inv(D)
        assert np.linalg.norm(K_bad,2)>1
        optimality_checks += 1

    print("VERIFY_OK")
    print("corrected_decomposition_checks =",identity_checks)
    print("branch_singular_value_checks =",singular_checks)
    print("corrected_kraus_completeness_checks =",kraus_checks)
    print("branch_success_checks =",branch_success_checks)
    print("printed_kraus_incompleteness_checks =",printed_incompleteness_checks)
    print("branch_optimality_checks =",optimality_checks)
    print("product_basis_limit_example =",2*(1-0.999999**2))

if __name__=="__main__":
    main()
