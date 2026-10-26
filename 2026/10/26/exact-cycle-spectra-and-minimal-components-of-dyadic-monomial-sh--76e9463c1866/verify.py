"""Independent finite checks for a finite-ring permutation-cycle theorem.

The mathematical proof covers all degrees and all moduli; this program checks
selected finite cases by following every orbit directly.
"""
from collections import Counter


def predicted_length(x, degree, bits):
    if x == 0:
        return 1
    if x & 1:
        if degree % 2 == 0:
            return 1 << max(0, bits - 1)
        if bits == 1:
            return 1
        return 1 << max(1, bits - 2)
    valuation = (x & -x).bit_length() - 1
    return 1 << max(0, bits - 1 - degree * valuation)


def assert_case(degree, bits):
    modulus = 1 << bits
    nxt = [(x + 2 * pow(x, degree, modulus)) % modulus for x in range(modulus)]
    assert len(set(nxt)) == modulus, (degree, bits, "not a permutation")
    seen = bytearray(modulus)
    length_hist = Counter()
    for x in range(modulus):
        if seen[x]:
            continue
        y = x
        orbit = []
        while not seen[y]:
            seen[y] = 1
            orbit.append(y)
            y = nxt[y]
        assert y == x, (degree, bits, "noncycle")
        L = len(orbit)
        for z in orbit:
            assert predicted_length(z, degree, bits) == L, (
                degree, bits, z, L, predicted_length(z, degree, bits)
            )
        length_hist[L] += 1
    # Independently enumerate asserted valuation-shell cardinalities.
    theoretical = Counter()
    theoretical[predicted_length(0, degree, bits)] += 1
    odd_len = predicted_length(1, degree, bits)
    theoretical[odd_len] += (modulus >> 1) // odd_len
    for s in range(1, bits):
        shell_size = 1 << (bits - s - 1)
        shell_len = 1 << max(0, bits - 1 - degree * s)
        assert shell_size % shell_len == 0
        theoretical[shell_len] += shell_size // shell_len
    assert theoretical == length_hist, (degree, bits, theoretical, length_hist)
    return sum(length_hist.values())


def main():
    num_cases = 0
    num_states = 0
    all_cycles = 0
    for d in range(3, 22):
        for k in range(1, 14):
            all_cycles += assert_case(d, k)
            num_cases += 1
            num_states += 1 << k
    print(f"VERIFY_OK: {num_cases} exhaustive parameter pairs; {num_states} total enumerated residues; {all_cycles} independently traced cycles")


if __name__ == '__main__':
    main()
