"""Standalone numerical reproduction for a two-cell sigmoid map; Python standard library only.

The analytical proof, not these finite tests, establishes the infinite theorem.
Run: python3 VERIFY.py
"""
from decimal import Decimal, localcontext
from itertools import product

D = Decimal
A = D(17) / 10
B = D(3) / 10
M = ((A, -D(1)), (D(1), A))
b = (-B, B)
v = (D(7) / 10, D(27) / 10)
one = D(1)
zero = D(0)

def add(x, y):
    return tuple(a + b for a, b in zip(x, y))

def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))

def scale(a, x):
    return tuple(a * z for z in x)

def mv(x):
    return (M[0][0] * x[0] + M[0][1] * x[1],
            M[1][0] * x[0] + M[1][1] * x[1])

def norm(x):
    return max(abs(z) for z in x)

def sig(x):
    e = (-2 * abs(x)).exp()
    val = (one - e) / (one + e)
    return val if x >= 0 else -val

def sech2(x):
    e = (-2 * abs(x)).exp()
    return 4 * e / (one + e) ** 2

def act(x, alpha):
    return tuple(sig(alpha * z) for z in x)

def f(x, t, alpha):
    return add(scale(one-t, x), scale(t, add(mv(act(x, alpha)), b)))

def g(m, w, c, alpha):
    p = add(m, scale(one/c, w))
    q = sub(m, scale(one/c, w))
    tp, tq = act(p, alpha), act(q, alpha)
    return add(b, scale(D(1)/2, mv(add(tp, tq)))), scale(D(1)/2, mv(sub(tp, tq)))

def matmul(P, Q):
    return tuple(tuple(sum((P[i][k]*Q[k][j] for k in range(2)), zero)
                       for j in range(2)) for i in range(2))

def jac(x, t, alpha):
    d1, d2 = (alpha * sech2(alpha * z) for z in x)
    return (((one-t)+t*A*d1, -t*d2), (t*d1, (one-t)+t*A*d2))

with localcontext() as ctx:
    ctx.prec = 95
    assert mv((one, one)) == v
    assert 216 * (-D(6)).exp() < one
    assert 108 * (-D(6)).exp() < one
    assert D('5.4') * (-D(6)).exp() < one/20
    checked = 0
    for ts, alphas in product(('2.0001', '2.01', '2.1', '2.5', '3', '10', '100'),
                               ('10', '12', '20')):
        t, alpha = D(ts), D(alphas)
        c = (t-2)/t
        m, w = b, v
        for n in range(300):
            m1, w1 = g(m, w, c, alpha)
            change = max(norm(sub(m1,m)), norm(sub(w1,w)))
            m,w = m1,w1
            if change < D('1e-78'):
                break
        p, q = add(m, scale(one/c,w)), sub(m,scale(one/c,w))
        assert p[0]>0 and p[1]>0 and q[0]<0 and q[1]<0
        assert norm(sub(m,b)) < one/20 and norm(sub(w,v)) < one/20
        err = max(norm(sub(f(p,t,alpha),q)), norm(sub(f(q,t,alpha),p)))
        assert err < D('1e-72'), (ts,alphas,err)
        assert norm(sub(p,add(b,scale(one/c,v)))) <= D('5.4')*(one+one/c)*(-D('0.6')*alpha/c).exp()
        assert norm(sub(q,sub(b,scale(one/c,v)))) <= D('5.4')*(one+one/c)*(-D('0.6')*alpha/c).exp()
        expansion_bound = t-one - t*D('10.8')*alpha*(-D('0.6')*alpha/c).exp()
        assert expansion_bound>one
        Jp, Jq = jac(p,t,alpha),jac(q,t,alpha)
        # Compare exact derivative components against the conservative bound.
        for J in (Jp,Jq):
            perturb = ((J[0][0]+t-one,J[0][1]),(J[1][0],J[1][1]+t-one))
            assert max(sum(abs(h) for h in row) for row in perturb) < t-2
        # A return derivative can be computed without approximating the orbit numerically over time.
        JR = matmul(Jq,Jp)
        assert JR[0][0] > 0 and JR[1][1] > 0
        checked += 1
    # Independent direct evaluation of the special sample.
    t, alpha = D(3), D(10)
    c = (t-2)/t
    m,w = b,v
    for _ in range(12):
        m,w = g(m,w,c,alpha)
    p,q = add(m,scale(one/c,w)),sub(m,scale(one/c,w))
    print('PASS: 21 high-precision two-cycle pairs, 42 return equations, 42 coordinate bounds, 21 uniform derivative inequalities.')
    print('T=3, alpha=10, p =',tuple(str(z.quantize(D('0.0000000000001'))) for z in p))
    print('T=3, alpha=10, q =',tuple(str(z.quantize(D('0.0000000000001'))) for z in q))
