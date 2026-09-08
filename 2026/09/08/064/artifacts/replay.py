"""Self-contained exact replay: recounts witness unit-circle zeros from
embedded +-1 strings using exact rational arithmetic only (stdlib).
Method: P(e^{iθ})=e^{imθ}U(cosθ); U built via exact Chebyshev; Sturm
count on (-1,1) with multiplicity ladder; Z=2*sum. Endpoints ±1 never
roots (P(±1) odd). No numpy. Asserts claimed Z_L minima.
"""
from fractions import Fraction

WIT = {
 8: ([1,1,1,1,-1,1,1,1,1], 2),
 10: ([1,1,1,1,1,-1,1,1,1,1,1], 2),
 12: ([1,1,1,1,1,1,-1,1,1,1,1,1,1], 2),
 14: ([1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1], 6),
 16: ([1,1,1,1,1,1,1,-1,1,-1,1,1,1,1,1,1,1], 4),
 18: ([1,1,1,1,1,1,1,1,-1,-1,-1,1,1,1,1,1,1,1,1], 4),
 20: ([1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1], 6),
 22: ([1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1], 6),
 24: ([1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1], 6),
}

def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0: p.pop()
    return p

def prem(A, B):
    A = trim([Fraction(x) for x in A]); B = trim([Fraction(x) for x in B])
    while len(A) > 1 or A[0] != 0:
        if len(A) < len(B): break
        c = A[-1]/B[-1]; s = len(A)-len(B)
        sub = [Fraction(0)]*s + [c*b for b in B]
        sub += [Fraction(0)]*(len(A)-len(sub))
        A = trim([a-b for a, b in zip(A, sub)])
        if len(A) == 1 and A[0] == 0: break
    return A

def pgcd(A, B):
    A = trim([Fraction(x) for x in A]); B = trim([Fraction(x) for x in B])
    while not (len(B) == 1 and B[0] == 0):
        A, B = B, prem(A, B)
    c = A[-1]
    return [a/c for a in A]

def deriv(A):
    return trim([Fraction(i)*A[i] for i in range(1, len(A))]) if len(A) > 1 else [Fraction(0)]

def sturm(U):
    seq = [trim([Fraction(x) for x in U]), deriv([Fraction(x) for x in U])]
    while not (len(seq[-1]) == 1 and seq[-1][0] == 0):
        R = trim([-x for x in prem(seq[-2], seq[-1])])
        if len(R) == 1 and R[0] == 0: break
        seq.append(R)
    return seq

def var(seq, pt):
    s = []
    for p in seq:
        v = sum(c*(pt**i) for i, c in enumerate(p))
        if v > 0: s.append(1)
        elif v < 0: s.append(-1)
    return sum(1 for i in range(1, len(s)) if s[i] != s[i-1])

def ev(p, pt):
    return sum(c*(pt**i) for i, c in enumerate(p))

def circle_count(full):
    N = len(full)-1; m = N//2
    assert full == full[::-1] and set(full) <= {1, -1}
    half = full[:m+1]
    T = [[Fraction(1)], [Fraction(0), Fraction(1)]]
    for k in range(2, m+1):
        a = [Fraction(0)] + [2*t for t in T[k-1]]
        b = list(T[k-2])
        n = max(len(a), len(b))
        a += [Fraction(0)]*(n-len(a)); b += [Fraction(0)]*(n-len(b))
        T.append(trim([x-y for x, y in zip(a, b)]))
    U = [Fraction(0)]*(m+1)
    U[0] += Fraction(half[m])
    for k in range(1, m+1):
        for i, t in enumerate(T[k]):
            U[i] += Fraction(2*half[m-k])*t
    U = trim(U)
    assert ev(U, Fraction(1)) != 0 and ev(U, Fraction(-1)) != 0
    tot, cur = 0, U
    while True:
        if len(trim(cur)) <= 1: break
        tot += var(sturm(cur), Fraction(-1)) - var(sturm(cur), Fraction(1))
        G = pgcd(cur, deriv(cur))
        if len(trim(G)) <= 1: break
        cur = G
        if tot > m: break
    return 2*tot

ok = True
for N, (full, claimed) in sorted(WIT.items()):
    z = circle_count(full)
    flag = "OK" if z == claimed else "MISMATCH"
    if z != claimed: ok = False
    print(f"N={N} exact_count={z} claimed={claimed} {flag}")
print("REPLAY:", "OK" if ok else "FAIL")
assert ok
