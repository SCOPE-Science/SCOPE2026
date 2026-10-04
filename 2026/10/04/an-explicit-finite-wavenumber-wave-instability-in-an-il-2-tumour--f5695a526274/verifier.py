from fractions import Fraction as F

ru=F(173,250); mu=F(167,1000); gv=F(1,10); rw=F(5,2)
gw=F(6,1); mw=F(11,1000); alpha=F(27,250); sigw=F(1,25000)
du=F(543,1); dw=F(7,125); v=F(1,500); k2=F(1,4000)
u=(gv+v)*(1-v)
w=(sigw+rw*u*v/(gw+v))/mw
sigu=mu*u-alpha*v-ru*u*w/(1+w)

# Exact equilibrium residuals.
r1=alpha*v-mu*u+ru*u*w/(1+w)+sigu
r2=v*(1-v)-u*v/(gv+v)
r3=rw*u*v/(gw+v)-mw*w+sigw
assert r1 == r2 == r3 == 0
assert u>0 and v>0 and w>0 and sigu>0

j11=ru*w/(1+w)-mu
j12=alpha
j13=ru*u/(1+w)**2
j21=-v/(gv+v)
j22=u*v/(gv+v)**2-u/(gv+v)-2*v+1
j31=rw*v/(gw+v)
j32=rw*u*gw/(gw+v)**2
j33=-mw

def coeffs(s):
    a2=(du+1+dw)*s-(j11+j22+j33)
    a1=(du+du*dw+dw)*s*s-(du*(j22+j33)+(j11+j33)+dw*(j11+j22))*s + (j11*j22+j11*j33+j22*j33-j12*j21-j13*j31)
    a0=du*dw*s**3-(du*j33+du*dw*j22+dw*j11)*s*s + (du*j22*j33+j11*j33+dw*j11*j22-j13*j31-dw*j12*j21)*s + (-j11*j22*j33+j12*j21*j33-j13*j21*j32+j13*j22*j31)
    return a2,a1,a0,a2*a1-a0

c0=coeffs(F(0))
ck=coeffs(k2)
assert all(x>0 for x in c0)
assert ck[0]>0 and ck[1]>0 and ck[2]>0 and ck[3]<0
print('u0 =',u)
print('w0 =',w)
print('sigma_u =',sigu)
print('k=0: a2,a1,a0,H =',*c0)
print('k^2=1/4000: a2,a1,a0,H =',*ck)
print('VERIFY_OK')
