#!/usr/bin/env python3
"""Self-contained finite witness verifier for a six-letter cyclic order-four sequence."""
from pathlib import Path


def verify(word):
    q, n, m = 6, 4, 603
    assert len(word) == m, ('length', len(word))
    assert set(word) == set('012345')
    forward = [''.join(word[(i+j) % m] for j in range(n)) for i in range(m)]
    backward = [''.join(word[(i-j) % m] for j in range(n)) for i in range(m)]
    fw, bw = set(forward), set(backward)
    assert len(fw) == m and len(bw) == m
    assert fw.isdisjoint(bw)
    assert all(w != w[::-1] for w in fw)
    # Exhaustive all-pairs test of the original definition, including same start.
    assert all(forward[i] != forward[j][::-1]
               for i in range(m) for j in range(m))
    pal = {a+b+b+a for a in '012345' for b in '012345'}
    assert len(pal) == 36 and fw.isdisjoint(pal)
    assert len(fw | bw | pal) == 1242
    assert (6**4-len(fw | bw | pal))//2 == 27
    # Distinct forward windows force fundamental period exactly m.
    assert all(any(word[i] != word[(i+d)%m] for i in range(m))
               for d in range(1,m))
    return len(forward), len(fw), len(bw), len(fw | bw | pal)


def main():
    s = Path(__file__).with_name('witness.txt').read_text(encoding='utf-8').strip()
    a,b,c,d = verify(s)
    print(f'VERIFY_OK period={a} distinct_four_windows={b} distinct_reverse_windows={c} partitioned_words={d} omitted_reversal_pairs=27')

if __name__ == '__main__': main()
