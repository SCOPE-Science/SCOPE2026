#!/usr/bin/env python3
"""Exhaustive finite enumeration of minimal absent factors in dyadic Rudin--Shapiro prefixes.

Run using: python3 verify.py
Only standard-library Python is required.
"""
import hashlib
import random
from collections import Counter
from pathlib import Path

EXPECTED_DIGESTS = {
    7: '2d75eaf797a84b0c7ac57dec70e61421a228ae9d9d464ddc6c6ca3b63194888d',
    8: 'a62c2e19dd913fb82860c3fc49b73343983509a1b896a997c07ed3d546381892',
    9: 'ab3d5e7b7d42dc6ed12bc009b5d453bfc886bb5cbbc2c3ca0b744e8bd1fc5651',
    10: '8c8dda5808016c808d5f1b64ddabf0b876e0f0c05abd723986aa291cfad41056',
    11: 'c1d203512ff245b31d34d94b0f61b526ed761b441c036264602667c89db82956',
    12: '47c420c682cf352ec7f2ee943e8c356d0ae1664f658819cc8dc3b83ad3c45a90',
    13: '8b49c683611bd14710dfbbc635315bb65e7f34e165a06bf85d8c2683fd70c91d',
    14: '45f3f133fba28ae5d13caa457a8cc4e08a98dc9facea1a76e70c04f53e82a763',
    15: 'fd38ae3c5df38965b46e88e732f63bae6c058446d65295c64aa37dc7882c65ce',
    16: '03a86f3dd02d3ac44734981148d68bbc66917441ae1f319dd9001bb152a561fa',
}


def rudin_shapiro_binary(length):
    return ''.join(str((i & (i >> 1)).bit_count() & 1) for i in range(length))


def recursive_rudin_shapiro(length):
    # The two decimation identities are exact consequences of binary 11 counting.
    r = [0] * length
    for i in range(1, length):
        p = i // 2
        r[i] = r[p] if i % 2 == 0 else r[p] ^ (p & 1)
    return ''.join(map(str, r))


def suffix_array(word):
    n = len(word)
    order = list(range(n))
    rank = [ord(c) for c in word]
    temporary = [0] * n
    step = 1
    while True:
        order.sort(key=lambda i: (rank[i], rank[i + step] if i + step < n else -1))
        temporary[order[0]] = 0
        for j in range(1, n):
            a, b = order[j - 1], order[j]
            temporary[b] = temporary[a] + (
                (rank[a], rank[a + step] if a + step < n else -1)
                != (rank[b], rank[b + step] if b + step < n else -1)
            )
        rank, temporary = temporary, rank
        if rank[order[-1]] == n - 1:
            return order
        step *= 2


def adjacent_lcp(word, order):
    n = len(word)
    position = [0] * n
    for j, i in enumerate(order):
        position[i] = j
    lengths = [0] * (n - 1)
    common = 0
    for i in range(n):
        p = position[i]
        if p == n - 1:
            common = 0
            continue
        j = order[p + 1]
        while i + common < n and j + common < n and word[i + common] == word[j + common]:
            common += 1
        lengths[p] = common
        common = max(0, common - 1)
    return lengths


def absent_words(word):
    n = len(word)
    order = suffix_array(word)
    lcp = adjacent_lcp(word, order)
    cores = {''}
    cores.update(word[order[i]:order[i] + h] for i, h in enumerate(lcp) if h)
    missing = set()
    for core in cores:
        size = len(core)
        # Bits 0--3: observed two-sided combinations; 4--5: left letters;
        # 6--7: right letters. Boundary-only occurrences count on one side.
        mask = 0
        start = word.find(core)
        while start != -1:
            left = ord(word[start - 1]) - 48 if start else -1
            after = start + size
            right = ord(word[after]) - 48 if after < n else -1
            if left >= 0:
                mask |= 1 << (4 + left)
            if right >= 0:
                mask |= 1 << (6 + right)
            if left >= 0 and right >= 0:
                mask |= 1 << (2 * left + right)
            start = word.find(core, start + 1)
        for left in range(2):
            for right in range(2):
                if ((mask >> (4 + left)) & 1 and (mask >> (6 + right)) & 1
                        and not ((mask >> (2 * left + right)) & 1)):
                    missing.add(str(left) + core + str(right))
    missing.update(a for a in '01' if a not in word)
    return sorted(missing, key=lambda x: (len(x), x))


def all_factors_direct(word):
    factors = {''}
    for start in range(len(word)):
        for stop in range(start + 1, len(word) + 1):
            factors.add(word[start:stop])
    return factors


def direct_absent_words(word):
    factors = all_factors_direct(word)
    missing = {a for a in '01' if a not in factors}
    for core in factors:
        for a in '01':
            if a + core not in factors:
                continue
            for b in '01':
                if core + b in factors and a + core + b not in factors:
                    missing.add(a + core + b)
    return sorted(missing, key=lambda x: (len(x), x))


def expected_histogram(m):
    spectrum = {5: 8, 6: 4, 7: 10, 8: 4, 9: 4}
    for j in range(3, m - 1):
        spectrum[(1 << j) + 2] = 1 if j == m - 2 else 12 if j == m - 4 else 8
    return spectrum


def verify():
    table = ['m\tprefix_length\tcount\tmaximum_length\tsha256_of_sorted_maws']
    for m in range(7, 17):
        word = rudin_shapiro_binary(1 << m)
        assert word == recursive_rudin_shapiro(1 << m)
        maws = absent_words(word)
        assert len(maws) == len(set(maws))
        assert dict(Counter(map(len, maws))) == expected_histogram(m)
        assert len(maws) == 8 * m - 5
        for candidate in maws:
            assert candidate not in word
            if len(candidate) > 1:
                assert candidate[:-1] in word and candidate[1:] in word
        digest = hashlib.sha256(('\n'.join(maws) + '\n').encode('utf-8')).hexdigest()
        assert digest == EXPECTED_DIGESTS[m], (m, digest)
        if m <= 8:
            assert maws == direct_absent_words(word)
        table.append(f'{m}\t{len(word)}\t{len(maws)}\t{max(map(len, maws))}\t{digest}')
        print(f'checked m={m}, length={len(word)}, MAWs={len(maws)}')
    rng = random.Random(2026)
    for length in range(2, 18):
        for _ in range(8):
            word = ''.join(rng.choice('01') for _ in range(length))
            assert absent_words(word) == direct_absent_words(word)
    assert '\n'.join(table) + '\n' == Path(__file__).with_name('SPECTRUM.tsv').read_text(encoding='utf-8')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
