from fractions import Fraction as F

def cross(P,Q):
    return P[0]*Q[1]-P[1]*Q[0]

def centroid(poly):
    S=sum(cross(poly[i],poly[(i+1)%4]) for i in range(4))
    assert S != 0
    nx=sum((poly[i][0]+poly[(i+1)%4][0])*cross(poly[i],poly[(i+1)%4]) for i in range(4))
    ny=sum((poly[i][1]+poly[(i+1)%4][1])*cross(poly[i],poly[(i+1)%4]) for i in range(4))
    return nx/(3*S), ny/(3*S)

def test_centroid(alpha,beta,gamma,delta,t,s):
    A=(alpha,F(0)); B=(beta*t,beta*s); C=(-gamma,F(0)); D=(-delta*t,-delta*s)
    G=centroid([A,B,C,D])
    p=alpha-gamma; q=beta-delta
    expected=((p+q*t)/3,q*s/3)
    assert G==expected, (G,expected)

# Exact rational unit directions.
test_centroid(F(5),F(7),F(2),F(3),F(3,5),F(4,5))
test_centroid(F(11),F(5),F(4),F(2),F(5,13),F(12,13))
test_centroid(F(2),F(9),F(1),F(6),F(-3,5),F(4,5))

# Coincidence equations are p=2qt and q=2pt; their determinant is 1-4t^2.
for t in [F(0),F(1,3),F(1,2),F(-1,2),F(3,5)]:
    det=1-4*t*t
    assert det == F(1)-F(4)*t*t

# Parallelogram branch.
p=q=F(0); t=F(2,5)
assert p==2*q*t and q==2*p*t

# Explicit non-parallelogram branch: alpha=beta=2, gamma=delta=1, cos(theta)=1/2.
alpha=beta=F(2); gamma=delta=F(1); t=F(1,2)
p=alpha-gamma; q=beta-delta
assert p != 0 and q != 0
assert p==2*q*t and q==2*p*t
# Squared side lengths use only cos(theta), so remain exact without adjoining sqrt(3).
AB2=alpha*alpha+beta*beta-2*alpha*beta*t
BC2=beta*beta+gamma*gamma+2*beta*gamma*t
CD2=gamma*gamma+delta*delta-2*gamma*delta*t
DA2=delta*delta+alpha*alpha+2*delta*alpha*t
assert (AB2,BC2,CD2,DA2)==(F(4),F(7),F(1),F(7))
assert len({AB2,BC2,CD2,DA2})>1
print('VERIFY_OK')
