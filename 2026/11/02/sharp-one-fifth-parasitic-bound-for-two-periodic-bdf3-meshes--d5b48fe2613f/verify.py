"""Exact and finite consistency checks for the alternating-step BDF3 theorem.

Requires Python 3.10+ and SymPy 1.12+.
Analytic inequalities in RESULT.md, not finite tests, prove the all-ratio result.
"""
from fractions import Fraction
import sympy as sp

r, z = sp.symbols('r z', positive=True)
N = 0

def check(condition, message):
    global N
    assert condition, message
    N += 1

# Three previous time gaps are h, h/r, h; rescale h to one.
nodes = [sp.Integer(0), -sp.Integer(1), -sp.Integer(1) - 1/r,
         -sp.Integer(2) - 1/r]
weights = []
for j in range(4):
    basis = sp.prod((z - nodes[i])/(nodes[j] - nodes[i])
                    for i in range(4) if i != j)
    weights.append(sp.factor(sp.diff(basis, z).subs(z, 0)))
for deg in range(4):
    moment = sp.factor(sum(weights[j]*nodes[j]**deg for j in range(4)))
    check(sp.simplify(moment - int(deg == 1)) == 0,
          'Lagrange derivative exactness degree %d' % deg)

A = sp.factor(-(weights[0] + weights[1])/weights[0])
B = sp.factor(weights[3]/weights[0])
check(sp.simplify(A - r*r*(4*r+3)/(5*r*r+5*r+1)) == 0, 'A coefficient')
check(sp.simplify(B + r*(r+1)/(5*r*r+5*r+1)) == 0, 'B coefficient')
T = sp.Matrix([[A, B], [1, 0]])
M = sp.simplify(T.subs(r, 1/r)*T)
K = (r*r+5*r+5)*(5*r*r+5*r+1)
tr = sp.factor(sp.trace(M)); det = sp.factor(M.det())
check(sp.simplify(tr + (r**4-r**3-5*r*r-r+1)/K) == 0, 'trace')
check(sp.simplify(det - r*(r+1)**2/K) == 0, 'determinant')
check(sp.simplify(1 + 5*tr + 25*det - 6*r*(10*r*r+21*r+10)/K) == 0,
      'Jury positive inequality 1')
check(sp.simplify(1 - 5*tr + 25*det -
                  2*(5*r**4+25*r**3+38*r*r+25*r+5)/K) == 0,
      'Jury positive inequality 2')
check(sp.simplify(1-25*det - (5*r**4+5*r**3+r*r+5*r+5)/K) == 0,
      'Jury positive inequality 3')
check(sp.limit(tr, r, sp.oo) == -sp.Rational(1, 5), 'limiting trace')
check(sp.limit(det, r, sp.oo) == 0, 'limiting determinant')
check(sp.limit(A/r, r, sp.oo) == sp.Rational(4, 5), 'transient growth')
check(sp.simplify(tr - tr.subs(r, 1/r)) == 0, 'trace phase symmetry')
check(sp.simplify(det - det.subs(r, 1/r)) == 0, 'det phase symmetry')

# Independent exact-rational finite runs use the interpolation coefficients
# directly, rather than inserting the simplified step coefficients above.
def diffs_from_interpolation(rr, prev, prevprev):
    # current h=1, previous=1/rr, before previous h=1
    pts = [Fraction(0), Fraction(-1), -1-Fraction(1, rr),
           -2-Fraction(1, rr)]
    w = []
    for j in range(4):
        den = Fraction(1)
        for i in range(4):
            if i != j:
                den *= pts[j]-pts[i]
        num = Fraction(0)
        for m in range(4):
            if m == j: continue
            product = Fraction(1)
            for i in range(4):
                if i != j and i != m:
                    product *= -pts[i]
            num += product
        w.append(num/den)
    # w0*y_n+w1*y_{n-1}+w2*y_{n-2}+w3*y_{n-3}=0.
    y0, y1, y2 = prevprev
    new = -(w[1]*y2+w[2]*y1+w[3]*y0)/w[0]
    return new, w

ratios = [Fraction(1,100),Fraction(1,10),Fraction(1,3),Fraction(2,3),
          Fraction(1),Fraction(3,2),Fraction(7),Fraction(101),
          Fraction(101,103), Fraction(1003,7)]
for rr in ratios:
    valA = Fraction(rr*rr*(4*rr+3), 5*rr*rr+5*rr+1)
    valB = Fraction(-rr*(rr+1),5*rr*rr+5*rr+1)
    for init in [(Fraction(0),Fraction(0),Fraction(1)),
                 (Fraction(1),Fraction(-2),Fraction(5)),
                 (Fraction(2),Fraction(3),Fraction(3))]:
        u, ww = diffs_from_interpolation(rr, init, init)
        actual = u-init[2]
        expected = valA*(init[2]-init[1])+valB*(init[1]-init[0])
        check(actual == expected, 'rational BDF recurrence at ratio %s' % rr)
        check(sum(ww) == 0, 'constant exactness at ratio %s' % rr)
        check(sum(ww[j]*([Fraction(0),-1,-1-1/rr,-2-1/rr][j])
                  for j in range(4)) == 1, 'linear exactness at ratio %s' % rr)
    # Two sequential direct steps agree with a product of companion matrices.
    d0,d1=Fraction(2),Fraction(-3)
    d2=valA*d1+valB*d0
    rr2=1/rr
    a2=rr2*rr2*(4*rr2+3)/(5*rr2*rr2+5*rr2+1)
    b2=-rr2*(rr2+1)/(5*rr2*rr2+5*rr2+1)
    d3=a2*d2+b2*d1
    T1=sp.Matrix([[sp.Rational(valA.numerator,valA.denominator),
                   sp.Rational(valB.numerator,valB.denominator)],[1,0]])
    T2=sp.Matrix([[sp.Rational(a2.numerator,a2.denominator),
                   sp.Rational(b2.numerator,b2.denominator)],[1,0]])
    v=T2*T1*sp.Matrix([d1,d0])
    check(v[0]==d3 and v[1]==d2,'two-step product')

print('PASS: %d exact/symbolic checks.' % N)
print('Analytic positivity of the three factored Jury polynomials supplies the infinite proof.')
