from itertools import product

I = (1, 0, 0, 1)

def mm(A, B, p):
    return tuple(sum(A[2*i+k] * B[2*k+j] for k in range(2)) % p
                 for i in range(2) for j in range(2))

def det(A, p):
    return (A[0]*A[3] - A[1]*A[2]) % p

def inv(A, p):
    q = pow(det(A, p), -1, p)
    return (A[3]*q % p, -A[1]*q % p, -A[2]*q % p, A[0]*q % p)

def comm(A, B, p):
    return mm(mm(mm(A, B, p), inv(A, p), p), inv(B, p), p)

def transvections(p):
    out = []
    for N in product(range(p), repeat=4):
        if N == (0,0,0,0):
            continue
        if (N[0] + N[3]) % p == 0 and det(N, p) == 0:
            T = tuple((I[i] + N[i]) % p for i in range(4))
            if det(T, p):
                out.append(T)
    return list(dict.fromkeys(out))

def has_eigenvalue(A, p):
    tr = (A[0] + A[3]) % p
    d = det(A, p)
    return any((x*x - tr*x + d) % p == 0 for x in range(p))

def negdet_square(A, p):
    target = (-det(A, p)) % p
    return any((x*x) % p == target for x in range(1, p))

def predicted(A, p):
    if p == 2:
        return has_eigenvalue(A, p)
    return has_eigenvalue(A, p) or negdet_square(A, p)

for p in (2, 3, 5, 7):
    gl2 = [A for A in product(range(p), repeat=4) if det(A, p)]
    tv = transvections(p)
    mismatches = 0
    for S in gl2:
        actual = any(comm(comm(S, T1, p), T2, p) == I
                     for T1 in tv for T2 in tv)
        if actual != predicted(S, p):
            mismatches += 1
    print(f"F_{p}: |GL2|={len(gl2)}, transvections={len(tv)}, mismatches={mismatches}")
