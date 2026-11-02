"""Exact arithmetic checks for two-sink capture on strongly regular graphs.

Requires SymPy. Directly verifies probabilities, site class counts,
and total absorption using algebraic eigenvalues and rational simplification.
"""
from sympy import Rational, sqrt, simplify


def classes(v, k, lam, mu, adj):
    q = v - 1 - k
    rt = sqrt((lam-mu)**2 + 4*(k-mu))
    r, s = (lam-mu+rt)/2, (lam-mu-rt)/2
    mr = simplify((-k-(v-1)*s)/(r-s))
    ms = simplify(v-1-mr)
    t = lam if adj else mu
    pop = [(1, 1, t), (1, 0, 2*(k-adj-t)), (0, 0, v-2-2*k+2*adj+t)]

    def rho(z, eig):
        return eig/k if z == 1 else -(1+eig)/q

    result=[]
    for alpha, beta, count in pop:
        if not count:
            continue
        eff=Rational(1, v)
        for eig,mul in [(r,mr),(s,ms)]:
            z=rho(adj, eig)
            aa, bb=rho(alpha,eig), rho(beta,eig)
            eff += (mul/v)*(aa*aa+bb*bb-2*z*aa*bb)/(1-z*z)
        result.append((str((alpha,beta)),count,simplify(eff)))
    assert simplify(sum(count*eff for _,count,eff in result) - 3)==0
    assert sum(count for _,count,_ in result)==v-2
    return result


if __name__ == '__main__':
    for name, params in [('Petersen',(10,3,0,1)),('Rook-Shrikhande',(16,6,2,2)),('Paley13',(13,6,2,3)),('Cycle5',(5,2,0,1))]:
        for d in (0,1):
            c=classes(*params,d)
            print(name,'sink_adjacent',d,'classes',c)
    assert classes(16,6,2,2,1)==[('(1, 1)', 2, Rational(5,16)), ('(1, 0)', 6, Rational(1,4)), ('(0, 0)', 6, Rational(7,48))]
    assert classes(16,6,2,2,0)==[('(1, 1)', 2, Rational(3,10)), ('(1, 0)', 8, Rational(1,5)), ('(0, 0)', 4, Rational(1,5))]
    print('Exact class and identity checks: PASS')
