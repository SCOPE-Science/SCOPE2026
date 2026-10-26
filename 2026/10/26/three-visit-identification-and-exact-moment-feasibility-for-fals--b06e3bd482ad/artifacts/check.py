#!/usr/bin/env python3
"""Exact rational checks for a closed three-visit Poisson-abundance count model."""
from fractions import Fraction as F
from itertools import product
import hashlib
import json


def subsets(t):
    return range(1, 1 << t)


def shocks(lam, probs, false_rates):
    """Independent Poisson rates for all nonempty subsets of visits."""
    t = len(probs)
    out = {}
    for s in subsets(t):
        v = lam
        for i, p in enumerate(probs):
            v *= p if ((s >> i) & 1) else (1-p)
        for i, rate in enumerate(false_rates):
            if s == 1 << i:
                v += rate
        out[s] = v
    return out


def cross_cumulant(shock_rates, index_mask):
    return sum((rate for s, rate in shock_rates.items()
                if (s & index_mask) == index_mask), F(0))


def moment_tuple(lam, probs, false_rates):
    r = shocks(lam, probs, false_rates)
    return ([cross_cumulant(r, 1 << i) for i in range(3)],
            { (0,1):cross_cumulant(r, 3), (0,2):cross_cumulant(r, 5),
              (1,2):cross_cumulant(r, 6)}, cross_cumulant(r, 7))


def recover(mu, cov, triple):
    c01,c02,c12 = cov[0,1], cov[0,2], cov[1,2]
    p0,p1,p2 = triple/c12, triple/c02, triple/c01
    lam = c01*c02*c12 / (triple*triple)
    phi = (mu[0]-c01*c02/triple, mu[1]-c01*c12/triple,
           mu[2]-c02*c12/triple)
    return lam,(p0,p1,p2),phi


def encode(x):
    if isinstance(x, F): return str(x)
    if isinstance(x, dict): return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x, (tuple,list)): return [encode(v) for v in x]
    return x


def run():
    p_choices=(F(1,7),F(1,3),F(1,2),F(5,6))
    phi_choices=(F(0),F(1,5),F(3,4))
    lam_choices=(F(1,2),F(7,3))
    count=0
    for la in lam_choices:
        for ps in product(p_choices,repeat=3):
            for phi in product(phi_choices,repeat=3):
                mu,c,t=moment_tuple(la,ps,phi)
                assert recover(mu,c,t)==(la,ps,phi)
                assert all(c[k]>t>0 for k in c)
                assert all(mu[i]*t >= c[a,b]*c[d,e] for i,((a,b),(d,e))
                           in enumerate((((0,1),(0,2)),((0,1),(1,2)),((0,2),(1,2)))))
                count+=1
    assert count==2*4**3*3**3

    a=(F(3),[F(1,3),F(1,2)],[F(1,5),F(1,4)])
    b=(F(5,2),[F(2,5),F(1,2)],[F(1,5),F(1,2)])
    assert a!=b and shocks(*a)==shocks(*b)
    m3=moment_tuple(F(5,2), (F(1,4),F(2,5),F(3,7)), (F(1,3),F(2,7),F(1,6)))
    inv=recover(*m3)
    assert inv==(F(5,2),(F(1,4),F(2,5),F(3,7)),(F(1,3),F(2,7),F(1,6)))
    # Scaling p_i by s while adjusting lambda,phi_i preserves every mean/covariance.
    la,ps,phi=inv
    s=F(21,20)
    la2=la/(s*s)
    ps2=tuple(s*p for p in ps)
    phi2=tuple(phi[i]+la*ps[i]*(1-F(1)/s) for i in range(3))
    m3b=moment_tuple(la2,ps2,phi2)
    assert m3b[0]==m3[0] and m3b[1]==m3[1] and m3b[2]==s*m3[2]
    assert la2!=la and all(0<x<1 for x in ps2) and all(x>=0 for x in phi2)
    cert={
      'method':'exact Fraction arithmetic; independent Poisson subset intensities',
      'checked_parameter_tuples':count,
      'example_three_visit':{'lambda':str(inv[0]),'detection':encode(inv[1]),'false_positive':encode(inv[2]),'means':encode(m3[0]),'covariances':encode(m3[1]),'third_cross_cumulant':encode(m3[2])},
      'two_visit_equal_law':{'first':encode(a),'second':encode(b),'rates_by_subset':encode(shocks(*a))},
      'scaled_three_visit_same_first_second_moments':{'scale':str(s),'altered_lambda':str(la2),'altered_detection':encode(ps2),'altered_false_positive':encode(phi2),'altered_third_cross_cumulant':str(m3b[2])},
      'limits':'The finite test is not a proof for all real parameters; the accompanying analytic PGF proof establishes the theorem.'
    }
    print(json.dumps(cert,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':run()
