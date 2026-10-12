from fractions import Fraction as F
from math import pi, gcd

def delta(q):
    return min(F(1,20), q/F(12), (1-q)/F(12))

# A deterministic enumeration of reduced rationals in (0,1).
rats=[]
for den in range(2,26):
    for num in range(1,den):
        if gcd(num,den)==1:
            rats.append(F(num,den))

# Calibration: the source bounds r(1)<6 delta and r(0)>1-6 delta
# leave every target q strictly inside the realizable ratio interval.
for q in rats:
    d=delta(q)
    assert d > 0
    assert d <= F(1,20)
    assert 6*d < q
    assert q < 1-6*d

# Scaling b=1/d turns a source Hessian bound K/d^2 into the uniform K,
# while the orbit gradient norm becomes d and stays strictly positive.
for q in rats:
    d=delta(q)
    b=1/d
    hessian_factor=(1/(b*b))*(1/(d*d))
    gradient_factor=1/b
    assert hessian_factor == 1
    assert gradient_factor == d > 0

# A safe transverse half-width after scaling.  Recursive translations make
# the containing strips pairwise disjoint with a unit gap and locally finite.
W=[float((1/d)*(F(2)*d))+pi/(3*float(d)) for d in map(delta,rats[:40])]
L=[0.0]
for j in range(len(W)-1):
    L.append(L[-1]+W[j]+W[j+1]+1.0)
for j in range(len(W)-1):
    assert L[j]+W[j]+1.0 <= L[j+1]-W[j+1] + 1e-12
left=[L[j]-W[j] for j in range(len(W))]
assert all(left[j+1] > left[j] for j in range(len(left)-1))

# Dense-rational coverage illustrated exactly on representative line-search
# intervals: choose a rational midpoint, which lies strictly inside.
pairs=[
    (F(1,10),F(9,10)),
    (F(1,1000),F(1,100)),
    (F(49,100),F(51,100)),
    (F(99,100),F(999,1000)),
]
for c1,c2 in pairs:
    q=(c1+c2)/2
    assert c1 < q < c2

# No fixed normalized decrease ratio R can satisfy Goldstein for every pair.
# The following witness construction excludes each representative R.
def excluding_pair(R):
    R=F(R)
    if R <= 0:
        return F(1,4), F(1,2)
    if R >= 1:
        return F(1,4), F(1,2)
    if R <= F(1,2):
        return (R+1)/2, (R+3)/4   # both strictly above R and below 1
    return R/4, R/2               # both strictly below R and above 0

for R in [F(-1),F(0),F(1,10),F(1,2),F(9,10),F(1),F(2)]:
    c1,c2=excluding_pair(R)
    assert 0 < c1 < c2 < 1
    assert not (c1 <= R <= c2)

print("VERIFY_OK")
