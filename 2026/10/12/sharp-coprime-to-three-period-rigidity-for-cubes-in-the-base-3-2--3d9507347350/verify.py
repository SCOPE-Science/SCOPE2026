"""Reproducibility checks for cube-period rigidity in sesquinary digit parity.
All finite tests supplement the unrestricted combinatorial proof.
"""
from math import gcd

N = 120_000
x = bytearray(N)
for n in range(1, N):
    q, r = divmod(n, 3)
    x[n] = x[2*q] ^ (r == 1)

def parity_direct(n):
    total = 0
    while n:
        r = n % 3
        total ^= r & 1
        n = 2 * (n-r) // 3
    return total

for n in range(5000):
    assert x[n] == parity_direct(n), (n, x[n], parity_direct(n))

for n in range((N-2)//3):
    assert x[3*n] == x[3*n+2] == x[2*n]
    assert x[3*n+1] == 1-x[2*n]

last = 0
max_alternation = 1
starts = []
for i in range(1, N):
    if x[i] == x[i-1]:
        length = i-last
        if length > max_alternation:
            max_alternation = length
            starts = [last]
        elif length == max_alternation and len(starts) < 4:
            starts.append(last)
        last = i
length = N-last
if length > max_alternation:
    max_alternation = length
    starts = [last]
assert max_alternation == 9, (max_alternation, starts)
assert bytes(x[12:21]) == b'\x01\x00\x01\x00\x01\x00\x01\x00\x01'
assert bytes(x[18:33]) == bytes([1,0,1])*5

# Independently test all shift/period patterns of the cube theorem
# using a streaming single-period comparison, not a pre-specified factor list.
cases = 0
for p in range(1, 91):
    if gcd(p,3) != 1:
        continue
    matches = 0
    for i in range(N-p):
        if x[i] == x[i+p]:
            matches += 1
            if matches >= 2*p:
                assert p == 2, (p, i-2*p+1)
                cases += 1
        else:
            matches = 0
assert cases > 0

# Purely finite validation of the modular edge-coverage lemma.
for p in range(2, 91):
    if gcd(p,3) != 1:
        continue
    for omitted in range(p):
        residues = set(range(p)) - {omitted}
        supported_edges = set()
        for r in residues:
            supported_edges.add(r)
            supported_edges.add((r+1) % p)
        assert supported_edges == set(range(p))

print('VERIFY_OK')
print('digit_sum_parity_independent_checks=5000_PASS')
print('block_recurrence_checks=' + str((N-2)//3) + '_PASS')
print('max_alternating_prefix_length=' + str(max_alternation) + '_PASS')
print('periods_coprime_to_three_up_to_90_direct_cube_scan=PASS')
print('residue_edge_coverage_check_up_to_90=PASS')
print('period_2_four_and_half_power_at_index_12=PASS')
print('period_3_fifth_power_at_index_18=PASS')
print('finite_checks_do_not_prove_infinite_classification')
