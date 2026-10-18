"""Exact checks for two-stage Gauss positivity on balanced double stars.

Run: python artifacts/check_double_star.py
SymPy is required. The analytical root/sign arguments are in RESULT.md.
"""
import sympy as s

m,h=s.symbols('m h', positive=True)
I=s.eye(2)
A=s.Matrix([[m,-m],[-1,1]])
B=s.Matrix([[m+2,-m],[-1,1]])
def step(X):
    return (I-h*X/2+h*h*X*X/12)*(I+h*X/2+h*h*X*X/12).inv()
S,T=step(A),step(B)
r=(h*h-6*h+12)/(h*h+6*h+12)
D1=h*h+6*h+12
DS=(m+1)**2*h*h+6*(m+1)*h+12
DA=h**4+3*(m+3)*h**3+3*(m*m+6*m+11)*h*h+18*(m+3)*h+36
H=(h*h+6*h+12)**2 +m*m*h*h*(h*h-12)
P=(h*h+6*h+12)**2 +m*m*h*h*(12-h*h)+2*m*h*h*(24-h*h)+72*m*h
Q=(3-m*m)*h**5+(6*m*m+24*m+42)*h**4+(12*m**3+84*m*m+228*m+252)*h**3+(144*m*m+648*m+792)*h*h+(576*m+1296)*h+864
expr=[(S[0,0]-T[0,0])/2,
 (S[0,1]+T[0,1])/(2*m),
 (S[0,1]-T[0,1])/(2*m),
 (S[1,1]+T[1,1])/(2*m)-r/m,
 (S[1,1]-T[1,1])/(2*m)]
pred=[3*h*H/(DS*DA),
 3*h*P/(DS*DA),
 3*h*h*((m*m+2*m+3)*h**3+(12*m+24)*h*h+(24*m+72)*h+72)/(DS*DA),
 3*h*h*Q/(D1*DS*DA),
 3*h**3*((m*m+4*m+5)*h*h+(12*m+24)*h+24)/(DS*DA)]
for j,(a,b) in enumerate(zip(expr,pred)):
    d=s.factor(s.cancel(a-b))
    assert d==0
assert s.expand(H.subs(m,4))==17*h**4+12*h**3-132*h*h+144*h+144
assert s.expand(P.subs(h,12))==51984-19008*m*m-33696*m
assert s.expand(Q.subs(h,12))==864*(24*m**3+48*m*m+1148*m+2527)
assert s.expand(H.subs(h,2))==784-32*m*m
count=9
for k in range(2,11):
  n=2*k+2
  L=s.zeros(n)
  edges=[(0,1)]+[(0,i) for i in range(2,k+2)]+[(1,i) for i in range(k+2,n)]
  for i,j in edges:
    L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
  for z in [s.Rational(1,10),s.Rational(1,2),1,2,3,4,6,12]:
    LL=z*L
    MM=(12*s.eye(n)-6*LL+LL*LL)*(12*s.eye(n)+6*LL+LL*LL).inv()
    pairs=[(0,1),(0,2),(0,k+2),(2,3),(2,k+2)]
    assert all(s.cancel(MM[i,j]-pred[a].subs({m:k,h:z}))==0 for a,(i,j) in enumerate(pairs))
    assert all(sum(MM[i,j] for j in range(n))==1 for i in range(n))
    assert MM==MM.T
    count+=7
print('PASS: %d symbolic identities and exact full-matrix checks' % count)
