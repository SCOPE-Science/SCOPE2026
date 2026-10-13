from math import exp, factorial, pi, sqrt
try:
    import mpmath as mp
except ImportError as exc:
    raise SystemExit("This regression checker requires mpmath") from exc

mp.mp.dps = 60

def exact_formula(lam):
    z=2*lam
    r=mp.e**(-z)*mp.besseli(0,z)
    q=mp.e**(-z)*(mp.besseli(0,z)+mp.besseli(1,z))
    em=lam*(1-q); ea=lam*(1+q)
    vm=lam*(1-r-lam*q*q); va=lam*(1+r-lam*q*q)
    return em,ea,vm,va

def brute(lam):
    # Tail threshold chosen so omitted mass is negligible at the tested lambdas.
    nmax=int(mp.ceil(lam+14*mp.sqrt(lam+1)+35))
    ps=[mp.e**(-lam)*lam**k/mp.factorial(k) for k in range(nmax+1)]
    mass=sum(ps)
    vals=[]
    for use_max in (False,True):
        e=e2=mp.mpf('0')
        for i,p in enumerate(ps):
            for j,q in enumerate(ps):
                v=max(i,j) if use_max else min(i,j)
                e += p*q*v
                e2 += p*q*v*v
        vals.extend([e,e2-e*e])
    em,vm,ea,va=vals
    return mass,em,ea,vm,va

for lam in [mp.mpf('0.1'),mp.mpf('1'),mp.mpf('5'),mp.mpf('20')]:
    mass,em_b,ea_b,vm_b,va_b=brute(lam)
    em,ea,vm,va=exact_formula(lam)
    assert 1-mass < mp.mpf('1e-24')
    for x,y in [(em,em_b),(ea,ea_b),(vm,vm_b),(va,va_b)]:
        assert abs(x-y) < mp.mpf('2e-20')

c=(mp.mpf('0.5')-1/mp.pi)/mp.sqrt(mp.pi)
for lam in [mp.mpf('100'),mp.mpf('400'),mp.mpf('1600')]:
    em,ea,vm,va=exact_formula(lam)
    base=1-1/mp.pi
    sm=mp.sqrt(lam)*(vm/em-base)
    sa=mp.sqrt(lam)*(va/ea-base)
    assert abs(sm-c) < mp.mpf('0.012')
    assert abs(sa+c) < mp.mpf('0.012')
print("VERIFY_OK")
