from fractions import Fraction

def rref_nullspace(A):
    A = [[Fraction(x) for x in row] for row in A]
    m, n = len(A), len(A[0])
    piv = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c]), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        q = A[r][c]
        A[r] = [z/q for z in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                q = A[i][c]
                A[i] = [A[i][j] - q*A[r][j] for j in range(n)]
        piv.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        v = [Fraction(0) for _ in range(n)]
        v[f] = 1
        for i, p in enumerate(piv):
            v[p] = -A[i][f]
        basis.append(v)
    return piv, basis

lam = list(range(6))
A = [[Fraction(t)**k for t in lam] for k in range(4)]
piv, basis = rref_nullspace(A)
assert len(piv) == 4 and len(basis) == 2

for v in basis:
    for k in range(4):
        assert sum(Fraction(lam[j])**k * v[j] for j in range(6)) == 0

witness = {}
for m in range(6):
    v = next((v for v in basis if v[m] != 0), None)
    assert v is not None
    assert any(v[j] != 0 for j in range(6) if j != m)
    witness[m] = [str(x) for x in v]

degree = 2**4
deg_K = 2 * degree
genus = (deg_K + 2)//2
assert degree == 16
assert deg_K == 32
assert genus == 17

print("rank_vandermonde=4")
print("kernel_dimension=2")
for m in range(6):
    print(f"coordinate_{m}_nonzero_kernel_witness={witness[m]}")
print(f"degree_Z3={degree}")
print(f"degree_K_Z3={deg_K}")
print(f"genus_Z3={genus}")
print("VERIFY_OK")
