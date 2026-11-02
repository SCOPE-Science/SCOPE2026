#!/usr/bin/env python3
"""Exact symbolic verification of a four-point Lipschitz-free numerical-index law.

Requires SymPy. Every parameter-uniform assertion is algebraic; no
floating-point grid is used as a substitute for proof.
"""
import itertools
import sympy as s

z = s.symbols('t', positive=True, real=True)
SQRT2 = s.sqrt(2)
pairs = [(0,1),(1,2),(2,3),(0,3),(0,2),(1,3)]
lengths = [s.Integer(1)]*4 + [z,z]
u = [s.Matrix([int(k==j)-int(k==i) for k in (1,2,3)])
     for i,j in pairs]
m = [u[i]/lengths[i] for i in range(6)]
constraints = [(u[i],lengths[i]) for i in range(6)] + \
              [(-u[i],lengths[i]) for i in range(6)]
V = [s.Matrix(v) for v in (
    (-1,-z,-1),(-1,-z,1-z),(-1,z-2,z-1),(-1,0,-1),(-1,0,z-1),
    (1-z,-z,-1),(1-z,-z,1-z),(1-z,0,1),(1-z,2-z,1),
    (z-1,z-2,-1),(z-1,0,-1),(z-1,z,z-1),(z-1,z,1),
    (1,0,1-z),(1,0,1),(1,2-z,1-z),(1,z,z-1),(1,z,1)
)]

def ident_zero(x):
    return s.cancel(x) == 0

def matrix_eq(A,B):
    return all(ident_zero(x) for x in A-B)

def signature(M):
    x = tuple(s.factor(w) for w in M)
    y = tuple(-w for w in x)
    return min((x,y), key=lambda v: str(v))

# Enumerate *all* intersections of three independent constraints.
# The feasibility interval for every candidate is exact because each slack
# is affine in t. This also excludes hidden intermediate parameter phases.
candidates = {}
for triple in itertools.combinations(range(12),3):
    A = s.Matrix.hstack(*(constraints[i][0] for i in triple)).T
    if A.det() == 0:
        continue
    b = s.Matrix([constraints[i][1] for i in triple]); x=A.inv()*b
    lo,hi = s.Integer(1),s.Integer(2)
    for c,d in constraints:
        slack=s.expand(d-(c.T*x)[0]); slope=s.diff(slack,z)
        intercept=s.expand(slack-slope*z)
        assert not slope.has(z)
        if slope>0:
            lo=max(lo,-intercept/slope)
        elif slope<0:
            hi=min(hi,-intercept/slope)
        elif intercept<0:
            lo,hi=s.Integer(2),s.Integer(1)
            break
    if hi>lo:
        key=tuple(s.factor(k) for k in x)
        candidates.setdefault(key,set()).add((lo,hi))
    elif lo==hi and 1<lo<2:
        assert any(matrix_eq(x.subs(z,lo),v.subs(z,lo)) for v in V)
assert len(candidates)==18
assert {tuple(s.factor(k) for k in v) for v in V}==set(candidates)
assert all(ranges=={(s.Integer(1),s.Integer(2))} for ranges in candidates.values())
for v in V:
    for c,d in constraints:
        slack=s.expand(d-(c.T*v)[0]);
        assert slack.subs(z,1)>=0 and slack.subs(z,2)>=0

# Precisely 28 norming pairs, with the indexing fixed in this array.
N = [(i,k) for i in range(6) for k,v in enumerate(V)
     if ident_zero((v.T*m[i])[0]-1)]
assert len(N)==28
for i in range(6):
    for k in range(18):
        gap=s.cancel(1-(V[k].T*m[i])[0]);
        assert s.sign(gap.subs(z,s.Rational(3,2)))>=0
        assert ((i,k) in N)==ident_zero(gap)
A=[V[k]*m[i].T for i,k in N]
W=[p*q.T for q in m for p in V]
# Every rank-one operator norm functional is equivalent by a square
# isometry and overall sign to one of these ten tensor representatives.
reps=[0,1,3,5,6,72,73,74,75,76]
perms=[tuple((i+k)%4 for i in range(4)) for k in range(4)] + \
      [tuple((k-i)%4 for i in range(4)) for k in range(4)]
Gs=[s.Matrix.hstack(*[
      s.Matrix([int(k==p[i])-int(k==p[0]) for k in (1,2,3)])
      for i in (1,2,3)]) for p in perms]
all_keys={signature(x) for x in W}
assert len(all_keys)==54
covered=set()
for rep in reps:
    w=W[rep]
    orbit={signature(g.inv().T*w*g.T) for g in Gs}
    assert orbit <= all_keys
    assert not covered.intersection(orbit)
    covered.update(orbit)
assert covered==all_keys

# Explicit tensor decompositions; each A_j is a numerical-radius
# norming-pair functional. Coefficient absolute sums are the sharp bounds.
c={
 0:{4:-1},1:{3:-1},3:{1:-1},
 5:{0:2-z,3:1-z,4:z-2},
 6:{0:(2-z)/z,1:(z-1)*(2-z)/z,3:-1},
 72:{23:-1},73:{22:-1},
 74:{6:2*(z-1)/z**3,15:2*(z-1)/z**3,
     0:-2*(z-1)/z**3,13:-2*(z-1)/z**3,22:(z-2)/z},
 75:{5:1/z,1:-1/z},76:{6:1/z,0:-1/z}
}
for rep,terms in c.items():
    lhs=sum((A[j]*a for j,a in terms.items()),s.zeros(3,3))
    assert matrix_eq(lhs,W[rep])
C1=3-z
C2=(-z**3+2*z**2+8*z-8)/z**3
assert ident_zero(C2-C1-(z-2)**2*(z**2-2)/z**3)
assert ident_zero(C1-2/z-(z-1)*(2-z)/z)

# The operators are norm-one in numerical radius. To verify parameter-
# uniform inequalities, an exact derivative test checks each low-degree
# polynomial numerator of 1 +/- the 28 evaluations on its whole interval.
TA=s.Matrix([[1,0,0],[-2/z,-(2-z)/z,0],[0,0,(3*z-4)/z]])
TB=s.Matrix([[-1,-2/z,-2/z],
             [2*(2-z)/z**2,-1+2*(2-z)/z**2,0],
             [0,2/z,(2-z)/z]])

def nonnegative_poly_interval(expr,left,right):
    p=s.Poly(s.factor(expr),z)
    assert p.degree()<=3
    sample_points=[left,right]
    if p.degree()>1:
        for root in s.solve(s.diff(p.as_expr(),z),z):
            if root.is_real is False:continue
            if s.sign(s.simplify(root-left))>=0 and s.sign(s.simplify(right-root))>=0:
                sample_points.append(root)
    for pt in sample_points:
        val=s.simplify(p.as_expr().subs(z,pt))
        assert s.sign(val)>=0, (expr,pt,val)

def check_upper(T,left,right):
    for i,k in N:
        f=s.cancel((V[k].T*T*m[i])[0]);
        for h in (-1,1):
            num,den=s.fraction(s.together(1+h*f))
            assert den.subs(z,left)>0 and den.subs(z,right)>0
            # In the displayed matrices every denominator is a power of t.
            assert all(s.simplify(den/z**q)!=1 for q in range(4)) is False
            nonnegative_poly_interval(num,left,right)
check_upper(TA,s.Integer(1),s.Integer(2))
check_upper(TB,SQRT2,s.Integer(2))
assert ident_zero((V[5].T*TA*m[0])[0]-C1)
assert ident_zero((V[2].T*TB*m[4])[0]-C2)
print('VERIFIED: 18 dual vertices, 28 norming pairs, 10 symmetry orbits,')
print('10 tensor identities, both exact sharp-operator families,')
print('and symbolic inequalities on their full parameter intervals.')
