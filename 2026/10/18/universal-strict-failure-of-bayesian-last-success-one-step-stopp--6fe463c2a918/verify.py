"""Exact rational checks for a two-stage Bayesian last-success stopping policy."""
from fractions import Fraction
from math import ceil, gamma


def rise(x, n):
    z = Fraction(1)
    for j in range(n):
        z *= x + j
    return z


def check(alpha, beta, m):
    alpha, beta = Fraction(alpha), Fraction(beta)
    A = alpha + 1
    f = ceil(m * alpha - beta + 1) + 1
    assert f >= 0
    i, N = f + 1, f + m + 1
    B = beta + f + m - 1
    delta = B - m*A
    assert 1 <= delta < 2
    g = rise(beta + f, m) / rise(A + beta + f, m)
    # A next success at index i+k, followed by no further successes.
    common = g * A / B
    first_future_then_stop = Fraction(0)
    exact_policy = Fraction(0)
    advantage_sum = Fraction(0)
    for k in range(1, m+1):
        j = i + k
        posterior_second = beta + f + k - 1
        weight = rise(posterior_second, 0)*rise(beta+f, k-1)*A/rise(A+beta+f,k)
        stop_at_j = rise(posterior_second, m-k) / rise(A+1+posterior_second,m-k)
        assert weight*stop_at_j == common
        first_future_then_stop += weight*stop_at_j
        # Waiting until one further success, then stopping there.
        one_more_success = Fraction(0)
        for h in range(1, m-k+1):
            later_probability = rise(posterior_second,h-1)*(A+1)/rise(A+1+posterior_second,h)
            later_second = posterior_second+h-1
            reward = rise(later_second,m-k-h)/rise(A+2+later_second,m-k-h)
            one_more_success += later_probability*reward
        H = (A+1)*(m-k)/(B-1)
        assert one_more_success == stop_at_j*H
        exact_policy += weight*max(stop_at_j,one_more_success)
        advantage_sum += max(Fraction(0), m+1-delta-(A+1)*k)
    assert first_future_then_stop == g*m*A/B
    R = (-delta + A*advantage_sum/(B-1))/B
    assert exact_policy == g*(1+R)
    if m >= 100: assert R>0
    return {'alpha':str(alpha),'beta':str(beta),'m':m,'N':N,'first_success_i':i,
            'delta':str(delta),'ratio':float(R),'g':float(g),
            'target_ratio_limit':float(1/(2*A*(A+1)))}


def main():
    tests=[(1,1,20),(1,4,20),(Fraction(1,2),Fraction(3,7),20),
           (Fraction(11,2),Fraction(51,2),40), (Fraction(1,3),Fraction(80,3),80),
           (1,1,100),(Fraction(1,2),Fraction(3,7),100)]
    for row in tests:
        print(check(*row))
    print('PASS: exact rational policy and posterior identities for',len(tests),'cases')

if __name__=='__main__': main()
