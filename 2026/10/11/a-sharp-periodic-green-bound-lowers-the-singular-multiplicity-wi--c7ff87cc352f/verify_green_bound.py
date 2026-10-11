from fractions import Fraction as F

# Dimensionless Green kernel: G(pi*u)/pi on u in [0,2].
def g(u):
    return -F(1,6) + u/F(2) - u*u/F(4)

# For d=pi*a, 0<=a<=1, the difference H_d(s)=G(s)-G(s-d mod 2pi)
# has the exact branch formulas below after division by pi.
def h_direct(u,a):
    v = u-a
    if v < 0:
        v += 2
    return g(u)-g(v)

def h_formula(u,a):
    if u < a:
        return (2-a)*(2*u-a)/4
    return a*(2+a-2*u)/4

for den in range(1,41):
    for ia in range(den+1):
        a=F(ia,den)
        A=a*(2-a)/4
        assert A <= F(1,4)
        assert F(1,4)-A == (1-a)*(1-a)/4
        for iu in range(2*den+1):
            u=F(iu,den)
            assert h_direct(u,a)==h_formula(u,a)
            assert -A <= h_formula(u,a) <= A
print('VERIFY_OK')
