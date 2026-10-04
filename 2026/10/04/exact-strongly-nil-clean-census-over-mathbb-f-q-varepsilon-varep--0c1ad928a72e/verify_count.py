from itertools import product


def matmul(A, B, n, q):
    return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n)) % q
                 for i in range(n) for j in range(n))


def matsub(A, B, q):
    return tuple((a-b) % q for a, b in zip(A, B))


def is_zero(A):
    return all(x == 0 for x in A)


def is_nilpotent(A, n, q):
    P = A
    for _ in range(1, n+1):
        if is_zero(P):
            return True
        P = matmul(P, A, n, q)
    return False


def is_strongly_nil_clean(A, n, q):
    A2 = matmul(A, A, n, q)
    return is_nilpotent(matsub(A, A2, q), n, q)


def gaussian_binomial(n, r, q):
    if r < 0 or r > n:
        return 0
    num = den = 1
    for i in range(r):
        num *= q**(n-i) - 1
        den *= q**(r-i) - 1
    assert num % den == 0
    return num // den


def residue_formula(n, q):
    return sum(gaussian_binomial(n, r, q) * q**(n*n-n-r*(n-r))
               for r in range(n+1))


def dual_formula(n, q):
    return q**(n*n) * residue_formula(n, q)


for q, n in [(2,1), (2,2), (2,3), (3,1), (3,2), (5,2)]:
    brute = sum(is_strongly_nil_clean(A, n, q)
                for A in product(range(q), repeat=n*n))
    predicted = residue_formula(n, q)
    print(f"q={q} n={n} residue={brute} formula={predicted} dual={dual_formula(n,q)}")
    assert brute == predicted

print("CHECK_OK")
