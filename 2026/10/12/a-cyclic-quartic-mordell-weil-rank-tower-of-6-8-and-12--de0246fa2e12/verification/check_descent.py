"""Exact height-pairing certificate for cyclic quartic descent of an elliptic K3 family.
Requires Python 3 and sympy. All computations use Q(i) and exact polynomial gcds.
"""
import sys
import sympy as sp
I = sp.I
v, t = sp.symbols('v t')

def B(z):
    return sp.expand(z * (z**4 - 1))

def sections(u):
    m = B(u)*B(v)
    g, d = B(u), B(v)
    a = [-18*(1+I)*(u*v+I),18*(1+I)*(u*v+I),
         18*(1-I)*(u*v-I),18*(1-I)*(u+I*v),
         -18*(1+I)*(u-I*v), 0]
    b = [-3*(5*u**4*v**4-u**4-v**4+24*I*u**3*v**3-24*u**2*v**2-24*I*u*v+5)]*2 + [
         -3*(5*u**4*v**4-u**4-v**4-24*I*u**3*v**3-24*u**2*v**2+24*I*u*v+5),
          3*(u**4*v**4-5*u**4-5*v**4-24*I*u**3*v+24*u**2*v**2+24*I*u*v**3+1),
          3*(u**4*v**4-5*u**4-5*v**4+24*I*u**3*v+24*u**2*v**2-24*I*u*v**3+1),
          3*(u**4*v**4+u**4+v**4+6*u**4*v**2+6*u**2*v**4-12*u**2*v**2+6*u**2+6*v**2+1)]
    out = []
    for aj,bj in zip(a,b):
        c = sp.expand(aj**3 / 108)
        q = sp.expand((3*aj**2*bj-11664*m-c**2)/108)
        x = sp.Poly(sp.expand(aj*g*t**3+bj*t**2+aj*d*t),t)
        y = sp.Poly(sp.expand(54*g**2*t**5+c*g*t**4+(108*g*d+q)*t**3+c*d*t**2+54*d**2*t),t)
        out.append((x,y))
    return out

P = sections(sp.Integer(2)) + sections(2*I)
A=lambda z:z**8+14*z**4+1
C=lambda z:z**12-33*z**8-33*z**4+1
# Verify that all twelve universal sections lie on the asserted Weierstrass curve.
for x,y in P:
    check=sp.Poly(y.as_expr()**2-x.as_expr()**3 + 27*481*A(v)*t**4*x.as_expr()
        -2916*(30**4*t**10+B(v)**4*t**2)+54*4879*C(v)*t**6,t)
    assert all(sp.expand(c)==0 for c in check.all_coeffs())

def specialize(value):
    return [(sp.Poly(sp.expand(x.as_expr().subs(v,value)),t,extension=I),
             sp.Poly(sp.expand(y.as_expr().subs(v,value)),t,extension=I)) for x,y in P]

special_value = sp.Integer(sys.argv[1]) if len(sys.argv)>1 else sp.Integer(5)
if special_value not in (5,7):
    raise SystemExit('Use certified nonsingular specializations 5 or 7')
Q = specialize(special_value)
Q_i = specialize(special_value*I)
Q_minus = specialize(-special_value)

def order_zero(poly):
    if poly.is_zero:
        raise AssertionError('Unexpected coincident x coordinates')
    return min(m[0] for m,_ in poly.terms())

def boundary_intersection(x,z,at_infty=False):
    diff=x-z
    e = 4-diff.degree() if at_infty else order_zero(diff)
    return max(0,e-1)

def point_intersection(left,right,j,k,same_at_zero):
    x,y=left[j];z,w=right[k]
    dx,dy=x-z,y-w
    if dx.is_zero and dy.is_zero:
        raise AssertionError('Coincident points require diagonal treatment')
    if dx.is_zero:
        gcd=dy
    elif dy.is_zero:
        gcd=dx
    else:
        gcd=sp.gcd(dx,dy)
    away=0 if gcd.is_zero else gcd.degree()-order_zero(gcd)
    at_zero=boundary_intersection(x,z) if same_at_zero else 0
    at_infty=boundary_intersection(x,z,True) if (j<6)==(k<6) else 0
    return away + at_zero + at_infty

def correction(j,k,same_at_zero):
    return ((sp.Rational(2,3) if same_at_zero else sp.Rational(1,3))
          + (sp.Rational(2,3) if (j<6)==(k<6) else sp.Rational(1,3)))

def pair(left,right,j,k,same_at_zero):
    if left[j] == right[k]:
        return sp.Rational(8,3)
    return 2-point_intersection(left,right,j,k,same_at_zero)-correction(j,k,same_at_zero)

H=sp.Matrix(12,12,lambda j,k:pair(Q,Q,j,k,True))
M=sp.Matrix([[8,-4,2,2,2,2],[-4,8,2,2,2,2],
             [2,2,8,2,2,2],[2,2,2,8,2,2],
             [2,2,2,2,8,2],[2,2,2,2,2,8]])
N=sp.Matrix([[3,-3,-3,0,0,0],[-3,3,3,0,0,0],
             [3,-3,3,0,0,0],[0,0,0,3,3,0],
             [0,0,0,-3,3,0],[0,0,0,0,0,0]])
H_expected=sp.BlockMatrix([[M,N],[N.T,M]]).as_explicit()/3
assert H==H_expected, 'Baseline Gram matrix differs from published Appendix A.10'
assert H.det()==sp.Rational(4096,9)

G4=sp.Matrix(12,12,lambda j,k:pair(Q,Q_i,j,k,False))
T4=H.inv()*G4
G2=sp.Matrix(12,12,lambda j,k:pair(Q,Q_minus,j,k,True))
T2=H.inv()*G2
ident=sp.eye(12)
assert all(a.q==1 for a in T4), 'Action matrix is not integral'
assert T4**4==ident
assert T4**2==T2, 'Independent order-two computation does not agree'
assert T4.T*H*T4==H
traces=[sp.trace(T4**j) for j in range(4)]
assert traces==[12,4,4,4]
assert [int((sum((T4**j for j in range(4)),sp.zeros(12))).rank()),
        int((ident+T4**2).rank()),12]==[6,8,12]
print('CHECK_OK: baseline_height_matrix, mixed_height_pairings, quartic_action, independent_square, isometry; specialization', special_value)
print('ACTION_TRACES',list(map(int,traces)))
print('QUARTIC_DESCENT_RANKS', [6,8,12])
print('ACTION_MATRIX',T4.tolist())
