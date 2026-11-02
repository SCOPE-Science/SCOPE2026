"""Independent algebraic and finite-Fourier diagnostics for the angular-tumble theorem.

Requires Python 3, SymPy and mpmath. Tests do not replace the analytic
Fourier perturbation argument or global measure inequality in RESULT.md.
"""
import sympy as sp
import mpmath as mp

A,B,w,v=sp.symbols('A B w v',positive=True,real=True)
I=sp.I
rp=1/(A-I*w)
rm=1/(A+I*w)
r2p=1/(B-2*I*w)
r2m=1/(B+2*I*w)
c2=sp.cancel(v**2*(rp+rm)/4)
c4=sp.cancel(v**4*(rp**2*r2p+rm**2*r2m-(rp+rm)*(rp**2+rm**2))/16)
assert sp.simplify(c2.subs(A,w)-v**2/(4*w))==0
assert sp.simplify(c4.subs(A,w)+v**4/(8*w*(B**2+4*w**2)))==0
print('PASS: symbolic fourth-cumulant coefficient at optimal persistence')

# Algebraic test cases for exact half-turn, quarter-turn, and sixth-turn laws.
tests=[('half-turn',sp.Rational(-1),sp.Rational(1),sp.Rational(1),sp.Rational(4)),
       ('quarter-turn',sp.Rational(0),sp.Rational(-1),sp.Rational(2),sp.Rational(8)),
       ('sixth-turn',sp.Rational(1,2),sp.Rational(-1,2),sp.Rational(4),sp.Rational(10))]
for name,f1,f2,lam,bb in tests:
    assert sp.simplify(1+lam*(1-f1)-3)==0
    assert sp.simplify(4+lam*(1-f2)-bb)==0
    assert sp.simplify(24*c4.subs({A:3,B:bb,w:3,v:2})+48/(3*(bb**2+36)))==0
    print('PASS: exact distribution',name,'fourth cumulant',sp.factor(24*c4.subs({A:3,B:bb,w:3,v:2})))

# Sharp-bound identities for any positive D<w.
D,t=sp.symbols('D t',positive=True,real=True)
Btheta=4*D+2*(w-D)*(1+t)
assert sp.simplify(Btheta.subs(t,0)-(2*w+2*D))==0
assert sp.simplify(Btheta.subs(t,1)-4*w)==0
assert sp.simplify(Btheta.subs(t,-1)-4*D)==0
assert sp.simplify((20*w*w)/(16*D*D+4*w*w)-5*w*w/(4*D*D+w*w))==0
print('PASS: sharp endpoint identities and range amplification')

# Independent finite Fourier-matrix eigenvalue diagnostic. The Fourier
# truncation is exact through order four and higher-mode effects are O(k^6).
mp.mp.dps=45
wm=mp.mpf(3);Dm=mp.mpf(1);vm=mp.mpf(2)
for name,f1,f2,lam,bb in tests:
    angle={'half-turn':mp.pi,'quarter-turn':mp.pi/2,'sixth-turn':mp.pi/3}[name]
    rate=mp.mpf(int(lam))
    def near_zero_eigenvalue(k):
        width=4;n=2*width+1
        M=mp.matrix(n)
        for j in range(n):
            z=j-width
            M[j,j]=-Dm*z*z+mp.j*wm*z+rate*(mp.cos(z*angle)-1)
            if j>0:M[j,j-1]=k*vm/2
            if j<n-1:M[j,j+1]=k*vm/2
        eigenvalues=mp.eig(M,left=False,right=False)
        return mp.re(min(eigenvalues,key=lambda y:abs(y)))
    step=mp.mpf('0.02')
    a4_estimate=(near_zero_eigenvalue(2*step)-4*near_zero_eigenvalue(step))/(12*step**4)
    a4_exact=-vm**4/(8*wm*(mp.mpf(int(bb))**2+4*wm**2))
    err=abs(a4_estimate-a4_exact)
    assert err<mp.mpf('0.00001'),(name,err)
    print('PASS: independent tilted-spectrum',name,'absolute fourth-order error',mp.nstr(err,7))
print('PASS: all analytic identities and finite diagnostics')
