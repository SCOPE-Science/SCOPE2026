#!/usr/bin/env python3
"""Finite-field PSL(2,q) two-round atomic-diagram verification.

Uses exact full atomic signatures, not truncated element orders or hash comparisons.
Works with g++ (C++17) and Python 3 standard library.
"""
import hashlib
import pathlib
import subprocess
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
CASES = {
    2: (2, 1, [0]), 3: (3, 1, [0]), 4: (2, 2, [1, 1]),
    5: (5, 1, [0]), 7: (7, 1, [0]), 8: (2, 3, [1, 1, 0]),
    9: (3, 2, [1, 0]), 11: (11, 1, [0]), 13: (13, 1, [0]),
    16: (2, 4, [1, 1, 0, 0]), 17: (17, 1, [0]),
    19: (19, 1, [0]), 23: (23, 1, [0]),
    25: (5, 2, [2, 0]), 27: (3, 3, [1, 2, 0]),
    29: (29, 1, [0]), 31: (31, 1, [0]),
}

def flags(q):
    return (q % 2 == 1 and q % 8 in (1, 7),
            q % 2 == 1 and q % 12 in (1, 11),
            q % 2 == 1 and q % 16 in (1, 15),
            q % 2 == 1 and q >= 11)

def category(q):
    return ('exception', q) if q in (2, 3) else ('regular', flags(q))

with tempfile.TemporaryDirectory() as td:
    binary = pathlib.Path(td) / 'types'
    subprocess.run(['g++', '-std=c++17', '-O3', str(HERE / 'verify.cpp'), '-o', str(binary)], check=True)
    signatures = {}
    for q, (p, f, modulus) in CASES.items():
        args = [str(binary), str(p), str(f)] + [str(x) for x in modulus]
        text = subprocess.check_output(args, text=True)
        lines = text.strip().splitlines()
        tag, qq, n, typ = lines[0].split()
        assert tag == 'GROUP' and int(qq) == q and int(n) == q * (q * q - 1) // (1 if q % 2 == 0 else 2)
        assert int(typ) == len(lines) - 1
        assert all(s.startswith('SIG ') for s in lines[1:])
        # Exact bytewise signature used in comparisons. Digest only for compact output.
        signatures[q] = '\n'.join(sorted(lines[1:]))
        h = hashlib.sha256(signatures[q].encode()).hexdigest()[:16]
        print(f'FIELD q={q:2d} size={n:>5} rooted={typ} digest={h}')
    for q in CASES:
        for r in CASES:
            assert (signatures[q] == signatures[r]) == (category(q) == category(r)), (q, r)
    print('DIRECT_EXHAUSTIVE_2ROUND_SIGNATURE_COMPARISONS_OK')
    print('TESTED_GROUPS', len(CASES))
    print('VERIFY_OK')
