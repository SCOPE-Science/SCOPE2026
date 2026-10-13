import mpmath as mp

mp.mp.dps = 80

def zfun(t,beta,theta):
    x=(t/theta)**(1/beta)
    return x/(1+x)

def survival(t,a,b,beta,theta):
    z=zfun(t,beta,theta)
    return (mp.e**(-(z**a)/b)-mp.e**(-1/b))/(1-mp.e**(-1/b))

def tail_constant(a,b,beta,theta):
    return (a*mp.e**(-1/b)/(b*(1-mp.e**(-1/b))))*(theta**(1/beta))

rows=[
    (mp.mpf("0.64"),mp.mpf("0.8"),mp.mpf("0.5"),mp.mpf("0.8")),
    (mp.mpf("0.80"),mp.mpf("0.8"),mp.mpf("0.5"),mp.mpf("0.8")),
    (mp.mpf("1.60"),mp.mpf("0.8"),mp.mpf("0.5"),mp.mpf("0.8")),
    (mp.mpf("2.80"),mp.mpf("0.8"),mp.mpf("0.5"),mp.mpf("0.8")),
]

for a,b,beta,theta in rows:
    C=tail_constant(a,b,beta,theta)
    assert C>0
    ratios=[]
    for t in (mp.mpf("1e2"),mp.mpf("1e4"),mp.mpf("1e6")):
        ratios.append((t**2)*survival(t,a,b,beta,theta)/C)
    assert abs(ratios[-1]-1) < abs(ratios[0]-1)
    assert abs(ratios[-1]-1) < mp.mpf("1e-5")
    assert 2*C>0
    print("row", mp.nstr(a,8), "C", mp.nstr(C,20),
          "normalized_tail", mp.nstr(ratios[-1],20),
          "log_divergence_coefficient", mp.nstr(2*C,20))

print("VERIFY_OK")
