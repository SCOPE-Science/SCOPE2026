import mpmath as mp

mp.mp.dps = 70

def F(t, a):
    t = mp.mpf(t); a = mp.mpf(a)
    return (1 + a/(2*(1+a)*t))*mp.e**(-a/t)

def pdf(t, a):
    t = mp.mpf(t); a = mp.mpf(a)
    return a/(2*(1+a)*t**2)*(1+2*a+a/t)*mp.e**(-a/t)

def hazard(t, a):
    return pdf(t,a)/(1-F(t,a))

def quantile(p, a):
    p = mp.mpf(p); a = mp.mpf(a)
    lo = mp.mpf("1e-30")
    hi = max(mp.mpf(1), a)
    while F(hi,a) < p:
        hi *= 2
    for _ in range(250):
        mid = (lo+hi)/2
        if F(mid,a) < p:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

def Hp(p,a):
    return hazard(quantile(p,a), a)

def x_of(p,a):
    q = quantile(p,a)
    return mp.mpf(a)/q

def dlog_closed(p,a):
    a=mp.mpf(a); b=1+a
    x=x_of(p,a)
    N=4*b**3+4*b**2*x-2*b**2+b*x**2-2*b-2*x+1
    return -N/(b*(b-1)*(2*b+x-1)**2)

# Verify the fixed-quantile identity, implicit derivative, and log-H derivative.
for p in [mp.mpf("0.01"),mp.mpf("0.1"),mp.mpf("0.4"),mp.mpf("0.8"),mp.mpf("0.99")]:
    for a in [mp.mpf("0.08"),mp.mpf("0.3"),mp.mpf("0.7"),mp.mpf("1.5"),mp.mpf("4"),mp.mpf("12")]:
        b=1+a
        x=x_of(p,a)
        assert abs((1+x/(2*b))*mp.e**(-x)-p) < mp.mpf("1e-60")
        dx_closed=-x/(b*(2*b+x-1))
        eps=mp.mpf("1e-6")*max(1,a)
        dx_num=(x_of(p,a+eps)-x_of(p,a-eps))/(2*eps)
        assert abs(dx_num-dx_closed) < mp.mpf("5e-8")
        dl=dlog_closed(p,a)
        assert dl < 0
        dln_num=(mp.log(Hp(p,a+eps))-mp.log(Hp(p,a-eps)))/(2*eps)
        assert abs(dln_num-dl) < mp.mpf("5e-8")

# Source Figure 1 values.
p=mp.mpf("0.4")
a1=mp.mpf("1.5")
a2=mp.mpf("0.7")
q1=quantile(p,a1)
q2=quantile(p,a2)
h1=Hp(p,a1)
h2=Hp(p,a2)
assert h2 > h1
assert pdf(q2,a2) > pdf(q1,a1)
ratio=h2/h1
assert abs(q1-mp.mpf("1.341555252123364")) < mp.mpf("1e-14")
assert abs(q2-mp.mpf("0.5720293366329949")) < mp.mpf("1e-14")

# Multi-step jump direction across several matched exposure levels.
for p in [mp.mpf("0.03"),mp.mpf("0.25"),mp.mpf("0.6"),mp.mpf("0.95")]:
    params=[mp.mpf("3"),mp.mpf("1.4"),mp.mpf("0.9"),mp.mpf("0.25")]
    vals=[Hp(p,a) for a in params]
    assert vals[0] < vals[1] < vals[2] < vals[3]

print("VERIFY_OK")
print("q_alpha1", mp.nstr(q1, 30))
print("q_alpha2", mp.nstr(q2, 30))
print("hazard_before", mp.nstr(h1, 30))
print("hazard_after", mp.nstr(h2, 30))
print("jump_ratio", mp.nstr(ratio, 30))
