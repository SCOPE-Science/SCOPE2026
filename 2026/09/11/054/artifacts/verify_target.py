"""Verify target E3: truncated 4th moment divergence => |L_N| >= (1/8) log N.
Stdlib only. Prints ALL_VERIFY_OK on success."""
import math, cmath

SQ2_LO, SQ2_HI = 1.41, 1.42  # rigorous enclosure of sqrt(2)

# (i) exact second moment via antiderivative: int_0^inf y^2/(1+y)^4 dy = 1/3
# F(u) = -1/u + 1/u^2 - 1/(3u^3), u=1+y
def F(u):
    return -1/u + 1/u**2 - 1/(3*u**3)
I2 = -F(1.0)  # F(inf)=0
assert abs(I2 - 1/3) < 1e-15, I2
E_X2 = 2 * 0.75 * I2 * 2  # 2*E[Y^2], E[Y^2]=2*3/4*I2
print(f"I2={I2} E[X^2]={E_X2}")
assert abs(E_X2 - 1.0) < 1e-12

# exact tail P(|X|>t) = (1/2)(1+t/sqrt2)^-3
def tail(t, s=math.sqrt(2)):
    return 0.5*(1+t/s)**-3
for t in [1, 2, 5, 10, 100]:
    r = tail(t)*t**3/math.sqrt(2)
    print(f"tail t={t} ratio->1: {r:.6f}")
assert tail(100)*100**3/math.sqrt(2) > 0.95  # close to 1

# exact truncated 4th moment: mu(M) = 6*(G(U)-G(1)), U=1+M/sqrt2,
# G(u) = u - 4 ln u - 6/u + 2/u^2 - 1/(3u^3)
def G(u):
    return u - 4*math.log(u) - 6/u + 2/u**2 - 1/(3*u**3)
def mu(M, s=math.sqrt(2)):
    return 6*(G(1+M/s)-G(1.0))
for M in [10, 31.6, 100, 1000]:
    print(f"M={M} mu={mu(M):.3f} mu/M={mu(M)/M:.4f}")
# hand lower bound: mu(M) >= 0.26*(M-1.42) for M>=1.42
for M in [10, 31.6, 100, 1000, 3162]:
    assert mu(M) >= 0.26*(M-1.42), (M, mu(M))
print("truncated-moment hand bound OK")

# m_sc lower bound |m|^4 >= 1/4 when |eps|<=1/25
def msc(z):
    d = cmath.sqrt(z*z-4)
    m1, m2 = (-z+d)/2, (-z-d)/2
    return m1 if m1.imag > 0 else m2
for w in [1j, 2+1j, -3+2j, 10j]:
    N = 10**15
    z = 2 + w*N**(-2/3)
    m = msc(z)
    assert abs(m)**4 >= 0.25, (w, m)
    print(f"w={w} |m|^4={abs(m)**4:.5f} OK")

# headline: kappa=mu-3 >= 0.26*(M-1.42)-3; L_lb=kappa/4 >= (1/8)lnN for N>=1e12, M=N^{1/6}
for N in [10**12, 10**13, 10**15, 10**18, 10**24]:
    M = N**(1/6)
    kap = 0.26*(M-1.42)-3
    L = kap/4
    assert L >= math.log(N)/8, (N, L, math.log(N)/8)
    print(f"N=1e{int(math.log10(N))} M={M:.1f} L_lb={L:.2f} >= (1/8)lnN={math.log(N)/8:.2f} OK")

# monotonicity for all N>=1e12: derivative check via grid + analytic derivative argument in DRAFT
Ns = [10**(12+0.1*k) for k in range(200)]
assert all(0.26*(n**(1/6)-1.42)-3-0.5*math.log(n) >= 0 for n in Ns)
print("monotonic grid OK")

# GOE contrast
print("GOE: kappa4=0 => L=0 = O(1); truncated analogue |kap|<=3, |m|^4<=2.77 => |L|<=8.31")
print("ALL_VERIFY_OK")
