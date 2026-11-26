"""Exact integer check of the eight-vertex path certificate."""

def mul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]

n = 8
L = [[0]*n for _ in range(n)]
for i in range(n-1):
    L[i][i] += 1
    L[i+1][i+1] += 1
    L[i][i+1] = L[i+1][i] = -1
L2 = mul(L, L)
B = [[3*(i == j)+6*L[i][j]+4*L2[i][j] for j in range(n)] for i in range(n)]
A = [[3*(i == j)-6*L[i][j]+4*L2[i][j] for j in range(n)] for i in range(n)]
N = [[22767445,7237548,12586536,8978304,5124384,2634048,1318656,776448],
     [7237548,28116433,3629316,8732616,6487968,3808992,2091840,1318656],
     [12586536,3629316,24262513,1138980,7417224,5945760,3808992,2634048],
     [8978304,8732616,1138980,22947121,596772,7417224,6487968,5124384]]
N += [row[::-1] for row in N[::-1]]
D = 61423369
assert mul(B, N) == [[D*a for a in row] for row in A]
assert all(sum(row) == D for row in N)
assert N == [list(row) for row in zip(*N)]
assert min(map(min, N)) == 596772
assert [(i,j) for i in range(n) for j in range(n) if N[i][j] == 596772] == [(3,4),(4,3)]
print("Integer certificate verified; minimum 596772/61423369.")
