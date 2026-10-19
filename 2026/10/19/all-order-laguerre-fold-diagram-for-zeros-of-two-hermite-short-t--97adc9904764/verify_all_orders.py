"""Reproducible finite checks for the Laguerre–Hermite STFT zero phase diagram.

This tests the published formula against direct STFT integrals and probes the
all-order Sturm assertion for finitely many n; the all-order theorem is analytic.
Python 3 with SymPy and mpmath required.
"""
import math
import sympy as sp
import mpmath as mp

s=sp.symbols('s',positive=True)
for n in range(1,13):
 L=sp.laguerre(n,s)
 R=s**sp.Rational(-n,2)*L
 O=sp.expand(s*sp.diff(R,s,2)+(n+1-s)*sp.diff(R,s)+(sp.Rational(n*n,4)/s+sp.Rational(n,2))*R)
 assert sp.simplify(O)==0,(n,O)
 # Finite-degree critical polynomial independent of half-integer power.
 H=sp.expand(2*s*sp.diff(L,s)-n*L)
 roots=sp.polys.polytools.intervals(H,eps=sp.Rational(1,10**12))
 pos=[]
 for (aa,bb),mult in roots:
  if aa > 0:
   assert mult==1
   pos.append(float((aa+bb)/2))
 assert len(pos)==n-1,(n,pos)
 lag=sorted(float(sp.re(rr)) for rr in sp.nroots(L,maxsteps=500) if abs(float(sp.im(rr)))<1e-12)
 assert len(lag)==n
 for j,v in enumerate(pos):assert lag[j]<v<lag[j+1]
print('PASS: exact Laguerre-ratio Sturm ODE for n=1,...,12')
print('PASS: each critical-polynomial zero lies in one distinct Laguerre gap for n=1,...,12')

# Direct defining-integral checks across nontrivial positive Hermite orders.
mp.mp.dps=45
pi=mp.pi
h0=lambda x:mp.power(2,mp.mpf('0.25'))*mp.exp(-pi*x*x)
def h(n,x):return mp.hermite(n,mp.sqrt(2*pi)*x)*h0(x)/mp.sqrt(mp.power(2,n)*mp.factorial(n))
def direct(n,q,eta,t):
 return mp.quad(lambda x:h(n,x)*(h0(x-q)+t*h(n,x-q))*mp.exp(2j*pi*eta*x),[-mp.inf,mp.inf])
def formula(n,q,eta,t):
 z=mp.sqrt(pi)*mp.mpc(q,eta)
 return mp.exp(1j*pi*q*eta)*mp.exp(-pi*(q*q+eta*eta)/2)*(z**n/mp.sqrt(mp.factorial(n))+t*mp.laguerre(n,0,abs(z)**2))
residuals=[]
for n in [1,2,3,4,5]:
 for q,eta,t in [('.2','.3','.8'),('.5','-.2','1.4')]:
  qq,ee,tt=map(mp.mpf,[q,eta,t])
  error=abs(direct(n,qq,ee,tt)-formula(n,qq,ee,tt))
  assert error<mp.mpf('1e-35'),(n,q,eta,t,error)
  residuals.append(error)
print('PASS: 10 defining-integral comparisons with n=1,...,5; worst residual',mp.nstr(max(residuals),8))

# Entire symmetric threshold example n=2.
rt2=sp.sqrt(2)
tau=(1+rt2)/2
L=sp.laguerre(2,s)
H=sp.expand(2*s*sp.diff(L,s)-2*L)
assert sp.simplify(H- (s*s-2))==0
assert sp.simplify((sp.sqrt(2)/(sp.sqrt(sp.factorial(2))*abs(L.subs(s,rt2))))-tau)==0
print('PASS: n=2 transition occurs at (1+sqrt(2))/2, giving 4/6/8 zeros')

# Numerical n=3,...,7 critical thresholds and total counts, as a finite diagnostic.
for n in range(3,8):
 L=sp.laguerre(n,s)
 H=sp.Poly(sp.expand(2*s*sp.diff(L,s)-n*L),s)
 betas=sorted(float(sp.re(v)) for v in sp.nroots(H,maxsteps=500) if abs(float(sp.im(v)))<1e-11 and float(sp.re(v))>0)
 assert len(betas)==n-1
 ts=[float(beta**(n/2)/(math.sqrt(math.factorial(n))*abs(float(L.subs(s,beta))))) for beta in betas]
 assert all(t>0 and math.isfinite(t) for t in ts)
 tmin=min(ts);tmax=max(ts)
 def count(t):return 2*n+2*n*sum(t>tau_j for tau_j in ts)
 assert count(tmin/2)==2*n
 assert count(2*tmax)==2*n*n
 print('n=%d, threshold list=%s, small/large zero counts=%d/%d' %(n,[round(v,7) for v in ts],count(tmin/2),count(2*tmax)))
print('ALL TESTS PASSED; finite checks are not proofs for unbounded n.')
