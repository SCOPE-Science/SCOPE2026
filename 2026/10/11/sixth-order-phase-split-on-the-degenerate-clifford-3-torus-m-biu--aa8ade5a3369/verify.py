import sympy as sp

u0,u1,u2=sp.symbols("u0 u1 u2", real=True)
g0,g1,g2=sp.symbols("g0 g1 g2", real=True)
u=[u0,u1,u2]
g=[g0,g1,g2]

s=(u0*g0+u1*g1+u2*g2)/sp.sqrt(3)
V=sum(u[i]**2*(1-g[i]**2) for i in range(3))
P=sp.expand(V+s**2)

def cos_moment(k):
    if k%2:
        return sp.Integer(0)
    return sp.binomial(k,k//2)/sp.Integer(4)**(k//2)

def average(expr):
    poly=sp.Poly(sp.expand(expr),g0,g1,g2)
    out=0
    for exponents,coef in poly.terms():
        term=coef
        for e in exponents:
            term*=cos_moment(e)
        out+=term
    return sp.factor(out)

a=sp.Rational(3,2)
coeff={}
for power in (2,4,6,8):
    expr=0
    for j in range(power//2+1):
        k=power-2*j
        left=sp.binomial(a,j)*(-1)**j*P**j
        right=(-1)**k*sp.rf(3,k)/sp.factorial(k)*s**k
        expr+=left*right
    coeff[power]=sp.factor(average(expr))

w0,w1,w2=sp.symbols("w0 w1 w2", real=True)

def even_to_w(expr):
    poly=sp.Poly(sp.expand(expr),u0,u1,u2)
    out=0
    for exponents,coef in poly.terms():
        assert all(e%2==0 for e in exponents)
        out += coef*w0**(exponents[0]//2)*w1**(exponents[1]//2)*w2**(exponents[2]//2)
    return sp.expand(out)

assert coeff[2]==0
S2=w0**2+w1**2+w2**2
Pi=w0*w1*w2
for power,target in (
    (4,(2*S2-1)/16),
    (6,(105*S2-41-690*Pi)/1728),
    (8,(-382+1440*S2-555*S2**2-11400*Pi)/27648),
):
    actual=even_to_w(coeff[power])
    # Unit direction means w0+w1+w2=1.
    check=sp.factor((actual-target).subs(w2,1-w0-w1))
    assert check==0

c6_boundary=sp.simplify((sp.Rational(105,2)-41-690*Pi)/1728)
assert c6_boundary==(23-1380*Pi)/3456
c8_boundary=sp.simplify((-382+1440*sp.Rational(1,2)-555*sp.Rational(1,4)-11400*sp.Rational(1,60))/27648)
assert c8_boundary==sp.Rational(37,110592)

# Feasible product endpoints on the quartic boundary.
for weights,product in [
    ((sp.Rational(1,2),sp.Rational(1,2),0),sp.Rational(0)),
    ((sp.Rational(2,3),sp.Rational(1,6),sp.Rational(1,6)),sp.Rational(1,54)),
]:
    assert sum(weights)==1
    assert sum(x*x for x in weights)==sp.Rational(1,2)
    assert sp.prod(weights)==product

z=sp.symbols("z")
poly=z**3-z**2+sp.Rational(1,4)*z-sp.Rational(1,60)
assert sp.discriminant(poly,z)==sp.Rational(1,1200)
intervals=[(sp.Rational(1,10),sp.Rational(1,9)),(sp.Rational(1,5),sp.Rational(1,4)),(sp.Rational(13,20),sp.Rational(2,3))]
for lo,hi in intervals:
    assert sp.sign(poly.subs(z,lo))*sp.sign(poly.subs(z,hi))==-1

print("VERIFY_OK")
print("even_quadratic_coefficient=0")
print("quartic_coefficient=true")
print("sixth_order_phase_boundary=1/60")
print("secondary_eighth_coefficient=37/110592")
print("feasible_product_range_endpoints=true")
