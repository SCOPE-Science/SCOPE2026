"""Exact rational tests for a symmetric doubling-map transfer subspace and digit pairs.

The finite parameter grid is diagnostic; the accompanying algebraic proof is universal.
"""
from fractions import Fraction as Q
from math import log

HALF = Q(1, 2)
ONE = Q(1)
ZERO = Q(0)


def regions(alpha):
    c = alpha - ONE
    p = 2 - alpha
    r = 2 * alpha - 2
    return c, p, r


def indicator(z, t):
    return Q(int(abs(z) < t))


def g0(z, alpha):
    c, p, r = regions(alpha)
    return ONE + indicator(z, c)


def g1(z, alpha):
    c, p, r = regions(alpha)
    return indicator(z, p) + indicator(z, r)


def density(z, alpha):
    return (g0(z, alpha) + HALF * g1(z, alpha)) / (3 * alpha)


def transfer(f, z, alpha):
    # Inverse branches are used only where their source coordinates are valid.
    c, p, r = regions(alpha)
    ret = f(z / 2, alpha)
    if -p < z < c:
        ret += f((z-alpha)/2, alpha)
    if -c < z < p:
        ret += f((z+alpha)/2, alpha)
    return ret/2


def test_transfer(alpha):
    c, p, r = regions(alpha)
    breaks = {-ONE, ZERO, ONE}
    source_cuts = {-ONE, -r, -p, -c, ZERO, c, p, r, ONE, -HALF, HALF}
    for s in source_cuts:
        for k in (-alpha, ZERO, alpha):
            y = 2*s+k
            if -ONE < y < ONE:
                breaks.add(y)
    breaks.update([-c,c,-p,p,-r,r])
    ordered=sorted(x for x in breaks if -ONE<=x<=ONE)
    num = 0
    for lo,hi in zip(ordered,ordered[1:]):
        if lo==hi: continue
        z=(lo+hi)/2
        assert transfer(g0,z,alpha)==(g0(z,alpha)+g1(z,alpha))/2,('g0',alpha,z)
        assert transfer(g1,z,alpha)==g0(z,alpha),('g1',alpha,z)
        assert transfer(density,z,alpha)==density(z,alpha),('density',alpha,z)
        num +=3
    return num


def integrate_density(a,b,alpha):
    if a>=b: return ZERO
    c,p,r=regions(alpha)
    cuts=sorted(set([a,b]+[z for z in (-r,-p,-c,ZERO,c,p,r) if a<z<b]))
    result=ZERO
    for lo,hi in zip(cuts,cuts[1:]):
        result+=(hi-lo)*density((hi+lo)/2,alpha)
    return result


def pair_prob(i,j,alpha):
    def cell(d):
        return {-1:(-ONE,-HALF),0:(-HALF,HALF),1:(HALF,ONE)}[d]
    lo_i,hi_i=cell(i)
    lo_j,hi_j=cell(j)
    # On cell i, map is y=2x-i*alpha.
    lo=max(lo_i,(lo_j+i*alpha)/2)
    hi=min(hi_i,(hi_j+i*alpha)/2)
    return integrate_density(lo,hi,alpha)


def validate(alpha):
    assert Q(4,3)<=alpha<=Q(3,2)
    assert integrate_density(-ONE,ONE,alpha)==ONE
    c,p,r=regions(alpha)
    assert ZERO<c<=p<=r<=ONE
    n=test_transfer(alpha)
    A=(3-2*alpha)/(12*alpha)
    B=(4*alpha-3)/(12*alpha)
    C=1/(2*alpha)
    expected={(-1,-1):A,(-1,0):B,(-1,1):ZERO,
              (0,-1):B,(0,0):C,(0,1):B,
              (1,-1):ZERO,(1,0):B,(1,1):A}
    for (i,j),value in expected.items():
        measured=pair_prob(i,j,alpha)
        assert measured==value,('pair',alpha,i,j,measured,value)
        n+=1
    assert sum(expected.values())==ONE
    assert 2*A+4*B+C == ONE  # all 9 cells, zeros omitted
    for i in (-1,0,1):
        marginal = sum(expected[i,j] for j in (-1,0,1))
        assert marginal == (Q(2,3) if i==0 else Q(1,6))
        n+=1
    return n


def cond_entropy(alpha):
    a=float((3-2*alpha)/(12*alpha))
    b=float((4*alpha-3)/(12*alpha))
    c=float(1/(2*alpha))
    f=lambda x,y: -x*log(y) if x>0 else 0.0
    return 2*f(a,6*a)+2*f(b,6*b)+2*f(b,1.5*b)+f(c,1.5*c)


def main():
    checks=0
    params=[Q(4,3),Q(3,2)]+[Q(4,3)+(Q(1,6)*Q(i,31)) for i in range(1,31)]
    for alpha in params:
        checks += validate(alpha)
    for left,right in zip(params[2:-1],params[3:]):
        # Parameter order in this segment is increasing, independent diagnostic.
        assert cond_entropy(left)>cond_entropy(right)
        checks+=1
    print('CHECK_OK', 'parameters',len(params),'exact_or_derived_checks',checks)


if __name__ == '__main__':
    main()
