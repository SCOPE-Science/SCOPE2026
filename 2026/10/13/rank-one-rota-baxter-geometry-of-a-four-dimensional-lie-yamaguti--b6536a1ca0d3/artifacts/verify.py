import sympy as sp
from itertools import product

# Symbolic reconstruction for the 4-dimensional Lie-Yamaguti algebra
# [e1,e2]=2e4 and <<e1,e2,e1>>=e4.
u1,u2,u3,u4,l1,l2,l3,l4=sp.symbols('u1 u2 u3 u4 l1 l2 l3 l4')
x1,x2,x3,x4,y1,y2,y3,y4,z1,z2,z3,z4=sp.symbols('x1 x2 x3 x4 y1 y2 y3 y4 z1 z2 z3 z4')
u=sp.Matrix([u1,u2,u3,u4]); ell=sp.Matrix([l1,l2,l3,l4])
x=sp.Matrix([x1,x2,x3,x4]); y=sp.Matrix([y1,y2,y3,y4]); z=sp.Matrix([z1,z2,z3,z4])

def ev(v): return sp.expand((ell.T*v)[0])
def R(v): return sp.expand(ev(v))*u
def om(a,b): return sp.expand(a[0]*b[1]-a[1]*b[0])
def br(a,b): return sp.Matrix([0,0,0,2*om(a,b)])
def tri(a,b,c): return sp.Matrix([0,0,0,sp.expand(om(a,b)*c[0])])

def db(a,b):
    return sp.simplify(br(R(a),R(b))-R(br(R(a),b)-br(R(b),a)))
def dt(a,b,c):
    return sp.simplify(tri(R(a),R(b),R(c))-R(tri(R(a),R(b),c)+tri(a,R(b),R(c))+tri(R(a),b,R(c))))

h=lambda v: sp.expand(u1*v[1]-u2*v[0])
wedge=sp.expand(ev(x)*h(y)-ev(y)*h(x))
assert sp.simplify(db(x,y) - (-2*l4*wedge)*u)==sp.zeros(4,1)
assert sp.simplify(dt(x,y,z) - (-l4*u1*ev(z)*wedge)*u)==sp.zeros(4,1)
print('SYMBOLIC_DEFECT_FORMULAS_OK')

# Finite-field replay: direct identities for all rank <= 1 matrices over F_3.
def mv(M,v,q):
    return tuple(sum(M[4*i+j]*v[j] for j in range(4))%q for i in range(4))
def brq(a,b,q):
    return (0,0,0,(2*(a[0]*b[1]-a[1]*b[0]))%q)
def triq(a,b,c,q):
    return (0,0,0,((a[0]*b[1]-a[1]*b[0])*c[0])%q)
def add(*vs,q): return tuple(sum(v[i] for v in vs)%q for i in range(4))
def neg(v,q): return tuple((-x)%q for x in v)
BAS=((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))

def is_rb(M,q):
    for a in BAS:
      for b in BAS:
        Ra,Rb=mv(M,a,q),mv(M,b,q)
        lhs=brq(Ra,Rb,q)
        inside=add(brq(Ra,b,q),neg(brq(Rb,a,q),q),q=q)
        if lhs != mv(M,inside,q): return False
    for a in BAS:
      for b in BAS:
        for c in BAS:
          Ra,Rb,Rc=mv(M,a,q),mv(M,b,q),mv(M,c,q)
          lhs=triq(Ra,Rb,Rc,q)
          inside=add(triq(Ra,Rb,c,q),triq(a,Rb,Rc,q),triq(Ra,b,Rc,q),q=q)
          if lhs != mv(M,inside,q): return False
    return True

def rank1_mats(q):
    S={(0,)*16}
    vecs=[v for v in product(range(q),repeat=4) if any(v)]
    # Canonicalize factor pairs through matrices; q=3 only for direct ambient replay.
    for u in vecs:
      for l in vecs:
        M=tuple((u[i]*l[j])%q for i in range(4) for j in range(4))
        S.add(M)
    return S

def predicted(M,q):
    last_col_zero=all(M[4*i+3]%q==0 for i in range(4))
    image_in_C=all(M[4*i+j]%q==0 for i in (0,1) for j in range(4))
    return last_col_zero or image_in_C

S=rank1_mats(3)
assert len(S)==1+(3**4-1)**2//(3-1)
rb={M for M in S if is_rb(M,3)}
pred={M for M in S if predicted(M,3)}
assert rb==pred
expected3=3**6+2*3**5+3**4-3**3-3**2-3
assert len(rb)==expected3
E21=(0,0,0,0, 1,0,0,0, 0,0,0,0, 0,0,0,0)
assert E21 in rb
print({'q':3,'rank_le_1_total':len(S),'rank_le_1_rb':len(rb),'E21':True})

# Exact structural point counts over further odd fields, obtained by determinantal counts.
for q in (5,7,11):
    A=1+(q**4-1)*(q**3-1)//(q-1)
    B=1+(q**2-1)*(q**4-1)//(q-1)
    I=1+(q**2-1)*(q**3-1)//(q-1)
    union=A+B-I
    formula=q**6+2*q**5+q**4-q**3-q**2-q
    assert union==formula
    print({'q':q,'A':A,'B':B,'intersection':I,'union':union})

print('VERIFY_OK')
