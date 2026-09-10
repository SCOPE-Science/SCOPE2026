"""Target: covering-collection census for X_31: y^2 = x^6+31x^4+31x^2+1.
Step 1: factor identity, known-point verification, twist assignment.
Step 2: mod-7 pruning certificates for d=7,14 (infinite descent).
Step 3: quartic-to-Weierstrass model for C_1 via series matching + mod-p check.
Stdlib only, exact integer arithmetic."""
from fractions import Fraction

def f(X): return X**6+31*X**4+31*X**2+1
def g1(X): return X**2+1
def g2(X): return X**4+30*X**2+1

# --- Step 1 ---
for x in range(-9, 10):
    assert g1(x)*g2(x) == f(x)
print("factor identity OK")
from fractions import Fraction as Fr
pts = [(Fr(0),Fr(1)),(Fr(0),Fr(-1)),(Fr(1),Fr(8)),(Fr(1),Fr(-8)),
       (Fr(-1),Fr(8)),(Fr(-1),Fr(-8)),(Fr(7),Fr(440)),(Fr(7),Fr(-440)),
       (Fr(-7),Fr(440)),(Fr(-7),Fr(-440)),
       (Fr(1,7),Fr(440,343)),(Fr(1,7),Fr(-440,343)),
       (Fr(-1,7),Fr(440,343)),(Fr(-1,7),Fr(-440,343))]
for (x,y) in pts:
    assert y*y == f(x), (x,y)
print("14 affine known points on X_31 verified + 2 infinity pts = 16 total")
# twist assignment: d = squarefree part of g1(x) for rational x
def sqfree_part(n):
    # n>0 int (as numerator*denominator)
    assert n > 0
    d = 1
    p = 2
    import math
    m = n
    q = 2
    while q*q <= m:
        e = 0
        while m % q == 0:
            m //= q; e += 1
        if e % 2 == 1: d *= q
        q += 1 if q == 2 else 2
    if m > 1: d *= m
    return d
def twist_of(x):
    # g1(x) = X^2+1 value as Fraction; d = squarefree part of num*den
    v = x*x+1
    n, dd = v.numerator, v.denominator
    return sqfree_part(n*dd)
from collections import Counter
c = Counter()
for (x,y) in pts:
    d = twist_of(x)
    c[d]+=1
print("twist assignment of 14 affine pts:", dict(c))
assert set(c) <= {1,2}, c
print("RESULT: twists in {1,2,7,14}; pruned below; known pts only on {1,2}")

# --- Step 2: prune d=7,14 ---
# Lemma: X^2+Z^2 = d U^2 with coprime X,Z has no nonzero solutions for d=7,14.
# Proof: mod 7: squares are {0,1,2,4}. X^2+Z^2 = 0 mod 7 forces 7|X,Z:
sq = { (i*i) % 7 for i in range(7) }
sums = { (a+b) % 7 for a in sq for b in sq }
print("squares mod7:", sorted(sq), "pair sums:", sorted(sums))
assert 0 in sums
# check: X^2+Z^2=0 mod7 -> X=Z=0 mod7
bad = [(x,z) for x in range(7) for z in range(7) if (x*x+z*z)%7==0 and (x%7!=0 or z%7!=0)]
assert bad == [], bad
print("lemma: x^2+z^2=0 mod7 => 7|x and 7|z: VERIFIED by exhaustion")
# Descent: d=7: X^2+Z^2=7U^2, gcd(X,Z)=1. mod7: 7|X,Z contradiction (nonzero since U!=0... if X=Z=0 then U=0).
# d=14: X^2+Z^2=14U^2: mod7 -> 7|X,Z -> X=7X1,Z=7Z1 -> 49(X1^2+Z1^2)=14U^2 -> 7(X1^2+Z1^2)=2U^2 -> 7|U -> U=7U1 -> 7(X1^2+Z1^2)=98U1^2 -> X1^2+Z1^2=14U1^2, smaller -> infinite descent -> only (0,0,0).
# Conclude D_7(Q), D_14(Q) empty. (Full writeup in DRAFT.)
print("RESULT: D_7(Q) and D_14(Q) are EMPTY (mod-7 descent certificates)")

# --- Step 3 (deferred): explicit Weierstrass model of C_1 needs pole-cancellation
# (naive generators carry extra poles at infinity-); recorded as open step.
print("STEP3-DEFERRED")
