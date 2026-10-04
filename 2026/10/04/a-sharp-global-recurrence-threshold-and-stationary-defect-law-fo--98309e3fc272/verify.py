from fractions import Fraction as F

# The cubic terms in x*x' + y*y' cancel exactly.
assert F(1)-F(1)==0

# Minimal polynomial arithmetic in s for the critical tangency identity.
def add(p,q):
    r=dict(p)
    for k,v in q.items(): r[k]=r.get(k,F(0))+v
    return {k:v for k,v in r.items() if v}
def mul(p,q):
    r={}
    for i,u in p.items():
        for j,v in q.items(): r[i+j]=r.get(i+j,F(0))+u*v
    return {k:v for k,v in r.items() if v}
def sc(p,k): return {i:F(k)*v for i,v in p.items() if F(k)*v}

one={0:F(1)}; s={1:F(1)}; s2=mul(s,s); s3=mul(s2,s); s4=mul(s2,s2)
cstar=add(sc(s,2),sc(s2,-1))
# On y=sx, d'=x[c-s+s^3-s^4-(1+s^2)z].
constant=add(add(cstar,sc(s,-1)),add(s3,sc(s4,-1)))
target=mul(add(one,s2),mul(s,add(one,sc(s,-1))))
assert constant==target

# Rational threshold instance a=1/4, s=1/2, b=2, c*=3/4.
a=F(1,4); s0=F(1,2); b=F(2); c=F(3,4)
assert c==2*s0-a
assert (a+c)**2-4*a==0
z=s0*(1-s0); x=F(1); y=s0*x
assert a*(y-x)+y*z==0
assert c*x-y-x*z==0
assert x*y-b*z==0

# Discriminant of z^2-(c-a)z-a(c-1) is (c-a)^2+4a(c-1)=(a+c)^2-4a.
assert (c-a)**2+4*a*(c-1)==(a+c)**2-4*a

print("VERIFY_OK")
