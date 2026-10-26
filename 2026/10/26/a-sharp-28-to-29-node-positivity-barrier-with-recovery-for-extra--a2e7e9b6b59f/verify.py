"""Independent exact checks for extrapolated backward-Euler diffusion on complete graphs."""
import sympy as s
x,n=s.symbols('x n',positive=True)
r=8/(x+2)**2-1/(x+1)
den=(x+2)**2*(x+1)
hnum=s.factor((1+(n-1)*r)*den)
assert s.expand(hnum-(x**3+(6-n)*x**2+(4*n+4)*x+4*n))==0
assert s.factor((1-r)*den)==x*(x*x+6*x+4)
assert s.factor(hnum.subs(n,28)- (x*(x-11)**2-5*x+112))==0
assert hnum.subs({n:29,x:12})==-28
for N in [2,3,5,10,28,29,35]:
    J=s.ones(N)
    L=N*s.eye(N)-J
    for X in [s.Rational(1,5),s.Rational(12),s.Rational(100)]:
        h=X/N
        A=s.eye(N)+h*L/2
        B=s.eye(N)+h*L
        T=2*A.inv()**2-B.inv()
        R=r.subs(x,X)
        P=(s.eye(N)-J/N)*R+J/N
        assert T==P,(N,X)
        assert T*s.ones(N,1)==s.ones(N,1)
        assert all(T[i,j]>=0 for i in range(N) for j in range(N)) == (hnum.subs({n:N,x:X})>=0)
print('VERIFY_OK symbolic identities=4 exact full-matrix cases=21 orders=7')
