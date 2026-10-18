"""Independent numerical checks for the rare-jump endpoint asymptotics.
Run with Python 3.10+; uses the standard library only.
Finite numerical tests illustrate but do not prove the asymptotic theorem.
"""
import math


def P(z, degree):
    return sum(z**k / math.factorial(k) for k in range(degree + 1)) if degree >= 0 else 0.0


def mgf_and_derivative(z, beta):
    """J ~ Beta(1, beta), with integer beta=1,2,3."""
    ez = math.exp(z)
    B = math.factorial(beta)
    F = B * (ez - P(z, beta - 1)) / z**beta
    Fprime = B * ((ez - P(z, beta - 2)) / z**beta
                  - beta * (ez - P(z, beta - 1)) / z**(beta + 1))
    return F, Fprime


def stationary_data(z, L, beta):
    delta = math.exp(-L)
    mu = 1.0 / (beta + 1)
    nu = 2.0 / ((beta + 1)*(beta + 2))
    F, Fprime = mgf_and_derivative(z, beta)
    H = F - 1.0 - mu*z
    q = 2.0*delta*H/z**2
    qprime = 2.0*delta*((Fprime-mu)/z**2 - 2.0*H/z**3)
    M = (1+q)/(1+delta*nu)
    Mprime = qprime/(1+delta*nu)
    residual = z*Mprime - M*(M-1)
    psi = (1.0-1.0/M)/z
    return residual, psi, q, M


def optimal_z(L, beta):
    lo=L
    hi=L+12*(beta+4)*math.log(L)
    assert stationary_data(lo, L, beta)[0] > 0
    assert stationary_data(hi, L, beta)[0] < 0
    for _ in range(100):
        mid=(lo+hi)/2
        if stationary_data(mid, L, beta)[0] > 0:
            lo=mid
        else:
            hi=mid
    z=(lo+hi)/2
    assert abs(stationary_data(z,L,beta)[0]) < 2e-8*(z**2)
    return z


def run():
    checks=0
    for beta in (1, 2, 3):
        prev_error=float('inf')
        for L in (40, 80, 160):
            z=optimal_z(L,beta)
            r,psi,q,M=stationary_data(z,L,beta)
            predicted=L+(beta+3)*math.log(L)+1-math.log(2*math.factorial(beta))
            computed=1/psi
            err=abs(computed-predicted)
            assert math.isfinite(computed) and computed > L
            assert q > 1 and M > 1
            assert err < prev_error
            for shift in (-6, -3, -1, 1, 3, 6):
                val=stationary_data(max(0.01,z+shift),L,beta)[1]
                assert val < psi
                checks+=1
            prev_error=err
            checks += 4
            print('Beta(1,%d): L=%3d z*=%.8f 1/c=%.8f prediction=%.8f difference=%.8f'
                  % (beta,L,z,computed,predicted,computed-predicted))
    print('PASS: %d deterministic checks; none substitutes for the analytical proof.' % checks)


if __name__=='__main__':
    run()
