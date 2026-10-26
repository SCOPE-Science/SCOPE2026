"""Finite diagnostics for canonical two-token self-attention cycles.

The analytic assertions, including all-parameter necessity, rely on the proof;
these diagnostics exercise identities at independent numerical parameters.
"""
from fractions import Fraction
import math


def angle_diff(a, b):
    return math.atan2(math.sin(a-b), math.cos(a-b))


def step(theta, eta, lam, M, kappa):
    vec = [(math.cos(t), math.sin(t)) for t in theta]
    result = []
    for i in range(2):
        logits = [kappa * (vec[i][0]*vec[j][0]+vec[i][1]*vec[j][1]) for j in range(2)]
        shift = max(logits)
        weights = [math.exp(t-shift) for t in logits]
        scale = sum(weights)
        avg_x = sum(weights[j]*vec[j][0] for j in range(2))/scale
        avg_y = sum(weights[j]*vec[j][1] for j in range(2))/scale
        u = vec[i][0]+eta*lam*avg_x
        v = vec[i][1]-eta*M*avg_y
        if math.hypot(u,v) < 1e-13:
            raise ValueError("undefined normalized map at diagnostic point")
        result.append(math.atan2(v,u))
    return tuple(result)


def derivative(theta, eta, lam, M, kappa, double=False):
    eps=1e-6
    def fun(t):
        z=step(t,eta,lam,M,kappa)
        return step(z,eta,lam,M,kappa) if double else z
    p0=fun(theta)
    mat = [[0.,0.],[0.,0.]]
    for j in range(2):
        pos=list(theta); neg=list(theta)
        pos[j]+=eps; neg[j]-=eps
        p=fun(tuple(pos)); n=fun(tuple(neg))
        for i in range(2):
            mat[i][j] = angle_diff(p[i],n[i])/(2*eps)
    return mat


def eigen_sym(M):
    return M[0][0]+M[0][1], M[0][0]-M[0][1]


def check_close(a,b,err=3e-6):
    if abs(a-b)>err:
        raise AssertionError(f"{a} != {b}")


def run():
    checks=0
    for lam,M,q,eta in [(1,4,0.5,3),(2,7,0.6,4),(0.8,3.1,0.75,2),(1.0,2.5,0.8,5),(1.5,4.7,0.9,3)]:
        kappa=math.atanh(q)
        c=2/(M-lam)
        a=2/(q*M-lam) if q*M>lam else float('inf')
        for x in [(0.,0.),(math.pi,math.pi)]:
            p=step(x,eta,lam,M,kappa)
            for v,u in zip(x,p):check_close(angle_diff(v,u),0)
            J=derivative(x,eta,lam,M,kappa)
            s,d=eigen_sym(J)
            check_close(s,(1-eta*M)/(1+eta*lam))
            check_close(d,1/(1+eta*lam))
            checks+=4
        if eta>1/M:
            x=(math.pi/2,math.pi/2)
            y=step(x,eta,lam,M,kappa)
            for v,u in zip(y,(-math.pi/2,-math.pi/2)):check_close(angle_diff(v,u),0)
            JJ=derivative(x,eta,lam,M,kappa,double=True)
            s,d=eigen_sym(JJ)
            check_close(s,((1+eta*lam)/(eta*M-1))**2)
            check_close(d,1/(eta*M-1)**2)
            checks+=4
        if eta>1/(q*M):
            x=(math.pi/2,-math.pi/2)
            y=step(x,eta,lam,M,kappa)
            for v,u in zip(y,(-math.pi/2,math.pi/2)):check_close(angle_diff(v,u),0)
            JJ=derivative(x,eta,lam,M,kappa,double=True)
            s,d=eigen_sym(JJ)
            check_close(d,((1+eta*lam)/(eta*q*M-1))**2)
            check_close(s,((1+eta*lam*q)/(eta*q*M-1))**2)
            checks+=4
        if eta>a:
            assert max(eigen_sym(derivative((math.pi/2,-math.pi/2),eta,lam,M,kappa,double=True))) < 1
            assert max(eigen_sym(derivative((math.pi/2,math.pi/2),eta,lam,M,kappa,double=True))) < 1
            checks+=2
        if eta>c:
            assert abs((1-eta*M)/(1+eta*lam))>1
            checks+=1
    for lam,M,q in [(1.,4.,.5),(2.,5.,.8),(.4,2.,.7)]:
        eta=2/(M-lam)
        kappa=math.atanh(q)
        scale=(M+lam)/(M-lam)
        for k in range(19):
            theta=-2.8+5.6*k/18
            x=(theta,theta)
            y=step(x,eta,lam,M,kappa)
            for p in y:check_close(angle_diff(p,-theta),0)
            z=step(y,eta,lam,M,kappa)
            for p in z:check_close(angle_diff(p,theta),0)
            JJ=derivative(x,eta,lam,M,kappa,double=True)
            s,d=eigen_sym(JJ)
            check_close(s,1)
            check_close(d,math.cos(2*theta)**2/scale**2)
            checks+=6
    # Exact rational identities for a concrete co-attracting pair.
    lam,M,q,eta=Fraction(1),Fraction(4),Fraction(1,2),Fraction(3)
    assert eta>2/(M*q-lam)
    assert ((1+eta*lam)/(eta*M-1))**2==Fraction(16,121)
    assert (1/(eta*M-1))**2==Fraction(1,121)
    assert ((1+eta*lam)/(eta*M*q-1))**2==Fraction(16,25)
    assert ((1+eta*lam*q)/(eta*M*q-1))**2==Fraction(1,4)
    checks+=5
    print('CANONICAL_CYCLE_AND_JACOBIAN_CHECKS_PASS',checks)
    print('EXACT_EXAMPLE_LAMBDA1_M4_Q_HALF_ETA3: SYNC (16/121,1/121), ANTIPODAL (16/25,1/4)')
    print('RESONANCE_DIAGONAL_INVARIANT_CIRCLE_AND_TRANSVERSE_MULTIPLIER_PASS',19*3)
    print('GENERAL_PARAMETER_THEOREMS_REQUIRE_ANALYTIC_PROOF')


if __name__ == '__main__':
    run()
