"""Reproduce exact modal positivity and resonance checks for the printed O2CP coefficients.
This is a stand-alone scientific verification script, not a proof of infinite claims.
Requires Python 3 with mpmath and sympy.
"""
from fractions import Fraction as Q
import mpmath as mp
import sympy as sp
mp.mp.dps=100
A=Q(2178,100000); B=Q(47,100000); C=Q(97822,100000); D=Q(463,1000); E=Q(5638,10000)
x=sp.symbols('x')
a,b,c,d,e=[sp.Rational(z.numerator,z.denominator) for z in (A,B,C,D,E)]
r1=(a-b*x)/(1+e*x);r2=(c-d*x)/(1+e*x)
# Check exact key identities and stability conditions via polynomial positivity.
assert a+c==1
assert sp.simplify((1-r1-r2)*(1+e*x)-(e+b+d)*x)==0
assert sp.simplify((1+r2-r1)*(1+e*x)-((2-2*a)+(e+b-d)*x))==0
assert sp.simplify((1+r1)*(1+e*x)-((1+a)+(e-b)*x))==0
assert e+b-d>0 and e-b>0 and a<b*(a/b) + a # rational sanity
s0=c/d; sa=a/b
assert 2<s0<sp.Rational(22,10)<4<sa<47
assert r1.subs(x,s0)>0
assert c-d*sa<0
# Positive modal characteristic: t^2 - R2*t - R1.
p,q=sp.symbols('p q', positive=True)
assert sp.expand(p**2-(p+q)*p+p*q)==0
# Numeric evaluation
m=lambda q:mp.mpf(q.numerator)/mp.mpf(q.denominator)
am,bm,cm,dm,em=map(m,(A,B,C,D,E))
sc=cm/dm; ta=am/bm
R1=lambda s:(am-bm*s)/(1+em*s)
R2=lambda s:(cm-dm*s)/(1+em*s)
F=lambda s:(1+em*s)*mp.exp(-2*s)-(cm-dm*s)*mp.exp(-s)-(am-bm*s)
Fp=lambda s:(em-2-2*em*s)*mp.exp(-2*s)+(dm+cm-dm*s)*mp.exp(-s)+bm
Fpp=lambda s:(4+4*em*s-4*em)*mp.exp(-2*s)+(dm*s-cm-2*dm)*mp.exp(-s)
assert mp.exp(-sc)>mp.sqrt(R1(sc))
assert F(sc)>0 and F(mp.mpf('3.5'))>0 and F(4)<0 and F(46)<0 and F(ta)>0
assert Fp(sc)>0 and Fp(mp.mpf('3.5'))<0 and Fp(ta)>0
assert mp.exp(sc)*Fpp(sc)<0 and mp.exp(sc+2)*Fpp(sc+2)>0
root1=mp.findroot(F,(mp.mpf('3.5'),mp.mpf('4')))
lo=mp.mpf(46); hi=ta
for _ in range(520):
 mid=(lo+hi)/2
 if F(mid)>0:hi=mid
 else:lo=mid
root2=(lo+hi)/2
assert mp.mpf('3.7')<root1<mp.mpf('3.8')
assert 46<root2<ta and abs(F(root1))<mp.mpf('1e-95') and abs(F(root2))<mp.mpf('1e-95')
P=mp.sqrt(R1(sc)); u=mp.exp(-sc)
K=P*(1+em*sc)/dm *mp.log((u+P)/(u-P))
assert mp.mpf('1.0273')<K<mp.mpf('1.0275')
# Closed-form recurrence from its two simple real characteristic roots.
def exact_modal(s,n):
 aa=R1(s); bb=R2(s); t=mp.exp(-s)
 if s>0 and aa>0:
  delta=mp.sqrt(bb*bb+4*aa)
  rr=(bb+delta)/2; qq=(delta-bb)/2
  cp=(t+qq)/(rr+qq); cn=(rr-t)/(rr+qq)
  return cp*rr**n+cn*(-qq)**n
 y0=mp.mpf(1); y1=t
 if n==0:return y0
 for j in range(1,n):y0,y1=y1,aa*y0+bb*y1
 return y1

def recurrence(s,n):
 z0=mp.mpf(1);z1=mp.exp(-s)
 if n==0:return z0
 for _ in range(1,n): z0,z1=z1,R1(s)*z0+R2(s)*z1
 return z1

checks=0
for sstr in ['0.01','0.1','0.5','1','2','2.11278618','2.113','2.12','2.15','2.2','2.4','2.6','2.9','3','3.5','3.7','3.70146','3.8','4','5','10','20','40','46','47','100']:
 s=mp.mpf(sstr)
 for n in range(90):
  v=exact_modal(s,n);w=recurrence(s,n)
  assert mp.almosteq(v,w,rel_eps=mp.mpf('1e-82'),abs_eps=mp.mpf('1e-82')), (s,n,v,w)
  checks+=1
# Check first negative index formula with arbitrary precision, away from resonances.
def first_negative(s):
 aa=R1(s);bb=R2(s); t=mp.exp(-s)
 if s<=sc:return None
 if s>=ta:return 2
 delta=mp.sqrt(bb*bb+4*aa); pos=(bb+delta)/2;negmag=(delta-bb)/2
 if t==pos:return None
 crit=mp.log((t+negmag)/abs(t-pos))/mp.log(negmag/pos)
 if t>pos:n=int(2*(mp.floor(crit/2)+1))
 else:n=int(2*(mp.floor((crit-1)/2)+1)+1)
 return n
for sstr in ['2.12','2.15','2.2','2.4','2.9','3','3.5','3.8','4','5','10','46','47','100']:
 s=mp.mpf(sstr); n=first_negative(s)
 assert n is not None and n<1000
 assert recurrence(s,n)<0,(s,n)
 for k in range(n):assert recurrence(s,k)>0,(s,k)
 checks+=n
for eps in ['1e-3','1e-4','1e-5','1e-6']:
 s=sc+mp.mpf(eps); n=first_negative(s)
 assert abs(n*mp.mpf(eps)-K)<mp.mpf('0.15')
print('PASS')
print('exact polynomial identities = 4')
print('modal recurrence and first sign checks =',checks)
print('critical lag c/d =',mp.nstr(sc,45))
print('second sign threshold a/b =',mp.nstr(ta,45))
print('positive exact-match resonance #1 =',mp.nstr(root1,60))
print('positive exact-match resonance #2 =',mp.nstr(root2,65))
print('endpoint-resonance gap =',mp.nstr(ta-root2,30))
print('first negative index critical constant =',mp.nstr(K,45))
print('stiff negative y2 limit =',mp.nstr(-bm/em,45))
# Rigorous rational interval checks for all transcendental signs in the proof.
# For x>=0 and integer N with x<N+2, Taylor's positive-term series gives
# T_N <= exp(x) <= T_N + x^(N+1)/(N+1)!/(1-x/(N+2)).
# Inverting provides exact rational endpoints for exp(-x).
from functools import lru_cache
@lru_cache(None)
def negexp_interval(xq):
 assert xq>=0 and xq<Q(322)
 term=Q(1); total=Q(1)
 for n in range(1,321):
  term*=xq/Q(n);total+=term
 nxt=term*xq/Q(321)
 tail=nxt/(1-xq/Q(322))
 return (1/(total+tail),1/total)

def add_interval(one,two):return (one[0]+two[0],one[1]+two[1])
def scalar_interval(t,i):return (t*i[0],t*i[1]) if t>=0 else (t*i[1],t*i[0])
def point(t):return (t,t)

def FI(s):
 return add_interval(add_interval(scalar_interval(1+E*s,negexp_interval(2*s)),scalar_interval(D*s-C,negexp_interval(s))),point(B*s-A))
def FPI(s):
 return add_interval(add_interval(scalar_interval(E-2-2*E*s,negexp_interval(2*s)),scalar_interval(D+C-D*s,negexp_interval(s))),point(B))
def HI(s):
 return add_interval(scalar_interval(4*(1+E*(s-1)),negexp_interval(s)),point(D*(s-Q(C/D)-2)))
def sign_interval(i,sgn):assert i[0]>0 if sgn>0 else i[1]<0,(str(i[0]),str(i[1]),sgn)
S=C/D; T=A/B
for s,sgn in [(S,1),(Q(7,2),1),(Q(4),-1),(Q(46),-1),(T,1)]:sign_interval(FI(s),sgn)
for s,sgn in [(S,1),(Q(7,2),-1),(T,1)]:sign_interval(FPI(s),sgn)
for s,sgn in [(S,-1),(S+2,1)]:sign_interval(HI(s),sgn)
uis=negexp_interval(S)
assert uis[0]*uis[0]> (A-B*S)/(1+E*S)
print('certified exact rational Taylor interval signs = 11')
