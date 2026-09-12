"""Verify the monomial (cycle + diagonal projector) classification lemma.
A = L-cycle shift (A[i][(i+1)%L]=1), B = diag(1_S).
Claim: f_n |-> 0  iff  (L divides 2n) and (S+n == S mod L).
Corollary: no triple (L<=8, S) has f_2=f_3=0 with some f_N != 0 (N<=10)
except all-zero representations. Checked over Z (exact ints)."""
import itertools

def cyc(L):
    A = [[0]*L for _ in range(L)]
    for i in range(L):
        A[i][(i+1) % L] = 1
    return A

def diag(v):
    L = len(v)
    return [[v[i] if i == j else 0 for j in range(L)] for i in range(L)]

def mm(A, C):
    n = len(A)
    return [[sum(A[i][k]*C[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def mpw(A, k):
    n = len(A)
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = mm(R, A)
    return R

def sub(A, C):
    return [[A[i][j]-C[i][j] for j in range(len(A))] for i in range(len(A))]

def isz(M):
    return all(v == 0 for r in M for v in r)

def cond(L, S, n):
    # B^{n+1}: zero projector stays zero (0^{n+1}=0); nonzero projector entries stay 1.
    if not S:
        return True  # zero representation: every f_n vanishes
    return (2*n) % L == 0 and all(((i+n) % L in S) == (i in S) for i in range(L))

bad = 0
checked = 0
for L in range(1, 9):
    for mask in range(1 << L):
        S = {i for i in range(L) if (mask >> i) & 1}
        A, B = cyc(L), diag([(1 if i in S else 0) for i in range(L)])
        for n in range(2, 11):
            Pn = mpw(A, n)
            fn = sub(mm(mm(Pn, B), Pn), mpw(B, n+1))
            if isz(fn) != cond(L, S, n):
                print(f"MISMATCH L={L} mask={mask} n={n}")
                bad += 1
            checked += 1
print(f"classification checks: {checked}, mismatches: {bad}")
assert bad == 0

# Corollary: f_2 = f_3 = 0  =>  all f_4..f_10 = 0  (within L<=8 monomial class)
counter = 0
for L in range(1, 9):
    for mask in range(1 << L):
        S = {i for i in range(L) if (mask >> i) & 1}
        A, B = cyc(L), diag([(1 if i in S else 0) for i in range(L)])
        f = {}
        for n in range(2, 11):
            Pn = mpw(A, n)
            f[n] = sub(mm(mm(Pn, B), Pn), mpw(B, n+1))
        if isz(f[2]) and isz(f[3]):
            if any(not isz(f[n]) for n in range(4, 11)):
                print(f"SEPARATOR L={L} mask={mask}")
                counter += 1
print(f"monomial (f2,f3)-separators with later nonzero: {counter}")
assert counter == 0
print("MONOMIAL LEMMA + COROLLARY VERIFIED over Z (hence over Q)")
