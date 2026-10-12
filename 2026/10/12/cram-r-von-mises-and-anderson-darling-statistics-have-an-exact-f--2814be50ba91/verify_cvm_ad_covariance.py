#!/usr/bin/env python3
import mpmath as mp
mp.mp.dps = 60

qW=lambda u: u*u-u+mp.mpf(1)/3
qA=lambda u: -1-mp.log(u*(1-u))
K=lambda s,t: min(s,t)-s*t

EW=mp.quad(qW,[0,1])
EA=mp.quad(qA,[0,1])
VW=mp.quad(lambda u:(qW(u)-EW)**2,[0,1])
VA=mp.quad(lambda u:(qA(u)-EA)**2,[0,0.5,1])
C=mp.quad(lambda u:(qW(u)-EW)*(qA(u)-EA),[0,0.5,1])

# Integrate over s<t and double by symmetry.
Iww=2*mp.quad(lambda t: mp.quad(lambda s:(s*(1-t))**2,[0,t]),[0,1])
Iwa=2*mp.quad(lambda t: mp.quad(lambda s:(s*(1-t))**2/(t*(1-t)),[0,t]),[0,1])
Iaa=2*mp.quad(lambda t: mp.quad(lambda s:(s*(1-t))**2/(s*(1-s)*t*(1-t)),[0,t]),[0,0.5,1])

def close(x,y,tol=mp.mpf("1e-40")):
    assert abs(x-y) <= tol*max(1,abs(x),abs(y)), (x,y)

close(EW,mp.mpf(1)/6)
close(EA,1)
close(VW,mp.mpf(1)/180)
close(VA,4-mp.pi**2/3)
close(C,mp.mpf(1)/18)
close(Iww,mp.mpf(1)/90)
close(Iwa,mp.mpf(1)/18)
close(Iaa,mp.pi**2/3-3)

checks=0
for n in range(1,101):
    cov=C/n+2*(n-1)*Iwa/n
    vw=VW/n+2*(n-1)*Iww/n
    va=VA/n+2*(n-1)*Iaa/n
    close(cov,mp.mpf(2*n-1)/(18*n))
    close(vw,mp.mpf(4*n-3)/(180*n))
    close(va,(10-6*n+(2*n-3)*mp.pi**2/3)/n)
    rho=cov/mp.sqrt(vw*va)
    assert 0 < rho < 1
    checks += 4

limit=mp.sqrt(5)/(3*mp.sqrt(2*mp.pi**2/3-6))
n=10**8
cov=mp.mpf(2*n-1)/(18*n)
vw=mp.mpf(4*n-3)/(180*n)
va=(10-6*n+(2*n-3)*mp.pi**2/3)/n
rho=cov/mp.sqrt(vw*va)
assert abs(rho-limit) < mp.mpf("1e-7")

print(
    "VERIFY_OK "
    "integral_checks=8 "
    f"finite_formula_checks={checks} "
    f"limit={mp.nstr(limit,16)}"
)
