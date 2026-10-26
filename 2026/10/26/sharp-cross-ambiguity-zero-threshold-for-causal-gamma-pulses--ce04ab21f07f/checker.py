"""Check symbolic stability identities and direct cross-ambiguity integrals."""
import math
import sympy as sp
import mpmath as mp

z, n = sp.symbols('z n')
P = lambda m: sum(sp.factorial(m)/sp.factorial(k)*z**k for k in range(m+1))

# Hurwitz leading principal minors for monic polynomial in descending order.
def minors(m):
    co = [sp.factorial(m)/sp.factorial(m-j) for j in range(m+1)]
    H = sp.Matrix(m, m, lambda i,j: co[2*j-i+1] if 0 <= 2*j-i+1 <= m else 0)
    return [sp.factor(H[:k,:k].det()) for k in range(1,m+1)]

expected={1:[1],2:[2,4],3:[3,12,72],4:[4,24,192,4608],5:[5,40,0,-38400,-4608000]}
for m, vals in expected.items():
    actual=minors(m)
    assert actual == vals,(m,actual,vals)
    print('Hurwitz minors',m,actual)

b1=n; b2=n*(n-1); b3=n*(n-1)*(n-2)
b4=n*(n-1)*(n-2)*(n-3); b5=n*(n-1)*(n-2)*(n-3)*(n-4)
D3=sp.factor(b1*b2*b3-b1*b1*b4-b3*b3+b1*b5)
assert sp.expand(D3+2*n**2*(n-1)*(n-2)*(n-5)) == 0
print('General third determinant:',D3)
for m in range(1,12):
    assert sp.gcd(P(m),sp.diff(P(m),z)) == 1
    if m >=6:
        assert D3.subs(n,m) == minors(m)[2] if m<=7 else D3.subs(n,m)<0
print('Squarefreeness checked through degree 11; general proof uses E_m-E_{m-1}=z^m/m!')

mp.mp.dps=60
Em=lambda m,w:sum(w**k/mp.factorial(k) for k in range(m+1))
root=mp.findroot(lambda w:Em(5,w),(mp.mpc('0.23','3.1'),mp.mpc('0.25','3.16')))
assert root.real > 0 and abs(Em(5,root))<mp.mpf('1e-50')
T=root.real/2; W=2*root.imag/root.real
print('Fifth-degree positive-delay witness root:',mp.nstr(root,45))
print('Corresponding delay and angular frequency:',mp.nstr(T,40),mp.nstr(W,40))

for m,t,w in [(0,mp.mpf('0.8'),mp.mpf('0.4')),(2,mp.mpf('1.1'),mp.mpf('-1.7')),(5,mp.mpf('0.4'),mp.mpf('1.6')),(6,mp.mpf('-0.4'),mp.mpf('1.3'))]:
    q=2+1j*w
    if t>=0:
        direct=mp.exp(-t-1j*w*t/2)*mp.quad(lambda s:(s+t)**m*mp.exp(-q*s),[0,mp.inf])
        formula=mp.exp(-t-1j*w*t/2)*mp.factorial(m)*Em(m,q*t)/q**(m+1)
    else:
        direct=mp.exp(t+1j*w*t/2)*mp.quad(lambda s:s**m*mp.exp(-q*s),[0,mp.inf])
        formula=mp.exp(t+1j*w*t/2)*mp.factorial(m)/q**(m+1)
    err=abs(direct-formula)
    assert err<mp.mpf('1e-48'),(m,t,w,err)
    print('Integral',m, 'delay sign', 'positive' if t>=0 else 'negative', 'absolute error',mp.nstr(err,7))
print('PASS: all checks')
