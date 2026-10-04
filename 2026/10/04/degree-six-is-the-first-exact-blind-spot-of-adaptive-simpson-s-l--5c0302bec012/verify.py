from fractions import Fraction as F

nodes1 = [F(-1), F(0), F(1)]
weights1 = [F(1,3), F(4,3), F(1,3)]
nodes2 = [F(-1), F(-1,2), F(0), F(1,2), F(1)]
weights2 = [F(1,6), F(2,3), F(1,3), F(2,3), F(1,6)]

def s1_monomial(n):
    return sum(w*x**n for w,x in zip(weights1,nodes1))

def s2_monomial(n):
    return sum(w*x**n for w,x in zip(weights2,nodes2))

def integral_monomial(n):
    return F(0) if n % 2 else F(2,n+1)

vals = {}
for n in range(7):
    s1 = s1_monomial(n)
    s2 = s2_monomial(n)
    exact = integral_monomial(n)
    vals[n] = (s1,s2,exact)
    if n <= 3:
        assert s1 == exact == s2

assert vals[4] == (F(2,3), F(5,12), F(2,5))
assert vals[6] == (F(2,3), F(17,48), F(2,7))
assert vals[4][1] - vals[4][0] == -F(1,4)
assert vals[6][1] - vals[6][0] == -F(5,16)
assert vals[4][2] - vals[4][1] == -F(1,60)
assert vals[6][2] - vals[6][1] == -F(23,336)

# Symbolic coefficient identities represented by independent rational substitutions.
tests = [
    [F(3),F(-2),F(5),F(7),F(11),F(-13),F(17)],
    [F(0),F(1),F(0),F(-4),F(-5),F(9),F(4)],
    [F(2),F(0),F(-3),F(0),F(5,2),F(0),F(-2)],
]
for a in tests:
    S1 = sum(a[n]*vals[n][0] for n in range(7))
    S2 = sum(a[n]*vals[n][1] for n in range(7))
    I = sum(a[n]*vals[n][2] for n in range(7))
    assert S2-S1 == -a[4]*F(1,4)-a[6]*F(5,16)
    if 4*a[4]+5*a[6] == 0:
        assert I-S2 == -a[6]*F(1,21)

# Degree <= 5: D=0 forces a4=0, hence exactness.
for a4 in [F(-3),F(-1),F(0),F(2),F(7,5)]:
    D = -a4*F(1,4)
    if D == 0:
        assert a4 == 0
        assert -a4*F(1,60) == 0

# Strictly positive degree-six witness.
a = [F(1,84),F(0),F(0),F(0),F(5,4),F(0),F(-1)]
S1 = sum(a[n]*vals[n][0] for n in range(7))
S2 = sum(a[n]*vals[n][1] for n in range(7))
I = sum(a[n]*vals[n][2] for n in range(7))
assert S1 == S2 == F(4,21)
assert I == F(5,21)
assert I-S2 == F(1,21)
assert (I-S2)/I == F(1,5)
# p(t)=t^4(5/4-t^2)+1/84 >= 1/84 since 0<=t^2<=1.

# Affine scaling on rational intervals.
for left,right in [(F(0),F(2)),(F(-3),F(5)),(F(2,7),F(19,7))]:
    L = right-left
    a6 = F(-1)
    normalized_error = -a6*F(1,21)
    physical_error = L*F(1,2)*normalized_error
    assert physical_error == -L*a6*F(1,42)

print("VERIFY_OK")
