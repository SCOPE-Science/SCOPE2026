from decimal import Decimal, getcontext
from math import factorial
getcontext().prec = 60

def i0(x):
    x = Decimal(x)
    term = Decimal(1)
    s = term
    k = 0
    q = x*x/Decimal(4)
    while True:
        k += 1
        term *= q/Decimal(k*k)
        old = s
        s += term
        if s == old:
            return s

def fidelity_closed(x):
    x = Decimal(str(x))
    return x.exp()*i0(x)/(Decimal(2)*i0(Decimal(2)*x))

def fidelity_double(x, K=100):
    x = Decimal(str(x))
    s = Decimal(0)
    for k in range(K+1):
        diag = Decimal(0)
        fk = factorial(k)
        for m in range(k+1):
            n = k-m
            diag += Decimal(fk)/Decimal(factorial(m)**2*factorial(n)**2)
        s += (x/Decimal(2))**k * diag
    return s/(Decimal(2)*i0(Decimal(2)*x))

def asym2(x):
    x = Decimal(str(x))
    rt2 = Decimal(2).sqrt()
    return (Decimal(1)/rt2)*(Decimal(1)+Decimal(1)/(Decimal(16)*x)+Decimal(25)/(Decimal(512)*x*x))

for x in ['0.25','0.5','1','1.2357','2']:
    a = fidelity_double(x)
    b = fidelity_closed(x)
    assert abs(a-b) < Decimal('1e-45'), (x,a,b,a-b)
assert abs(fidelity_closed('1.2357')-Decimal('0.7588362319921053')) < Decimal('2e-16')
err20 = abs(fidelity_closed('20')-asym2('20'))
err40 = abs(fidelity_closed('40')-asym2('40'))
assert err40 < err20
assert fidelity_closed('40') > Decimal(1)/Decimal(2).sqrt()
print('VERIFY_OK series_points=5 F_1.2357=%s err20=%s err40=%s' % (fidelity_closed('1.2357'),err20,err40))
