from fractions import Fraction as F

# Parameterize r = 1-q^2 so every identity remains rational.
for a,u,q in [
    (F(3,2),F(5,3),F(1,2)),
    (F(7,3),F(4,5),F(2,3)),
    (F(5),F(3,2),F(3,4)),
]:
    G=a*u*u/2
    r=1-q*q
    Delta=r*G
    ystar=u*q
    dstar=u-ystar
    S=dstar/Delta
    assert S == 2/(a*u*(1+q))

    # Exact W threshold: equality holds at the optimal tangent.
    mu=a*(1+q)/(1-q)
    assert S*S == 2/(mu*Delta)

    # The exact envelope loss is a square for representative positive slopes.
    for mult in [F(1,2),F(3,4),F(5,4),F(3,2)]:
        y=ystar*mult
        d=u-y/2-ystar*ystar/(2*y)
        assert dstar-d == (y-ystar)*(y-ystar)/(2*y)
        assert d <= dstar
        if y != ystar:
            assert d < dstar

# Exact-gap boundary: finite tangent slopes approach but never attain the supremum.
a=F(3,2)
u=F(5,3)
G=a*u*u/2
Ssup=2/(a*u)
for n in [2,4,8,16,64]:
    y=u/F(n)
    d=u-y/2
    s=d/G
    assert s < Ssup
# At the true modulus, the W threshold equals the unattained supremum.
assert Ssup*Ssup == 2/(a*G)
# With a strictly larger trial modulus, a finite tangent does certify.
mu=2*a
y=u/F(4)
d=u-y/2
s=d/G
assert s*s >= 2/(mu*G)

# For Delta>G, the constant zero minorant never reaches the negative target;
# by the source convention its descent distance and slowness are +infinity.
Delta=F(6,5)*G
assert G-Delta < 0

print('VERIFY_OK')
