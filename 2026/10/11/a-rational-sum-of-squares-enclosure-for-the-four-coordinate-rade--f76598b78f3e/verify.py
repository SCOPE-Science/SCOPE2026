from fractions import Fraction as Q
import sympy as s,itertools
A=s.symbols('a0:4');B=s.symbols('b0:4');X=A+B
c=s.Rational(123,200);p=s.Rational(255,100);ss=s.Rational(665,100);eta=s.Rational(483,100);q=s.Rational(252,100);v=s.Rational(636,100);u=s.Rational(639,100)
al=1-c;be=3-3*c-p/2;ga=1;de=3-ss/2;ep=3-eta/2;ze=3-u/2;th=12-q-v
M0=s.Matrix([[ (al if i==j else be) if i<4 and j<4 else ((ga if i==j else de) if i>=4 and j>=4 else (ep if i%4==j%4 else ze)) for j in range(8)] for i in range(8)])
M1=s.Matrix([[eta if i==j else th for j in range(4)] for i in range(4)])
M2=s.Matrix([[p,q,4,4],[q,ss,4,4],[4,4,u,v],[4,4,v,u]])
assert all(s.factor(M[:i,:i].det())>0 for M in (M0,M1,M2) for i in range(1,M.rows+1))
z=list(x**2 for x in X); w=[A[i]*B[i] for i in range(4)]
T=(s.Matrix([z]).T.T*M0*s.Matrix(z))[0]+(s.Matrix(w).T*M1*s.Matrix(w))[0]
for i,j in itertools.combinations(range(4),2):
 k,l=[x for x in range(4) if x not in (i,j)];zz=s.Matrix([A[i]*A[j],B[i]*B[j],A[k]*B[l],A[l]*B[k]])
 T+=(zz.T*M2*zz)[0]
AA=sum(x**2 for x in A);BB=sum(x**2 for x in B);AB=sum(A[i]*B[i] for i in range(4));F=lambda V:3*sum(x**2 for x in V)**2-2*sum(x**4 for x in V)
P=(1-c)*F(A)+F(B)+6*AA*BB+12*AB**2-12*sum(A[i]**2*B[i]**2 for i in range(4))+24*sum(B[i]*s.prod(A[j] for j in range(4) if j!=i)+A[i]*s.prod(B[j] for j in range(4) if j!=i) for i in range(4))
assert s.Poly(s.expand(P-T),X).is_zero
print('PASS: positive rational principal minors and exact quartic identity')
for M in (M0,M1,M2):print([str(s.factor(M[:i,:i].det())) for i in range(1,M.rows+1)])
