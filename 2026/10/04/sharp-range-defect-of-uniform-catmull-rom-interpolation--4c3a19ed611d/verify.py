from fractions import Fraction as F

# Polynomials are coefficient lists in ascending powers of t.
def add(a,b):
    n=max(len(a),len(b))
    return [(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(n)]

def scale(a,c):
    return [c*x for x in a]

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def deriv(a):
    return [F(i)*a[i] for i in range(1,len(a))] or [F(0)]

def val(a,x):
    s=F(0)
    p=F(1)
    for c in a:
        s+=c*p
        p*=x
    return s

one=[F(1)]
t=[F(0),F(1)]
one_minus_t=[F(1),F(-1)]

# Hermite basis.
h00=[F(1),F(0),F(-3),F(2)]
h10=[F(0),F(1),F(-2),F(1)]
h01=[F(0),F(0),F(3),F(-2)]
h11=[F(0),F(0),F(-1),F(1)]

# Check algebra at several exact sigma values, including both endpoints.
for s in [F(0),F(1,10),F(1,4),F(2,5),F(1,2)]:
    # Increment coefficients derived from
    # y0=a, y1=a+d0, y2=a+d0+d1, y3=a+d0+d1+d2.
    # m1=s(d0+d1), m2=s(d1+d2).
    q0 = add(h00, h01)
    q0 = add(q0, scale(h10,s))
    q1 = add(h01, scale(h10,s))
    q1 = add(q1, scale(h11,s))
    q2 = scale(h11,s)

    q0_expected = add(one, scale(mul(t,mul(one_minus_t,one_minus_t)),s))
    q1_expected = mul(t, add([s], scale(mul(t,[F(3),F(-2)]), F(1)-s)))
    q2_expected = scale(mul(mul(t,t),one_minus_t),-s)

    assert q0 == q0_expected
    assert q1 == q1_expected
    assert q2 == q2_expected

    one_minus_q1 = add(one, scale(q1,-1))
    factor = mul(one_minus_t, add(one, scale(mul(t,[F(1),F(-2)]),F(1)-s)))
    assert one_minus_q1 == factor

# Exact continuous extrema of the two cubic shape factors.
left_shape = mul(mul(t,t),one_minus_t)          # t^2(1-t)
right_shape = mul(t,mul(one_minus_t,one_minus_t)) # t(1-t)^2
assert deriv(left_shape) == [F(0),F(2),F(-3)]
assert deriv(right_shape) == [F(1),F(-4),F(3)]
assert val(left_shape,F(2,3)) == F(4,27)
assert val(right_shape,F(1,3)) == F(4,27)
assert val(left_shape,F(0)) == val(left_shape,F(1)) == 0
assert val(right_shape,F(0)) == val(right_shape,F(1)) == 0

# Standard uniform Catmull-Rom sigma=1/2.
s=F(1,2)
assert -s*F(4,27) == -F(2,27)
assert F(1)+s*F(4,27) == F(29,27)

# Strictly increasing witness:
# (eps,2eps,3eps,1) at t=2/3.
# Verify at several rational eps and the closed formula.
for s in [F(1,10),F(1,4),F(1,2)]:
    x=F(2,3)
    q0=F(1)+s*x*(F(1)-x)**2
    q1=x*(s+(F(1)-s)*x*(F(3)-2*x))
    q2=-s*x*x*(F(1)-x)
    # a=eps, d0=eps, d1=eps, d2=1-3eps
    for eps in [F(1,1000),F(1,100),F(1,50)]:
        direct=eps+q0*eps+q1*eps+q2*(F(1)-3*eps)
        closed=F(2,27)*((6*s+37)*eps-2*s)
        assert direct == closed

# Standard sigma=1/2: every eps<1/40 makes the witness negative.
s=F(1,2)
eps=F(1,50)
closed=F(2,27)*((6*s+37)*eps-2*s)
assert closed < 0
assert F(0) < eps < F(1,3)

print("VERIFY_OK")
