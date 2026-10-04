from itertools import product
from fractions import Fraction
import sympy as sp

ZERO = None
pairs = [(0,0),(0,1),(1,0),(1,1)]
vals = [ZERO,0,1]

def mul(t,a,b):
    if a is ZERO or b is ZERO:
        return ZERO
    return t[pairs.index((a,b))]

def sd(t):
    return all(mul(t,mul(t,a,b),c)==mul(t,mul(t,a,c),mul(t,b,c))
               for a,b,c in product([0,1], repeat=3))

def swap(t):
    out=[]
    for a,b in pairs:
        z=mul(t,1-a,1-b)
        out.append(ZERO if z is ZERO else 1-z)
    return tuple(out)

tables=[t for t in product(vals, repeat=4) if sd(t)]
fixed=[t for t in tables if swap(t)==t]
assert len(tables)==21
assert len(fixed)==5
assert sum(all(z is not ZERO for z in t) for t in fixed)==3
print('group_like_self_distributive_tables',len(tables))
print('swap_fixed_tables',len(fixed))
print('swap_fixed_counit_compatible_shelves',sum(all(z is not ZERO for z in t) for t in fixed))

# symbolic descent to x=(P+M)/2, y=(P-M)/(2s), a=s^2
s=sp.symbols('s', nonzero=True)
P=sp.Matrix([1,0]); M=sp.Matrix([0,1])
x=(P+M)/2; y=(P-M)/(2*s)

def vec(z):
    return sp.zeros(2,1) if z is ZERO else (P if z==0 else M)

def bprod(t,u,v):
    return sp.simplify(u[0]*v[0]*vec(t[0])+u[0]*v[1]*vec(t[1])+u[1]*v[0]*vec(t[2])+u[1]*v[1]*vec(t[3]))

def to_xy(w):
    return (sp.simplify(w[0]+w[1]), sp.simplify(s*(w[0]-w[1])))

def canon(expr):
    return sp.simplify(expr.subs(s**2, sp.Symbol('a')))

actual=[]
for t in fixed:
    row=[]
    for u,v in [(x,x),(x,y),(y,x),(y,y)]:
        c0,c1=to_xy(bprod(t,u,v))
        row.append((sp.simplify(c0), sp.simplify(c1)))
    actual.append(row)

# normalize s^-2 as 1/a for display comparison
A=sp.symbols('a', nonzero=True)
expected = [
    [((0,0)),((0,0)),((0,0)),((0,0))],
    [((sp.Rational(1,2),0)),((0,sp.Rational(1,2))),((0,sp.Rational(1,2))),((1/(2*s**2),0))],
    [((1,0)),((0,0)),((0,1)),((0,0))],
    [((1,0)),((0,1)),((0,0)),((0,0))],
    [((1,0)),((0,0)),((0,-1)),((0,0))],
]
# compare as an unordered set since enumeration order is canonical but not theorem order
key=lambda row: tuple((sp.simplify(u),sp.simplify(v)) for u,v in row)
assert {str(key(r)) for r in actual} == {str(key(r)) for r in expected}
print('descent_formulas_match',True)

# direct finite-field brute force for nonsquare a=2 over F3.
def vadd(u,v,q): return ((u[0]+v[0])%q,(u[1]+v[1])%q)
def vscale(c,u,q): return ((c*u[0])%q,(c*u[1])%q)
def vp(t,u,v,q):
    # table has 4 output vectors, bilinear extension
    out=(0,0)
    for i,ui in enumerate(u):
        for j,vj in enumerate(v):
            out=vadd(out,vscale(ui*vj,t[2*i+j],q),q)
    return out

def delta(u,a,q):
    # tensor basis xx,xy,yx,yy
    X,Y=u
    return (X%q,Y%q,Y%q,(a*X)%q)

def tensor_prod_q(t, du, dv, q):
    # (m⊗m)(id⊗tau⊗id)(du⊗dv), using du=sum u_i⊗u_j, dv=sum v_k⊗v_l
    # output tensor 4 coords
    out=[0,0,0,0]
    for i in range(2):
      for j in range(2):
       cu=du[2*i+j]
       if not cu: continue
       for k in range(2):
        for l in range(2):
         cv=dv[2*k+l]
         if not cv: continue
         left=vp(t, (1 if i==0 else 0,1 if i==1 else 0),(1 if k==0 else 0,1 if k==1 else 0),q)
         right=vp(t,(1 if j==0 else 0,1 if j==1 else 0),(1 if l==0 else 0,1 if l==1 else 0),q)
         c=(cu*cv)%q
         for r in range(2):
          for z in range(2): out[2*r+z]=(out[2*r+z]+c*left[r]*right[z])%q
    return tuple(out)

def compat(t,a,q):
    basis=[(1,0),(0,1)]
    for u in basis:
      for v in basis:
        lhs=delta(vp(t,u,v,q),a,q)
        rhs=tensor_prod_q(t,delta(u,a,q),delta(v,a,q),q)
        if lhs!=rhs: return False
    return True

def sd_general(t,a,q):
    basis=[(1,0),(0,1)]
    for u in basis:
      for v in basis:
       for w in basis:
        lhs=vp(t,vp(t,u,v,q),w,q)
        # Δw terms
        dw=delta(w,a,q); rhs=(0,0)
        for i in range(2):
         for j in range(2):
          c=dw[2*i+j]
          if not c: continue
          ei=(1 if i==0 else 0,1 if i==1 else 0)
          ej=(1 if j==0 else 0,1 if j==1 else 0)
          term=vp(t,vp(t,u,ei,q),vp(t,v,ej,q),q)
          rhs=vadd(rhs,vscale(c,term,q),q)
        if lhs!=rhs: return False
    return True

def count_maps(q,a):
    vectors=list(product(range(q),repeat=2))
    n=0
    for outputs in product(vectors, repeat=4):
        if compat(outputs,a,q) and sd_general(outputs,a,q): n+=1
    return n

n3=count_maps(3,2)
assert n3==5
print('F3_nonsquare_maps',n3)
print('CHECK_OK')
