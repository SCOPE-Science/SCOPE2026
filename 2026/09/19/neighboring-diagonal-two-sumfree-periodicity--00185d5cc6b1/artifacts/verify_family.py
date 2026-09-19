from itertools import combinations

def greedy(f, terms):
    seq = [f, 2*f + 1]
    pair_sums = {seq[0] + seq[1]}
    while len(seq) < terms:
        x = seq[-1] + 1
        while x in pair_sums:
            x += 1
        for y in seq:
            pair_sums.add(x + y)
        seq.append(x)
    return seq

def residue_set(f):
    M = 5*f + 1
    return (
        set(range(f-1, f+1))
        | set(range(2*f+2, 3*f))
        | set(range(4*f+1, 4*f+3))
    ), M

def closed_form(f, N):
    R, M = residue_set(f)
    prefix = {f} | set(range(2*f+1, 3*f+1))
    return [n for n in range(1, N+1)
            if n in prefix or (n >= 4*f+1 and n % M in R)]

def period_word(f):
    return [1, 2*f-2, 1, f+2] + [1]*(f-3) + [f+2]

def check_modular_identities(f):
    R, M = residue_set(f)
    Q = set(range(2*f+1, 3*f+1))
    RR = {(x+y) % M for x in R for y in R}
    QR = {(x+y) % M for x in Q for y in R}
    QQ = {x+y for x, y in combinations(sorted(Q), 2)}
    return (
        not (RR & R)
        and QR == set(range(M)) - R
        and QQ == set(range(4*f+3, 6*f))
        and len(R) == f+2
    )

def least_eventual_period(D, search_k, search_p):
    for k in range(search_k + 1):
        for p in range(1, search_p + 1):
            if all(D[i] == D[i+p] for i in range(k, len(D)-p)):
                return k, p
    return None

def check_greedy(f, terms=1200):
    seq = greedy(f, terms)
    predicted = closed_form(f, seq[-1])
    if seq != predicted:
        return False
    D = [seq[i] - seq[i-1] for i in range(1, len(seq))]
    k = f + 1
    initial = [f+1] + [1]*(f-1) + [f+1]
    p = period_word(f)
    expected_min_p = 2 if f == 4 else f+2
    return (
        D[:k] == initial
        and all(D[i] == p[(i-k) % len(p)] for i in range(k, len(D)))
        and least_eventual_period(D, k+2, f+3) == (k, expected_min_p)
        and len(p) == f+2
        and sum(p) == 5*f+1
    )

mods = [f for f in range(3, 501) if check_modular_identities(f)]
greedy_ok = [f for f in range(3, 101) if check_greedy(f)]

print(f"modular identities: {len(mods)}/498 passed for 3 <= f <= 500")
print(f"greedy/formula/period checks: {len(greedy_ok)}/98 passed for 3 <= f <= 100")
print("f=3 period word:", period_word(3))
print("f=4 period word:", period_word(4), "(minimal period [1, 6])")
print("f=5 period word:", period_word(5))
print("f=5 first 18 terms:", greedy(5, 18))
