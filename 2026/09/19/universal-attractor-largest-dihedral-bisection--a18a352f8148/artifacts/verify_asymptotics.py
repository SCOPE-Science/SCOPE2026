from decimal import Decimal, getcontext
from math import acos, degrees

getcontext().prec = 80
D = Decimal
c = D(7) / D(8)
s2 = D(15) / D(64)
s = s2.sqrt()


def poly(x):
    return D(7)*x**3 - D(12)*x**2 + D(4)

lo, hi = D(3)/D(4), D(4)/D(5)
for _ in range(260):
    mid = (lo+hi)/2
    # p is strictly decreasing on this interval
    if poly(mid) > 0:
        lo = mid
    else:
        hi = mid
rho = (lo+hi)/2
rho2 = rho*rho
inv_rho = D(1)/rho
A = -s2*rho**5 / ((D(1)-rho2)*(D(2)*rho2+D(1)))


def step(a,b):
    W = (a*a + b*b - D(2)*a*b*c + a*a*b*b*s2).sqrt()
    return a*b/(a+W), a


def inradius(a,b):
    W = (a*a + b*b - D(2)*a*b*c + a*a*b*b*s2).sqrt()
    return a*b*s/(a*b*s+a+b+W)


def run(a0,b0,nmax=90):
    a,b = D(a0),D(b0)
    rows=[]
    for n in range(nmax+1):
        t=a/b
        rin=inradius(a,b)
        h=(D(1)+b*b).sqrt()
        rows.append((n,a,b,t,rin,h))
        if n<nmax:
            a,b=step(a,b)
    return rows

cases=[
    (D(3)/D(16),D(1)/D(4),"source seed"),
    (D('0.15'),D('0.20'),"interior t=0.75"),
    (D('0.12'),D('0.15'),"interior t=0.8"),
    (D('0.077'),D('0.10'),"interior t=0.77"),
]

print("rho =", rho)
print("rho^2 =", rho2)
print("1/rho =", inv_rho)
print("A =", A)
print("beta_deg =", degrees(acos(float(D(1)/(D(2)*rho)))))
print("2beta_deg =", 2*degrees(acos(float(D(1)/(D(2)*rho)))))
print()

for a0,b0,label in cases:
    rows=run(a0,b0)
    # estimate C at n=80, before Decimal precision is remotely limiting
    nC=80
    C=rows[nC][2]/(rho**nC)
    # normalized second correction at n=55
    nA=55
    a,b,t=rows[nA][1],rows[nA][2],rows[nA][3]
    y=(t-rho)/(b*b)
    # volume ratio and cut fraction at n=70
    n=70
    a,b,t=rows[n][1],rows[n][2],rows[n][3]
    an,bn=step(a,b)
    tnext=an/bn
    vol_ratio=t*tnext
    # quality asymptotic normalization
    rin=rows[n][4]; h=rows[n][5]
    quality_scaled=(h/rin)*(rho**n)
    Kpred=(D(1)+rho)/(rho2*s*C)
    angle_scaled=(a)*(rho**(-n-D(1))) # should approach C
    print(label)
    print("  C_80 =", C)
    print("  ((t-rho)/b^2)_55 =", y)
    print("  volume_ratio_70 =", vol_ratio)
    print("  quality*rho^n at 70 =", quality_scaled)
    print("  predicted quality constant =", Kpred)
    print("  a_n/rho^(n+1) at 70 =", angle_scaled)
    print()
