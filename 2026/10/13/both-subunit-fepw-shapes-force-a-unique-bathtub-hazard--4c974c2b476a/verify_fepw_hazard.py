import mpmath as mp
mp.mp.dps=70

def h(x,tau,eta,kappa,phi):
    x=mp.mpf(x); tau=mp.mpf(tau); eta=mp.mpf(eta); kappa=mp.mpf(kappa); phi=mp.mpf(phi)
    z=(tau*x)**eta
    return eta*tau**eta*x**(eta-1)*mp.e**z + phi*kappa**phi*x**(phi-1)

def hp(x,tau,eta,kappa,phi):
    x=mp.mpf(x); tau=mp.mpf(tau); eta=mp.mpf(eta); kappa=mp.mpf(kappa); phi=mp.mpf(phi)
    z=(tau*x)**eta
    return eta*tau**eta*x**(eta-2)*mp.e**z*(eta*z+eta-1) - phi*(1-phi)*kappa**phi*x**(phi-2)

def x0(tau,eta):
    tau=mp.mpf(tau); eta=mp.mpf(eta)
    return (((1-eta)/eta)**(1/eta))/tau

def ratio_z(z,tau,eta,kappa,phi):
    z=mp.mpf(z); tau=mp.mpf(tau); eta=mp.mpf(eta); kappa=mp.mpf(kappa); phi=mp.mpf(phi)
    return (eta/(phi*(1-phi)))*(tau/kappa)**phi*z**(1-phi/eta)*mp.e**z*(eta*z+eta-1)

def dlogR(z,eta,phi):
    z=mp.mpf(z); eta=mp.mpf(eta); phi=mp.mpf(phi)
    return 1+(eta-phi)/(eta*z)+eta/(eta*z+eta-1)

def minimum(tau,eta,kappa,phi):
    tau=mp.mpf(tau); eta=mp.mpf(eta); kappa=mp.mpf(kappa); phi=mp.mpf(phi)
    zlo=(1-eta)/eta
    lo=zlo*(1+mp.mpf('1e-20'))
    hi=max(zlo+1, mp.mpf('1'))
    while ratio_z(hi,tau,eta,kappa,phi) < 1:
        hi=2*hi+1
    for _ in range(300):
        mid=(lo+hi)/2
        if ratio_z(mid,tau,eta,kappa,phi) < 1:
            lo=mid
        else:
            hi=mid
    z=(lo+hi)/2
    return z**(1/eta)/tau, z

# Formula and sign checks over varied interior parameters.
sets=[
    ('0.01','0.05','0.03','0.4'),
    ('0.2','0.25','1.3','0.7'),
    ('2','0.8','0.4','0.15'),
    ('1.1','0.55','3','0.55'),
    ('0.7','0.9','0.9','0.95'),
]
for ts,es,ks,ps in sets:
    tau,eta,kappa,phi=map(mp.mpf,(ts,es,ks,ps))
    xzero=x0(tau,eta)
    assert hp(xzero/2,tau,eta,kappa,phi) < 0
    xmin,zstar=minimum(tau,eta,kappa,phi)
    assert xmin>xzero
    assert hp(xmin*(1-mp.mpf('1e-8')),tau,eta,kappa,phi) < 0
    assert hp(xmin*(1+mp.mpf('1e-8')),tau,eta,kappa,phi) > 0
    z0=(1-eta)/eta
    for q in ['0.001','0.1','1','10']:
        z=z0+mp.mpf(q)
        assert dlogR(z,eta,phi)>0
        num=mp.diff(lambda zz: mp.log(ratio_z(zz,tau,eta,kappa,phi)), z)
        assert abs(num-dlogR(z,eta,phi)) < mp.mpf('1e-50')

# Source Figure 2(b), first displayed parameter setting.
tau=mp.mpf('0.01'); eta=mp.mpf('0.05'); kappa=mp.mpf('0.03'); phi=mp.mpf('0.4')
xzero=x0(tau,eta)
xmin,zstar=minimum(tau,eta,kappa,phi)
assert abs(mp.log10(xzero)-mp.mpf('27.575072019056579')) < mp.mpf('1e-12')
assert abs(mp.log10(xmin)-mp.mpf('30.247567115373204')) < mp.mpf('1e-12')
assert hp(mp.mpf('100'),tau,eta,kappa,phi) < 0
assert hp(xmin*(1-mp.mpf('1e-7')),tau,eta,kappa,phi)<0
assert hp(xmin*(1+mp.mpf('1e-7')),tau,eta,kappa,phi)>0

print('VERIFY_OK')
print('figure_x0',mp.nstr(xzero,35))
print('figure_xstar',mp.nstr(xmin,35))
print('figure_zstar',mp.nstr(zstar,35))
print('hprime_at_100',mp.nstr(hp(mp.mpf('100'),tau,eta,kappa,phi),30))
