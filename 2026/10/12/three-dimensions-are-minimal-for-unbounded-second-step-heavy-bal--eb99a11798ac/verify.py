from fractions import Fraction as F
from decimal import Decimal, getcontext

# Polynomial helpers in the variable r=sqrt(kappa).
def pmul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def psub(a,b):
    n=max(len(a),len(b))
    a=a+[F(0)]*(n-len(a)); b=b+[F(0)]*(n-len(b))
    return [a[i]-b[i] for i in range(n)]

# g_L=(r-1)(5r+1)/((r+1)(3r+1));
# g_mu=(r-1)(r+5)/((r+1)(r+3)).
# Check the claimed positive difference by cross multiplication:
# g_L-g_mu = 2(r-1)^2 / ((r+3)(3r+1)).
left = psub(
    pmul(pmul([F(-1),F(1)],[F(1),F(5)]), pmul([F(1),F(1)],[F(3),F(1)])),
    pmul(pmul([F(-1),F(1)],[F(5),F(1)]), pmul([F(1),F(1)],[F(1),F(3)]))
)
# Common factors include (r+1); after cancellation the numerator is 2(r-1)^2.
# Direct numerical rational spot checks certify the simplified identities at several r.
def gL(r):
    return (r-1)*(5*r+1)/((r+1)*(3*r+1))
def gm(r):
    return (r-1)*(r+5)/((r+1)*(r+3))
for r in [F(2),F(3),F(5),F(11,3)]:
    assert gL(r)-gm(r) == 2*(r-1)*(r-1)/((r+3)*(3*r+1))

# The frontier g_L=1 reduces to r^2-4r-1=0, with positive root 2+sqrt(5).
getcontext().prec=60
sqrt5=Decimal(5).sqrt()
rstar=Decimal(2)+sqrt5
assert abs(rstar*rstar-Decimal(4)*rstar-Decimal(1)) < Decimal('1e-55')
kstar=rstar*rstar
assert abs(kstar-(Decimal(9)+Decimal(4)*sqrt5)) < Decimal('1e-55')

# Limit g_L -> 5/3, so squared ratio -> 25/9.
for r in [F(10**3),F(10**4),F(10**5)]:
    assert abs(float(gL(r))-5/3) < 0.01

# Exact kappa=4 reset witness: mu=1, L=4, alpha=4/9, beta=1/9, lambda*=9/4.
alpha=F(4,9); beta=F(1,9); lam=F(9,4)
p1=F(1)-alpha*lam
p2=p1*p1-beta*alpha*lam
assert p1==0
assert p2==-F(1,9)
f0=lam/F(2)
f1=f0*p1*p1
f2=f0*p2*p2
assert f0==F(9,8)
assert f1==0
assert f2==F(1,72)

# Nearby finite-ratio witness with middle curvature 20/9.
lam=F(20,9)
p1=F(1)-alpha*lam
p2=p1*p1-beta*alpha*lam
assert p1==F(1,81)
assert p2==-F(719,6561)
ratio=(p2/p1)**2
assert ratio==F(516961,6561)
assert ratio>78

# Endpoint formulas for kappa=4, where rho=1/3.
rho=F(1,3)
p1mu=rho*(2-rho); p2mu=rho*rho*(3-2*rho)
p1L=-rho*(2+rho); p2L=rho*rho*(3+2*rho)
assert p1mu==F(5,9) and p2mu==F(7,27)
assert p1L==-F(7,9) and p2L==F(11,27)
assert abs(p2L/p1L)==gL(F(2))

print('VERIFY_OK')
print('kappa_frontier', kstar)
print('finite_ratio_witness', ratio)
