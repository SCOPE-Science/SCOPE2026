from fractions import Fraction as F

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def sd_step(lam,b,x):
    r=[bi-li*xi for bi,li,xi in zip(b,lam,x)]
    if all(ri==0 for ri in r):
        return x,r,None
    alpha=dot(r,r)/sum(li*ri*ri for li,ri in zip(lam,r))
    xn=[xi+alpha*ri for xi,ri in zip(x,r)]
    return xn,r,alpha

lam=[F(1),F(2),F(4)]
b=[F(1),F(1),F(1,10)]
x=[F(0),F(0),F(0)]
x1,r0,a0=sd_step(lam,b,x)
x2,r1,a1=sd_step(lam,b,x1)
assert a0 == F(201,304)
assert r1 == [F(103,304),F(-49,152),F(-25,152)]
assert a1 == F(22713,39817)
assert x2 == [F(646416,756523),F(5777343,12104368),F(-3353283,121043680)]
assert x2[2] < 0
assert all(b[i]/lam[i] > 0 for i in range(3))

a,c=F(2),F(7)
b2=[F(3),F(5)]
lam2=[a,c]
x=[F(0),F(0)]
x1,r0,aa0=sd_step(lam2,b2,x)
x2,r1,aa1=sd_step(lam2,b2,x1)
x3,r2,aa2=sd_step(lam2,b2,x2)
u,v=r0
gamma=((c-a)**2*u*u*v*v)/((a*u*u+c*v*v)*(a*v*v+c*u*u))
assert F(0) <= gamma < F(1)
assert r2 == [gamma*r0[0],gamma*r0[1]]
assert aa2 == aa0
assert all(t>=0 for t in x1+x2+x3)

x=[F(0),F(0)]
for _ in range(12):
    x,_,_=sd_step(lam2,b2,x)
    assert all(t>=0 for t in x)

print("VERIFY_OK")
