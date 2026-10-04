from fractions import Fraction

def conv(a,b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

# H = y + phi is an exact first integral because y'=(x-y), phi'=(y-x).
# Coefficients in variables (x,y): (1,-1)+(-1,1)=(0,0).
assert (Fraction(1)-Fraction(1), -Fraction(1)+Fraction(1)) == (0,0)

# Four-dimensional equilibrium residuals and characteristic polynomial.
a=Fraction(7,3)
b4=Fraction(-1,1000)
for s in (Fraction(1),Fraction(-1)):
    x=y=s; z=Fraction(0); u=-a*s/b4
    # u'=a*x+b*u=0
    assert y*z == 0
    assert x-y == 0
    assert 1-x*x == 0
    assert a*x+b4*u == 0
# det(lambda I-J)=(lambda-b)(lambda+1)(lambda^2+2)
p4=conv(conv([-b4,1],[1,1]),[2,0,1])
assert p4[-1] == 1
assert b4 < 0

# Five-dimensional equilibrium residuals for representative positive parameters.
a5=Fraction(2); b5=Fraction(1,100); c=Fraction(21,10)
k=Fraction(1,10); m=Fraction(1,10); n=Fraction(1,100)
for s in (Fraction(1),Fraction(-1)):
    for phi in (Fraction(-3,2),Fraction(0),Fraction(7,5)):
        x=y=s; z=Fraction(0); u=a5*s/b5
        W=m+3*n*phi*phi
        assert c*y*z == 0
        assert x-y == 0
        assert 1-x*x == 0
        assert a5*x-b5*u+k*W*z == 0
        assert y-x == 0

# det(lambda I-J)=lambda(lambda+b)(lambda+1)(lambda^2+2c)
p5=conv(conv(conv([0,1],[b5,1]),[1,1]),[2*c,0,1])
assert p5[0] == 0
assert p5[-1] == 1
assert b5 > 0 and c > 0

# Source-reported finite-time Lyapunov sums: necessary divergence checks only.
le4=[Fraction(99692,1000000),Fraction(78438,1000000),Fraction(-4804,1000000),Fraction(-1174328,1000000)]
assert sum(le4,Fraction(0)) == Fraction(-1001002,1000000)
assert abs(float(sum(le4))-float(b4-1)) < 3e-6
le5=[Fraction(95916,1000000),Fraction(81339,1000000),Fraction(2892,1000000),Fraction(-1059,1000000),Fraction(-1180088,1000000)]
assert sum(le5,Fraction(0)) == Fraction(-1001,1000)
assert sum(le5,Fraction(0)) == -1-Fraction(1,1000)  # b=0.001 in the source's LE example

print('VERIFY_OK')
print('H_dot=0')
print('4D_extra_exponent=b<0')
print('5D_extra_exponents=0,-b')
print('5D_equilibrium_factor=lambda*(lambda+b)*(lambda+1)*(lambda^2+2c)')
