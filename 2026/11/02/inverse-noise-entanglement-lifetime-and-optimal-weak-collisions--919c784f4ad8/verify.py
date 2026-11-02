"""Independent finite-matrix and numerical checks of the entangling-collision theorem.

The universal conclusions are proved analytically; numerical tests sample finite cases.
Run with Python 3 and NumPy (see requirements.txt).
"""
import math
import numpy as np

checks = 0


def check(cond, message):
    global checks
    assert bool(cond), message
    checks += 1


def root_threshold(p, t):
    r = 1.0-2.0*p
    eps = 1.0-r*r
    v = t*(1.0-t)
    return eps*(r+math.sqrt(1+4*v))/(r*(4*v+eps))


def finite_count(p, t):
    threshold = root_threshold(p, t)
    if threshold >= 1:
        return 0
    return math.ceil(math.log(threshold)/math.log1p(-t))


def direct_pre_reset_joint(p, t, k):
    # Both qubits use the basis |0> = ground, |1> = excited.
    c, s = math.sqrt(1-t), math.sqrt(t)
    q = 1-p
    a = q + (0.5-q)*((1-t)**k)
    rho_s = np.diag([1-a, a]).astype(complex)
    rho_a = np.diag([q, p]).astype(complex)
    U = np.eye(4, dtype=complex)
    U[0,0] = U[3,3] = c
    U[0,3] = U[3,0] = -1j*s
    return U @ np.kron(rho_s,rho_a) @ U.conj().T


def negativity(joint):
    pt = joint.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
    vals = np.linalg.eigvalsh(pt)
    return sum(max(0.0,-float(z)) for z in vals)


def explicit_negativity(p,t,k):
    c,s = math.sqrt(1-t),math.sqrt(t)
    q=1-p
    x=(1-t)**k
    a=q+(0.5-q)*x
    A=(1-a)*p
    B=a*q
    w=(q-a)*c*s
    return max(0,(math.sqrt((A-B)**2+4*w*w)-(A+B))/2)


def main():
    for p in (0.0005,0.01,0.03,0.08,0.14,0.17,0.28,0.49):
        for t in (0.02,0.08,0.2,0.34,0.5,0.75,0.95):
            m = finite_count(p,t)
            for k in range(0,30):
                rho=direct_pre_reset_joint(p,t,k)
                check(np.isclose(np.trace(rho),1.0,atol=1e-13),f'trace {p,t,k}')
                check(np.min(np.linalg.eigvalsh(rho))>=-1e-13,f'positive {p,t,k}')
                neg=negativity(rho)
                exact=explicit_negativity(p,t,k)
                check(abs(neg-exact)<1e-12,f'negativity {p,t,k}')
                if abs(exact)>1e-9 or (abs(k-m)>1):
                    check((neg>1e-10) == (k<m),f'interval {p,t,k,m}')
            xstar=root_threshold(p,t)
            if m>0:
                check((1-t)**(m-1) > xstar-1e-12,f'last entangled {p,t,m}')
                check((1-t)**m < xstar+1e-12,f'first separable {p,t,m}')
    # Independent physical replay: carry the reduced state forward rather than
    # reconstructing it from the closed-form population on every contact.
    for p in (0.004,0.025,0.10,0.18,0.35):
        for t in (0.012,0.13,0.43,0.87):
            q=1-p
            c,s=math.sqrt(1-t),math.sqrt(t)
            U=np.eye(4,dtype=complex)
            U[0,0]=U[3,3]=c
            U[0,3]=U[3,0]=-1j*s
            bath=np.diag([q,p]).astype(complex)
            system=np.eye(2,dtype=complex)/2
            for k in range(55):
                joint=U @ np.kron(system,bath) @ U.conj().T
                independently_rebuilt=direct_pre_reset_joint(p,t,k)
                check(np.max(np.abs(joint-independently_rebuilt)) < 4e-13,
                      f'fresh-bath recurrence {p,t,k}')
                check(abs(negativity(joint)-explicit_negativity(p,t,k)) < 4e-13,
                      f'replayed partial-transpose {p,t,k}')
                system=np.trace(joint.reshape(2,2,2,2),axis1=1,axis2=3)
    # Analytic startup threshold: no collision entangles above pcrit.
    pcrit=(1-1/math.sqrt(2))/2
    for p in (pcrit+1e-6,0.16,0.2,0.45):
        for t in np.linspace(0.002,0.998,105):
            check(finite_count(p,float(t))==0,f'global thermal threshold {p,t}')
    for p in (0.0003,0.002,0.01,0.04,0.08):
        check(finite_count(p,0.5)>0,f'nonzero below threshold {p}')
    # Rare-bath-noise scaling at the stationary optimum.
    lo,hi=1.0,10.0
    for _ in range(75):
        m=(lo+hi)/2
        f=m/(m+1)-math.log((m+1)/2)
        if f>0:lo=m
        else:hi=m
    astar=(lo+hi)/2
    coeff=math.log((astar+1)/2)/astar
    check(abs(astar-3.311070407000921)<1e-11,'optimal a')
    check(abs(coeff-0.23196095298653444)<1e-11,'optimal coefficient')
    for p in (0.01,0.002,0.0005,0.0001):
        ks=finite_count(p,astar*p)
        # The discrepancy is O(p log(1/p)) and decreases to zero.
        check(abs(p*ks-coeff)<0.04,f'asymptotic count {p,ks}')
        samples=np.geomspace(0.75*p,min(0.999,10000*p),700)
        best=max(finite_count(p,float(t)) for t in samples)
        check(best>=ks,f'grid below candidate {p}')
        check(p*best<coeff+0.05,f'uniform envelope {p,best}')
        print(f'p={p:.5g}; theta^2={astar*p:.6g}; candidate={ks}; gridmax={best}; p*gridmax={p*best:.8f}')
    print(f'PASS: {checks} finite assertions; a*={astar:.12f}; K*={coeff:.12f}')


if __name__=='__main__':
    main()
