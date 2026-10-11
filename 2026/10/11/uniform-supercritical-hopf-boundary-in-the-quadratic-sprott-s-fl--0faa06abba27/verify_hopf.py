"""Exact SymPy checks for the quadratic Sprott-S Hopf theorem.

Requires SymPy; this verifies algebraic identities, not the abstract Hopf theorem.
Run with: python verify_hopf.py
"""
import sympy as sp

w = sp.symbols('w', real=True, positive=True)
b = sp.symbols('b', real=True, positive=True)
lam = sp.symbols('lam')
a = w**2
I = sp.I
A = sp.Matrix([[-1, -a, 0], [1, 0, 1], [1, 0, 0]])
assert sp.simplify(A.charpoly(lam).as_expr() - (lam + 1)*(lam**2 + a)) == 0
q = sp.Matrix([I*w, 1-I/w, 1])
left = sp.Matrix([[1, I*w, 1]])
assert all(sp.simplify(u)==0 for u in A*q - I*w*q)
assert all(sp.simplify(u)==0 for u in left*A - I*w*left)
left = left / (left*q)[0]
assert sp.simplify((left*q)[0]-1)==0

def B(u, v):
    return sp.Matrix([0, 2*u[2]*v[2], 0])

qb = sp.conjugate(q)
g21 = sp.factor((left*(B(qb,(2*I*w*sp.eye(3)-A).inv()*B(q,q))
                         -2*B(q,A.inv()*B(q,qb))))[0])
lyap = sp.factor(sp.re(sp.expand_complex(g21))/(2*w))
expected = -w*(8*w*w+1)/((w*w+1)*(4*w*w+1))
assert sp.simplify(lyap - expected)==0
assert sp.simplify(lyap.subs(w,1)+sp.Rational(9,10))==0
# Characteristic polynomial and transversality in the original b parameter.
J=sp.Matrix([[-1,-a,0],[1,0,2*sp.sqrt(b)],[1,0,0]])
assert sp.simplify(J.charpoly(lam).as_expr()
                   -(lam**3+lam**2+a*lam+2*a*sp.sqrt(b)))==0
P=lam**3+lam**2+a*lam+2*a*sp.sqrt(b)
lambda_prime=-(sp.diff(P,b)/sp.diff(P,lam)).subs({lam:I*w,b:sp.Rational(1,4)})
assert sp.simplify(sp.re(sp.expand_complex(lambda_prime)) - a/(a+1))==0
print('PASS: characteristic polynomial, eigenvectors, Hopf crossing, and exact negative l1')
print('l1 =',sp.factor(lyap))
print('Re(lambda_prime) =', sp.simplify(sp.re(sp.expand_complex(lambda_prime))))
