"""Independent numerical substitutions for the two-dimensional RMSProp cycle formulas.
No floating-point experiment is used as a proof of the exhaustive census.
"""
from math import sqrt, isclose
from fractions import Fraction as Q


def families(a, b, c):
    assert a > b > 0 and c > 0
    out = []
    if c < (a + b) / 2:
        t = (1 - 2 * c / (a + b)) / 2
        out.append((t, t))
    if c < (a - b) / 2:
        t = (1 - 2 * c / (a - b)) / 2
        out.append((t, -t))
    if c < (a - b) ** 2 / (2 * (a + b)):
        s = (a + b - 2 * c) / (2 * a)
        delta = (a + b - 2*c)*((a - b)**2 - 2*c*(a+b))/(4*a*a*(a+b))
        x, z = (s + sqrt(delta))/2, (s - sqrt(delta))/2
        out.extend([(x, -z), (z, -x)])
    return out


def rmsprop_step(X, V, a, b, beta, c):
    grad = (a*X[0]+b*X[1], b*X[0]+a*X[1])
    W2 = [beta*V[i] + (1-beta)*grad[i]**2 for i in range(2)]
    Y = [X[i]-grad[i]/(sqrt(W2[i])+c) for i in range(2)]
    return Y, W2


def test():
    cases = 0
    for a, b in [(2.,1.), (3.,1.), (5.,2.), (3.,2.)]:
        cp, cm, cs = (a+b)/2, (a-b)/2, (a-b)**2/(2*(a+b))
        assert 0 < cs < cm < cp
        for c, expected in [(0.3*cs,4),(cs,2),(0.5*(cs+cm),2),(cm,1),(0.5*(cm+cp),1),(cp,0),(cp+0.1,0)]:
            S = families(a,b,c)
            assert len(S)==expected, (a,b,c,len(S),expected)
            for X in S:
                assert all(0 < abs(q) < 0.5 for q in X)
                g = [a*X[0]+b*X[1],b*X[0]+a*X[1]]
                for i in range(2):
                    assert abs(g[i] - 2*c*X[i]/(1-2*abs(X[i]))) < 1e-11
                for beta in [0.17,0.5,0.93]:
                    V=[g[0]**2,g[1]**2]
                    Y,U=rmsprop_step(X,V,a,b,beta,c)
                    assert max(abs(Y[i]+X[i]) for i in range(2))<1e-11
                    Z,W=rmsprop_step(Y,U,a,b,beta,c)
                    assert max(abs(Z[i]-X[i]) for i in range(2))<1e-11
                    assert max(abs(W[i]-V[i]) for i in range(2))<1e-11
                    cases += 1
    # Check the discriminant identity at exact rational parameters independently.
    rational=0
    for a,b,c in [(Q(2),Q(1),Q(1,20)),(Q(3),Q(1),Q(1,8)),(Q(5),Q(2),Q(1,6))]:
        s=(a+b-2*c)/(2*a)
        p=b*s/(2*(a+b))
        D=s*s-4*p
        closed=(a+b-2*c)*((a-b)**2-2*c*(a+b))/(4*a*a*(a+b))
        assert D==closed and D>0
        assert (1-2*s+4*p)==2*c/(a+b)
        rational+=1
    print(f'CHECKS_PASS: {cases} complete two-step orbit substitutions across four Hessians and three memory parameters; {rational} exact-rational discriminant checks.')

if __name__ == '__main__':
    test()
