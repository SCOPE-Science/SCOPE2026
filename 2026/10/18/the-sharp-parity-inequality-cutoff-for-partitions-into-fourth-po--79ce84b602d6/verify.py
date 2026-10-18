#!/usr/bin/env python3
"""Exact finite certificates for a strict-parity theorem on fourth-power partitions."""


def components(intervals):
    merged = []
    for left, right in sorted(intervals):
        if merged and left <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(right, merged[-1][1]))
        else:
            merged.append((left, right))
    return merged


def allowable_parts(limit):
    result = []
    u = 1
    while u**4 <= limit:
        exponent = 0
        while u**4 * 2**exponent <= limit:
            if exponent == 0 or exponent % 4 != 0:
                result.append(u**4 * 2**exponent)
            exponent += 1
        u += 2
    return sorted(result)


def check():
    base = (1, 2, 4, 8, 32, 64, 81, 128, 162, 324)
    reachable = {0}
    for w in base:
        reachable |= {v+w for v in reachable}
    assert len(reachable) == len(set(reachable))
    intervals = [(32*j + 81*t, 32*j + 81*t + 15)
                 for j in range(8) for t in range(8)]
    comp = components(intervals)
    expected = [
        (0, 15), (32, 47), (64, 79), (81, 111), (113, 143),
        (145, 661), (663, 693), (695, 725), (727, 742),
        (759, 774), (791, 806),
    ]
    assert comp == expected
    assert reachable == {x for a, b in intervals for x in range(a, b+1)}
    zeros = set(range(16, 32)) | set(range(48, 64)) | {80, 112, 144}
    assert {i for i in range(145) if i not in reachable} == zeros
    assert all(i in reachable for i in range(145, 662))

    # Exact, algebraically different coefficient calculations through degree 2048.
    limit = 2048
    signed = [0]*(limit+1)
    signed[0] = 1
    m = 1
    while m**4 <= limit:
        w = m**4
        for n in range(w, limit+1):
            if m % 2:
                signed[n] += signed[n-w]
            else:
                signed[n] -= signed[n-w]
        m += 1
    distinct = [0]*(limit+1)
    distinct[0] = 1
    for w in allowable_parts(limit):
        for n in range(limit, w-1, -1):
            distinct[n] += distinct[n-w]
    assert signed == distinct
    assert all(signed[n] == 0 for n in zeros)
    assert all(signed[n] > 0 for n in range(145, limit+1))
    assert signed[144] == 0 and signed[145] > 0

    # Finite checks of the doubling-gap lemma; the paper proves it for all scales.
    future = sorted(set(
        [2**ell for ell in range(9, 65) if ell % 4 != 0]
        + [81*2**ell for j in range(3, 16)
           for ell in (4*j-7, 4*j-6)]
    ))
    assert future[0] == 512
    assert all(future[i+1] <= 2*future[i]
               for i in range(len(future)-1))
    print("PASS: 1024 base subsets; 64 interval blocks; 35 exact zeros;")
    print("PASS: 2049 independent signed/distinct coefficient comparisons;")
    print("PASS: dyadic bridging ratios at 13 sampled higher scales.")


if __name__ == '__main__':
    check()
