"""Interval verification for the gamma-monotonicity tau bracket.

Requires mpmath 1.3.0.  The script uses mpmath.iv at 70 decimal digits.
It verifies only the explicit elementary inequalities quoted in RESULT.md;
the analytic reduction is proved there.
"""
from mpmath import iv, mp

iv.dps = 70
mp.dps = 90
T = iv.mpf('212.435')
A0 = mp.mpf('2.23')
B0 = mp.mpf('15')
H = mp.mpf('0.001')


def S(x):
    return ((x-iv.mpf('0.5'))*iv.log(x)-x
            + iv.log(2*iv.pi)/2 + 1/(12*x))


def Sp(x):
    return iv.log(x)-1/(2*x)-1/(12*x*x)


def Spp(x):
    return 1/x+1/(2*x*x)+1/(6*x*x*x)


def D(x, t=T):
    return iv.log((x*x+t)/(x+t))


def Dp(x, t=T):
    return 2*x/(x*x+t)-1/(x+t)


def Dpp(x, t=T):
    return 2*(t-x*x)/(x*x+t)**2+1/(x+t)**2


def P_point(c):
    x = iv.mpf([str(c), str(c)])
    return Sp(x)*D(x)-S(x)*Dp(x)


def Pprime_interval(a, b):
    x = iv.mpf([str(a), str(b)])
    return Spp(x)*D(x)-S(x)*Dpp(x)


def centered_bound(a, b):
    c = (a+b)/2
    pc = P_point(c)
    dp = Pprime_interval(a, b)
    delta = iv.mpf([str(a-c), str(b-c)])
    return pc + dp*delta


worst = None
n = int(mp.ceil((B0-A0)/H))
for i in range(n):
    a = A0+i*H
    b = min(A0+(i+1)*H, B0)
    enclosure = centered_bound(a, b)
    if not (enclosure.a > 0):
        raise AssertionError(f'P enclosure not positive on [{a}, {b}]: {enclosure}')
    if worst is None or float(enclosure.a) < float(worst[2].a):
        worst = (a, b, enclosure)

print('PASS: P_212.435(x)>0 on [2.23,15].')
print('smallest certified centered enclosure:', worst[0], worst[1], worst[2])

# For x>=15, the numerator K of D'' has K''<0.  These two endpoint
# checks therefore imply K'<0 and K<0 thereafter.
def K(x):
    return (2*T**3 - 2*T**2*x**2 + 4*T**2*x + T**2
            - 4*T*x**3 + 4*T*x**2 - x**4)


def Kp(x):
    return -4*x**3 - 12*T*x**2 + (8*T-4*T**2)*x + 4*T**2

x15 = iv.mpf(15)
print('K(15)=', K(x15))
print("K'(15)=", Kp(x15))
assert K(x15).b < 0
assert Kp(x15).b < 0

# At x=9, psi(9)=H_8-gamma=761/280-gamma and Gamma(9)=40320.
# Bracket the unique parameter where u_tau'(9)=0.
def A9(tau_text):
    tau = iv.mpf(tau_text)
    x = iv.mpf(9)
    psi9 = iv.mpf(761)/280 - iv.euler
    lg9 = iv.log(iv.mpf(40320))
    d = iv.log((x*x+tau)/(x+tau))
    dp = 2*x/(x*x+tau)-1/(x+tau)
    return psi9*d-lg9*dp

lo = A9('212.508612771')
hi = A9('212.508612772')
print('A_212.508612771(9)=', lo)
print('A_212.508612772(9)=', hi)
assert lo.a > 0
assert hi.b < 0
print('PASS: tau_9 lies in (212.508612771, 212.508612772).')
