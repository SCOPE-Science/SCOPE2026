"""Exact rational independent-cylinder check of a randomly switched full-branch map."""
from fractions import Fraction as Q
from itertools import product


def triple_exact(delta, p, n):
    # Enumerate every environment path and every full-branch inverse cylinder.
    branch_params = {1: (1 + delta) / 2, -1: (1 - delta) / 2}
    total_future = Q(0)
    total_past = Q(0)
    for env in product((-1, 1), repeat=n):
        probability = Q(1, 2)
        for j in range(n - 1):
            probability *= p if env[j] == env[j + 1] else 1 - p
        a_seq = [branch_params[e] for e in env]
        for word in product((0, 1), repeat=n):
            A, B = Q(1), Q(0)
            for a, left in zip(reversed(a_seq), reversed(word)):
                slope, offset = (a, Q(0)) if left == 0 else (-(1 - a), Q(1))
                A, B = slope * A, slope * B + offset
            # For every cylinder, x0=A*z+B, xn=z, z in (0,1), dx0=|A| dz.
            # Exact integrals of (x0-1/2)^2*(xn-1/2) and vice versa.
            weight = probability * abs(A)
            total_future += weight * A * (A + 2 * B - 1) / 12
            total_past += weight * (A + 2 * B - 1) / 24
    return total_future, total_past


def theorem(delta, p, n):
    d = delta * delta
    b = (1 + 3*d)/4
    z = d*(2*p-1)
    c = -(1-d)/4
    return (c / 12 * sum((b**(n-1-2*j)*z**j for j in range((n-1)//2+1)), Q(0)), Q(0))


def run():
    cases = [(Q(1,2),Q(1,3)), (Q(1,2),Q(1,16)),
             (Q(1,2),Q(15,128)), (Q(1,4),Q(1,16)),
             (Q(3,4),Q(1,12)),(Q(4,5),Q(4,5))]
    tests = 0
    for d,p in cases:
        for n in range(1,7):
            observed = triple_exact(d,p,n)
            expected = theorem(d,p,n)
            assert observed == expected, (d, p, n, observed, expected)
            tests += 1
    for d,p in ((Q(1,2),Q(1,16)), (Q(1,2),Q(15,128))):
        for n in (7,8):
            assert triple_exact(d,p,n) == theorem(d,p,n)
            tests += 1
    assert theorem(Q(1,2),Q(15,128),3)[0] == 0
    assert theorem(Q(1,2),Q(15,128),4)[0] == 0
    assert theorem(Q(1,2),Q(1,16),3)[0] > 0
    assert theorem(Q(1,2),Q(1,16),4)[0] > 0
    assert theorem(Q(1,2),Q(1,16),5)[0] < 0
    assert theorem(Q(1,2),Q(1,16),6)[0] < 0
    print(f'VERIFY_OK {tests} exact independent cylinder comparisons; 6 boundary and sign identities')


if __name__ == '__main__':
    run()
