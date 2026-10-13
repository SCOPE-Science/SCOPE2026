import mpmath as mp
mp.mp.dps = 70

def L(x, tau):
    x=mp.mpf(x); tau=mp.mpf(tau)
    return ((1+tau)**2 + tau*x + mp.mpf("0.5")*(tau*x)**2)*mp.e**(-tau*x)

def A(x,tau):
    tau=mp.mpf(tau)
    return L(x,tau)/(1+tau)**2

def F(x,delta,tau):
    return (1-A(x,tau))**mp.mpf(delta)

def deriv(x,tau):
    x=mp.mpf(x); tau=mp.mpf(tau)
    return -tau**2*(2+tau+tau*x*x/2)*mp.e**(-tau*x)

def q(z,delta,tau):
    z=mp.mpf(z); delta=mp.mpf(delta); tau=mp.mpf(tau)
    target=(1+tau)**2*(1-z**(1/delta))
    lo=mp.mpf("0"); hi=mp.mpf("1")
    while L(hi,tau)>target:
        hi*=2
    for _ in range(260):
        mid=(lo+hi)/2
        if L(mid,tau)>target:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

for tau in [mp.mpf("0.2"),mp.mpf("0.5"),1,3,8]:
    assert abs(L(0,tau)-(1+tau)**2) < mp.mpf("1e-65")
    for x in [0,mp.mpf("0.1"),1,5,20]:
        assert deriv(x,tau)<0
    for delta in [mp.mpf("0.2"),mp.mpf("0.5"),1,3]:
        for z in [mp.mpf("0.01"),mp.mpf("0.25"),mp.mpf("0.5"),mp.mpf("0.99")]:
            assert (1+tau)**2*(1+z**(1/delta)) > L(0,tau)

for delta in [mp.mpf("0.2"),mp.mpf("0.5"),1,3]:
    for tau in [mp.mpf("0.3"),mp.mpf("0.5"),1,2]:
        for z in [mp.mpf("0.01"),mp.mpf("0.25"),mp.mpf("0.5"),mp.mpf("0.75"),mp.mpf("0.99")]:
            x=q(z,delta,tau)
            assert abs(F(x,delta,tau)-z) < mp.mpf("1e-55")

expected={
    mp.mpf("0.5"):[mp.mpf("0.2382"),mp.mpf("1.1379"),mp.mpf("3.4049")],
    mp.mpf("1.0"):[mp.mpf("0.0870"),mp.mpf("0.4015"),mp.mpf("1.2298")],
    mp.mpf("1.5"):[mp.mpf("0.0515"),mp.mpf("0.2345"),mp.mpf("0.7043")],
    mp.mpf("2.0"):[mp.mpf("0.0365"),mp.mpf("0.1647"),mp.mpf("0.4882")],
    mp.mpf("3.0"):[mp.mpf("0.0230"),mp.mpf("0.1033"),mp.mpf("0.3019")],
}
for tau,row in expected.items():
    got=[q(z,mp.mpf("0.5"),tau) for z in [mp.mpf("0.25"),mp.mpf("0.5"),mp.mpf("0.75")]]
    for g,e in zip(got,row):
        assert abs(g-e) < mp.mpf("0.00006")

q1=q(mp.mpf("0.25"),mp.mpf("0.5"),mp.mpf("0.5"))
print("VERIFY_OK")
print("Q_0.25_delta0.5_tau0.5",mp.nstr(q1,35))
for tau in expected:
    got=[q(z,mp.mpf("0.5"),tau) for z in [mp.mpf("0.25"),mp.mpf("0.5"),mp.mpf("0.75")]]
    print("table_row",mp.nstr(tau,5),[mp.nstr(v,16) for v in got])
