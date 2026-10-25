"""Exact certificate for the sharp isolated-vertex covariance phase transition.
Requires Python 3 and sympy. All root counts use exact rational arithmetic.
"""
import sympy as s
r=s.symbols('r')
def numer(n):
    m=n-1
    return s.Poly(s.expand(2*(1-3*r)**m+(m-2)*(1-4*r)**m-m*(1-2*r)**(2*m)),r)
assert s.expand((1-3*r)-(1-2*r)**2-r*(1-4*r))==0
for n in range(2,22):
    p=numer(n)
    q=s.div(p,s.Poly(r,r))[0]
    count=q.count_roots(0,s.Rational(1,4))-int(q.eval(s.Rational(1,4))==0)
    wanted=0 if n<4 else (1 if n<=20 else 3)
    assert count==wanted,(n,count,wanted)
    print('n',n,'interior_sturm_roots',count)
# One-sided exact signs at n=21 certify three crossings.
n=21
p=numer(n)
assert s.sign(p.eval(s.Rational(1,n)))==-1
assert s.sign(p.eval(s.Rational(1,6)))==1
assert s.sign(p.eval(s.Rational(1,4)))==-1
assert s.sign(p.diff().eval(0))==1
# Verify derivative of the normalized function in the proof.
m=s.symbols('m',positive=True,integer=True)
X=(1-3*r)/(1-2*r)**2
Y=(1-4*r)/(1-2*r)**2
assert s.factor(s.diff(X,r)-(1-6*r)/(1-2*r)**3)==0
assert s.factor(s.diff(Y,r)+8*r/(1-2*r)**3)==0
H=(1-6*r)/(4*r)*((1-3*r)/(1-4*r))**(m-1)
logH_der=-6/(1-6*r)-1/r+(m-1)/((1-3*r)*(1-4*r))
assert s.factor(logH_der*r*(1-6*r)*(1-3*r)*(1-4*r)-(-1+(m+6)*r-6*(m+1)*r*r))==0
print('PASS exact finite root counts and derivative identities')
