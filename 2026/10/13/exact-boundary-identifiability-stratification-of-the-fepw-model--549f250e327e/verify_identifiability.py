import mpmath as mp
mp.mp.dps = 80

def R(x,tau,eta,kappa,phi):
    return mp.e**(1-mp.e**((tau*x)**eta)-(kappa*x)**phi)

xs=[mp.mpf("0.1"),mp.mpf("1"),mp.mpf("3"),mp.mpf("10")]

# tau=0 erases eta exactly.
for x in xs:
    r1=R(x,0,mp.mpf("0.3"),mp.mpf("1.7"),mp.mpf("2.2"))
    r2=R(x,0,mp.mpf("5.4"),mp.mpf("1.7"),mp.mpf("2.2"))
    assert r1 == r2

# kappa=0 erases phi exactly.
for x in xs:
    r1=R(x,mp.mpf("0.8"),mp.mpf("1.4"),0,mp.mpf("0.2"))
    r2=R(x,mp.mpf("0.8"),mp.mpf("1.4"),0,mp.mpf("7.0"))
    assert r1 == r2

# double zero is survival one.
for x in xs:
    assert R(x,0,mp.mpf("1.3"),0,mp.mpf("2.7")) == 1

# Interior asymptotic recovery.
tau=mp.mpf("0.7")
eta=mp.mpf("1.25")
kappa=mp.mpf("0.9")
phi=mp.mpf("0.8")
a=tau**eta
b=kappa**phi

def logK(x):
    A=a*x**eta
    # log(exp(A)+b*x**phi), evaluated stably.
    q=mp.log(b)+phi*mp.log(x)-A
    return A+mp.log1p(mp.e**q)

errs_eta=[]
errs_a=[]
for x in (mp.mpf("50"),mp.mpf("100"),mp.mpf("200")):
    lk=logK(x)
    eta_hat=mp.log(lk)/mp.log(x)
    # eta_hat itself has log(a)/log(x) bias; remove using two x values below.
    errs_a.append(abs(lk/x**eta-a))

# two-point slope of log(log K) converges to eta.
for x in (mp.mpf("25"),mp.mpf("50"),mp.mpf("100")):
    y=2*x
    ehat=(mp.log(logK(y))-mp.log(logK(x)))/(mp.log(y)-mp.log(x))
    errs_eta.append(abs(ehat-eta))

assert errs_eta[-1] < errs_eta[0]
assert errs_a[-1] < errs_a[0]
assert errs_eta[-1] < mp.mpf("1e-20")
assert errs_a[-1] < mp.mpf("1e-20")
print("VERIFY_OK")
