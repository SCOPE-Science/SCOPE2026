from fractions import Fraction as F
from decimal import Decimal, getcontext

getcontext().prec = 60
D = Decimal

def Q(x):
    return D(32)*x**3-D(131)*x**2-D(240)*x-D(100)

lo, hi = D(5), D(6)
assert Q(lo) < 0 < Q(hi)
for _ in range(240):
    mid=(lo+hi)/2
    if Q(mid) < 0:
        lo=mid
    else:
        hi=mid
x=(lo+hi)/2
k=(x+(x*x-D(4)).sqrt())/D(2)

def P(k):
    return (D(32)*k**6-D(131)*k**5-D(144)*k**4-D(362)*k**3
            -D(144)*k**2-D(131)*k+D(32))

assert abs(P(k)) < D("1e-45")
assert abs(k-D("5.36076789614546")) < D("1e-14")

def phi(k,u):
    return ((k-D(1))**2*u/(k+u)**2 *
            (D(1)+(k-D(1))**2*u/(D(1)+k*u)**2))

def gridmax(k):
    # Dense log grid plus local ternary refinement; corroborative only.
    import math
    best_u=D(1)
    best_v=phi(k,best_u)
    for j in range(-10000,10001):
        u=D(str(math.exp(j/1000.0)))
        v=phi(k,u)
        if v>best_v:
            best_u,best_v=u,v
    a=best_u/D("1.02")
    b=best_u*D("1.02")
    for _ in range(160):
        m1=(D(2)*a+b)/D(3)
        m2=(a+D(2)*b)/D(3)
        if phi(k,m1)<phi(k,m2):
            a=m1
        else:
            b=m2
    u=(a+b)/D(2)
    return u,phi(k,u)

_, below=gridmax(k-D("0.0001"))
_, above=gridmax(k+D("0.0001"))
assert below < D(1)
assert above > D(1)

# Exact witness.
a,b,c=F(5),F(2),F(2)
r1,r2=F(2),F(-5)
d1=r1/a
r2mid=r2-c*d1
d2=r2mid/b
r1final=-c*d2
assert r2mid==F(-29,5)
assert d2==F(-29,10)
assert r1final==F(29,5)
assert a+b==7 and a*b-c*c==6  # eigenvalues 1 and 6

print("VERIFY_OK")
print("kappa_star", k)
print("below_max_sq", below)
print("above_max_sq", above)
print("witness_final_residual", (r1final,F(0)))
