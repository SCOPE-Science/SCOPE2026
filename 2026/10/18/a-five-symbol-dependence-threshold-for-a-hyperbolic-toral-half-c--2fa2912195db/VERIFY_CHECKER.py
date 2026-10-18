"""Independent reproducibility checks for the toral half-circle sensor theorem.

Run: python3 VERIFY_CHECKER.py
Only Python's standard library is required. Finite-grid checks support,
not replace, the exact Fourier argument in RESULT.md.
"""
from itertools import combinations, product
from functools import reduce
from fractions import Fraction
from math import gcd, pi
from cmath import exp

A = ((1, 1, 0), (1, 2, 1), (0, 1, 2))

def rowmul(v):
    return tuple(sum(v[j] * A[j][i] for j in range(3)) for i in range(3))

def determinant(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))

rows = [(1,0,0)]
for n in range(1, 12):
    rows.append(rowmul(rows[-1]))
assert rows[:5] == [(1,0,0),(1,1,0),(2,3,1),(5,9,5),(14,28,19)]
assert determinant(*A) == 1
assert determinant(*rows[:3]) == 1
assert all(determinant(*[rows[i] for i in ts]) != 0
           for ts in combinations(range(12), 3))
# Direct Cayley-Hamilton check for each of the three standard row vectors.
for v in ((1,0,0),(0,1,0),(0,0,1)):
    a,b,c,d = v,rowmul(v),rowmul(rowmul(v)),rowmul(rowmul(rowmul(v)))
    assert tuple(d[i]-5*c[i]+6*b[i]-a[i] for i in range(3))==(0,0,0)

def primitive_relation(times):
    v=[rows[t] for t in times]
    raw=[((-1)**j)*determinant(*[v[i] for i in range(4) if i!=j]) for j in range(4)]
    g=reduce(gcd,raw)
    c=tuple(-a//g for a in raw)
    assert gcd(*c)==1 and all(a != 0 for a in c)
    assert all(sum(c[i]*v[i][j] for i in range(4))==0 for j in range(3))
    return c

relations={times:primitive_relation(times) for times in combinations(range(5),4)}
assert relations == {
 (0,1,2,3):(-1,6,-5,1),
 (0,1,2,4):(-5,29,-19,1),
 (0,1,3,4):(-6,31,-19,5),
 (0,2,3,4):(-1,31,-29,6),
 (1,2,3,4):(-1,6,-5,1)
}

def four_sign_moment(times):
    c=primitive_relation(times)
    if any(a%2 == 0 for a in c): return Fraction(0)
    den=3
    for a in c:den*=a
    return Fraction(1,den)

rho=Fraction(1,8265)
assert [four_sign_moment(times) for times in combinations(range(5),4)] == [0,rho,0,0,0]
assert tuple(sum(rows[n][j] for n in range(5))%2 for j in range(3))==(1,1,1)

# The exact 5-bit joint law is a probability measure and every <=4
# projection agrees with the fourth-order moment classification.
weights={s:(Fraction(1,32)*(1+rho*s[0]*s[1]*s[2]*s[4]))
         for s in product((-1,1),repeat=5)}
assert sum(weights.values())==1 and all(w>0 for w in weights.values())
for J in [(),*(tuple(c) for d in range(1,5) for c in combinations(range(5),d))]:
 for signs in product((-1,1),repeat=len(J)):
    val=sum(w for s,w in weights.items() if all(s[j]==t for j,t in zip(J,signs)))
    expected=Fraction(1,2**len(J))
    if J==(0,1,2,4): expected*=1+rho*__import__('math').prod(signs)
    assert val==expected,(J,signs,val,expected)

# A genuinely different calculation on finite uniform grid tori: for
# q even, use the explicit discrete Fourier transform of the half-step.
# As q grows this must converge to the continuous exact answer. This
# numerical comparison is NOT an infinite proof or an error certificate.
for q in (2048,8192):
    coeff=[0j]*q
    for m in range(1,q,2):
        coeff[m]=4/(q*(1-exp(-2j*pi*m/q)))
    value=sum(coeff[(-5*m)%q]*coeff[(29*m)%q]*
              coeff[(-19*m)%q]*coeff[m] for m in range(q))
    assert abs(value.imag)<1e-11
    assert abs(value.real-float(rho))<(7e-8 if q==2048 else 5e-9)

print('VERIFY_OK')
print('first_5_rows:', rows[:5])
print('all_4_circuits_to_lag_4:', relations)
print('four_point_moment:', rho)
print('five_block_joint_probabilities:',
      {'even_sign_product':str((1+rho)/32), 'odd_sign_product':str((1-rho)/32)})
