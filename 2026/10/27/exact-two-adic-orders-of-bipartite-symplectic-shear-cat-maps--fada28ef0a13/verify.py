"""Exact modular checks for the bipartite graph symplectic-shear cat map.

Scientific scope: regression tests for stated all-size algebraic proof.
No floating-point computation is used.
"""

def graph_matrix(a, b):
    n = a + b
    C = [[int((i < a <= j) or (j < a <= i)) for j in range(n)]
         for i in range(n)]
    I = [[int(i == j) for j in range(n)] for i in range(n)]
    return [[I[i][j] if i < n else I[i-n][j] for j in range(n)]
            + [C[i][j] if i < n else I[i-n][j] + C[i-n][j] for j in range(n)]
            for i in range(2*n)]


def matmul(A, B, modulus):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for k, v in enumerate(A[i]):
            if v % modulus:
                for j in range(n):
                    C[i][j] = (C[i][j] + v*B[k][j]) % modulus
    return C


def power(A, exponent, modulus):
    n = len(A)
    result = [[int(i==j) for j in range(n)] for i in range(n)]
    A = [[x % modulus for x in row] for row in A]
    while exponent:
        if exponent & 1:
            result = matmul(result, A, modulus)
        exponent >>= 1
        if exponent:
            A = matmul(A, A, modulus)
    return result


def order_formula(a,b,s):
    if a==b==1:
        return 6 * 2**max(0,s-2)
    if a%2 and b%2:
        return 3 * 2**s
    if not (a%2 or b%2):
        return 2**(s+1)
    even = a if a%2==0 else b
    if even%4==0:
        return 2**(s+2)
    return 8 * 2**max(0,s-2)


def valuation_mod(A, k, max_power=5):
    n=len(A)
    for j in range(1,max_power+1):
        B=power(A,k,2**j)
        if any(B[i][h] != int(i==h) for i in range(n) for h in range(n)):
            return j-1
    return max_power


def check():
    tests=0
    for a in range(1,9):
        for b in range(1,9):
            A=graph_matrix(a,b)
            for s in range(1,8):
                m=2**s
                t=order_formula(a,b,s)
                T=power(A,t,m)
                n=len(A)
                assert all(T[i][j]==int(i==j) for i in range(n) for j in range(n)),(a,b,s,t)
                for q in (2,3):
                    if t%q==0:
                        U=power(A,t//q,m)
                        assert any(U[i][j]!=int(i==j) for i in range(n) for j in range(n)),(a,b,s,t,q)
                tests+=1
            # The low-modulus exact valuation table needed for the lifting proof.
            if a==b==1: m0=6;v1=2
            elif a%2 and b%2: m0=6;v1=1
            elif not(a%2 or b%2): m0=4;v1=1
            else: m0=8;v1=1 if ((a if a%2==0 else b)%4==0) else 2
            assert valuation_mod(A,m0)==v1,(a,b,'base',v1)
            if v1==1:
                assert valuation_mod(A,2*m0)==2,(a,b,'lift')
    # Test representatives beyond 8 for residue versus literal-size separation.
    for a,b in ((1,9),(9,1),(9,9),(1,12),(12,1),(10,14),(11,12)):
        A=graph_matrix(a,b)
        for s in (1,2,3,5):
            t=order_formula(a,b,s)
            M=power(A,t,2**s)
            assert all(M[i][j]==int(i==j) for i in range(len(M)) for j in range(len(M)))
            for q in (2,3):
                if t%q==0:
                    W=power(A,t//q,2**s)
                    assert any(W[i][j]!=int(i==j) for i in range(len(W)) for j in range(len(W)))
            tests+=1
    print('VERIFY_OK: {} exact matrix-order comparisons; base valuation and lifting comparisons for 64 bipartitions'.format(tests))


if __name__=='__main__':
    check()
