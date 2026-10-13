import mpmath as mp

mp.mp.dps = 80

def params(mu):
    mu = mp.mpf(mu)
    phi = mp.e**(-mu)
    a = mu/(2*(1+mu))
    return mu, phi, a

def Lam(k, mu):
    mu, phi, a = params(mu)
    return (1+a*k)*phi**k

def pmf(y, mu):
    return Lam(y,mu)-Lam(y+1,mu)

def exact_moments(mu):
    mu, phi, a = params(mu)
    m1 = phi/(1-phi) + a*phi/(1-phi)**2
    m2 = phi*(1+phi)/(1-phi)**2 + a*phi*(1+3*phi)/(1-phi)**3
    return m1, m2, m2-m1*m1

def source_displayed(mu):
    mu, phi, a = params(mu)
    m1 = phi**2/(1-phi) * (1 + mu*(2-phi)/((1+mu)*(1-phi)))
    m2 = 2*(phi/(1-phi))**2 * (1 + 2*mu/((1+mu)*(1-phi))) - m1**2
    var = m2 - m1**2
    return m1, m2, var

# Direct PMF summation versus corrected formulas.
for mu in ("0.5","0.8","1","1.5","2.5"):
    m1,m2,var = exact_moments(mu)
    N = 1000
    d1 = mp.fsum(mp.mpf(y)*pmf(y,mu) for y in range(N))
    d2 = mp.fsum((mp.mpf(y)**2)*pmf(y,mu) for y in range(N))
    assert abs(d1-m1) < mp.mpf("1e-55")
    assert abs(d2-m2) < mp.mpf("1e-55")

# Source Eq. (18) disagrees decisively at mu=1.
m1,m2,var = exact_moments("1")
s1,s2,svar = source_displayed("1")
assert abs(m1-mp.mpf("0.81214510542127450412")) < mp.mpf("1e-20")
assert abs(var-mp.mpf("1.3657697942970707523")) < mp.mpf("2e-20")
assert abs(s1-mp.mpf("0.49049434221605910146")) < mp.mpf("2e-20")
assert abs(m1-s1) > mp.mpf("0.3")

# A parameter value where the displayed Eq. (21)-(22) chain even yields negative variance.
_,_,v02 = exact_moments("0.2")
_,_,sv02 = source_displayed("0.2")
assert v02 > 0
assert sv02 < 0

# Tail asymptotic.
mu, phi, a = params("1")
for y in (100,300,700):
    ratio = pmf(y,mu)/(a*(1-phi)*y*phi**y)
    assert abs(ratio-1) < mp.mpf("0.05")

# MGF partial sums converge below t=mu and boundary terms grow linearly.
def mgf_partial(mu,t,N):
    return mp.fsum(mp.e**(mp.mpf(t)*y)*pmf(y,mu) for y in range(N))

below1 = mgf_partial("1","0.5",300)
below2 = mgf_partial("1","0.5",700)
assert abs(below2-below1) < mp.mpf("1e-40")

target = a*(1-phi)
for y in (100,300,700):
    term = mp.e**(mu*y)*pmf(y,mu)
    assert abs(term/(target*y)-1) < mp.mpf("0.05")

print("VERIFY_OK")
print("mu1_exact_mean", mp.nstr(m1, 30))
print("mu1_exact_variance", mp.nstr(var, 30))
print("mu1_source_eq18", mp.nstr(s1, 30))
print("mu0.2_exact_variance", mp.nstr(v02, 30))
print("mu0.2_source_eq22_variance", mp.nstr(sv02, 30))
