"""Exact identities and independent quadrature for the five-knot spline projector."""
from fractions import Fraction
import sympy as s
from scipy.integrate import quad
import numpy as np

q=s.symbols('q',positive=True)
gaps=[1-q,q,q,1-q]
G=s.zeros(5)
for i,h in enumerate(gaps):
    G[i,i]+=h/3; G[i+1,i+1]+=h/3
    G[i,i+1]+=h/6; G[i+1,i]+=h/6
V=G.inv()
assert s.simplify(G*V-s.eye(5))==s.zeros(5)

C=(7+3*q)/(3*(1+q))
S=(5*q*q+38*q+25)/(3*(q+1)*(q+5))
E=(300+403*q+27*q*q-23*q**3-3*q**4)/(3*(q+1)*(q+5)*(12-3*q-q*q))
for idx,expected in [(0,E),(1,S),(2,C)]:
    terms=[]
    for i,h in enumerate(gaps):
        a,b=V[idx,i],V[idx,i+1]
        # For 0<q<1, all rows alternate signs at adjacent nodes.
        # Their absolute integrals are this exact opposite-sign formula.
        abs_a=s.factor((-1)**(i+idx)*a) if idx==1 else s.factor((-1)**i*a)
        abs_b=s.factor((-1)**(i+idx+1)*b) if idx==1 else s.factor((-1)**(i+1)*b)
        # handle actual sign using sample q=1/2, not guessed from row index
        sign_a=s.sign(a.subs(q,s.Rational(1,2)))
        sign_b=s.sign(b.subs(q,s.Rational(1,2)))
        aa=s.factor(sign_a*a); bb=s.factor(sign_b*b)
        assert sign_a*sign_b==-1
        assert aa.subs(q,s.Rational(1,20))>0 and bb.subs(q,s.Rational(19,20))>0
        terms.append(h*(aa*aa+bb*bb)/(2*(aa+bb)))
    assert s.simplify(sum(terms)-expected)==0

assert s.simplify(E-S-2*q*(q**3+15*q*q+53*q+11)/(3*(q+1)*(q+5)*(12-3*q-q*q)))==0
assert s.simplify(E-C-4*(q+6)*(2*q*q+11*q-5)/(3*(q+1)*(q+5)*(12-3*q-q*q)))==0
assert s.factor(s.diff(C,q))==-4/(3*(q+1)**2)
assert s.simplify(s.diff(E,q)-4*(q**6+30*q**5+298*q**4+1278*q**3+2483*q*q+2460*q+1770)/(3*(q+1)**2*(q+5)**2*(q*q+3*q-12)**2))==0
qstar=(s.sqrt(161)-11)/4
assert s.simplify(C.subs(q,qstar)-(s.Rational(4,3)+s.sqrt(161)/21))==0
assert s.limit(C,q,0,dir='+')==s.Rational(7,3)
assert s.limit(E,q,1,dir='-')==s.Rational(22,9)

# Independent from symbolic absolute-integral formula: build each spline
# hat and perform adaptive numerical quadrature with calculated zero points.
def hats(t,knots):
    out=np.zeros(5)
    if t<=knots[0]:out[0]=1;return out
    if t>=knots[-1]:out[-1]=1;return out
    i=np.searchsorted(knots,t,side='right')-1
    i=min(i,3)
    frac=(t-knots[i])/(knots[i+1]-knots[i])
    out[i]=1-frac;out[i+1]=frac
    return out
checks=0
for epsilon in [1/100,1/20,1/10,1/6,1/5,1/4,1/3,2/5,1/2,2/3,3/4,9/10,99/100]:
    knots=np.array([-1,-epsilon,0,epsilon,1],dtype=float)
    lengths=np.diff(knots)
    M=np.zeros((5,5))
    for j,h in enumerate(lengths):
        M[j,j]+=h/3;M[j+1,j+1]+=h/3
        M[j,j+1]+=h/6;M[j+1,j]+=h/6
    Vinv=np.linalg.inv(M)
    for i in range(5):
        total=0.
        for j in range(4):
            a,b=Vinv[i,j],Vinv[i,j+1]
            x0,x1=knots[j],knots[j+1]
            points=[]
            if a*b<0:points=[(abs(b)*x0+abs(a)*x1)/(abs(a)+abs(b))]
            v,_=quad(lambda t:abs(float(Vinv[i,:]@hats(t,knots))),x0,x1,points=points,epsabs=1e-11)
            total+=v
        expected=float([E,S,C,S,E][i].subs(q,s.Rational(str(epsilon))))
        assert abs(total-expected)<2e-10,(epsilon,i,total,expected)
        checks+=1
    # sample intra-element rows, whose norm is convex in the evaluation point
    for j in range(4):
        for t in np.linspace(knots[j],knots[j+1],9):
            row=hats(t,knots)@Vinv
            val=0.
            for k in range(4):
                a,b=row[k],row[k+1];left,right=knots[k],knots[k+1]
                points=[]
                if a*b<0:points=[(abs(b)*left+abs(a)*right)/(abs(a)+abs(b))]
                z,_=quad(lambda x:abs(float(row@hats(x,knots))),left,right,points=points,epsabs=1e-11)
                val+=z
            assert val<=max(float(E.subs(q,s.Rational(str(epsilon)))),float(C.subs(q,s.Rational(str(epsilon)))))+3e-10
            checks+=1
print('PASS: symbolic Gram identities, sharp formulas, branch monotonicity, limits, and',checks,'independent quadrature/interior-row checks')
