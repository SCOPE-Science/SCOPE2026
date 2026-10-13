#!/usr/bin/env python3
import mpmath as mp

mp.mp.dps = 60

a0=mp.mpf(10)
mu0=mp.mpf("0.1")
mu1=mp.mpf("0.5")
mu2=mp.mpf("0.4")
xi1=mp.mpf("0.5")
xi2=mp.mpf("0.4")

def a_of(t):
    return a0*mp.e**(-mu0*t)

def B(N,a):
    return N*(mu2+xi2*N)*(a-mu1-xi1*N)/a

def dB_poly_coeff(a):
    # derivative numerator of B with respect to N:
    # expand N*(mu2+xi2*N)*(delta-xi1*N)
    d=a-mu1
    # B*a = -xi1*xi2*N^3 + (d*xi2-xi1*mu2)*N^2 + d*mu2*N
    # derivative quadratic:
    return (-3*xi1*xi2, 2*(d*xi2-xi1*mu2), d*mu2)

def b0(t):
    a=a_of(t)
    if a <= mu1:
        return mp.mpf(0), mp.mpf(0)
    A,Bc,C=dB_poly_coeff(a)
    disc=Bc*Bc-4*A*C
    r1=(-Bc+mp.sqrt(disc))/(2*A)
    r2=(-Bc-mp.sqrt(disc))/(2*A)
    candidates=[x for x in (r1,r2) if x>0 and x<(a-mu1)/xi1]
    assert len(candidates)==1
    N=candidates[0]
    return B(N,a),N

# Figure values.
v0,n0=b0(mp.mpf(0))
v02,n02=b0(mp.mpf("0.2"))
v15,n15=b0(mp.mpf("1.5"))
v49,n49=b0(mp.mpf("4.9"))

assert abs(v0-mp.mpf("21.9375160203768")) < mp.mpf("1e-12")
assert abs(v02-mp.mpf("21.0432928772414")) < mp.mpf("1e-12")
assert abs(v15-mp.mpf("16.0416587978169")) < mp.mpf("1e-12")
assert abs(v49-mp.mpf("7.81905967141617")) < mp.mpf("1e-12")
assert v0 > v02 > v15 > v49 > 0

# Crossing for b=21.
f=lambda t:b0(t)[0]-21
tb=mp.findroot(f,(mp.mpf("0.20"),mp.mpf("0.22")))
assert mp.mpf("0.2098") < tb < mp.mpf("0.2100")

# Positive equilibria at tau=.2, b=21 from the exact cubic.
t=mp.mpf("0.2")
a=a_of(t)
b=mp.mpf(21)
# cubic coefficients from the source.
coeff=[
    xi1*xi2,
    -((a-mu1)*xi2-xi1*mu2),
    -(a-mu1)*mu2,
    a*b
]
roots=mp.polyroots(coeff,maxsteps=1000,error=False)
pos=sorted([mp.re(z) for z in roots if abs(mp.im(z)) < mp.mpf("1e-40") and mp.re(z)>0])
assert len(pos)==2
eq=[]
for N in pos:
    w=N*(mu1+xi1*N)/a
    g=b/(mu2+xi2*N)
    eq.append((w,g))
assert abs(eq[0][0]-mp.mpf("7.83873378557")) < mp.mpf("1e-10")
assert abs(eq[0][1]-mp.mpf("4.06772941473")) < mp.mpf("1e-10")
assert abs(eq[1][0]-mp.mpf("8.70473857031")) < mp.mpf("1e-10")
assert abs(eq[1][1]-mp.mpf("3.86803710902")) < mp.mpf("1e-10")

# Critical maturation delay.
tc=mp.log(a0/mu1)/mu0
assert tc > mp.mpf(29) and tc < mp.mpf(30)

# Monotonicity derivative identity checked numerically on arbitrary positive admissible data.
aa=mp.mpf(3)
NN=mp.mpf("0.4")
analytic=NN*(mu2+xi2*NN)*(mu1+xi1*NN)/(aa*aa)
h=mp.mpf("1e-8")
fd=(B(NN,aa+h)-B(NN,aa-h))/(2*h)
assert abs(fd-analytic) < mp.mpf("1e-15")
assert analytic > 0

print("VERIFY_OK")
print("b0_0", mp.nstr(v0,16))
print("b0_0_2", mp.nstr(v02,16))
print("b0_1_5", mp.nstr(v15,16))
print("b0_4_9", mp.nstr(v49,16))
print("tau_b_for_b21", mp.nstr(tb,16))
print("tau_c", mp.nstr(tc,16))
print("equilibria_tau_0_2_b_21", [(mp.nstr(x,14),mp.nstr(y,14)) for x,y in eq])
