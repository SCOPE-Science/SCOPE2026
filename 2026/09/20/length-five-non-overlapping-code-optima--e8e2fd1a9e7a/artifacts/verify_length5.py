from math import comb


def closed_S(q):
    if q == 2:
        return 2
    if q == 3:
        return 17
    return max(l**4 * (q-l) for l in range(1, q))


def best_l(q):
    vals = [(l**4 * (q-l), l) for l in range(1, q)]
    m = max(v for v, _ in vals)
    return [l for v, l in vals if v == m]


def brute_sqn5(q):
    best = -1
    optimizers = []
    for a in range(1, q):
        b = q-a
        for u in range(a*b + 1):
            v = a*b-u
            M = a*v + b*u
            for w in range(M + 1):
                z = M-w
                N = a*z + u*v + b*w
                if b > a:
                    x4 = N
                elif b < a:
                    x4 = 0
                else:
                    # either endpoint has the same objective; record x4=0 here
                    x4 = 0
                y4 = N-x4
                T = a*y4 + u*z + w*v + b*x4
                if T > best:
                    best = T
                    optimizers = [(a,b,u,v,w,z,x4,y4)]
                elif T == best:
                    optimizers.append((a,b,u,v,w,z,x4,y4))
    return best, optimizers




def residue_l(q):
    m, r = divmod(q, 5)
    return {0:4*m, 1:4*m+1, 2:4*m+2, 3:4*m+2, 4:4*m+3}[r]

def full_sqn5(q):
    best = -1
    optimizers = []
    for a in range(1, q):
        b = q-a
        for u in range(a*b + 1):
            v = a*b-u
            M = a*v + b*u
            for w in range(M + 1):
                z = M-w
                N = a*z + u*v + b*w
                for x4 in range(N + 1):
                    y4 = N-x4
                    T = a*y4 + u*z + w*v + b*x4
                    state = (a,b,u,v,w,z,x4,y4)
                    if T > best:
                        best = T
                        optimizers = [state]
                    elif T == best:
                        optimizers.append(state)
    return best, optimizers


def proposition11_weight(q, state):
    a,b,u,v,w,z,x4,y4 = state
    return (comb(q,a) * comb(a*b,u) * comb(a*v+b*u,w)
            * comb(a*z+u*v+b*w,x4))

def concat(A, B):
    return {a+b for a in A for b in B}


def explicit_q3_code():
    L1, R1 = {"0", "1"}, {"2"}
    L2, R2 = {"02"}, {"12"}
    L3 = set()
    R3 = concat(L1, R2) | concat(L2, R1)
    L4 = set()
    R4 = concat(L1, R3) | concat(L2, R2) | concat(L3, R1)
    C = concat(L1, R4) | concat(L2, R3) | concat(L3, R2) | concat(L4, R1)
    return C


def non_overlapping(C):
    C = list(C)
    n = len(C[0])
    for x in C:
        if len(x) != n:
            return False
        for y in C:
            for k in range(1, n):
                if x[-k:] == y[:k]:
                    return False
    return True


def main():
    print("Exact SQN( q,5 ) verification against the claimed formula")
    for q in range(2, 13):
        brute, opts = brute_sqn5(q)
        formula = closed_S(q)
        assert brute == formula, (q, brute, formula)
        print(f"q={q:2d}: S={brute:8d}; best Blackburn l={best_l(q)}")

    # Published 2024 Table 1 values for n=5, q=2,...,6.
    known_S = {2:2, 3:17, 4:81, 5:256, 6:625}
    known_N = {2:8, 3:12, 4:8, 5:10, 6:12}
    assert all(closed_S(q) == v for q, v in known_S.items())
    print("Table-1 size cross-check q=2..6: PASS")

    # Full optimizer enumeration for small q, followed by Proposition 11 counting.
    for q in range(2, 8):
        best, opts = full_sqn5(q)
        count = sum(proposition11_weight(q, o) for o in opts)
        expected = known_N[q] if q <= 6 else 2*comb(q, best_l(q)[0])
        assert best == closed_S(q)
        assert count == expected, (q, count, expected)
        print(f"q={q:2d}: full SQN optimizer count gives N={count}: PASS")

    # For q>=4, normalized optimizers a>=b are exactly the k=4 Blackburn size pattern.
    for q in range(4, 13):
        best, opts = brute_sqn5(q)
        L = best_l(q)
        normalized = [o for o in opts if o[0] >= o[1]]
        assert normalized
        for a,b,u,v,w,z,x4,y4 in normalized:
            assert a in L and u == 0 and w == 0 and x4 == 0
        print(f"q={q:2d}: normalized optimal SQN patterns are Blackburn k=4: PASS")

    C = explicit_q3_code()
    assert len(C) == 17
    assert non_overlapping(C)
    print("Explicit ternary length-5 code: 17 words, overlap check PASS")

    # Integer maximizer uniqueness for a^4(q-a), tested far beyond the brute-SQN range.
    for q in range(4, 10001):
        assert best_l(q) == [residue_l(q)]
    print("Explicit residue-class maximizer l_q verified for q=4..10000: PASS")


if __name__ == "__main__":
    main()
