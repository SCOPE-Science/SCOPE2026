# Certified analytic upper bounds for (k,3)-arcs in PG(2,7) and PG(2,8).
# Lemma (cap): fix P in K; q+1 lines through P each carry <=2 further points
# of K, so k-1 <= 2(q+1), i.e. k <= 2q+3.
# Divisibility refinement: if every P in K lies on the SAME number t of
# 3-secants, then 3*t3 = k*t (each 3-secant has 3 points of K), so k*t must
# be divisible by 3. This rules out k=16,17 at q=7 (both force a unique t).
# At q=8 no k in range has a unique forced t that is ruled out, so the
# certified bound there is just the cap k<=19.
# Run: python3 artifacts/bound.py  (stdlib only; asserts all claims)
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))

def forced_t3_per_point(q, k):
    """If the count of 'further points of K' on the q+1 lines through P forces
    a unique number of 3-secants through P, return it; else None."""
    others = k - 1
    nlines = q + 1
    sols = []
    for t in range(nlines + 1):          # t = #lines with 2 further points
        for s in range(nlines + 1 - t):  # s = #lines with 1 further point
            if 2 * t + s == others:
                sols.append(t)
    return sols[0] if len(sols) == 1 else None

def report(q):
    cap = 2 * q + 3
    rows = []
    for k in range(1, cap + 1):
        t = forced_t3_per_point(q, k)
        ruled = t is not None and (k * t) % 3 != 0
        rows.append((k, t, ruled))
    feasible = [k for k, t, r in rows if not r]
    return cap, rows, feasible

if __name__ == '__main__':
    out = {}
    for q in (7, 8):
        cap, rows, feas = report(q)
        print(f'q={q}: cap k<={cap}')
        for k, t, r in rows:
            if k >= cap - 4:
                print(f'  k={k}: 3-secants/P forced={t} product={k*t if t is not None else None} ruled_out={r}')
        print(f'  feasible k (not ruled out): ... max region {feas[-6:]}')
        out[q] = {'cap': cap, 'rows': [[k, t, r] for k, t, r in rows]}
    # Hard assertions = the certified claims
    assert forced_t3_per_point(7, 16) == 7 and (16 * 7) % 3 != 0   # no (16,3)-arc in PG(2,7)
    assert forced_t3_per_point(7, 17) == 8 and (17 * 8) % 3 != 0   # no (17,3)-arc in PG(2,7)
    assert forced_t3_per_point(8, 18) == 8 and (18 * 8) % 3 == 0   # k=18 q=8 consistent (t3=48)
    assert forced_t3_per_point(8, 19) == 9 and (19 * 9) % 3 == 0   # k=19 q=8 consistent (t3=57)
    # q=7: cap is 17, both 16,17 ruled out -> every (k,3)-arc has k<=15
    # q=8: cap is 19, nothing further ruled out -> certified interval k<=19
    print('BOUND_OK: q=7 max<=15; q=8 max<=19')
    json.dump(out, open(os.path.join(HERE, 'unsat_log.json'), 'w'))
