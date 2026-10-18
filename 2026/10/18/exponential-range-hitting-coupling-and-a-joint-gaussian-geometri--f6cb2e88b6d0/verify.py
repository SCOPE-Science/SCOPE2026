"""Deterministic finite diagnostics for biased-cycle range-cover coupling.

Run with Python 3.10+: python verify.py
The finite checks illustrate, but do not prove, the infinite probabilistic limits.
"""
from fractions import Fraction
from itertools import product


def exact_moments_and_ruin():
    assertions = 0
    for p in [Fraction(2, 3), Fraction(3, 4), Fraction(9, 10), Fraction(11, 20)]:
        q = 1 - p
        mu = p - q
        r = q / p
        mean = Fraction(1, 1) / mu
        second = (1 + 4 * q * mean + 2 * q * mean * mean) / mu
        variance = second - mean * mean
        assert variance == 4 * p * q / mu**3
        assertions += 1
        for k in range(1, 8):
            for level in range(-k + 1, k + 8):
                harm = r ** (level + k)
                assert harm == p * r ** (level + k + 1) + q * r ** (level + k - 1)
                assertions += 1
    return assertions


def finite_path_checks():
    assertions = 0
    admissible = 0
    # The prefix range equals the number of visited residues until full coverage.
    for n in range(3, 9):
        b = (n - 1) // 2
        for path in product((-1, 1), repeat=12):
            pos = [0]
            for step in path:
                pos.append(pos[-1] + step)
            prefix_min = 0
            prefix_max = 0
            covered = set()
            first_cover = None
            hit_b = None
            for t, z in enumerate(pos):
                covered.add(z % n)
                prefix_min = min(prefix_min, z)
                prefix_max = max(prefix_max, z)
                assert (len(covered) == n) == (prefix_max - prefix_min >= n - 1)
                assertions += 1
                if hit_b is None and z == b:
                    hit_b = t
                if first_cover is None and len(covered) == n:
                    first_cover = t
            if first_cover is None or hit_b is None:
                continue
            # Finite-horizon analogue of the sufficient good event in the proof.
            global_prefix_min = min(pos)
            k = -global_prefix_min
            if k > b or min(pos[:hit_b + 1]) != global_prefix_min:
                continue
            target = n - 1 - k
            hit_target = next((t for t, z in enumerate(pos) if z == target), None)
            assert hit_target == first_cover
            assert pos[first_cover] % n == target
            admissible += 1
            assertions += 2
    assert admissible > 0
    return assertions, admissible


def main():
    a = exact_moments_and_ruin()
    b, good_paths = finite_path_checks()
    print(f"PASS: {a + b} deterministic assertions; {good_paths} qualifying finite paths")
    print("Limits and exponentially small error estimates depend on the written proof.")


if __name__ == "__main__":
    main()
