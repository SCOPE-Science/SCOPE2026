"""Exact symbolic and independent rational-matrix checks for two-edge loss on bicliques.
Run: python verification/check.py (requires sympy)."""
import sympy as s
p,q,u=s.symbols('p q u', integer=True, positive=True)
n=p+q
r=(p+q-1)/(p*q)
k=(p-1)/(p*q**2)+(q-1)/(q*p**2)+1/(n*p*q)
cA=(p-1)/(p*q)
cB=(q-1)/(p*q)
cD=-1/(p*q)
dA=(p-1)/(p*q**2)-1/(q*p**2)+1/(n*p*q)
dB=-1/(p*q**2)+(q-1)/(q*p**2)+1/(n*p*q)
dD=-1/(p*q**2)-1/(q*p**2)+1/(n*p*q)
S=s.factor(n*k/(1-r))
Delta=lambda c,d:s.factor(2*n*(k*(1-r)+c*d)/((1-r)**2-c**2))
DA,DB,DD=[Delta(c,d) for c,d in [(cA,dA),(cB,dB),(cD,dD)]]
assert s.simplify(S-(p**3+p**2*q-p**2+p*q**2-p*q+q**3-q**2)/(p*q*(p-1)*(q-1)))==0
wantA=2*(p**3+p**2*q-p**2+p*q**2-2*p*q+q**3-2*q**2)/(p*q*(p-1)*(q-2))
wantB=wantA.xreplace({p:q,q:p})
wantD=2*(p**4*q-p**4+p**3*q**2-3*p**3*q+2*p**3+p**2*q**3-3*p**2*q**2+3*p**2*q+p*q**4-3*p*q**3+3*p*q**2-q**4+2*q**3)/(p*q*(p*q-p-q)*(p*q-p-q+2))
for a,b in [(DA,wantA),(DB,wantB),(DD,wantD)]:assert s.cancel(a-b)==0
J=[s.factor(v-2*S) for v in [DA,DB,DD]]
assert s.cancel(J[0]-2*p*(p+q-1)/(q*(p-1)*(q-2)*(q-1)))==0
assert s.cancel(J[1]-2*q*(p+q-1)/(p*(p-2)*(p-1)*(q-1)))==0
assert s.cancel(J[2]-2*(p**2+p*q-p+q**2-q)/((p-1)*(q-1)*(p*q-p-q)*(p*q-p-q+2)))==0
assert s.cancel(DA-DB-2*(p-q)*(p+q-1)*(p**2+p*q-2*p+q**2-2*q)/(p*q*(p-2)*(p-1)*(q-2)*(q-1)))==0
numA=s.factor(s.together(DA-DD)).as_numer_denom()[0]
denA=s.factor(s.together(DA-DD)).as_numer_denom()[1]
# Positive-coefficient certificate after p=q+u, valid for p>=q>=3.
positiveA=2*((q-1)*u**4+(q-1)*(5*q-3)*u**3+(q-1)**2*(9*q-2)*u**2+q*(q-1)*(7*q*q-13*q+4)*u+q**3*(q-2)*(2*q-3))
assert s.expand(numA.subs(p,q+u)-positiveA)==0
assert s.simplify(denA-q*(p-1)*(q-2)*(p*q-p-q)*(p*q-p-q+2))==0
H=p**3-(q**2*(q-2)+2)*p**2-q**2*(q-2)**2*p+q**2*(q-1)*(q-2)
assert s.cancel(DB-DD+2*H/(p*(p-2)*(q-1)*(p*q-p-q)*(p*q-p-q+2)))==0
T=q*(q-1)**2
assert s.factor(H.subs(p,q))==-q**3*(q-2)*(2*q-3)
assert s.factor(H.subs(p,T))==q**3*(q-2)*(q-1)
vv=s.symbols('v', nonnegative=True)
neg_tm1=s.factor(-H.subs(p,T-1).subs(q,vv+3))
assert all(c>0 for c in s.Poly(neg_tm1,vv).coeffs())

# Independently invert grounded Laplacians over the rationals.
def direct_kf(P,Q,removed):
 N=P+Q
 mat=s.zeros(N,N)
 for i in range(P):
  for j in range(Q):
   if (i,j) in removed:continue
   a,b=i,P+j
   mat[a,a]+=1;mat[b,b]+=1;mat[a,b]-=1;mat[b,a]-=1
 # L+J/n is nonsingular for these connected graphs.
 inv=(mat+s.ones(N,N)/N).inv()
 return s.factor(N*(sum(inv[i,i] for i in range(N))-1))

checks=0
for P in range(3,8):
 for Q in range(3,8):
  base=direct_kf(P,Q,[])
  sample=[(S,{(0,0)}),(DA,{(0,0),(0,1)}),(DB,{(0,0),(1,0)}),(DD,{(0,0),(1,1)})]
  for formula,removed in sample:
   observed=direct_kf(P,Q,removed)-base
   assert s.cancel(observed-formula.subs({p:P,q:Q}))==0,(P,Q,removed,observed,formula)
   checks+=1

# Sharp integer boundary for large imbalances, symbolic not matrix extrapolation.
for Q in range(3,16):
 for P in [Q,Q*(Q-1)**2-1,Q*(Q-1)**2,Q*(Q-1)**2+1]:
  assert (H.subs({p:P,q:Q})>0)==(P>=Q*(Q-1)**2) if P!=Q else H.subs({p:P,q:Q})<0
  checks+=1
print(f'VERIFY_OK {checks} exact direct and integer-boundary checks; all symbolic identities and positive coefficient certificates')
