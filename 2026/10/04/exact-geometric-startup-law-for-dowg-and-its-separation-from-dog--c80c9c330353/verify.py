import math


def dog_closed(n):
    if n == 0:
        return 0.0
    y = 1.0
    for j in range(2,n+1):
        y *= 1.0 + 1.0/math.sqrt(j)
    return y


def dog_direct(n):
    # Scale r_eps=G=1 and remain in the pre-hit regime.
    x = 0.0
    for t in range(n):
        rbar = max(1.0, x)
        eta = rbar/math.sqrt(t+1.0)
        x += eta
    return x

for n in range(1,80):
    a = dog_direct(n)
    b = dog_closed(n)
    assert abs(a-b) <= 2e-12*max(1.0,b)

# The logarithmic remainder stays bounded over a large finite range.
vals=[]
for n in (100,300,1000,3000,10000):
    logy = sum(math.log1p(1.0/math.sqrt(j)) for j in range(2,n+1))
    vals.append(logy - 2.0*math.sqrt(n) + 0.5*math.log(n))
assert max(vals)-min(vals) < 0.2


def F(p):
    u=p*(1.0+p)
    return u/math.sqrt(1.0+u*u)

# Positive root of p^3+2p^2-2=0.
lo,hi=0.0,2.0
for _ in range(200):
    mid=(lo+hi)/2.0
    phi=mid**3+2.0*mid**2-2.0
    if phi < 0.0:
        lo=mid
    else:
        hi=mid
pstar=(lo+hi)/2.0
lam=1.0+pstar
assert abs(lam-1.8392867552141612) < 2e-15
assert abs(lam**3-lam**2-lam-1.0) < 2e-14
assert (1.0+2.0*pstar)/(1.0+pstar)**3 < 1.0

# Reduced DoWG recurrence and direct source replay agree.
y=1.0
S=2.0
p=1.0/math.sqrt(2.0)
ys=[1.0]
ps=[p]
for _ in range(1,80):
    ynew=y*(1.0+p)
    Snew=S+ynew*ynew
    pnew=ynew/math.sqrt(Snew)
    assert abs(pnew-F(p)) < 5e-15
    y,S,p=ynew,Snew,pnew
    ys.append(y)
    ps.append(p)
assert all(ps[i+1] > ps[i] for i in range(30))
assert all(ps[i+1] >= ps[i]-2e-15 for i in range(len(ps)-1))
assert all(p <= pstar+2e-15 for p in ps)
assert abs(ps[-1]-pstar) < 1e-12
assert abs(ys[-1]/ys[-2]-lam) < 1e-12

# Direct source-form DoWG with r_eps=G=1.
x=0.0
vprev=0.0
rprev=1.0
direct=[]
for t in range(80):
    rbar=max(abs(x),rprev)
    v=vprev+rbar*rbar
    eta=rbar*rbar/math.sqrt(v)
    x=x+eta
    direct.append(x)
    rprev=rbar
    vprev=v
for n in range(1,80):
    assert abs(direct[n-1]-ys[n-1]) <= 2e-10*max(1.0,ys[n-1])

# First-hit counts: DoWG is linear in log R, DoG is quadratic in log R.
def hit_dog(R):
    x=0.0
    t=0
    while x < R:
        rbar=max(1.0,x)
        x += rbar/math.sqrt(t+1.0)
        t += 1
    return t

def hit_dowg(R):
    x=0.0
    v=0.0
    rprev=1.0
    t=0
    while x < R:
        rbar=max(abs(x),rprev)
        v += rbar*rbar
        x += rbar*rbar/math.sqrt(v)
        rprev=rbar
        t += 1
    return t

for R in (1e3,1e5,1e8,1e12):
    td=hit_dog(R)
    tw=hit_dowg(R)
    assert tw < td

# At large R, normalized counts approach the claimed leading constants.
R=1e18
L=math.log(R)
td=hit_dog(R)
tw=hit_dowg(R)
assert abs(td/(L*L)-0.25) < 0.08
assert abs(tw/L-1.0/math.log(lam)) < 0.08

print('verification passed')
