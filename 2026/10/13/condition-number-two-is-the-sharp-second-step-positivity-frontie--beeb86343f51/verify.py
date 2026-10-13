from fractions import Fraction as F

def moments(lam, b, maxj=4):
    return {j: sum((bi*bi)*(li**j) for li, bi in zip(lam, b))
            for j in range(1, maxj+1)}

def pair_D(lam, b):
    s = F(0)
    n = len(lam)
    for i in range(n):
        for j in range(i+1,n):
            wi, wj = b[i]*b[i], b[j]*b[j]
            li, lj = lam[i], lam[j]
            s += wi*wj*li*lj*(li-lj)**2
    return s

def pair_N(lam, b):
    s = F(0)
    n = len(lam)
    for i in range(n):
        for j in range(i+1,n):
            wi, wj = b[i]*b[i], b[j]*b[j]
            li, lj = lam[i], lam[j]
            s += wi*wj*li*lj*(li-lj)**2*(li+lj)
    return s

def coeffs(lam, b):
    m = moments(lam,b)
    den = m[2]*m[4]-m[3]*m[3]
    a = (m[1]*m[4]-m[2]*m[3])/den
    c = (m[1]*m[3]-m[2]*m[2])/den
    return a,c,m

# Replay pairwise identities on several exact rational spectra.
datasets = [
    ([F(1),F(3,2),F(3)], [F(1),F(1),F(1,20)]),
    ([F(2),F(5),F(7),F(9)], [F(3,2),F(2,3),F(4,5),F(1,7)]),
    ([F(1),F(1),F(2),F(4)], [F(1),F(2),F(3),F(4)]),
]
for lam,b in datasets:
    m = moments(lam,b)
    assert m[1]*m[3]-m[2]*m[2] == pair_D(lam,b)
    assert m[1]*m[4]-m[2]*m[3] == pair_N(lam,b)

# Exact kappa=3 witness.
lam = [F(1),F(3,2),F(3)]
b = [F(1),F(1),F(1,20)]
a,c,m = coeffs(lam,b)
assert a == F(833,545)
assert c == F(306,545)
assert a/c == F(49,18)

x2 = [bi*(a-c*li) for li,bi in zip(lam,b)]
assert x2 == [F(527,545),F(374,545),F(-17,2180)]
assert x2[2] < 0

xstar = [bi/li for li,bi in zip(lam,b)]
assert all(x > 0 for x in xstar)

# First GMRES step and exact residual norms.
alpha = sum((bi*bi)*li for li,bi in zip(lam,b)) / \
        sum((bi*bi)*(li**2) for li,bi in zip(lam,b))
assert alpha == F(59,77)
x1 = [alpha*bi for bi in b]
r0 = b
r1 = [bi-li*xi for li,bi,xi in zip(lam,b,x1)]
r2 = [bi-li*xi for li,bi,xi in zip(lam,b,x2)]
n0 = sum(z*z for z in r0)
n1 = sum(z*z for z in r1)
n2 = sum(z*z for z in r2)
assert n0 == F(801,400)
assert n1 == F(25,308)
assert n2 == F(4,545)
assert n2 < n1 < n0

# Two active eigenvalues terminate exactly at step two.
lam2=[F(1),F(9)]
b2=[F(2),F(3)]
a2,c2,_=coeffs(lam2,b2)
x2_two=[bi*(a2-c2*li) for li,bi in zip(lam2,b2)]
assert x2_two == [bi/li for li,bi in zip(lam2,b2)]

# Representative sharpness checks for rational kappa > 2.
# Choose delta^2 below the displayed threshold and verify top-coordinate negativity.
for kap, delta in [(F(5,2),F(1,100)), (F(3),F(1,20)),
                   (F(4),F(1,10)), (F(10),F(1,10))]:
    threshold = (kap-F(2))**3 / (kap**4 + 16*(kap-F(1))**2)
    assert delta*delta < threshold
    lamk=[F(1),kap/F(2),kap]
    bk=[F(1),F(1),delta]
    ak,ck,_=coeffs(lamk,bk)
    assert ck > 0
    assert ak/ck < kap
    assert bk[2]*(ak-ck*kap) < 0

print("VERIFY_OK")
