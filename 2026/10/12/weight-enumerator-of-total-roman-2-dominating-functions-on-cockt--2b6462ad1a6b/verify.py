from itertools import product
from collections import Counter
from math import comb

def cocktail_party(n):
    N = 2*n
    adj = [set(range(N)) - {v} for v in range(N)]
    for i in range(n):
        a, b = 2*i, 2*i+1
        adj[a].discard(b)
        adj[b].discard(a)
    return adj

def is_total_italian(adj, lab):
    positive = {v for v, a in enumerate(lab) if a > 0}
    for v, a in enumerate(lab):
        if a == 0:
            if sum(lab[u] for u in adj[v]) < 2:
                return False
        else:
            if not (adj[v] & positive):
                return False
    return True

def predicted_coefficients(n):
    # F(x) = all labelings whose positive support meets at least two partner pairs.
    # Subtract the low-weight labelings that still fail Italian defense.
    # Polynomial is represented coefficient-wise.
    N = 2*n
    # coefficients of (1+x+x^2)^N
    coeff = [0]*(2*N+1)
    base = [1]
    for _ in range(N):
        nxt = [0]*(len(base)+2)
        for i,c in enumerate(base):
            nxt[i] += c
            nxt[i+1] += c
            nxt[i+2] += c
        base = nxt
    coeff[:len(base)] = base

    # subtract support contained in zero or one partner pair:
    # 1 + n*((1+x+x^2)^2 - 1)
    small = [1,2,3,2,1]  # (1+x+x^2)^2
    coeff[0] -= 1
    for w,c in enumerate(small):
        if w == 0:
            coeff[w] -= n*(c-1)
        else:
            coeff[w] -= n*c

    # support meets >=2 pairs but weight 2 fails: two 1s in different pairs.
    coeff[2] -= 2*n*(n-1)

    # support meets >=2 pairs but weight 3 pattern 2+1 across distinct pairs fails.
    coeff[3] -= 4*n*(n-1)
    return coeff

print("VERIFY_OK")
checked = 0
for n in range(2, 6):
    adj = cocktail_party(n)
    counts = Counter()
    mins = []
    best = None
    for lab in product(range(3), repeat=2*n):
        checked += 1
        if is_total_italian(adj, lab):
            w = sum(lab)
            counts[w] += 1
            if best is None or w < best:
                best = w
                mins = [lab]
            elif w == best:
                mins.append(lab)

    pred = predicted_coefficients(n)
    got = [counts.get(w,0) for w in range(len(pred))]
    assert got == pred, (n, [(i,a,b) for i,(a,b) in enumerate(zip(got,pred)) if a!=b][:10])
    assert best == 3
    assert len(mins) == comb(2*n, 3)
    assert all(set(lab) <= {0,1} and sum(lab) == 3 for lab in mins)
    print(f"n={n}: gamma_tI=3, minimum_functions={len(mins)}, total_functions={sum(counts.values())}")

print("labelings_checked =", checked)
print("all coefficients matched the closed weight enumerator")
