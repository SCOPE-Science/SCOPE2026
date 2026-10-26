"""Exact computational checks for the characteristic-three cyclic-quintic strata.
Run: python cyclic_quintic_char3_checker.py (Python 3 standard library only).
The universal geometric conclusion also requires the proof in RESULT.md.
"""
from itertools import product
P = 3

def trim(v):
    while len(v)>1 and v[-1]%P == 0: v.pop()
    return v

def deriv(f):
    return trim([(i*f[i])%P for i in range(1,len(f))] or [0])

def rem(a,b):
    a=trim(a[:]); b=trim(b[:]); assert b != [0]
    inv=pow(b[-1],-1,P)
    while len(a)>=len(b) and a != [0]:
        d=len(a)-len(b); q=a[-1]*inv%P
        for i,t in enumerate(b): a[i+d]=(a[i+d]-q*t)%P
        trim(a)
    return a

def gcd(a,b):
    while b != [0]: a,b=b,rem(a,b)
    return a

def field_add(a,b): return ((a[0]+b[0])%3,(a[1]+b[1])%3)
def field_mul(a,b): return ((a[0]*b[0]-a[1]*b[1])%3,(a[0]*b[1]+a[1]*b[0])%3)
def field_pow(a,n):
    z=(1,0)
    while n:
        if n&1:z=field_mul(z,a)
        a=field_mul(a,a);n//=2
    return z

def evaluate(f,a):
    acc=(0,0)
    for v in reversed(f): acc=field_add(field_mul(acc,a),(v,0))
    return acc

def count(f,q):
    els=[(a,0) for a in range(3)] if q==3 else list(product(range(3),repeat=2))
    return 1+sum(field_pow(y,3)==evaluate(f,x) for x in els for y in els)

examples={
    'four_simple': [1,1,0,1,0,1],        # x^5+x^3+x+1
    'triple_and_simple':[2,0,0,0,1,1], # x^5+x^4+2
    'quadruple':[1,0,0,0,0,1],        # x^5+1
}
for name,f in examples.items():
    d=deriv(f)
    assert gcd(f,d)==[1] or len(gcd(f,d))==1
    assert len(f)==6 and f[-1]==1
    if name=='four_simple':
        assert len(gcd(d,deriv(d)))==1
        assert f[1]!=f[4]*f[2]%3
    elif name=='triple_and_simple':
        # 2*x^3*(x-1) = 2*x^4+x^3 modulo 3
        assert d==[0,0,0,1,2]
        assert f[1]==f[4]*f[2]%3
        assert f[2]!=(-f[4]**3)%3
    else:
        assert d==[0,0,0,0,2]
        assert f[2]==-f[4]**3%3
    for q in (3,9):
        assert count(f,q)==q+1,(name,q,count(f,q))
    print(name, 'smooth, derivative stratum correct, #F3=4, #F9=10')
# All 3^5 monic quintics: derivative only 4-simple, 3+1, or 4.
for c in product(range(3), repeat=5):
    f=list(c)+[1]
    d=deriv(f)
    if f[1]!=f[4]*f[2]%3:
        assert len(gcd(d,deriv(d)))==1
    elif f[2]!=(-f[4]**3)%3:
        # root r of r^3=-a2 equals -a2 over F3
        r=(-f[2])%3
        assert rem(d,[( -r)%3,1])==[0]
        assert len(gcd(d,deriv(d)))==4 # degree 3
    else:
        assert len(gcd(d,deriv(d)))==4
print('ALL_243_COEFFICIENT_PATTERNS_OK')
print('CHECK_OK')
