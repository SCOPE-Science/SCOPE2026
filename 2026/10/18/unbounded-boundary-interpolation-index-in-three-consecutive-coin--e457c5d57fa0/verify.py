"""Independent finite integer checks for the three-boundary lattice-index theorem.
No external packages; run: python verify.py
"""
from math import gcd


def enumerated_solutions(a, b, c, N):
    ans = set()
    for x in range(N // a + 1):
        R = N - a * x
        for y in range(R // b + 1):
            Z = R - b * y
            if Z % c == 0:
                ans.add((x, y, Z // c))
    return ans

cases = 0
points = 0
for k in range(2, 40):
    for r in range(1, k):
        a, b, c = 2*k + 1, 2*k + 2, 2*k + 3
        N = a * (k+3+r) + 1
        expect = {(k+2+r, 1, 0)}
        expect.update((j, 2*(r+1-j), k-r+j) for j in range(r+2))
        actual = enumerated_solutions(a, b, c, N)
        assert actual == expect, (k, r, actual ^ expect)
        B = {p for p in actual if 0 in p}
        assert B == {(k+2+r, 1, 0), (0, 2*(r+1), k-r), (r+1, 0, k+1)}
        C = (k+2+r, 1, 0)
        D0 = (0, 2*(r+1), k-r)
        D1 = (r+1, 0, k+1)
        determinant = (D1[0]-D0[0])*(C[1]-D0[1]) - (D1[1]-D0[1])*(C[0]-D0[0])
        assert determinant == (r+1)*c
        for j in range(1, r+1):
            den=(r+1)//gcd(j,r+1)
            assert all(((r+1-j)*D0[t] + j*D1[t]) == (r+1)*(j,2*(r+1-j),k-r+j)[t] for t in range(3))
            assert den>=2
            points+=1
        cases+=1
print(f'PASS {cases} parameter pairs, {points} interior points, exact brute enumeration and projected-lattice determinants')
