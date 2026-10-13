import math
from scipy import integrate, optimize, special

def R_hn(x, beta):
    return special.erfc(x/(math.sqrt(2.0)*beta))

def R_m(x, beta):
    return special.gammaincc(1.5, x*x/(2.0*beta*beta))

def hazard(x, alpha, beta, R):
    m = integrate.quad(
        lambda t: t**(alpha-1.0)*R(t,beta),
        x, math.inf, epsabs=1e-12, epsrel=1e-12, limit=300
    )[0]
    return x**(alpha-1.0)*R(x,beta)/m

for R in (R_hn, R_m):
    for alpha in (0.1, 0.5, 1.0, 2.0, 5.0):
        h10 = hazard(10.0, alpha, 1.0, R)
        assert abs(h10/10.0 - 1.0) < 0.08

# Small-shape endpoint pattern and representative minima.
hn_min = optimize.minimize_scalar(
    lambda x: hazard(x,0.1,1.0,R_hn),
    bounds=(1e-5,6.0), method="bounded", options={"xatol":1e-11}
)
m_min = optimize.minimize_scalar(
    lambda x: hazard(x,0.1,1.0,R_m),
    bounds=(1e-5,6.0), method="bounded", options={"xatol":1e-11}
)

assert abs(hn_min.x - 0.79251185) < 2e-6
assert abs(hn_min.fun - 2.49722593) < 2e-7
assert abs(m_min.x - 0.65565005) < 2e-6
assert abs(m_min.fun - 1.66888622) < 2e-7

hn01 = hazard(0.1,0.1,1.0,R_hn)
hn10 = hazard(10.0,0.1,1.0,R_hn)
m01 = hazard(0.1,0.1,1.0,R_m)
m10 = hazard(10.0,0.1,1.0,R_m)

assert hn01 > hn_min.fun and hn10 > hn_min.fun
assert m01 > m_min.fun and m10 > m_min.fun

print("VERIFY_OK")
print("IHSBHN_min_x", format(hn_min.x, ".12f"))
print("IHSBHN_min_h", format(hn_min.fun, ".12f"))
print("IHSBHN_h_0.1", format(hn01, ".12f"))
print("IHSBHN_h_10", format(hn10, ".12f"))
print("IHSBM_min_x", format(m_min.x, ".12f"))
print("IHSBM_min_h", format(m_min.fun, ".12f"))
print("IHSBM_h_0.1", format(m01, ".12f"))
print("IHSBM_h_10", format(m10, ".12f"))
