"""Exact classical distance of the 48x64 base QC code: d = 8 (stdlib only).
Lower bound d>=8: every codeword S of weight <=7 contains a 4-subset C (if |S|>=4)
with syndrome(C)==syndrome(S\\C), |S\\C|<=3; or |S|<=3 with syndrome 0.
So: (i) check no weight 1..3 pattern has syndrome 0; (ii) tabulate all syndromes
of weight<=3 patterns (43745 entries) and check every C(64,4)=635376 4-pattern
against the table. No match => no codeword of weight<=7.
Upper bound: explicit weight-8 codeword {18,22,26,30,34,38,42,46} has syndrome 0.
Syndromes are 48-bit Python ints; exact arithmetic throughout.
"""
from itertools import combinations

A = [[14, 1, 9, 6], [12, 10, 6, 0], [4, 4, 8, 3]]
L = 16

def base_cols():
    cols = []
    for j in range(4):
        for t in range(16):
            mask = 0
            for i in range(3):
                mask |= 1 << (i * 16 + ((t + A[i][j]) % 16))
            cols.append(mask)
    return cols

def main():
    cols = base_cols()
    n = len(cols)
    assert n == 64
    for w in (1, 2, 3):
        for c in combinations(range(n), w):
            s = 0
            for j in c:
                s ^= cols[j]
            assert s != 0, f"weight-{w} codeword found: {c}"
    print("no codeword of weight<=3: OK")
    tab = {0: 0}
    for w in (1, 2, 3):
        for c in combinations(range(n), w):
            s = 0
            m = 0
            for j in c:
                s ^= cols[j]
                m |= 1 << j
            if s not in tab:
                tab[s] = m
    print(f"syndrome table size: {len(tab)} (expect 43745 = C(64,0..3))")
    assert len(tab) == 1 + 64 + 2016 + 41664
    checked = 0
    for c in combinations(range(n), 4):
        s = cols[c[0]] ^ cols[c[1]] ^ cols[c[2]] ^ cols[c[3]]
        if s in tab:
            m = (1 << c[0]) | (1 << c[1]) | (1 << c[2]) | (1 << c[3])
            other = tab[s]
            diff = bin(m ^ other).count("1")
            raise SystemExit(f"codeword of weight<={4 + 3} exists (symmetric diff {diff})")
        checked += 1
    print(f"checked {checked} 4-patterns (expect 635376), no match")
    assert checked == 635376
    w8 = [18, 22, 26, 30, 34, 38, 42, 46]
    s = 0
    for j in w8:
        s ^= cols[j]
    assert s == 0
    print(f"explicit weight-8 codeword {w8}: syndrome 0")
    print("CLASSICAL_D8_OK: base classical distance == 8")

if __name__ == "__main__":
    main()
