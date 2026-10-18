"""Reproducible arithmetic checks for a golden-slope torus drift spectrum.
Analytic continued-fraction and asymptotic arguments are in the accompanying proof.
"""
from decimal import Decimal, getcontext
getcontext().prec = 64
D=Decimal
phi=(D(1)+D(5).sqrt())/2
alpha=1/phi
A=(1+alpha*alpha)**2/D(25)


def fib_pairs(n):
    u,v=1,1
    for i in range(2,n+1):
        yield i,u,v
        u,v=v,u+v


def cost(a,p,q):
    return D((p*p+q*q)**2)+a*a*(D(p)-alpha*D(q))**2


def best_fib(a):
    pairs=list(fib_pairs(50))
    return min((cost(a,p,q),n,p,q) for n,p,q in pairs)


def exhaustive(a):
    ub,_,_,_=best_fib(a)
    # A Fourier frequency minimizing the expression satisfies
    # p^2+q^2 <= sqrt(ub), and hence |p|,|q| <= ub^(1/4).
    R=int(ub.sqrt().sqrt())+2
    ans=(ub,None,None)
    for q in range(-R,R+1):
        for p in range(-R,R+1):
            if p==q==0 or p*p+q*q>R*R:
                continue
            x=cost(a,p,q)
            if x<ans[0]:
                ans=(x,p,q)
    return ans,R

for aval in (100,1000,10000,100000,1000000):
    a=D(aval)
    fb=best_fib(a)
    brute,R=exhaustive(a)
    if abs(brute[0]-fb[0])>D('1e-45'):
        raise AssertionError(('non-Fibonacci spectrum',aval,fb,brute))
    print('Fourier exhaustive',aval,'frequency',fb[2:],'radius',R,'gap',round(float(fb[0]),8))

for n in range(2,35):
    fn=list(fib_pairs(n))[-1]
    _,p,q=fn
    error=abs(D(p)-alpha*D(q))
    if abs(error-phi**(-n))>D('1e-48'):
        raise AssertionError(('Fibonacci residual',n,error,phi**(-n)))
    for k in range(q, (list(fib_pairs(n+1))[-1][2])):
        # Bound every denominator strictly before the next convergent.
        trial=abs(D(round(alpha*D(k)))-alpha*D(k))
        if trial + D('1e-44') < error:
            raise AssertionError(('best approximation',n,k))
print('Fibonacci residual and denominator intervals: PASS')

xstar=(D(1)/(2*A))**(D(1)/D(6))
xc=(D(1)/(A*phi**2*(phi**2+1)))**(D(1)/D(6))
f=lambda x: A*x**4+x**(-2)
gmin=f(xstar)
gmax=f(xc)
assert xstar/phi < xc < xstar < phi*xc
assert abs(f(xc)-f(phi*xc))<D('1e-48')
assert gmin<gmax
print('A, lower, upper=',A,gmin,gmax)


def profile(s):
    return min(A*phi**(4*j)*s**(-D(4)/3)+s**(D(2)/3)*phi**(-2*j) for j in range(-12,13))

for s in (D('0.5'),D('1'),D('1.2'),D('2'),D('3'),D('5')):
    t=profile(s)
    assert gmin-D('1e-40')<=t<=gmax+D('1e-40')
    assert abs(t-profile(s*phi**3))<D('1e-40')
    for N in (14,20,28):
        a=phi**(3*N)*s
        fb=best_fib(a)[0]
        scaled=fb/a**(D(4)/3)
        tolerance=D('0.000000001') if N>=14 else D('0.0000001')
        if abs(scaled-t)>tolerance:
            raise AssertionError(('profile',s,N,scaled,t))
    print('phase',s,'envelope',t,'fine error',scaled-t)
print('All finite arithmetic and profile sanity checks passed; infinite statements use the proof.')
