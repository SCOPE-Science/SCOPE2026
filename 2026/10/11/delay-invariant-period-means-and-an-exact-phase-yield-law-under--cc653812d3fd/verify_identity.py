from fractions import Fraction as F

# Check the two rational identities at many exact rational points after direct evaluation.
def inv(x,m):
    return F(1,1)/(F(1,1)+m*x)

def check_identity(x,c,m):
    lhs=inv(x,m)
    rhs=inv(c,m)-m*(x-c)/(F(1,1)+m*c)**2 + m*m*(x-c)**2/((F(1,1)+m*c)**2*(F(1,1)+m*x))
    assert lhs==rhs
    lhs2=(x-c)/(F(1,1)+m*x)
    rhs2=(x-c)/(F(1,1)+m*c)-m*(x-c)**2/((F(1,1)+m*c)*(F(1,1)+m*x))
    assert lhs2==rhs2

for x in [F(1,7),F(2,3),F(5,1),F(19,4)]:
    for c in [F(1,5),F(5,1),F(7,3)]:
        for m in [F(1,2),F(3,2),F(5,3)]:
            check_identity(x,c,m)

r=F(6,5); K=F(45); a=F(5,4); m=F(3,2); alpha=F(1,5); beta=F(1,25); d=F(1,5)
u_star=d/beta
v_star=(r*(1-u_star/K)-a/(1+m*u_star))/alpha
assert u_star==F(5)
assert v_star==F(469,102)
assert r/K==F(2,75)
assert a*m/(1+m*u_star)==F(15,68)
assert alpha*(1+m*u_star)/m==F(17,15)
assert a*m*m/(alpha*(1+m*u_star)**2)==F(225,1156)
# Eliminating Q between the two identities must match.
assert F(15,68) == F(17,15)*F(225,1156)
print('VERIFY_OK')
