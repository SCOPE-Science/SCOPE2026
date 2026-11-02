"""Exact checks of the two-stage Radau IIA endpoint map on balanced complete multipartite graphs.

Requires Python 3 and SymPy. Run: python verify_radau.py
"""
import sympy as sp

m,s,z=sp.symbols('m s z',integer=True,positive=True)
R=lambda x:(6-2*sp.sympify(x))/(sp.sympify(x)**2+4*sp.sympify(x)+6)
D=lambda x:x*x+4*x+6
u=(m-1)*z; v=m*z
N=sp.expand(D(u)*D(v)*(1+m*(s-1)*R(u)+(m-1)*R(v)))
F=(m**2*(m-1)**2*z**4
   -2*m*(m-1)*(s*m**2-6*m+3)*z**3
   -2*m*(s*m**2-4*s*m-9*m+9)*z**2
   +12*s*m*(m+1)*z+36*s*m)
assert sp.cancel(N-F)==0
W=sp.factor(1-m*R(u)+(m-1)*R(v))
W_expected=m*(m-1)*z**2*(m*(m-1)*z**2+(12*m-6)*z+18)/(D(u)*D(v))
assert sp.cancel(W-W_expected)==0
assert sp.cancel(R(z)+sp.Rational(1,11)-(z-6)*(z-12)/(11*D(z)))==0
assert sp.cancel(sp.diff(R(z),z)-2*(z*z-6*z-18)/D(z)**2)==0
assert sp.simplify(R(3+3*sp.sqrt(3))) == (5-3*sp.sqrt(3))/2
assert (26-15*sp.sqrt(3))>0
assert sp.cancel(1+10*R(8)+R(16)) == -sp.Rational(500,8313)

# The stage tableau reproduces R(z) (via y'=-z y).
A=sp.Matrix([[sp.Rational(5,12),-sp.Rational(1,12)],
             [sp.Rational(3,4),sp.Rational(1,4)]])
b=sp.Matrix([[sp.Rational(3,4),sp.Rational(1,4)]])
assert sp.factor(1-z*(b*(sp.eye(2)+z*A).inv()*sp.ones(2,1))[0]-R(z))==0

checks=8
for M,S in [(2,2),(2,5),(2,6),(3,4),(4,3),(7,2),(12,1)]:
    n=M*S
    # One representative rational nonzero step, keeping the inverse well-conditioned.
    Z=sp.Rational(7,2)
    h=Z/S
    adj=sp.zeros(n)
    for i in range(n):
        for j in range(n):
            if i!=j and i//S!=j//S:
                adj[i,j]=1
    lap=sp.diag(*([S*(M-1)]*n))-adj
    denom=6*sp.eye(n)+4*h*lap+h*h*lap*lap
    actual=denom.inv()*(6*sp.eye(n)-2*h*lap)
    ra=R((M-1)*Z); rb=R(M*Z)
    diag=(1+M*(S-1)*ra+(M-1)*rb)/n
    same=(1-M*ra+(M-1)*rb)/n
    cross=(1-rb)/n
    for i in range(n):
        assert sp.cancel(sum(actual[i,j] for j in range(n))-1)==0
        for j in range(n):
            expected=diag if i==j else same if i//S==j//S else cross
            assert sp.cancel(actual[i,j]-expected)==0,(M,S,i,j)
            checks+=1
    # The exact numerator has at most two positive roots (Descartes) for n>=12.
    poly=sp.Poly(F.subs({m:M,s:S}),z)
    roots=sp.polys.polytools.intervals(poly,eps=sp.Rational(1,10**8))
    pos=[(a,b) for (a,b),multiplicity in roots if a>0]
    assert len(pos)==(2 if n>=12 else 0),(M,S,pos)
    checks+=3
print('VERIFIED',checks,'exact assertions, exact matrix inversions, root isolations')
