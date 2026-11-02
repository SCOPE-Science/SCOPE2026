"""Symbolic verification of the exact quadrant block matrices.

Usage: python symbolic_checker.py
Requires SymPy. This checks algebraic matrix identities; the geometric block
decomposition is proved in the accompanying mathematical document.
"""
from functools import lru_cache
import sympy as s

d=s.symbols('d', positive=True, integer=True)
mu,nu=s.symbols('mu nu',positive=True)
@lru_cache(None)
def M(a,b):
    if a>=2:return s.factor(s.Rational(a-1,1)*M(a-2,b)/(d+a+b-2))
    if b>=2:return s.factor(s.Rational(b-1,1)*M(a,b-2)/(d+a+b-2))
    return {(0,0):s.S.One,(1,0):mu,(0,1):mu,(1,1):nu}[(a,b)]
B=[{(0,0):1},{(1,0):1,(0,1):1},{(2,0):1,(0,2):1},
   {(1,1):1},{(1,0):1,(0,1):-1},{(2,0):1,(0,2):-1}]

def gram(basis,quarter,vector=False):
    output=s.zeros(len(basis))
    for i,p in enumerate(basis):
        for j,q in enumerate(basis):
            val=s.S.Zero
            for (a,b),c in p.items():
                for (e,f),h in q.items():
                    x,y=a+e,b+f
                    if quarter or (x%2==0 and y%2==0):
                        z=M(x,y)
                        if vector:z/=d+x+y
                        val+=c*h*z
            output[i,j]=s.factor(val/(4 if quarter else 1))
    return output


def eq(a,b):
    diff=s.simplify(a-b)
    assert diff==0, diff


def run():
    Gp,Kp=gram(B[:4],False),gram(B[:4],True)
    Gm,Km=gram(B[4:],False),gram(B[4:],True)
    Gv,Kv=gram(B[:2],False,True),gram(B[:2],True,True)
    Gw,Kw=gram(B[4:5],False,True),gram(B[4:5],True,True)
    eq(s.trace(Gp.inv()*Kp),1+d*nu/4)
    eq(s.trace(Gm.inv()*Km),s.Rational(1,2)-d*nu/4)
    eq(s.trace(Gv.inv()*Kv),s.Rational(1,2)+d*nu/4)
    eq((Kw[0]/Gw[0]),(1-d*nu)/4)
    eq((Kp-Gp/4).det(),mu**2*nu**2*(d-2)**2/(64*(d+1)**2*(d+2)**2))
    eq((Km-Gm/4).det(),-mu**2/(4*(d+1)**2))
    eq((Kv-Gv/4).det(),-mu**2/(4*(d+1)**2))
    eq(Gp.det(),8*(d-2)/(d**4*(d+2)**2))
    eq(Gv.det(),2/(d**2*(d+2)))
    print('SYMBOLIC_IDENTITIES_PASS',9)

if __name__=='__main__':run()
