from fractions import Fraction as F

# Reproducible exact-arithmetic witness for a direct trapezoidal Lyapunov step.
x=F(1,4)
y=F(4,5)
r=1-x
ell=1-y
z=(2-x-y)/(2+x+y)
k=z*z*(1+x)*(1+y)
E=k-r*ell
assert r==F(3,4) and ell==F(1,5) and z==F(19,61)
assert k==F(3249,14884)
assert E==F(2541,37210)
assert E==2*(x-y)**2*(x+y)/(2+x+y)**2
sqrt_k=F(57,122)
assert sqrt_k*sqrt_k==k
sstar=E/(r+ell+2*sqrt_k)
tstar=F(1,2)-sstar*(r-ell)/(2*E)
assert sstar==F(42,1159)
assert tstar==F(74,209)
assert 0<tstar<1

def Fdet(s,t):
    return s*s+s*(r*t+ell*(1-t))-E*t*(1-t)

assert Fdet(sstar,tstar)==0
assert Fdet(F(1,100),tstar)<0
assert Fdet(F(0),F(1,2))==-E/4

# At zero diffusion the equal-weight rank-one covariance is rational.
p11=r*F(1,2)/(1+x)
p22=ell*F(1,2)/(1+y)
p12=z*F(1,2)
assert (p11,p22,p12)==(F(3,10),F(1,18),F(19,122))
det=p11*p22-p12*p12
assert det==F(-847,111630)
assert det<0

# Independent exact checks of the structural identity on other stable rates.
for xx,yy in [(F(1,6),F(1,2)),(F(1,3),F(3,4)),(F(2,5),F(2,5))]:
    zz=(2-xx-yy)/(2+xx+yy)
    kk=zz*zz*(1+xx)*(1+yy)
    ee=kk-(1-xx)*(1-yy)
    rhs=2*(xx-yy)**2*(xx+yy)/(2+xx+yy)**2
    assert ee==rhs

print('VERIFY_OK')
print('sharp_scaled_noise',sstar)
print('critical_squared_weight',tstar)
print('zero_noise_determinant',det)
