from fractions import Fraction as F

def cm(points, probs):
    m=sum(p*x for x,p in zip(points,probs))
    z=[x-m for x in points]
    m2=sum(p*t*t for t,p in zip(z,probs))
    m3=sum(p*t*t*t for t,p in zip(z,probs))
    m4=sum(p*t*t*t*t for t,p in zip(z,probs))
    return m,m2,m3,m4

a,b=F(-1),F(2); q,p=F(3,5),F(2,5)
m,v,c,m4=cm([a,b],[q,p])
assert v*m4-c*c-v**3==0
d2=(c/v)**2+4*v
assert d2==(b-a)**2
d=F(3)
assert m+((c/v)-d)/2==a
assert m+((c/v)+d)/2==b
assert (1-c/(v*d))/2==p

m3p,v3,c3,m43=cm([F(-1),F(0),F(2)],[F(1,4),F(1,2),F(1,4)])
assert v3*m43-c3*c3-v3**3>0

sigma2=F(1); sp=F(0); spp=F(0); sppp=F(-6)
u=1+sigma2*sp
expr=sigma2*sigma2*u*sppp-sigma2**3*spp*spp+2*u**3
assert u>0 and expr==F(-4)<0
print('VERIFY_OK')
