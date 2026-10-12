import math

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def qq(k,p):
    m=2.0**(k/2)
    a=math.pi/m
    w=complex(1-p+p*math.cos(2*a), p*math.sin(2*a))
    return 2.0**(-k)+(1-2.0**(-k))*abs(w)**(2**(k-1))*(0.5+0.5*math.cos(m*math.atan2(w.imag,w.real)))

def qlim(p):
    return math.exp(-math.pi**2*p*(1-p))*math.cos(math.pi*p)**2

def qc_nC(k,p):
    n=2**k-1
    phi=4*math.pi/(2.0**(k/2))
    x=math.sin(phi/2)
    c=1-h2((1-(1-2*p)*x)/2)
    return n*c

for k in (6,10,16):
    for p in (0.0,0.1,0.3,0.49):
        m=2.0**(k/2); a=math.pi/m
        w=complex(1-p+p*math.cos(2*a),p*math.sin(2*a))
        rhs=1-4*p*(1-p)*math.sin(a)**2
        assert abs(abs(w)**2-rhs) < 2e-14
for k in (6,10,20):
    assert abs(qq(k,0.5)-2.0**(-k)) < 5e-13
for p in (0.0,0.01,0.1,0.2,0.4,0.49):
    assert abs(qq(30,p)-qlim(p)) < 2e-6
for p in (0.0,0.1,0.3,0.49):
    target=2*math.pi**2*(1-2*p)**2/math.log(2)
    assert abs(qc_nC(28,p)-target) < 2e-4
# Endpoint coefficient check.
coef=math.pi**2*math.exp(-math.pi**2/4)
for eps in (1e-2,5e-3,2e-3):
    ratio=qlim(0.5-eps)/(eps*eps)
    assert abs(ratio/coef-1) < 0.01
print('VERIFY_OK')
