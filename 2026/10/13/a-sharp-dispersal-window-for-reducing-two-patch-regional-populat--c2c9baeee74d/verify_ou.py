"""Exact-algebra and rational reconstruction checks for a two-patch fluctuation model.

Run: python3 verify_ou.py   (Python 3 standard library only).
The infinite-parameter theorem additionally uses the sign argument in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

NVAR = 5  # a, b, dispersal, first-noise intensity, second-noise intensity
ZERO = (0,) * NVAR

class P:
    def __init__(self, entries=None):
        if isinstance(entries, P):
            self.t = dict(entries.t)
        elif isinstance(entries, dict):
            self.t = {k: int(v) for k, v in entries.items() if v}
        elif entries is None:
            self.t = {}
        else:
            self.t = {ZERO: int(entries)} if entries else {}
    def __add__(self, other):
        q = P(other)
        d = dict(self.t)
        for k, v in q.t.items(): d[k] = d.get(k, 0) + v
        return P(d)
    __radd__ = __add__
    def __neg__(self): return P({k: -v for k, v in self.t.items()})
    def __sub__(self, other): return self + -P(other)
    def __rsub__(self, other): return P(other) - self
    def __mul__(self, other):
        q = P(other)
        d = {}
        for x, vx in self.t.items():
            for y, vy in q.t.items():
                z = tuple(xx + yy for xx, yy in zip(x, y))
                d[z] = d.get(z, 0) + vx * vy
        return P(d)
    __rmul__ = __mul__
    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        res, base = P(1), P(self)
        while n:
            if n & 1: res = res * base
            base = base * base; n >>= 1
        return res
    def diff(self, var):
        d = {}
        for k, v in self.t.items():
            if k[var]:
                kk = list(k); kk[var] -= 1
                d[tuple(kk)] = v * k[var]
        return P(d)
    def __eq__(self, other): return self.t == P(other).t
    def eval(self, vec):
        return sum((F(v) * __import__('functools').reduce(lambda x,y:x*y,
                (F(z)**j for z,j in zip(vec,k)),F(1)) for k,v in self.t.items()),F(0))

def variable(i):
    k = list(ZERO);k[i] = 1;return P({tuple(k):1})

a,b,d,u,v = [variable(i) for i in range(NVAR)]
s = a+b; B = s+2*d; K = a*b+s*d
N = (s+4*d) * (b*u+a*v+d*(u+v))
P1 = b*b*s+4*b*s*d+2*(a+3*b)*d*d
P2 = a*a*s+4*a*s*d+2*(3*a+b)*d*d
# Equalities between full multivariate integer polynomials, not sample points.
assert N.diff(2)*B*K-N*(B.diff(2)*K+B*K.diff(2)) == (a-b)*(u*P1-v*P2)
assert P1.diff(2)*P2-P1*P2.diff(2) == 4*(a-b)*s*B*K
# Substitute u=a, v=b directly in the polynomial by monomial relabeling.
def noise_match(poly):
    entries = {}
    for key,val in poly.t.items():
        e = (key[0]+key[3], key[1]+key[4], key[2], 0, 0)
        entries[e] = entries.get(e,0)+val
    return P(entries)
assert noise_match(2*B*K-N) == d*(a-b)**2

def solve(M, rhs):
    mat = [[F(x) for x in row] + [F(y)] for row,y in zip(M,rhs)]
    n = len(mat)
    for c in range(n):
        r = next(r for r in range(c,n) if mat[r][c])
        mat[c],mat[r] = mat[r],mat[c]
        factor = mat[c][c]
        mat[c] = [x/factor for x in mat[c]]
        for j in range(n):
            if j!=c:
                fac = mat[j][c]
                mat[j] = [x-fac*y for x,y in zip(mat[j],mat[c])]
    return [row[-1] for row in mat]

count = 0
for aa,bb,dd,uu,vv in product((F(1,3),F(1),F(2),F(5)),
        (F(1,2),F(1),F(3)), (F(0),F(1,5),F(1),F(7)),
        (F(1,4),F(1),F(3)), (F(1,3),F(2))):
    # Lyapunov equations for c11,c12,c22.
    mat = [[2*(aa+dd), -2*dd, F(0)],
           [-dd, aa+bb+2*dd, -dd],
           [F(0), -2*dd, 2*(bb+dd)]]
    c11,c12,c22 = solve(mat,[uu,F(0),vv])
    total = c11+2*c12+c22
    direct = (aa+bb+4*dd)*(bb*uu+aa*vv+dd*(uu+vv))/(2*(aa+bb+2*dd)*(aa*bb+(aa+bb)*dd))
    assert total == direct
    count += 1

# Sharp matched-noise witness: a=1, b=2, u=1, v=2, unique optimum d=1.
def variance(aa,bb,dd,uu,vv):
    return (aa+bb+4*dd)*(bb*uu+aa*vv+dd*(uu+vv))/(2*(aa+bb+2*dd)*(aa*bb+(aa+bb)*dd))
assert variance(F(1),F(2),F(0),F(1),F(2)) == 1
assert variance(F(1),F(2),F(1),F(1),F(2)) == F(49,50)
assert variance(F(1),F(2),F(100),F(1),F(2)) > F(49,50)
print('VERIFY_OK polynomial_derivative=1 polynomial_ratio_monotonicity=1 matched_noise_identity=1 rational_lyapunov_cases='+str(count)+' exact_witness=1')
