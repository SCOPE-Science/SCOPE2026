"""Exact and finite-field checks for compatible products on K[t]/(t^3).
Uses Python's standard library only. Run: python3 verify.py
"""
from fractions import Fraction
from itertools import product
from random import Random

N = 9
ZERO = (0,) * N
class Poly:
    def __init__(self, d=None): self.d = {m: v for m, v in (d or {}).items() if v}
    @staticmethod
    def const(k): return Poly({ZERO: k})
    @staticmethod
    def var(i):
        m = list(ZERO); m[i] = 1
        return Poly({tuple(m): 1})
    def __add__(self, other):
        if not isinstance(other, Poly): other = Poly.const(other)
        d = self.d.copy()
        for m, c in other.d.items(): d[m] = d.get(m, 0) + c
        return Poly(d)
    __radd__ = __add__
    def __neg__(self): return Poly({m: -c for m, c in self.d.items()})
    def __sub__(self, other): return self + -other if isinstance(other, Poly) else self + (-other)
    def __rsub__(self, other): return -self + other
    def __mul__(self, other):
        if not isinstance(other, Poly): other = Poly.const(other)
        d = {}
        for m, c in self.d.items():
            for n, e in other.d.items():
                k = tuple(m[i] + n[i] for i in range(N))
                d[k] = d.get(k, 0) + c * e
        return Poly(d)
    __rmul__ = __mul__
    def __eq__(self, other):
        if not isinstance(other, Poly): other = Poly.const(other)
        return self.d == other.d
    def plug_zero(self, indices):
        return Poly({m:c for m,c in self.d.items() if all(m[i] == 0 for i in indices)})

v = [Poly.var(i) for i in range(9)]
a,b,c,d,e,f,g,h,j = v
z = Poly.const(0)
one = Poly.const(1)
def table(params):
    a,b,c,d,e,f,g,h,j = params
    return [[(a,b,c), (0,a,b), (0,0,a)],
            [(0,a,b), (d-e,g,h), (f,d,j)],
            [(0,0,a), (f,d,j), (0,f,e)]]

def mul(P, X, Y):
    out = [0,0,0]
    for i in range(3):
        for j in range(3):
            for k in range(3):out[k] += X[i]*Y[j]*P[i][j][k]
    return tuple(out)

E = [(1,0,0),(0,1,0),(0,0,1)]
MU = [[E[i+j] if i+j < 3 else (0,0,0) for j in range(3)] for i in range(3)]
def asso(P,i,j,k):
    return tuple(x-y for x,y in zip(mul(P,mul(P,E[i],E[j]),E[k]), mul(P,E[i],mul(P,E[j],E[k]))))
def mixed(P,i,j,k):
    A=mul(MU,mul(P,E[i],E[j]),E[k]); B=mul(P,mul(MU,E[i],E[j]),E[k])
    C=mul(MU,E[i],mul(P,E[j],E[k])); D=mul(P,E[i],mul(MU,E[j],E[k]))
    return tuple(A[t]+B[t]-C[t]-D[t] for t in range(3))

P=table(v)
assert all(all(x == z for x in mixed(P,i,j,k)) for i,j,k in product(range(3),repeat=3))
poly_assocs=[x for i,j,k in product(range(3),repeat=3) for x in asso(P,i,j,k) if x != z]
# Necessary field equations for the three disjoint strata.
need=[b*f,b*e,b*d+c*f,b*g+c*d,b*j+c*e,b*(h-a)+c*j]
assert all(any(t == n or t == -n for t in poly_assocs) for n in need)
# On b=c=0 the full set of associative equations becomes three 2-by-2 minors.
minors=[f*(h-a)-d*j,f*(g-j)-d*(d-e),j*(g-j)-(h-a)*(d-e)]
reduced={tuple(sorted(p.d.items())) for p in poly_assocs if p.plug_zero([1,2]) == p and p != z}
restricted=[p.plug_zero([1,2]) for p in poly_assocs]
for p in restricted:
    assert p==z or any(p==m or p==-m for m in minors)
assert all(any(p==m or p==-m for p in restricted) for m in minors)
# Every equation vanishes identically on the two linear component closures.
branches=[[a,b,c,z,z,z,z,a,z], [a,z,c,z,z,z,g,h,z]]
for Q in branches:
    assert all(all(t==z for t in asso(table(Q),i,j,k)) for i,j,k in product(range(3),repeat=3))

# Reconstruct the compatibility rank from all 27 independent structure coefficients.
def ambient(i):
    Q = [[list((0,0,0)) for j in range(3)] for k in range(3)]
    Q[i//9][(i//3)%3][i%3] = 1
    return Q
rows=[]
for i,j,k,t in product(range(3),repeat=4):
    rows.append([mixed(ambient(m),i,j,k)[t] for m in range(27)])
def rank(mat, mod=None):
    A=[[Fraction(q) if mod is None else q%mod for q in row] for row in mat]
    r=0
    for col in range(len(A[0])):
        pivot=next((s for s in range(r,len(A)) if A[s][col]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=(1/A[r][col]) if mod is None else pow(A[r][col],-1,mod)
        A[r]=[(x*inv if mod is None else x*inv%mod) for x in A[r]]
        for t in range(r+1,len(A)):
            if not A[t][col]:continue
            c0=A[t][col]
            A[t]=[(A[t][s]-c0*A[r][s] if mod is None else (A[t][s]-c0*A[r][s])%mod) for s in range(len(A[0]))]
        r+=1
        if r==len(A):break
    return r
assert rank(rows)==18
assert all(rank(rows,p)==18 for p in [2,3,5,7])
# The nine coefficient templates are linearly independent even mod 2.
template=[]
for t in range(9):
    inp=[int(s==t) for s in range(9)]; T=table(inp)
    template.append([T[i][j][k] for i,j,k in product(range(3),repeat=3)])
assert rank(template)==9 and all(rank(template,p)==9 for p in [2,3,5])

def mod_associative(params,q):
    T=table(params)
    return all(all(z%q==0 for z in asso(T,i,j,k)) for i,j,k in product(range(3),repeat=3))
def geometric(params,q):
    a,b,c,d,e,f,g,h,j=[w%q for w in params]
    if b: return d==e==f==g==j==0 and h==a
    if c: return d==e==f==j==0
    return (f*(h-a)-d*j)%q==0 and (f*(g-j)-d*(d-e))%q==0 and (j*(g-j)-(h-a)*(d-e))%q==0
for q in (2,3):
    total=0
    for params in product(range(q),repeat=9):
        actual=mod_associative(params,q)
        predicted=geometric(params,q)
        assert actual==predicted, (q,params)
        total+=actual
    expected=q**5+2*q**4-2*q**2
    assert total==expected,(q,total,expected)
    print('EXHAUSTIVE',q,total)
rng=Random(1507)
for q in (5,7,11):
    for _ in range(3000):
        params=[rng.randrange(q) for _ in range(9)]
        assert mod_associative(params,q)==geometric(params,q)
    print('SAMPLES',q,3000)
print('RANK_27_VARIABLE_COMPATIBILITY',rank(rows))
print('FIELDPATH_MATRIX_CONE_COUNTS',[(q,q**5+2*q**4-2*q**2) for q in (2,3,5,7,11)])
print('VERIFY_OK')
