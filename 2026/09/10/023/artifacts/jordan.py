"""Jordan type of xL0 on B=R/Ann(G0) (dim 44) + generator degrees of Ann.
Quotient-basis projection method, exact QQ."""
from sympy import Matrix, Rational
from audit_target import catalecticant, monomials_4

a = Rational(0); b = Rational(0)
L = (Rational(1), Rational(1), Rational(1), Rational(1))

# quotient data per degree
info = {}
for e in range(7):
    Re = monomials_4(e)
    _, _, C = catalecticant(a, b, e)
    he = C.rank()
    # independent row set (quotient basis monomials)
    _, pivR = C.T.rref()
    pivR = list(pivR)
    _, pivC = C.rref()
    pivC = list(pivC)
    M = C.extract(pivR, pivC)
    assert M.det() != 0, e
    Minv = M.inv()
    info[e] = dict(Re=Re, C=C, he=he, pivR=pivR, pivC=pivC, Minv=Minv)

print("h =", [info[e]['he'] for e in range(7)], "dim =", sum(info[e]['he'] for e in range(7)))

def class_coords(e, mon):
    """coordinates of [mon] (mon in R_e) on quotient basis pivR[e]."""
    d = info[e]
    r = d['C'].row(d['Re'].index(mon))
    sub = Matrix([r[j] for j in d['pivC']]).T  # 1 x he
    return (sub * d['Minv'])  # 1 x he

# global basis offsets
offs = {}
t = 0
for e in range(7):
    offs[e] = t
    t += info[e]['he']
N = t
Mat = Matrix.zeros(N, N)  # Mat[i,j] = coord i of L*b_j
for e in range(6):
    for j, mj in enumerate([info[e]['Re'][i] for i in info[e]['pivR']]):
        col = offs[e] + j
        for k in range(4):
            if L[k] == 0:
                continue
            g = tuple(mj[i] + (1 if i == k else 0) for i in range(4))
            cc = class_coords(e + 1, g)
            for i in range(info[e + 1]['he']):
                Mat[offs[e + 1] + i, col] += L[k] * cc[i]

# Jordan partition via kernel dims of powers
kdims = []
P = Mat
for k in range(1, 12):
    P = P * Mat if k > 1 else Mat
    n = N - P.rank()
    kdims.append(n)
    if n == N:
        break
print("ker dims:", kdims)
# partition conjugate: block sizes from differences
prev = 0
diffs = [kdims[0]] + [kdims[i] - kdims[i - 1] for i in range(1, len(kdims))]
# number of blocks of size >= k is diffs[k-1]; blocks:
nblocks = kdims[0]
sizes = []
for blk in range(nblocks):
    s = sum(1 for d in diffs if d > blk)
    sizes.append(s)
sizes.sort(reverse=True)
print("Jordan partition of xL0:", sizes, "sum:", sum(sizes), "nblocks:", len(sizes))
# generic Jordan type for h=(1,4,10,14,10,4,1) with WLP: conjugate of h-vector sorted?
# For WLP Lefschetz element, Jordan type = conjugate partition of Hilbert function.
from collections import Counter
h = [info[e]['he'] for e in range(7)]
conj = sorted([sum(1 for x in h if x > i) for i in range(max(h))], reverse=True)
print("conjugate-of-h partition:", conj, "sum:", sum(conj))
print("generic?", sizes == conj)

# Ann generator degrees: dim Ann_e and minimal generators
for e in range(1, 7):
    d = info[e]
    print(f"e={e}: dim R={len(d['Re'])} h={d['he']} dimAnn={len(d['Re'])-d['he']}")
