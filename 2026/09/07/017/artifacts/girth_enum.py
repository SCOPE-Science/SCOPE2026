"""Exhaustive reduced-word enumeration for girth. Stdlib only.
Reduced = no immediate inverse pair (a/A, b/B). Identity in PSL means product = +I or -I in SL.
"""
P = 13

def mm(A, B):
    return ((A[0]*B[0]+A[1]*B[2]) % P,
            (A[0]*B[1]+A[1]*B[3]) % P,
            (A[2]*B[0]+A[3]*B[2]) % P,
            (A[2]*B[1]+A[3]*B[3]) % P)

GENS = [('a', (1, 1, 0, 1)), ('A', (1, 12, 0, 1)),
        ('b', (1, 0, 1, 1)), ('B', (1, 0, 12, 1))]
GDICT = dict(GENS)
INV = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
IDENT = (1, 0, 0, 1)
NEGI = (12, 0, 0, 12)

def enumerate_length(L):
    hits = []
    total = [0]
    def rec(prod, word, last):
        if len(word) == L:
            total[0] += 1
            if prod == IDENT or prod == NEGI:
                hits.append(word)
            return
        for letter, G in GENS:
            if last is not None and letter == INV[last]:
                continue
            rec(mm(prod, G), word + letter, letter)
    rec(IDENT, '', None)
    return total[0], sorted(hits)

def eval_word(w):
    M = IDENT
    for ch in w:
        M = mm(M, GDICT[ch])
    return M

def main():
    import sys
    sys.setrecursionlimit(10000)
    maxL = 8 if len(sys.argv) < 2 else int(sys.argv[1])
    for L in range(1, maxL + 1):
        total, hits = enumerate_length(L)
        print("L=%d total_reduced=%d hits=%d" % (L, total, len(hits)))
        for w in hits[:40]:
            M = eval_word(w)
            tag = "+I" if M == IDENT else "-I"
            print("  ", w, tag)
    # certify girth
    totals = {}
    for L in range(1, 7):
        t, h = enumerate_length(L)
        totals[L] = (t, len(h))
    assert all(totals[L][1] == 0 for L in range(1, 6)), totals
    assert totals[6][1] == 28, totals
    assert totals[6][0] == 972
    wg = "aaBaaB"
    assert eval_word(wg) == NEGI, eval_word(wg)
    assert all(wg[i+1] != INV[wg[i]] for i in range(len(wg)-1))
    print("girth g=6 certified; witness w_g=aaBaaB -> -I OK")

if __name__ == "__main__":
    main()
