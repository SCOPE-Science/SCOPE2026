#!/usr/bin/env python3
"""Exact finite checks for dyadic-shell minima of the cumulative binary digit deficit."""

def predicted_offsets(k):
    if k == 1:
        return {1}
    ell = k - 1
    prefixes = {''}
    pair_count = (ell - 1)//2 if ell % 2 else (ell - 2)//2
    for _ in range(pair_count):
        prefixes = {p + q for p in prefixes for q in ('01', '10')}
    endings = ('1',) if ell % 2 else ('01', '10', '11')
    return {int(p + s, 2) for p in prefixes for s in endings}

def check_shells(K=17):
    total, current_k, min_value, minimizers = 0, 1, None, []
    def check_one(k, value, positions):
        expected = {(1 << k)+j-1 for j in predicted_offsets(k)}
        assert value == (1 << (k+1)) // 3, (k, value)
        assert set(positions) == expected, (k, positions, expected)
    for n in range(1, 1 << (K+1)):
        total += 2 * n.bit_count() - n.bit_length()
        k = n.bit_length()-1
        if k < 1:
            continue
        if k > current_k:
            check_one(current_k, min_value, minimizers)
            current_k, min_value, minimizers = k, None, []
        if min_value is None or total < min_value:
            min_value, minimizers = total, [n]
        elif total == min_value:
            minimizers.append(n)
    check_one(K, min_value, minimizers)

def check_takagi(ell_max=15):
    # Integer evaluation of 2^ell*tau(j/2^ell) via the finite tent-function series.
    for ell in range(1, ell_max+1):
        den = 1 << ell
        vals = []
        for j in range(den+1):
            val = sum(min(j % (den >> h), (den >> h)-j % (den >> h)) for h in range(ell))
            vals.append(val)
        assert max(vals) == (1 << (ell+1)) // 3
        assert {j for j,v in enumerate(vals) if v == max(vals)} == predicted_offsets(ell+1)

if __name__ == '__main__':
    check_shells()
    check_takagi()
    print('VERIFIED: exact cumulative binary-defect minima on 17 dyadic shells (262142 terms above index 1), plus integer Takagi maximizers at levels 1 through 15.')
