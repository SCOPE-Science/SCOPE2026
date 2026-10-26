"""Exact rational checks for coordinate-conductance cube Hodge projections.
Run: python check.py (requires SymPy)."""
import itertools
import sympy as sp


def formulas(weights):
    d = len(weights)
    q = []
    r = []
    p = []
    for i in range(d):
        qi = 1 + sum(sp.sqrt(weights[i] * weights[j]) / (weights[i] + weights[j])
                     for j in range(d) if j != i)
        ri = sp.Rational(1, 2**(d-1)) * sum(
            weights[i] / sum(weights[k] for k in range(d) if (mask >> k) & 1)
            for mask in range(1, 2**d) if (mask >> i) & 1)
        q.append(sp.cancel(qi));r.append(sp.cancel(ri));p.append(sp.cancel(qi + 1 - 2 * ri))
    return q, r, p


def grounded_check(weights):
    d = len(weights)
    edges = [(v, v ^ (1 << i), i)
             for v in range(1 << d) for i in range(d) if not ((v >> i) & 1)]
    D = sp.zeros(1 << d, len(edges))
    for col, (v, u, i) in enumerate(edges):
        D[v,col] = sp.sqrt(weights[i]); D[u,col] = -sp.sqrt(weights[i])
    Lap = D * D.T
    K = Lap[1:,1:].inv()
    Q = D[1:,:].T * K * D[1:,:]
    q, r, p = formulas(weights)
    for col, (v,u,i) in enumerate(edges):
        qc = sum(abs(Q[row,col]) for row in range(len(edges)))
        pc = 1 + qc - 2*Q[col,col]
        assert sp.simplify(qc-q[i]) == 0, (d,weights,col,'cut',qc,q[i])
        assert sp.simplify(Q[col,col]-r[i]) == 0, (d,weights,col,'diagonal')
        assert sp.simplify(pc-p[i]) == 0, (d,weights,col,'cycle')
    return len(edges)


def sturm_variations(poly,z):
    x=next(iter(poly.free_symbols)); seq=sp.sturm(poly,x)
    if z is sp.oo:
        sg = [sp.sign(sp.LC(sp.Poly(f,x))) for f in seq]
    else:
        sg = [sp.sign(f.subs(x,z)) for f in seq]
    sg = [s for s in sg if s]
    return sum(sg[i] != sg[i+1] for i in range(len(sg)-1))


def phase_certificate():
    t=sp.symbols('t', positive=True)
    ww=[t**(2*i) for i in range(4)]
    q,r,p=formulas(ww)
    poly = (t**24-4*t**23+3*t**22-4*t**21+9*t**20-8*t**19
            +15*t**18-12*t**17+24*t**16-4*t**15+33*t**14
            -8*t**13+33*t**12+8*t**11+38*t**10+4*t**9
            +27*t**8+12*t**7+24*t**6+8*t**5+14*t**4
            +4*t**3+6*t**2+4*t+4)
    den=4*(t**2+1)*(t**4+1)*(t**2-t+1)*(t**2+t+1)*(
        t**4-t**2+1)*(t**6+t**2+1)*(t**6+t**4+1)
    assert sp.cancel(p[0]-p[1]-(t**2-1)*poly/den) == 0
    assert sp.gcd(poly, sp.diff(poly,t)) == 1
    assert len(sp.sturm(poly,t)) == 25
    points=[sp.Integer(1),sp.Rational(181,100),sp.Rational(183,100),
            sp.Integer(2),sp.Rational(321,100),sp.Rational(323,100),sp.Integer(4),sp.oo]
    observed=[sturm_variations(poly,x) for x in points]
    assert observed == [13,13,12,12,12,11,11,11], (points,observed)
    assert poly.subs(t,1)>0 and poly.subs(t,2)<0 and poly.subs(t,4)>0
    for rho,winning in [(sp.Rational(3,2),0),(sp.Rational(2),1),(sp.Rational(10),0)]:
        values=[sp.factor(v.subs(t,rho)) for v in p]
        assert values[winning] > max(values[j] for j in range(4) if j!=winning)
    return observed


def main():
    total = 0
    cases = [(1,4), (1,4,9), (1,4,16), (1,4,16,64),
             (1,9,25,49), (4,9,16,25),
             tuple(sp.Rational(3,2)**(2*i) for i in range(4)),
             tuple(sp.Integer(10)**(2*i) for i in range(4))]
    for case in cases:
        total+=grounded_check(list(map(sp.Integer,case)))
    v=phase_certificate()
    print(f'ANISOTROPIC_CUBE_EXACT_OK graphs={len(cases)} grounded_columns={total} sturm_variations={v} phase_roots=2')


if __name__ == '__main__': main()
