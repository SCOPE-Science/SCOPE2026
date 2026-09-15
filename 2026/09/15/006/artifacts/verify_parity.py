"""Brute-force verification of parity obstruction for literal QTC2 definition.

Definition (literal target): pi in (a,a,c)-box, pi[i][j]+pi[a-1-j][a-1-i]==c
for all i!=j (0-indexed i!=j, i.e. 1-indexed i!=j, main diagonal free).
Cell (0,a-1) [1-indexed (1,a)] is fixed by the involution for every a>=2
and satisfies i!=j, hence requires 2*pi[0][a-1]==c.
For odd c this is impossible: count must be 0.
Paper/target formulas predict nonzero values there (e.g. 4 for a=2,c=1).
"""
import itertools


def plane_partitions(a, c):
    res = []
    def rec(idx, cur):
        if idx == a * a:
            res.append([cur[i * a:(i + 1) * a] for i in range(a)])
            return
        i, j = divmod(idx, a)
        hi = c
        if j > 0:
            hi = min(hi, cur[idx - 1])
        if i > 0:
            hi = min(hi, cur[idx - a])
        for v in range(hi + 1):
            cur.append(v)
            rec(idx + 1, cur)
            cur.pop()
    rec(0, [])
    return res


def count_qtc2_literal(a, c):
    cnt = 0
    for pi in plane_partitions(a, c):
        ok = True
        for i in range(a):
            for j in range(a):
                if i == j:
                    continue
                if pi[i][j] + pi[a - 1 - j][a - 1 - i] != c:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            cnt += 1
    return cnt


if __name__ == "__main__":
    # Key counterexamples: odd box heights where formula predicts nonzero.
    cases = [(2, 1, 4), (2, 3, 16), (3, 1, 7)]
    for a, c, predicted in cases:
        got = count_qtc2_literal(a, c)
        print(f"a={a} c_box={c}: brute-force count={got} predicted={predicted} "
              f"{'PARITY REFUTED' if got == 0 and predicted != 0 else ''}")
    # Even cases for context
    for a, c in [(2, 0), (2, 2), (3, 0), (3, 2)]:
        print(f"a={a} c_box={c}: count={count_qtc2_literal(a, c)}")
