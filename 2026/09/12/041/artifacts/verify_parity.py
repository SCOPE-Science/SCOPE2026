"""Exact verification (integers) of the parity separation theorem.
P = 4-cycle shift, B = diag(1,0,1,0). f_n = P^n B P^n - B^{n+1}.
Asserts f_n == 0 iff n even, for n = 2..12, and prints f_2, f_3."""
P = [[0]*4 for _ in range(4)]
for i in range(4):
    P[i][(i+1) % 4] = 1
B = [[1 if i == j and i % 2 == 0 else 0 for j in range(4)] for i in range(4)]

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

print("B^2 == B:", mpw(B, 2) == B)
for n in range(2, 13):
    Pn = mpw(P, n)
    fn = sub(mm(mm(Pn, B), Pn), mpw(B, n+1))
    print(f"n={n}: f_n == 0 ? {isz(fn)}   (expected {n % 2 == 0})  diag={ [fn[i][i] for i in range(4)] }")
    assert isz(fn) == (n % 2 == 0)
print("f_2 =", mm(mm(mpw(P,2),B),mpw(P,2)))
print("f_3 =", sub(mm(mm(mpw(P,3),B),mpw(P,3)), mpw(B,4)))
print("PARITY THEOREM VERIFIED over Z (hence over Q)")
