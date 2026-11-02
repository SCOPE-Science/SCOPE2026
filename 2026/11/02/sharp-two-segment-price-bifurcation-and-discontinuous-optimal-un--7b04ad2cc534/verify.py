"""Independent, finite checks of the two-segment exponential-demand theorem.

Requires Python 3 standard library and SymPy. The analytical proof is in RESULT.md.
"""
import math
import sympy as s

p, k = s.symbols('p k', real=True)
poly = k*p*p - (k+1)*p + 2
log_derivative = -(k-1) + k/(k*p-1) + 1/(1-p)
assert s.factor(log_derivative-(k-1)*poly/((1-p)*(k*p-1))) == 0
assert s.factor(s.discriminant(poly,p)) == k*k-6*k+1


def H(p,k):
    return math.exp(-(k-1)*p)*(k*p-1)/(1-p)


def revenue(p,k,w):
    return p*(w*math.exp(-p)+(1-w)*math.exp(-k*p))


def deriv(p,k,w):
    return w*math.exp(-p)*(1-p)+(1-w)*math.exp(-k*p)*(1-k*p)


def root(f,a,b):
    fa = f(a)
    fb = f(b)
    assert fa*fb < 0, (a,b,fa,fb)
    for _ in range(100):
        m = (a+b)*0.5
        fm = f(m)
        if fa*fm > 0:
            a,fa = m,fm
        else:
            b,fb = m,fm
    return (a+b)*0.5


def classify(k,w):
    if k <= 3+2*math.sqrt(2):
        return [root(lambda x:deriv(x,k,w),1/k,1)]
    disc = math.sqrt(k*k-6*k+1)
    a = (k+1-disc)/(2*k)
    b = (k+1+disc)/(2*k)
    low = H(b,k)/(1+H(b,k))
    high = H(a,k)/(1+H(a,k))
    if low < w < high:
        f=lambda x:deriv(x,k,w)
        return [root(f,1/k,a),root(f,a,b),root(f,b,1)]
    return [root(lambda x:deriv(x,k,w),1/k,1)]

for kval in (1.01,2,5.8,5.828427124746,6,10,20,100):
    for w in (0.001,0.03,0.1,0.5,0.95,0.999):
        x=classify(kval,w)
        for q in x:
            assert abs(deriv(q,kval,w))<1e-9
            assert 1/kval-1e-14 < q <= 1, (kval,w,q)
        if len(x)==3:
            assert revenue(x[0],kval,w)>revenue(x[1],kval,w)
            assert revenue(x[2],kval,w)>revenue(x[1],kval,w)
            assert x[0]<x[1]<x[2]

kval=10
b,a = ((kval+1+t*math.sqrt(kval*kval-6*kval+1))/(2*kval) for t in (1,-1))
w_lower = H(b,kval)/(1+H(b,kval))
w_upper = H(a,kval)/(1+H(a,kval))
def gap(w):
    xx=classify(kval,w)
    assert len(xx)==3
    return revenue(xx[-1],kval,w)-revenue(xx[0],kval,w)
w_star = root(gap,w_lower+1e-9,w_upper-1e-9)
p1,p2,p3=classify(kval,w_star)
assert abs(w_star-0.1228819699964)<1e-11
assert abs(p1-0.1437379172148)<1e-10
assert abs(p3-0.9915241809537)<1e-10
assert abs(gap(w_star))<1e-13
assert gap(w_star-0.01)<0<gap(w_star+0.01)
print('PASS: symbolic derivative and discriminant; 48 parameter examples; unique numerical switch bracket')
print('k=10, lower/upper mixture weight:',w_lower,w_upper)
print('coexistence weight:',w_star)
print('three stationary prices:',p1,p2,p3)
print('equal maximizing revenue:',revenue(p1,kval,w_star))
