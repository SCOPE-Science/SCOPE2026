import mpmath as mp
mp.mp.dps = 60

lam = mp.mpf("2.3")
theta = mp.mpf("1.7")
eta = mp.mpf("0.6")
L = -mp.log(1-eta)

def S(y):
    return mp.nsum(
        lambda n: eta**n/n * (lam/(lam+n*theta*y))**lam,
        [1, mp.inf]
    )/L

def f(y):
    return theta*lam**(lam+1)/L * mp.nsum(
        lambda n: eta**n/(lam+n*theta*y)**(lam+1),
        [1, mp.inf]
    )

def h(y):
    return f(y)/S(y)

A = (lam/theta)**lam * mp.polylog(lam+1, eta)/L
B = lam**2/theta * mp.polylog(lam+2, eta)/mp.polylog(lam+1, eta)

for y in (mp.mpf("300"), mp.mpf("1000"), mp.mpf("3000")):
    lead = y**lam*S(y)
    first = y*(S(y)/(A*y**(-lam))-1)
    haz = y**2*(lam/y-h(y))
    assert abs(lead/A-1) < mp.mpf("0.02")
    assert abs(first + B) < mp.mpf("0.08")
    assert abs(haz - B) < mp.mpf("0.05")

def quantile(q):
    y0 = (A/q)**(1/lam)
    lo = y0/4
    hi = y0*4
    while S(lo) < q:
        lo /= 2
    while S(hi) > q:
        hi *= 2
    for _ in range(220):
        mid=(lo+hi)/2
        if S(mid)>q:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

target = -B/lam
for q in (mp.mpf("1e-5"), mp.mpf("1e-7")):
    y0 = (A/q)**(1/lam)
    corr = quantile(q)-y0
    assert abs(corr-target) < mp.mpf("0.01")

print("VERIFY_OK")
