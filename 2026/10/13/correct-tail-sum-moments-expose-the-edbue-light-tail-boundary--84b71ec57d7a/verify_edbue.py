import mpmath as mp

mp.mp.dps = 120

def params(alpha, theta):
    alpha = mp.mpf(alpha)
    theta = mp.mpf(theta)
    lam = -mp.log(theta)
    return alpha, theta, lam

def u(k, theta, lam):
    return theta**k/(1 + lam*k)

def G(k, alpha, theta, lam):
    if k == 0:
        return mp.mpf("0")
    return (1-u(k,theta,lam))**alpha

def pmf(n, alpha, theta, lam):
    return G(n+1,alpha,theta,lam)-G(n,alpha,theta,lam)

def surv_ge(k, alpha, theta, lam):
    return 1-G(k,alpha,theta,lam)

# Tail constants, with k chosen to avoid catastrophic cancellation.
for a,th,k in [
    ("0.5","0.8",500),
    ("2.0","0.5",250),
    ("1.7","0.9",600),
]:
    alpha,theta,lam=params(a,th)
    s=surv_ge(k,alpha,theta,lam)
    p=pmf(k,alpha,theta,lam)
    s0=(alpha/lam)*theta**k/k
    p0=(alpha*(1-theta)/lam)*theta**k/k
    assert abs(s/s0-1) < mp.mpf("0.02")
    assert abs(p/p0-1) < mp.mpf("0.01")

# Direct PMF moments equal corrected tail sums.
alpha,theta,lam=params("0.7","0.8")
N=1200
for r in (1,2,3,4):
    direct=mp.fsum((mp.mpf(n)**r)*pmf(n,alpha,theta,lam) for n in range(N))
    tails=mp.fsum(
        ((mp.mpf(k)**r)-mp.mpf(k-1)**r)*surv_ge(k,alpha,theta,lam)
        for k in range(1,N)
    )
    assert abs(direct-tails) < mp.mpf("1e-60")

# Printed Eq. (6.4) partial sums run negative and do not stabilize.
def bad_partial(r,N):
    return mp.fsum(
        ((mp.mpf(k-1)**r)-mp.mpf(k)**r)*G(k,alpha,theta,lam)
        for k in range(1,N+1)
    )

b100=bad_partial(1,100)
b500=bad_partial(1,500)
assert b500 < b100 - 300

# MGF below the exact boundary stabilizes.
def mgf_partial(t,N):
    return mp.fsum(mp.e**(t*n)*pmf(n,alpha,theta,lam) for n in range(N))

below=lam/2
m1=mgf_partial(below,300)
m2=mgf_partial(below,700)
assert abs(m2-m1) < mp.mpf("1e-15")

# At t=lambda, n times the nth term tends to the positive harmonic coefficient.
target=alpha*(1-theta)/lam
vals=[]
for n in (100,300,700):
    term=mp.e**(lam*n)*pmf(n,alpha,theta,lam)
    vals.append(n*term)
assert abs(vals[-1]/target-1) < mp.mpf("0.02")

print("VERIFY_OK")
print("lambda", mp.nstr(lam,30))
print("direct_mean", mp.nstr(
    mp.fsum(mp.mpf(n)*pmf(n,alpha,theta,lam) for n in range(N)),30))
print("bad_mean_partial_500", mp.nstr(b500,30))
print("boundary_n_term", [mp.nstr(v,20) for v in vals])
