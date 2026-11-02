"""Finite rational checks of the convex Bergman mode-curvature identities.

Run with Python >= 3.9: python verify_modes.py
These finite checks supplement, rather than replace, the analytic argument.
"""
from fractions import Fraction as Q
from math import comb, factorial


def poch(x, n):
    r = 1
    for j in range(n):
        r *= (x+j)
    return r


def beta_integer(a, b):
    assert a > 0 and b > 0 and int(a) == a and int(b) == b
    return Q(factorial(a-1)*factorial(b-1), factorial(a+b-1))


def lambda_power(beta, power, n):
    return Q(power, beta*power-1) * (1 - Q(power*poch(beta,n), poch(beta*power,n)))


def gap_from_hinges(beta, power, n):
    c = Q(poch(beta,n), factorial(n))
    return c * Q(power*(power-1),n+1) * (
        beta_integer(beta*power-1,n+1) + n*beta_integer(beta*power,n+1))


def normalized_power_value(beta, power, n, epsilon):
    # f=(1+epsilon*sqrt((beta)_n/n!)*z**n)/sqrt(1+epsilon**2)
    q = Q(poch(beta,n),factorial(n))
    val = Q(0)
    for k in range(power+1):
        val += comb(power,k)**2 * epsilon**(2*k) * q**k * beta_integer(n*k+1,beta*power-1)
    return val/(1+epsilon**2)**power


def run():
    checks=0
    for beta in [2,3,5,9]:
        for power in [2,3,4,6]:
            assert lambda_power(beta,power,1)==0; checks+=1
            prev=Q(0)
            for n in range(1,17):
                current = lambda_power(beta,power,n+1)
                assert current-prev == gap_from_hinges(beta,power,n)
                assert current>prev
                prev=current
                checks+=2
            assert prev < Q(power,beta*power-1); checks+=1
            for n in [1,2,3,5,8]:
                for epsilon in [Q(1,100),Q(1,200)]:
                    actual=(Q(1,beta*power-1)-normalized_power_value(beta,power,n,epsilon))/epsilon**2
                    target=lambda_power(beta,power,n)
                    assert abs(actual-target) < Q(1,100)
                    checks+=1
    print(f'PASS {checks} rational identities and Taylor checks')


if __name__=='__main__':
    run()
