from fractions import Fraction as F

def moments(a1,a2,b1,b2,c1,c2):
    D=a1*c2+a2*c1
    assert D != 0 and b1 != 0
    X=a1*b2/(b1*D)
    Y=a2/D
    Z=a1/D
    assert a1*Y-a2*Z == 0
    assert b1*X-b2*Z == 0
    assert c1*Y+c2*Z == 1
    return X,Y,Z

# Nominal published parameters.
assert moments(F(1),F(1),F(2),F(1),F(3),F(1)) == (F(1,8),F(1,4),F(1,4))

# Published multistable setting: c1=2.6=13/5, others as above.
assert moments(F(1),F(1),F(2),F(1),F(13,5),F(1)) == (F(5,36),F(5,18),F(5,18))

# Equilibrium-coordinate squares from the source formulas equal the same moments.
a1,a2,b1,b2,c1,c2=F(7,5),F(9,8),F(11,6),F(5,4),F(13,7),F(4,3)
D=a1*c2+a2*c1
xeq2=a1*b2/(b1*D)
yeq2=a2/D
zeq2=a1/D
assert moments(a1,a2,b1,b2,c1,c2) == (xeq2,yeq2,zeq2)
print('VERIFY_OK')
