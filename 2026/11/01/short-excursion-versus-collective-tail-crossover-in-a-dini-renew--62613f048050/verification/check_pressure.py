"""Numerical diagnostics for power-tail renewal pressure and crossover.

Run: python3 verification/check_pressure.py
Requires only Python's standard library. It tests finite computational identities,
not the infinite asymptotic theorem.
"""
import math


def zeta_euler(s, N=25000):
    """Euler-Maclaurin approximation; s>1. Error not interval-certified."""
    assert s > 1
    total = sum(n ** (-s) for n in range(1, N))
    total += N ** (1-s) / (s-1) + 0.5 * N**(-s)
    total += s * N**(-s-1) / 12
    total -= s * (s+1) * (s+2) * N**(-s-3) / 720
    total += s * (s+1) * (s+2) * (s+3) * (s+4) * N**(-s-5) / 30240
    return total


def critical_p():
    f=lambda p:(p-1)*zeta_euler(p)-1-2**(-p)
    lo,hi=1.2,1.9
    assert f(lo)<0<f(hi)
    for _ in range(55):
        m=(lo+hi)/2
        if f(m)>0:hi=m
        else:lo=m
    return (lo+hi)/2


def pressure_bracket(beta, p, cutoff=24000):
    S=zeta_euler(p)
    A=0.0
    weights=[]
    for k in range(cutoff):
        A+=1/(k+1)**p
        weights.append(math.exp(-beta*A))
    A_cut=A+1/(cutoff+1)**p
    b=math.exp(-beta*S)
    def series(P, upper):
        z=math.exp(-P)
        r=z
        acc=0.0
        for weight in weights:
            acc+=weight*r
            r*=z
        coeff=math.exp(-beta*A_cut) if upper else b
        return acc+coeff*r/(-math.expm1(-P))
    def root(upper):
        lo,hi=0.0,2.0
        for _ in range(65):
            mid=(lo+hi)/2
            if series(mid, upper)>1:lo=mid
            else:hi=mid
        return (lo+hi)/2
    lower,upper=root(False),root(True)
    return lower,upper,b


def run():
    p_star=critical_p()
    assert 1.5531 < p_star < 1.5533
    print('crossover exponent approximately:', format(p_star,'.12f'))
    checks=1
    for p in (1.2,1.4,1.5,1.7,2.,3.):
        g=(p-1)*zeta_euler(p)
        h=1+2**(-p)
        assert (g<h) == (p<p_star)
        checks+=1
    for p in (1.5,2.,3.):
        for beta in (1.,2.,3.):
            low,high,b=pressure_bracket(beta,p)
            assert 0 < low<=high<2
            assert low > math.log1p(b)-2e-11
            assert (high-low)/low<0.01
            print('p,beta',p,beta,'P in [',format(low,'.12g'),',',format(high,'.12g'),']')
            checks+=3
    # Exact finite Shannon/Gibbs variational identity, with arbitrary finite weights.
    for beta in (0.5,1.5,3.):
        A=[sum(1/j**1.7 for j in range(1,k+2)) for k in range(30)]
        w=[math.exp(-beta*a) for a in A]
        z=sum(w)
        pi=[r/z for r in w]
        entropy=-sum(t*math.log(t) for t in pi)
        assert abs(entropy-beta*sum(t*a for t,a in zip(pi,A))-math.log(z))<1e-12
        checks+=1
    print('PASS:',checks,'finite checks; no claim of proof by computation')

if __name__=='__main__':
    run()
