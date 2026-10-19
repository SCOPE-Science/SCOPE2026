"""Exact checks for a two-leader finite-gain placement theorem on complete bipartite networks.
Run: python verify_bipartite.py (requires sympy >=1.12).
These finite checks supplement, but do not replace, the all-parameter algebraic proof.
"""
import sympy as s

p,q,a,b=s.symbols('p q a b',positive=True)
N=p+q
T=(p-1)/q+(q-1)/p+1/N
Gaa=(1-1/p)/q+q/(p*N**2)
Gab_same=-1/(p*q)+q/(p*N**2)
Gbb=(1-1/q)/p+p/(q*N**2)
Gbb_same=-1/(p*q)+p/(q*N**2)
Gab=-1/N**2
Haa=(1-1/p)/q**2+q/(p*N**3)
Hab_same=-1/(p*q**2)+q/(p*N**3)
Hbb=(1-1/q)/p**2+p/(q*N**3)
Hbb_same=-1/(q*p**2)+p/(q*N**3)
Hab=-1/N**3

def performance(x,y,z,xx,yy,zz):
  D=a+b+a*b*(x+y-2*z)
  U=N*(1+a*x+b*y+a*b*(x*y-z*z))-a*b*(xx+yy-2*zz)
  return T+U/D
JAA=performance(Gaa,Gaa,Gab_same,Haa,Haa,Hab_same)
JBB=performance(Gbb,Gbb,Gbb_same,Hbb,Hbb,Hbb_same)
JAB=performance(Gaa,Gbb,Gab,Haa,Hbb,Hab)
JBA=performance(Gbb,Gaa,Gab,Hbb,Haa,Hab)

S=q*(q*q-q-3*p*p)
H=(p-2)*(q*q-p*(p-1))+q*(p+2)
W=(2*p-1)*q*(q-1)-p*p*(2*p-5)
C=b*p*q*q*(q-p)*(N-1)
B=q*(2*p*p*q+b*W)
P=(S-b*H)*a*a-B*a-C
Delta=p*q*(2*a*b+q*(a+b))*(a*b*(N-1)+p*q*(a+b))
Q=2*a*a*b*b*(N-4)+a*b*(a+b)*N*(N-4)+p*q*((N-1)*(a-b)**2+2*a*b*(N-2))

assert s.cancel(JAB-JAA+b*P/Delta)==0
assert s.cancel(JAA-JBB-(p-q)*Q/(p*q*(2*a*b+p*(a+b))*(2*a*b+q*(a+b))))==0
assert s.cancel(JAB-JBA-(a-b)*(p-q)*(N-1)/(a*b*(N-1)+p*q*(a+b)))==0

# Check the positive-summand argument for P(b)<0 symbolically.
U=(p-1)*q*(q-1)-p*p*(p-4)
assert s.expand((W-(q*q-q-3*p*p))-2*U)==0
assert s.cancel(P.subs(a,b)+b*(b*b*H+2*b*q*U+2*p*p*q*q+p*q*q*(q-p)*(N-1)))==0

# Independently reconstruct the complete matrix and compute its inverse trace.
def explicit(p0,q0,a0,b0,i,j):
 n=p0+q0
 L=s.zeros(n)
 for u in range(p0):
  for v in range(p0,n):
   L[u,u]+=1;L[v,v]+=1;L[u,v]-=1;L[v,u]-=1
 L[i,i]+=a0;L[j,j]+=b0
 return s.trace(L.inv())

count=3
for p0 in range(2,7):
 for q0 in range(p0+1,10):
  for a0,b0 in [(s.Rational(1,3),s.Rational(1,5)),(1,1),(5,2),(28,1),(101,s.Rational(2,3))]:
   subs={p:p0,q:q0,a:a0,b:b0}
   for fn,i,j in [(JAA,0,1),(JBB,p0,p0+1),(JAB,0,p0),(JBA,p0,0)]:
    assert s.cancel(fn.subs(subs)-explicit(p0,q0,a0,b0,i,j))==0
    count+=1
   if a0>=b0:
    AA=JAA.subs(subs);BB=JBB.subs(subs);AB=JAB.subs(subs);BA=JBA.subs(subs)
    assert AA<BB and AB<=BA
    assert (AB<AA)==(P.subs(subs)>0)
    count+=3
# Exact onset witness and one-parameter boundary.
z=s.symbols('z',positive=True)
assert s.expand(P.subs({p:2,q:5,b:1,a:z})-20*(z*z-26*z-45))==0
for z0 in (27,28):
 val=P.subs({p:2,q:5,b:1,a:z0})
 assert (val<0) if z0==27 else (val>0)
 count+=1
print('VERIFY_OK',count,'exact symbolic identities, rational matrix traces and location inequalities')
