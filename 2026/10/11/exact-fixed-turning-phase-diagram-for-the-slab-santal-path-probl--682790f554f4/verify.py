import math

def simpson(f, a, b, n=20000):
    if n % 2:
        n += 1
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a+i*h)
    return s*h/3

def pa(n,a):
    return 0.5*math.sqrt(a*(1+a)**n)

def psi_F(n,a,p):
    L = math.log(1/a)
    def f(w):
        return (1-w)**n
    def S(w):
        return math.sqrt(4*p*p + w*f(w))
    psi = L - simpson(lambda w: f(w)/(S(w)*(S(w)+2*p)), -a, 1, 6000)
    F = 2*p*L + simpson(lambda w: f(w)/(S(w)+2*p), -a, 1, 6000)
    return psi,F

def root(n,a):
    lo = pa(n,a)*(1+1e-10)
    hi = max(1.0,2*lo)
    while psi_F(n,a,hi)[0] <= 0:
        hi *= 2
    for _ in range(70):
        mid=(lo+hi)/2
        if psi_F(n,a,mid)[0] < 0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

for n in (2,3,5):
    a=0.99
    p=root(n,a)
    ps=[p*0.9,p,p*1.1]
    vals=[psi_F(n,a,x)[0] for x in ps]
    assert vals[0] < vals[1] < vals[2]
    assert abs(vals[1]) < 2e-7

    h=1e-4*p
    Fp=psi_F(n,a,p+h)[1]
    Fm=psi_F(n,a,p-h)[1]
    deriv=(Fp-Fm)/(2*h)
    psi,_=psi_F(n,a,p)
    assert abs(deriv-2*psi) < 2e-5

for n in (2,3,5):
    a=0.999
    p=root(n,a)
    _,F=psi_F(n,a,p)
    cp=2**((n-2)/2)/math.sqrt(n+1)
    cF=2**((n+2)/2)/math.sqrt(n+1)
    rp=p*math.sqrt(1-a)/cp
    rF=F/math.sqrt(1-a)/cF
    assert abs(rp-1) < 0.02
    assert abs(rF-1) < 0.02

print("VERIFY_OK")
print("strict_momentum_phase=sampled")
print("derivative_identity=sampled")
print("boundary_constants=sampled")
