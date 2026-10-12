"""Independent finite checks of a nice-integer asymptotic.

The asymptotic itself is proved analytically in RESULT.md; this script checks
finite arithmetic inputs and small residue-compatibility instances only.
"""
import math
from itertools import combinations


def sieve_profile(limit):
    spf = list(range(limit + 1))
    for p in range(2, math.isqrt(limit) + 1):
        if spf[p] == p:
            for multiple in range(p * p, limit + 1, p):
                if spf[multiple] == multiple:
                    spf[multiple] = p
    omega = bytearray(limit + 1)
    for n in range(2, limit + 1):
        p = spf[n]
        m = n // p
        omega[n] = omega[m] + int(m % p != 0)
    return spf, omega


def test_residue_assignment(n):
    """Directly decide the definition for small n, independently of the theorem.

    Every d>1 dividing n receives a residue a_d (mod d). Two congruences
    whose moduli are noncoprime must not be simultaneously solvable.
    """
    ds = [d for d in range(2, n + 1) if n % d == 0]
    residues = []
    def dfs(i):
        if i == len(ds):
            return True
        d = ds[i]
        for a in range(d):
            ok = True
            for prior, b in zip(ds, residues):
                g = math.gcd(d, prior)
                if g > 1 and (a - b) % g == 0:
                    ok = False
                    break
            if ok:
                residues.append(a)
                if dfs(i + 1):
                    return True
                residues.pop()
        return False
    return dfs(0)


def main():
    limit = 2_000_000
    spf, omega = sieve_profile(limit)
    assert spf[1] == 1 and omega[1] == 0
    for n in range(2, 2001):
        prime_divisors = [d for d in range(2, n + 1) if n % d == 0 and all(d % k for k in range(2, math.isqrt(d) + 1))]
        assert spf[n] == prime_divisors[0]
        assert omega[n] == len(prime_divisors)
        assert omega[n // spf[n]] == omega[n] - int(n // spf[n] % spf[n] != 0)

    small_instances = 0
    for n in range(2, 37):
        pred = omega[n // spf[n]] < spf[n]
        assert test_residue_assignment(n) == pred, n
        small_instances += 1

    checkpoints = []
    for x in (10000, 100000, 1000000, limit):
        good = sum(omega[n // spf[n]] < spf[n] for n in range(2, x + 1))
        L = math.log(math.log(x))
        approx = math.exp(-0.5772156649015329) * x / math.log(L)
        threshold_low, threshold_high = L / 2, 2 * L
        rough_low = 1 + sum(spf[n] > threshold_low for n in range(2, x + 1))
        rough_high = 1 + sum(spf[n] > threshold_high for n in range(2, x + 1))
        outside = sum(abs(omega[n] - L) > L / 4 for n in range(2, x + 1))
        assert good <= rough_low + outside
        assert rough_high - outside <= good + 1
        checkpoints.append((x, good, rough_low, rough_high, outside, round(good / approx, 6)))

    print('VERIFY_OK direct_prime_profile=2..2000 independent_residue_instances=2..36')
    for x, good, rough_low, rough_high, outside, ratio in checkpoints:
        print(f'x={x} nice={good} rough_low={rough_low} rough_high={rough_high} concentration_exceptions={outside} ratio_to_asymptotic={ratio}')
    print('finite_checks_only=yes infinite_asymptotic_proof_in_RESULT.md=yes')

if __name__ == '__main__':
    main()
