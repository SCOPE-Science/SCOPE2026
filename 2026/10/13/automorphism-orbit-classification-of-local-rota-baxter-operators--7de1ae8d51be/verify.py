from fractions import Fraction as F

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def eq(A,B):
    return all(A[i][j] == B[i][j] for i in range(3) for j in range(3))

def phi(a,c):
    return [[a,F(0),F(0)],[F(0),a*a,F(0)],[c,F(0),a**4]]

def phi_inv(a,c):
    return [[1/a,F(0),F(0)],[F(0),1/(a*a),F(0)],[-c/(a**5),F(0),1/(a**4)]]

def T(d1,d2,r1,r2,r3):
    return [[d1,F(0),F(0)],[F(0),d2,F(0)],[r1,r2,r3]]

def conj_formula(d1,d2,r1,r2,r3,a,c):
    return T(d1,d2,a**3*r1+(c/a)*(d1-r3),a*a*r2,r3)

def mul(x,y):
    # e1^2=e2, e2^2=e3, all cross products and e3^2 vanish
    x1,x2,x3=x; y1,y2,y3=y
    return (F(0), x1*y1, x2*y2)

def lin(M,x):
    return tuple(sum(M[i][j]*x[j] for j in range(3)) for i in range(3))

def check_auto(a,c):
    P=phi(a,c)
    basis=[(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))]
    for x in basis:
        for y in basis:
            if lin(P,mul(x,y)) != mul(lin(P,x),lin(P,y)):
                return False
    return True

# Exact automorphism and inverse checks.
for a,c in [(F(2),F(3)),(F(-3),F(5)),(F(5,2),F(-7,3))]:
    assert check_auto(a,c)
    assert eq(mm(phi(a,c),phi_inv(a,c)), [[F(1),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(1)]])

# Exact conjugation law on varied parameters.
samples=[
    (F(0),F(0),F(2),F(3),F(5),F(2),F(7)),
    (F(0),F(6),F(-1),F(4),F(9),F(3),F(-2)),
    (F(8),F(4),F(5),F(-3),F(8),F(5,2),F(11,3)),
]
for d1,d2,r1,r2,r3,a,c in samples:
    lhs=mm(mm(phi(a,c),T(d1,d2,r1,r2,r3)),phi_inv(a,c))
    rhs=conj_formula(d1,d2,r1,r2,r3,a,c)
    assert eq(lhs,rhs)

# Nonresonant elimination: choose r2 to be a visible inverse square so no root extraction is needed in replay.
for d1,r3,r1,a in [(F(0),F(5),F(7),F(2)),(F(8),F(3),F(-4),F(3))]:
    r2=1/(a*a)
    c=-(a**4)*r1/(d1-r3)
    out=conj_formula(d1,F(6),r1,r2,r3,a,c)
    assert out[2][0] == 0
    assert out[2][1] == 1

# Resonant both-nonzero normal form and invariant.
for r1,r2 in [(F(2),F(3)),(F(-5),F(7)),(F(9,2),F(-4,3))]:
    Delta=r1*r1/(r2*r2*r2)
    a=Delta*r2/r1
    out=conj_formula(F(4),F(2),r1,r2,F(4),a,F(17))
    assert out[2][0] == Delta*Delta
    assert out[2][1] == Delta
    assert out[2][2] == F(4)
    assert (out[2][0]**2)/(out[2][1]**3) == Delta

# Invariance of Delta under weighted scaling.
for r1,r2,a in [(F(2),F(3),F(5)),(F(-7),F(4),F(2,3))]:
    before=r1*r1/(r2*r2*r2)
    after=(a**3*r1)**2/((a*a*r2)**3)
    assert before == after

print('automorphism_checks=3')
print('conjugation_formula_checks=3')
print('nonresonant_reductions=2')
print('resonant_normal_form_checks=3')
print('weighted_invariant_checks=2')
print('CHECK_OK')
