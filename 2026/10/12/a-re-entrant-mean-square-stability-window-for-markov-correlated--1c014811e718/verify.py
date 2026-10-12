"""Exact algebra checks for a two-state correlated-delay gradient method."""
import sympy as sp
from fractions import Fraction
from itertools import product

h=sp.Rational(6,5)
p=sp.symbols('p')
z=sp.symbols('z')
P=432*p**3-156*p**2-305*p+125
A0=sp.Matrix([[1-h,0],[1,0]])
A1=sp.Matrix([[1,-h],[1,0]])
def moment(A):
    a,b,c,d=A[0,0],A[0,1],A[1,0],A[1,1]
    return sp.Matrix([[a*a,2*a*b,b*b],[a*c,a*d+b*c,b*d],[c*c,2*c*d,d*d]])
K0,K1=moment(A0),moment(A1)
T=sp.BlockMatrix([[p*K0,(1-p)*K0],[(1-p)*K1,p*K1]]).as_explicit()
assert sp.factor((sp.eye(6)-T).det()+24*P/3125)==0
v=A0*sp.Matrix([1,0]); assert v==sp.Matrix([-sp.Rational(1,5),1])
m0=sp.Matrix([v[0]**2,v[0]*v[1],v[1]**2])
S=sp.factor((K1*(sp.eye(3)-p*K1).inv()*m0)[0])
S_exp=-(216*p**2+5430*p+6125)/(25*(6*p-5)*(36*p**2+35*p+25))
assert sp.simplify(S-S_exp)==0
B=sp.factor(p/25+(1-p)**2*S)
assert sp.simplify(1-B-24*P/(25*(6*p-5)*(36*p**2+35*p+25)))==0
assert B.subs(p,sp.Rational(1,2))==sp.Rational(91,103)
assert P.subs(p,sp.Rational(2,5))>0 and P.subs(p,sp.Rational(1,2))<0
assert P.subs(p,sp.Rational(3,4))<0 and P.subs(p,sp.Rational(4,5))>0
assert P.subs(p,sp.Rational(5,6))>0
# A rational mean-square Lyapunov equality proves stability at independent delays.
Q=sp.Matrix([[sp.Rational(100,3),-sp.Rational(25,2)],[-sp.Rational(25,2),25]])
assert Q[0,0]>0 and Q.det()>0
assert sp.simplify(Q-(A0.T*Q*A0+A1.T*Q*A1)/2-sp.eye(2))==sp.zeros(2)
# Recursive weighted enumeration agrees with the exact three-moment Markov operator.
for stay in [sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4),sp.Rational(4,5)]:
    MT=T.subs(p,stay)
    init=sp.Matrix([1,1]); ms=sp.Matrix([1,1,1]);
    w=sp.Matrix.vstack(ms/2,ms/2)
    # w is the moment of state before the first update, conditioned on D_0.
    for n in range(1,8):
        w=MT*w
        enum=sp.Rational(0)
        for bits in product([0,1], repeat=n):
            pr=sp.Rational(1,2)
            for i in range(1,n):pr*=stay if bits[i]==bits[i-1] else 1-stay
            state=init
            for b in bits:state=(A0 if b==0 else A1)*state
            enum+=pr*state[0]**2
        direct=sp.factor(w[0]+w[3])
        assert enum==direct,(stay,n,enum,direct)
# Independently check the zero-event renewal equation and the last-zero decomposition.
for stay in [sp.Rational(1,4), sp.Rational(1,2), sp.Rational(4,5)]:
    u=[]
    full=[]
    y0=sp.Matrix([1,1])
    for n in range(8):
        e_u=e_full=sp.Rational(0)
        for path in product([0,1],repeat=n+1):
            pr=sp.Rational(1,2)
            for i in range(1,n+1):pr*=stay if path[i]==path[i-1] else 1-stay
            y=y0
            for bit in path[:n]:y=(A0 if bit==0 else A1)*y
            e_full+=pr*y[0]**2
            if path[n]==0:e_u+=pr*y[0]**2
        u.append(e_u);full.append(e_full)
        forcing=sp.Rational(1,2) if n==0 else (1-stay)*stay**(n-1)*(A1**n*y0)[0]**2/2
        convolution=0
        for g in range(1,n+1):
            r=(A1**(g-1)*v)[0]
            b=stay*v[0]**2 if g==1 else (1-stay)**2*stay**(g-2)*r**2
            convolution+=b*u[n-g]
        assert sp.simplify(e_u-forcing-convolution)==0,(stay,n,'renewal')
        if n>=1:
            first=stay**(n-1)*(A1**n*y0)[0]**2/2
            last=v[0]**2*u[n-1]
            for L in range(1,n):last+=(1-stay)*stay**(L-1)*(A1**L*v)[0]**2*u[n-L-1]
            assert sp.simplify(e_full-first-last)==0,(stay,n,'last zero')
print('PASS: rational transfer determinant, renewal resolvent, cubic sign brackets, Lyapunov matrix, 28 exact moment paths, 24 renewal and 21 last-zero path identities')
