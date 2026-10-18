#!/usr/bin/env python3
"""Independent finite numerical diagnostics for a pure n-body SIS mean-field flow.

Requires only Python 3 standard library. The infinite-parameter and global
convergence claims are proved analytically in RESULT.md, not by this script.
"""
import math
import itertools


def activation(z):
    # Positive root of x*x/(1-x)=z, stable at both small and large z.
    return 2.0 * z / (z + math.sqrt(z * z + 4.0 * z))


def rate_and_state(s, b):
    x = [activation(v * s) for v in b]
    return s / math.prod(x), x


def elasticity_sum(s, b):
    return sum((1.0 - x) / (2.0 - x) for x in rate_and_state(s, b)[1])


def threshold(b):
    assert len(b) >= 3 and all(v > 0 for v in b)
    lo, hi = -25.0, 25.0
    assert elasticity_sum(math.exp(lo), b) > 1
    assert elasticity_sum(math.exp(hi), b) < 1
    for _ in range(130):
        m = (lo + hi) / 2
        if elasticity_sum(math.exp(m), b) > 1:
            lo = m
        else:
            hi = m
    s = math.exp((lo + hi) / 2)
    lam, x = rate_and_state(s, b)
    return lam, s, x


def jacobian(x, b, lam, recover):
    ans = []
    for i in range(len(x)):
        row = []
        for j in range(len(x)):
            if i == j:
                row.append(-recover[i] - lam * recover[i] * b[i] *
                           math.prod(x[k] for k in range(len(x)) if k != i))
            else:
                row.append(lam * recover[i] * b[i] * (1-x[i]) *
                           math.prod(x[k] for k in range(len(x)) if k != i and k != j))
        ans.append(row)
    return ans


def max_residual(x, b, lam, recover):
    return max(abs(-recover[i] * x[i] + lam * recover[i] * b[i] *
                   (1-x[i])*math.prod(x[j] for j in range(len(x)) if j != i))
               for i in range(len(x)))


def potential(x, b, lam):
    return sum((-v-math.log1p(-v))/bi for v,bi in zip(x,b)) - lam*math.prod(x)


def check_case(b, recover):
    n = len(b)
    lc, sc, xc = threshold(b)
    g = math.prod(b) ** (1.0 / n)
    lower = (n-1)**(n-1)/(g*(n-2)**(n-2))
    assert lc >= lower-1.e-11
    if max(b)-min(b) > 1.e-12:
        assert lc > lower+1.e-7
    assert max_residual(xc,b,lc,recover) < 1.e-9
    for factor in (0.6,0.9,1.2,2.0):
        # Direct substitution of upper/lower branch states.
        level = factor*lc
        if factor < 1:
            continue
        for left in (True, False):
            lo,hi = (sc*1.e-5,sc) if left else (sc,sc*10000)
            fl = (rate_and_state(lo,b)[0]-level)
            fr = (rate_and_state(hi,b)[0]-level)
            assert fl*fr < 0
            for _ in range(110):
                mid = (lo+hi)/2
                fm = rate_and_state(mid,b)[0]-level
                if fl*fm > 0:
                    lo=mid;fl=fm
                else:
                    hi=mid
            _,x = rate_and_state((lo+hi)/2,b)
            assert max_residual(x,b,level,recover)<1.e-8
            E = sum((1-v)/(2-v) for v in x)
            assert (E>1)==left
            j=jacobian(x,b,level,recover)
            for i in range(n):
                assert abs(j[i][i] + recover[i]/(1-x[i]))<1.e-7
                for k in range(n):
                    if k!=i:
                        assert abs(j[i][k] - recover[i]*x[i]/x[k])<1.e-7
    for i in range(n):
        eps=1.e-5
        pert=list(b)
        pert[i]*=math.exp(eps)
        ell=(math.log(threshold(pert)[0])-math.log(lc))/eps
        want=-(1-xc[i])/(2-xc[i])
        assert abs(ell-want)<5.e-6,(ell,want)
    # Gradient relation is checked directly at a generic strict-interior state.
    sample=[.18 +.04*i for i in range(n)]
    lam=lc*1.31
    eps=1.e-6
    for i in range(n):
        u=sample.copy();v=sample.copy();u[i]+=eps;v[i]-=eps
        partial=(potential(u,b,lam)-potential(v,b,lam))/(2*eps)
        rhs=-recover[i]*sample[i] + lam*recover[i]*b[i]*(1-sample[i])*math.prod(sample[j] for j in range(n) if j!=i)
        assert abs(rhs+recover[i]*b[i]*(1-sample[i])*partial)<2.e-8
    print('n=',n,'ratios=',b,'lambda_fold=',format(lc,'.12f'),
          'homogeneous_bound=',format(lower,'.12f'),'PASS')


if __name__ == '__main__':
    specs=[([1.,1.,1.],[1.,1.,1.]),
           ([.25,1.,4.],[2.,1.,.5]),
           ([1.,1.,1.,1.],[1.,2.,3.,4.]),
           ([.25,.5,2.,4.],[2.,1.,3.,.5]),
           ([.2,.4,.8,1.5,2.],[1.,2.,3.,4.,5.])]
    for b,r in specs:
        check_case(b,r)
    print('All finite diagnostics passed; they do not substitute for the analytical proof.')
