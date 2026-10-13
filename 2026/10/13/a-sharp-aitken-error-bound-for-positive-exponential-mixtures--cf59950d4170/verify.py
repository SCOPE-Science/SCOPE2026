from fractions import Fraction as F

def aitken(vals):
    x0,x1,x2=vals
    d1=x1-x0
    d2=x2-2*x1+x0
    assert d2 != 0
    return x0-d1*d1/d2

def check(lams, coeffs, n):
    e=sum(c*l**n for c,l in zip(coeffs,lams))
    vals=[sum(c*l**(n+k) for c,l in zip(coeffs,lams)) for k in range(3)]
    ah=aitken(vals)
    cur=[c*l**n for c,l in zip(coeffs,lams)]
    weights=[v/e for v in cur if v != 0]
    aa=[1-l for v,l in zip(cur,lams) if v != 0]
    Ea=sum(w*a for w,a in zip(weights,aa))
    Ea2=sum(w*a*a for w,a in zip(weights,aa))
    ratio=ah/e
    assert ratio == 1-Ea*Ea/Ea2
    assert ratio >= 0
    return ratio

tests=[
([F(1,4),F(3,4)],[F(1),F(3)],0),
([F(1,3),F(1,2),F(4,5)],[F(2),F(5),F(7)],2),
([F(1,5),F(2,5),F(3,5),F(4,5)],[F(1),F(2),F(3),F(4)],1)]
for lams,coeffs,n in tests:
    ratio=check(lams,coeffs,n)
    lm,lp=min(lams),max(lams)
    bound=((lp-lm)/(F(2)-lp-lm))**2
    assert ratio <= bound

lams=[F(1,4),F(3,4)]
coeffs=[F(1),F(3)]
vals=[sum(c*l**k for c,l in zip(coeffs,lams)) for k in range(3)]
assert vals == [F(4),F(5,2),F(7,4)]
ah=aitken(vals)
assert ah == F(1)
assert ah/vals[0] == F(1,4)
bound=((F(3,4)-F(1,4))/(F(2)-F(3,4)-F(1,4)))**2
assert bound == F(1,4)

for q in [F(1,10),F(1,2),F(9,10)]:
    assert (q/(2-q))**2 < q*q

print("VERIFY_OK")
