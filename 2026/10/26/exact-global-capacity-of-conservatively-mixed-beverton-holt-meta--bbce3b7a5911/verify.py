"""Reproduce algebraic and numerical checks for multi-patch Beverton-Holt capacity.

Public scientific verification; Python 3 standard library only. Finite checks
illustrate the identities and are not substitutes for the universal proof.
"""
from fractions import Fraction
from math import sqrt, isclose
from random import Random


def solution(K, r):
    a = [ki / ri for ki, ri in zip(K, r)]
    s = [sqrt(1 + ri) for ri in r]
    B = sum(ai * si for ai, si in zip(a, s))
    C = sum(ai * (2 + ri) for ai, ri in zip(a, r))
    q = C / B
    t = 2 / (q + sqrt(q * q - 4))
    y = [ai * (si / t - 1) for ai, si in zip(a, s)]
    return t * t, y, sum(y)


def growth(x, k, r):
    return (1+r) * x / (1+(r/k)*x)


def iterate(D, K, r):
    n = len(K)
    x = K[:]
    for j in range(30000):
        y = [sum(D[i][a]*x[a] for a in range(n)) for i in range(n)]
        z = [growth(y[i], K[i], r[i]) for i in range(n)]
        if max(abs(z[i]-x[i]) for i in range(n)) < 5e-14:
            return z, j
        x = z
    raise AssertionError('not converged')


class Q5:
    """Exact arithmetic in Q(sqrt(5))."""
    def __init__(self, a=0, b=0):
        if isinstance(a, Q5): self.a, self.b = a.a, a.b
        else: self.a, self.b = Fraction(a), Fraction(b)
    @staticmethod
    def cv(x): return x if isinstance(x, Q5) else Q5(x)
    def __add__(self, o):
        o=self.cv(o); return Q5(self.a+o.a, self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+-self.cv(o)
    def __rsub__(self,o): return self.cv(o)+-self
    def __mul__(self,o):
        o=self.cv(o)
        return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=self.cv(o); den=o.a*o.a-5*o.b*o.b
        assert den
        return self*Q5(o.a/den,-o.b/den)
    def __rtruediv__(self,o): return self.cv(o)/self
    def __eq__(self,o):
        o=self.cv(o);return self.a==o.a and self.b==o.b
    def __repr__(self): return f'({self.a})+({self.b})*sqrt(5)'


def exact_benchmark():
    s=Q5(0,1)
    t=(3-s)/2
    tau=t*t
    y=[2+s,(7+3*s)/2]
    N=sum(y)
    assert N==(11+5*s)/2
    assert sum((1+r)*y[i]/(1+Q5(r)/K*y[i]) for i,(r,K) in enumerate([(3,3),(8,8)]))==N
    for i,(r,K) in enumerate([(3,3),(8,8)]):
        assert Q5(1+r)/(1+Q5(r)/K*y[i])**2==tau
    D=[[y[i]/N for j in range(2)] for i in range(2)]
    x=[(1+r)*y[i]/(1+Q5(r)/K*y[i]) for i,(r,K) in enumerate([(3,3),(8,8)])]
    assert all(sum(D[i][j]*x[j] for j in range(2))==y[i] for i in range(2))
    baseline=[Q5(3),Q5(8)]
    deficit=tau/(1-tau)*sum((Q5(r)/K)*(baseline[i]-y[i])**2/(1+(Q5(r)/K)*baseline[i]) for i,(r,K) in enumerate([(3,3),(8,8)]))
    assert deficit==N-11
    return N

# Add positive-integer exponent to exact field elements.
def _q5_power(self, exponent):
    assert isinstance(exponent,int) and exponent>=0
    z=Q5(1)
    for _ in range(exponent): z=z*self
    return z
Q5.__pow__=_q5_power


def numeric_trials():
    rng=Random(310203)
    checks=0
    for p in range(1,7):
        for case in range(130):
            K=[rng.uniform(.7,12) for _ in range(p)]
            r=[rng.uniform(.5,9) for _ in range(p)]
            if case%17==0: r=[r[0]]*p
            tau,ystar,Nstar=solution(K,r)
            assert 0<tau<1
            assert all(y>0 for y in ystar)
            assert abs(sum(growth(ystar[i],K[i],r[i])-ystar[i] for i in range(p)))<1e-9
            assert all(abs((1+r[i])/(1+(r[i]/K[i])*ystar[i])**2-tau)<1e-11 for i in range(p))
            assert Nstar+1e-8>=sum(K)
            if len(set(r))==1: assert abs(Nstar-sum(K))<1e-8
            else: assert Nstar>sum(K)+1e-9
            W=[[rng.uniform(.1,3.5) for _ in range(p)] for _ in range(p)]
            D=[[W[i][j]/sum(W[a][j] for a in range(p)) for j in range(p)] for i in range(p)]
            x,_=iterate(D,K,r)
            y=[sum(D[i][j]*x[j] for j in range(p)) for i in range(p)]
            N=sum(x)
            lhs=(1-tau)*(Nstar-N)
            rhs=tau*sum((r[i]/K[i])*(y[i]-ystar[i])**2/(1+(r[i]/K[i])*y[i]) for i in range(p))
            assert N<=Nstar+1e-8
            assert abs(lhs-rhs)<1e-9*max(1,Nstar)
            v=[yy/Nstar for yy in ystar]
            Dopt=[[v[i] for _ in range(p)] for i in range(p)]
            xopt,_=iterate(Dopt,K,r)
            assert abs(sum(xopt)-Nstar)<1e-8*max(1,Nstar)
            checks += 1
    return checks


def main():
    assert exact_benchmark()==(Q5(11)+5*Q5(0,1))/2
    n=numeric_trials()
    print('PASS: exact Q(sqrt(5)) benchmark (all identities, maximum, conservation)')
    print('PASS: %d deterministic random cases p=1..6 (existence convergence, unique optimum, exact deficit, strict heterogeneity)'%n)

if __name__=='__main__':main()
