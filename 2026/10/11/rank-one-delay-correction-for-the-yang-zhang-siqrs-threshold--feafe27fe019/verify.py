#!/usr/bin/env python3
from fractions import Fraction
import cmath, math


def pmul(a,b):
    out=[Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def padd(a,b):
    n=max(len(a),len(b)); out=[Fraction(0)]*n
    for i in range(n):
        out[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    return out


def peval(a,z):
    s=0
    for c in reversed(a):
        s=s*z+c
    return s


def pder(a,z):
    return sum(i*a[i]*z**(i-1) for i in range(1,len(a)))

# Printed numerical parameters.
beta=Fraction(13,20); sigma=Fraction(2,5)
d=Fraction(1,10); alpha1=Fraction(1,10); gamma=Fraction(3,10)
eps=Fraction(7,50); eta=Fraction(1,10); alpha2=Fraction(9,50)
delta=Fraction(7,10); pfeed=Fraction(9,10); birth=Fraction(1,1)
c=d+alpha1+gamma+eps
h_print=Fraction(12,25)
h_table=eta+d+alpha2
assert c==Fraction(16,25)
assert h_table==Fraction(19,50)
assert h_print!=h_table

# Exact positive equilibrium of printed (5.1).
S=Fraction(320,197)
I=Fraction(1371240,665663)
Q=Fraction(399945,665663)
R=Fraction(1313079,665663)
infect=beta*S*I/(1+sigma*S)
res=(
    (1-pfeed)*birth-infect-d*S+delta*R,
    infect-c*I,
    eps*I-h_print*Q,
    pfeed*birth+gamma*I+eta*Q-(d+delta)*R,
)
assert res==(0,0,0,0)

# Reported rounded point: quarantine residual is too large to be rounding.
Ir=Fraction(20598,10000); Qr=Fraction(7739,10000)
rq_print=eps*Ir-h_print*Qr
rq_table=eps*Ir-h_table*Qr
assert rq_print==Fraction(-831,10000)
assert rq_table==Fraction(-571,100000)
max_round_print=(eps+h_print)*Fraction(5,100000)
max_round_table=(eps+h_table)*Fraction(5,100000)
assert abs(rq_print)>max_round_print and abs(rq_table)>max_round_table

# Rank-one delayed infection block and exact characteristic polynomials.
a=beta*I/(1+sigma*S)**2
assert a==Fraction(1038978,2111875)
# delayed 2x2 block [[-a,-c],[a,c]] has zero determinant
assert (-a)*c-(-c)*a==0
P0=pmul(pmul([d,1],[c,1]),pmul([h_print,1],[d+delta,1]))
br=[a*c-c*d,a-c]
Q0=pmul(br,pmul([h_print,1],[d+delta,1]))
Q0=padd(Q0,[-a*delta*(gamma*h_print+eta*eps),-a*delta*gamma])
scale=Fraction(26398437500,1)
P=[int(x*scale) for x in P0]
Qpoly=[int(x*scale) for x in Q0]
assert P==[648768000,9663940000,36831100000,53324843750,26398437500]
assert Qpoly==[1106585331,4248671870,1620372000,-3907775000]

# Zero-delay Routh-Hurwitz.
A=[P[i]+(Qpoly[i] if i<len(Qpoly) else 0) for i in range(5)]
# ascending A0..A4
assert A==[1755353331,13912611870,38451472000,49417068750,26398437500]
a0,a1,a2,a3,a4=A
delta2=a3*a2-a4*a1
delta3=a3*a2*a1-a4*a1*a1-a3*a3*a0
assert delta2==1532887820450746875000 and delta2>0
assert delta3==17039818505241533448549351562500 and delta3>0

# Exact modulus polynomial in u=omega^2.
def imodsquared_coeff(poly):
    # poly ascending in lambda; split even/odd parts after lambda=i*omega.
    # return polynomial coefficients in u for |poly(i sqrt(u))|^2.
    even=[]; odd=[]
    maxe=(len(poly)-1)//2
    for k in range(maxe+1):
        j=2*k
        if j<len(poly):
            even.append(Fraction(poly[j]) * ((-1)**k))
    maxo=(len(poly)-2)//2
    for k in range(maxo+1):
        j=2*k+1
        if j<len(poly):
            odd.append(Fraction(poly[j]) * ((-1)**k))
    ev2=pmul(even,even)
    od2=[Fraction(0)]+pmul(odd,odd)
    return padd(ev2,od2)
FP=imodsquared_coeff(P)
FQ=imodsquared_coeff(Qpoly)
F=padd(FP,[-x for x in FQ])
Fint=[int(x) for x in F]
assert Fint==[
    -803631176960379561,
    31137005266996967100,
    324295356339287500000,
    883701272698789062500,
    696877502441406250000,
]
assert Fint[0]<0 and all(x>0 for x in Fint[1:])
# Hence F'(u)>0 for u>0.

# Source omega fails exactly.
wsrc=Fraction(393,5000)
usrc=wsrc*wsrc
Fsrc=sum(F[i]*usrc**i for i in range(len(F)))
assert Fsrc<0 and Fsrc!=0

# Locate the unique positive root by bisection.
def ff(u):
    return sum(float(Fint[i])*(u**i) for i in range(len(Fint)))
lo,hi=0.0,0.05
assert ff(lo)<0<ff(hi)
for _ in range(220):
    mid=(lo+hi)/2
    if ff(mid)>0: hi=mid
    else: lo=mid
u=(lo+hi)/2
w=math.sqrt(u)
assert abs(w-0.1447950754167241)<2e-15
Pc=peval(P,1j*w); Qc=peval(Qpoly,1j*w)
z=-Pc/Qc
assert abs(abs(z)-1.0)<2e-12
arg=cmath.phase(z)
tau=-arg/w
assert abs(tau-13.87960223606146)<3e-12
# Direct characteristic residual.
char=Pc+Qc*cmath.exp(-1j*w*tau)
assert abs(char)<1e-4
# next positive phase branch is later
assert tau < tau+2*math.pi/w
# no zero root for any delay
assert P[0]+Qpoly[0]>0

# Transversality.
lam=1j*w
exp=cmath.exp(-lam*tau)
dl=lam*peval(Qpoly,lam)*exp/(pder(P,lam)+(pder(Qpoly,lam)-tau*peval(Qpoly,lam))*exp)
assert dl.real>0.0017

print('VERIFY_OK')
