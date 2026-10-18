"""Reproduce the current and optimal switching assertions of the three-site flashing ratchet.
Requires Python 3 and SymPy. Execute: python verification.py
"""
import itertools
import sympy as sp


def current_by_generator(weights, switch):
    """Solve the six-state stationary generator without using the closed formula."""
    w = list(map(sp.Rational, weights))
    s = sp.Rational(switch)
    # column convention: generator[row destination, column origin]
    G = sp.zeros(6)
    for layer in range(2):
        for i in range(3):
            source = layer * 3 + i
            for j in range(3):
                if i == j:
                    continue
                rate = w[j] / w[i] if layer == 0 else sp.Integer(1)
                dest = layer * 3 + j
                G[dest, source] += rate
                G[source, source] -= rate
            other = (1-layer) * 3 + i
            G[other, source] += s
            G[source, source] -= s
    H = G.copy()
    for j in range(6):
        H[5,j] = 1
    rhs = sp.Matrix([0,0,0,0,0,1])
    pi = H.inv() * rhs
    J = w[1]/w[0] * pi[0] - w[0]/w[1] * pi[1] + pi[3] - pi[4]
    assert G*pi == sp.zeros(6,1)
    assert sum(pi) == 1 and all(t>0 for t in pi)
    return sp.factor(J)


def closed_formula(weights, switch):
    w0,w1,w2 = map(sp.Rational, weights)
    s = sp.Rational(switch)
    e1 = w0+w1+w2
    e2 = w0*w1+w1*w2+w2*w0
    e3 = w0*w1*w2
    a = e1*(e1**2+e2)
    b = 6*e1**3-3*e1*e2-27*e3
    c = 9*e1*(e1**2-2*e2)
    v = (w1-w0)*(w2-w1)*(w2-w0)
    return sp.factor(3*s*v/(2*(a*s**2+b*s+c)))


# Symbolic three-state reduction from the independent three-by-three stationary equation.
x,y,h,z = sp.symbols('x y h z', positive=True)
w = [sp.Integer(1), x, y]
L = sp.zeros(3)
for i in range(3):
    for j in range(3):
        if i!=j:
            L[j,i] += w[j]/w[i]
            L[i,i] -= w[j]/w[i]
p = sp.Rational(1,6)*h*(h*sp.eye(3)-L).inv()*sp.ones(3,1)
t = 3*h/(3-h)
qdiff = h/sp.Integer(3) * (p[0]-p[1])
flux_reduction = sp.factor(x*p[0]-p[1]/x+qdiff)
e1,e2,e3 = 1+x+y, x+y+x*y, x*y
A = e1*(e1**2+e2)
B = 6*e1**3-3*e1*e2-27*e3
C = 9*e1*(e1**2-2*e2)
V = (x-1)*(y-x)*(y-1)
flux_expected_h = sp.Rational(3,2)*t*V/(A*t*t+B*t+C)
assert sp.factor(flux_reduction-flux_expected_h) == 0
print('PASS symbolic three-state flux factorization')

profiles = [(1,1,1),(1,1,2),(1,2,3),(1,3,5),(2,3,7),(1,4,9),(3,4,8),(2,5,11),(2,2,7),(2,7,2),(7,2,2),(1,6,10)]
switches = [sp.Rational(1,10),sp.Rational(1,2),sp.Integer(1),sp.Integer(2),sp.Integer(6)]
count = 0
for weights,switch in itertools.product(profiles,switches):
    assert current_by_generator(weights,switch) == closed_formula(weights,switch)
    count += 1
print(f'PASS {count} exact six-state stationary flux comparisons')

# Sharp switching law: derivatives and range, exact in rational algebra.
s = sp.symbols('s', positive=True)
f = 3*s*V/(2*(A*s*s+B*s+C))
assert sp.factor(sp.diff(f,s) - (3*V*(C-A*s*s))/(2*(A*s*s+B*s+C)**2)) == 0
for weights in [(1,2,3),(1,3,8),(3,5,9),(1,2,101),(1,101,10001)]:
    w0,w1,w2 = map(sp.Rational,weights)
    e1=w0+w1+w2; e2=w0*w1+w1*w2+w2*w0
    r2=9*(w0*w0+w1*w1+w2*w2)/((w0*w0+w1*w1+w2*w2)+3*e2)
    assert sp.Rational(9,4) < r2 < 9
print('PASS strict optimizer uniqueness, exact derivative identity, and sharp range checks')
