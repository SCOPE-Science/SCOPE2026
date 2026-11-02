#!/usr/bin/env python3
"""Exact finite-field replay of terminal controllability on perfect binary trees.

The infinite-height theorem is proved separately; these finite computations
are independent exact checks, not a substitute for that proof.
"""


def tree_laplacian(h):
    n = (1 << (h + 1)) - 1
    rows = [[0] * n for _ in range(n)]
    for i in range((1 << h) - 1):
        for j in (2*i + 1, 2*i + 2):
            rows[i][i] += 1
            rows[j][j] += 1
            rows[i][j] -= 1
            rows[j][i] -= 1
    return rows


def nullspace_mod(A, p):
    A = [[x % p for x in row] for row in A]
    n = len(A); m = len(A[0]); pivots = []
    row = 0
    for col in range(m):
        j = next((j for j in range(row, n) if A[j][col]), None)
        if j is None: continue
        A[row], A[j] = A[j], A[row]
        z = pow(A[row][col], -1, p)
        A[row] = [(x*z) % p for x in A[row]]
        for k in range(n):
            if k == row or not A[k][col]: continue
            z = A[k][col]
            A[k] = [(x-z*y) % p for x, y in zip(A[k], A[row])]
        pivots.append(col)
        row += 1
        if row == n: break
    free = [j for j in range(m) if j not in set(pivots)]
    basis = []
    for j in free:
        v = [0]*m; v[j] = 1
        for k, col in enumerate(pivots):v[col] = (-A[k][j]) % p
        basis.append(v)
    return basis


class IncrementalRank:
    def __init__(self, p, n):
        self.p = p; self.n = n; self.basis = {}
    def add(self, vector):
        p = self.p
        x = [a % p for a in vector]
        for k, v in sorted(self.basis.items()):
            if x[k]:
                z = x[k]
                x = [(a-z*b) % p for a,b in zip(x,v)]
        k = next((j for j,a in enumerate(x) if a), None)
        if k is None: return False
        z = pow(x[k], -1, p)
        self.basis[k] = [(a*z) % p for a in x]
        return True
    @property
    def rank(self):return len(self.basis)


def optimal_leaves(L, h, p):
    n = len(L); M = 1 << (h-1)
    A = [[L[i][j] - (i == j) for j in range(n)] for i in range(n)]
    E = nullspace_mod(A, p)
    c = len(E)
    lower = sum(1 << (h-1-4*j) for j in range((h-1)//4+1)) + int(h%4==3)
    assert c == lower, (h,c,lower)
    parents = range((1 << (h-1))-1, (1 << h)-1)
    chosen = [2*j+1 for j in parents]
    other = [2*j+2 for j in parents]
    rank = IncrementalRank(p, c)
    for i in chosen:
        assert rank.add([v[i] for v in E])
    assert rank.rank == M
    for i in other:
        if rank.rank == c:break
        if rank.add([v[i] for v in E]): chosen.append(i)
    assert rank.rank == c and len(chosen) == c
    return chosen, c, [2*j+1 for j in parents]


def kalman_rank(L, S, p):
    n = len(L)
    cur = [[int(j==i) for j in range(n)] for i in S]
    basis = IncrementalRank(p,n)
    for step in range(n):
        for v in cur: basis.add(v)
        if basis.rank == n:return n,step
        cur = [[sum(L[i][j]*v[j] for j in range(n))%p for i in range(n)] for v in cur]
    return basis.rank,n


def main():
    for p in (1000003,1000033):
        for h in range(1,7):
            L=tree_laplacian(h)
            S,m,baseline=optimal_leaves(L,h,p)
            r,it=kalman_rank(L,S,p)
            assert r == len(L),(p,h,r,len(L))
            if h>=3 and h%4==3:
                base_rank,_=kalman_rank(L,baseline,p)
                assert base_rank < len(L)
            print(f'prime={p}, height={h}, vertices={len(L)}, lambda1_mult={m}, '+
                  f'baseline={len(baseline)}, selected={len(S)}, Kalman_rank={r}, Krylov_degree={it}')
    print('ALL_FINITE_CHECKS_PASSED')

if __name__ == '__main__':main()
