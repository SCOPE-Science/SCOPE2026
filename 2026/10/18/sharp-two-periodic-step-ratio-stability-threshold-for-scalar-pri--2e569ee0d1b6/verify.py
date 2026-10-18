"""Exact symbolic and rational checks for periodic scalar primal-first PDHG.

Requires Python 3 and SymPy. Finite checks supplement the universal proof.
"""
from itertools import product
from sympy import Matrix, Rational, Symbol, cancel, simplify, sqrt

count=0

def eq(actual,expected,label):
    global count
    assert simplify(actual-expected)==0,(label,actual,expected)
    count+=1

r,q,t=Symbol('r',positive=True),Symbol('q',positive=True),Symbol('t',positive=True)
U=q+1/q

def M(tau,sigma):
    w=tau*sigma
    return Matrix([[1,-tau],[sigma,1-2*w]])

A=M(t,r/t)
B=M(q*t,r/(q*t))
P=B*A
for matrix,name in ((A,'first phase'),(B,'second phase')):
    eq(matrix.trace(),2-2*r,name+' trace')
    eq(matrix.det(),1-r,name+' determinant')
eq(P.trace(),2-4*r+4*r*r-r*U,'period-two trace')
eq(P.det(),(1-r)**2,'period-two determinant')
eq(1-P.det(),r*(2-r),'first Jury condition')
eq(1-P.trace()+P.det(),r*(U+2-3*r),'positive-edge Jury condition')
eq(1+P.trace()+P.det(),5*r*r-(U+6)*r+4,'negative-edge Jury condition')

V=Symbol('V',positive=True)
U0=Symbol('U0',positive=True)
poly=lambda z:5*z*z-(U0+6)*z+4
rootlo=(U0+6-V)/10
rootup=(U0+6+V)/10
for root in (rootlo,rootup):
    eq(cancel(poly(root)).subs(V*V,(U0+6)**2-80),0,'quadratic root relation')
eq(rootlo+rootup,(U0+6)/5,'root sum')
eq(cancel(rootlo*rootup).subs(V*V,(U0+6)**2-80),Rational(4,5),'root product')
eq(poly(1),3-U0,'upper-edge classification')

# Derive the two stage update independently at rational inputs.
def direct(x,y,tau,sigma):
    xnext=x-tau*y
    ynext=y+sigma*(2*xnext-x)
    return Matrix([xnext,ynext])
for rr,qq,tt,x,y in product(
    [Rational(1,5),Rational(2,3),Rational(4,5),Rational(9,10)],
    [Rational(1,2),Rational(1),Rational(2),Rational(3),Rational(6)],
    [Rational(2,3),Rational(3,2)],
    [Rational(1),Rational(-3,4)],
    [Rational(2),Rational(-1,3)]):
    for k in range(6):
        tau=tt if k%2==0 else qq*tt
        sigma=rr/tau
        nxt=direct(x,y,tau,sigma)
        delta=M(tau,sigma)*Matrix([x,y])
        eq(nxt[0],delta[0],'direct primal')
        eq(nxt[1],delta[1],'direct dual')
        x,y=nxt

rr=Rational(4,5);qq=Rational(3);tt=Rational(4,5)
A0=M(tt,rr/tt)
B0=M(qq*tt,rr/(qq*tt))
W=B0*A0
assert A0==Matrix([[1,-Rational(4,5)],[1,-Rational(3,5)]])
assert B0==Matrix([[1,-Rational(12,5)],[Rational(1,3),-Rational(3,5)]])
assert W==Matrix([[-Rational(7,5),Rational(16,25)],[-Rational(4,15),Rational(7,75)]])
eq(W.trace(),-Rational(98,75),'witness trace')
eq(W.det(),Rational(1,25),'witness determinant')
eq(1+W.trace()+W.det(),-Rational(4,15),'witness strict instability')
assert 0<rr<1 and qq>1
count+=4
print('PASS:',count,'exact algebraic/rational checks')
