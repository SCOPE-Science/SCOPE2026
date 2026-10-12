from itertools import combinations
from math import gcd, lcm


def nu(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def D_S(n, S):
    return sum((n // p) * nu(n, p) for p in S)


def subsets(S):
    for r in range(1, len(S) + 1):
        yield from combinations(S, r)


def P(T):
    out = 1
    for p in T:
        out *= p
    return out


def H(T):
    pt = P(T)
    return sum(pt // p for p in T)


def predicted_fiber(y, S):
    out = []
    for T in subsets(S):
        h = H(T)
        if y % h == 0:
            out.append(P(T) * (y // h))
    return sorted(out)


def brute_fiber(y, S):
    # If D_S(n)=y>0, then D_S(n)>=n/max(S), hence n<=max(S)*y.
    return [n for n in range(1, max(S) * y + 1) if D_S(n, S) == y]


def admissible(S):
    ps = P(S)
    return [T for T in subsets(S) if gcd(H(T), ps) == 1]


def main():
    cases = [(2, 3), (2, 3, 5), (3, 5, 7), (2, 5, 7, 11)]
    tested = 0
    for S in cases:
        ps = P(S)
        for y in range(1, 100):
            if gcd(y, ps) != 1:
                continue
            got = brute_fiber(y, S)
            want = predicted_fiber(y, S)
            assert got == want, (S, y, got, want)
            tested += 1
        A = admissible(S)
        ystar = 1
        for T in A:
            ystar = lcm(ystar, H(T))
        assert gcd(ystar, ps) == 1
        assert len(predicted_fiber(ystar, S)) == len(A)
        assert len(predicted_fiber(1, S)) == len(S)

    S = (2, 3, 5)
    y = 217
    example = predicted_fiber(y, S)
    assert example == [210, 310, 434, 651, 1085]
    assert all(D_S(n, S) == y for n in example)
    print(f"VERIFY_OK coprime_targets_tested={tested} example_S=2,3,5 y=217 fiber={','.join(map(str, example))}")


if __name__ == "__main__":
    main()
