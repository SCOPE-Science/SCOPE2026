from sympy import symbols, diff, expand, simplify, Rational
Q,D,V,mu,nu,Gamma = symbols('Q D V mu nu Gamma')
fQ = mu*Q - V*D
fD = -nu*D + V*Q
fV = Gamma - V + Q*D

def L(expr):
    return expand(diff(expr,Q)*fQ + diff(expr,D)*fD + diff(expr,V)*fV)

assert simplify(L((Q**2 + D**2)/2) - (mu*Q**2 - nu*D**2)) == 0
assert simplify((V*D - mu*Q) + fQ) == 0
assert simplify((V*Q - nu*D) - fD) == 0
assert simplify((Q*D - (V-Gamma)) - fV) == 0
assert simplify((Rational(119,1000)/Rational(1,10)) - Rational(119,100)) == 0
print('VERIFY_OK')
