"""Exact checks for 24-cell harmonic sampling; no third-party modules."""
from itertools import combinations, product

def roots():
    out = []
    for i, j in combinations(range(4), 2):
        for s, t in product((-1, 1), repeat=2):
            v = [0] * 4
            v[i], v[j] = s, t
            if next(c for c in v if c) == 1:
                out.append(tuple(v))
    return sorted(out)

X = roots()
assert len(X) == 12 and len(set(X)) == 12

def inner2(v,w):
    return sum(a*b for a,b in zip(v,w)) # twice unit-sphere inner product

T = [[inner2(x,y) for y in X] for x in X]
I = [[int(i==j) for j in range(12)] for i in range(12)]
A = [[int(i!=j and abs(T[i][j]) == 1) for j in range(12)] for i in range(12)]
B = [[int(i!=j and T[i][j] == 0) for j in range(12)] for i in range(12)]
S = [[(T[i][j] if i!=j else 0) for j in range(12)] for i in range(12)]
assert all(A[i][j]+B[i][j]+I[i][j]==1 for i in range(12) for j in range(12))

def mm(M,N):
    return [[sum(M[i][k]*N[k][j] for k in range(12)) for j in range(12)] for i in range(12)]
assert mm(S,S) == [[2*S[i][j]+8*I[i][j] for j in range(12)] for i in range(12)]
assert mm(B,B) == [[2*B[i][j]+3*I[i][j] for j in range(12)] for i in range(12)]
assert all(sum(B[i]) == 3 and sum(A[i]) == 8 for i in range(12))

# U_n(t) is the Chebyshev polynomial of the second kind.
# t takes the rational values integer/2, so this recurrence uses integers.
def U(n, twice_t):
    a,b = 1, twice_t
    if n == 0: return a
    if n == 1: return b
    for _ in range(2,n+1):
        a,b=b,twice_t*b-a
    return b

spectrum = {}
for ell in range(48):
    M = [[2*U(ell,T[i][j]) for j in range(12)] for i in range(12)]
    if ell%2:
        w=U(ell,1)
        pred = [[2*(ell+1)*I[i][j]+2*w*S[i][j] for j in range(12)] for i in range(12)]
        eig=[(2*(ell+1)+8*w,4),(2*(ell+1)-4*w,8)]
    else:
        w,c=U(ell,1),U(ell,0)
        pred=[[2*(ell+1)*I[i][j]+2*w*A[i][j]+2*c*B[i][j] for j in range(12)] for i in range(12)]
        eig=[(2*(ell+1)+16*w+6*c,1),(2*(ell+1)-8*w+6*c,2),(2*(ell+1)-2*c,9)]
    assert M==pred,('matrix',ell)
    assert all(e >= 0 for e,m in eig),('sign',ell,eig)
    assert sum(m for e,m in eig)==12
    assert sum(e*m for e,m in eig)==24*(ell+1)
    spectrum[ell]=eig
    if ell>=12:
        prev=[[2*U(ell-12,T[i][j]) for j in range(12)] for i in range(12)]
        assert M==[[prev[i][j]+24*I[i][j] for j in range(12)] for i in range(12)]

assert [sum(m for e,m in spectrum[ell] if e>0) for ell in range(11)]==[1,4,9,8,11,12,10,12,12,12,11]
assert all(sum(m for e,m in spectrum[ell] if e>0)==12 for ell in range(11,48))
print('PASS: 12 root lines, orthogonality/signed-graph identities, all Gram spectra for degrees 0..47, 12-step recurrence, exact ranks')
for l in range(12):
    print(l, spectrum[l])
