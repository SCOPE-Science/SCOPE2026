from fractions import Fraction
from decimal import Decimal, getcontext


def N(t, a, b):
    a = abs(a); b = abs(b)
    return max(a, b, (a+b)/(1+t))


def objective(t, c, d):
    assert N(t,c,d) == 1
    return min(N(t,1+c,d), N(t,c,1+d))


def formula(t):
    return max((Fraction(3)+t)/2, (Fraction(2)+t)/(1+t))

count=0
# Parameters with varied denominators, including endpoints and values around sqrt(2)-1.
params={Fraction(0),Fraction(1)}
for q in range(2,31):
    for p in range(q+1):
        params.add(Fraction(p,q))

for t in sorted(params):
    target=formula(t)
    diag=(1+t)/2
    assert N(t,diag,diag)==1
    assert objective(t,diag,diag)==target
    count += 1

    # vertical and horizontal boundary segments
    for k in range(41):
        lam=Fraction(k,40)
        d=t*lam
        c=t*lam
        assert objective(t,Fraction(1),d) <= target
        assert objective(t,c,Fraction(1)) <= target
        count += 2

    # diagonal cut segment c+d=1+t, from (1,t) to (t,1)
    for k in range(81):
        lam=Fraction(k,80)
        c=t + (1-t)*lam
        d=1+t-c
        assert N(t,c,d)==1
        assert objective(t,c,d) <= target
        count += 1

assert formula(Fraction(0)) == 2
assert formula(Fraction(1)) == 2

# Exact branch comparison is controlled by t^2+2t-1.
for t in sorted(params):
    g=(Fraction(3)+t)/2
    h=(Fraction(2)+t)/(1+t)
    poly=t*t+2*t-1
    if poly < 0:
        assert h > g
    elif poly > 0:
        assert g > h
    else:
        assert g == h

getcontext().prec=50
root=Decimal(2).sqrt()-Decimal(1)
minimum=Decimal(1)+Decimal(1)/Decimal(2).sqrt()
# Numerical identity only for the irrational closed form, after exact rational checks above.
g=(Decimal(3)+root)/Decimal(2)
h=(Decimal(2)+root)/(Decimal(1)+root)
assert abs(g-minimum) < Decimal('1e-45')
assert abs(h-minimum) < Decimal('1e-45')
print(f"VERIFY_OK samples={count} rational_parameters={len(params)}")
