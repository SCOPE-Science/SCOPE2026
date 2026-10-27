"""Exact rational moment checks for a three-season occupancy detection model.

Run with Python 3 standard library: python verify.py > certificate.json
"""
from fractions import Fraction as F
from itertools import product
import json


def chain_law(pi, lam, sensitivities, false_positives=None):
    """Population probabilities for three binary surveys of one latent site."""
    assert len(sensitivities) == 3
    if false_positives is None:
        false_positives = (F(0),) * 3
    assert len(false_positives) == 3
    c = pi * (1 - lam)
    e = (1 - pi) * (1 - lam)
    assert 0 < c < 1 and 0 < e < 1
    out = {}
    for y in product((0, 1), repeat=3):
        val = F(0)
        for x in product((0, 1), repeat=3):
            p = pi if x[0] else 1 - pi
            for t in (1, 2):
                p *= ((1 - e) if x[t] else e) if x[t - 1] else (c if x[t] else 1 - c)
            for t in range(3):
                prob = sensitivities[t] if x[t] else false_positives[t]
                p *= prob if y[t] else 1 - prob
            val += p
        out[''.join(map(str, y))] = val
    assert sum(out.values()) == 1
    return out


def summaries(law):
    m = [sum(p * int(k[i]) for k, p in law.items()) for i in range(3)]
    cov = {}
    r = {}
    for i, j in ((0, 1), (1, 2), (0, 2)):
        c = sum(p * int(k[i]) * int(k[j]) for k, p in law.items()) - m[i] * m[j]
        cov[f'{i}{j}'] = c
        r[f'{i}{j}'] = c / (m[i] * m[j])
    return m, cov, r


def invert(m, r):
    assert r['01'] == r['12'] and r['01'] != 0 and r['02'] > 0
    lam = r['02'] / r['01']
    a = r['01'] * r['12'] / r['02']
    pi = 1 / (1 + a)
    sensitivities = tuple(x / pi for x in m)
    return pi, lam, sensitivities, pi * (1 - lam), (1 - pi) * (1 - lam)


def fmt(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, (tuple, list)):
        return [fmt(i) for i in x]
    if isinstance(x, dict):
        return {k: fmt(v) for k, v in x.items()}
    return x


def check_example(pi, lam, d):
    law = chain_law(pi, lam, d)
    m, cov, r = summaries(law)
    got = invert(m, r)
    assert got == (pi, lam, d, pi*(1-lam), (1-pi)*(1-lam))
    return {'parameters':fmt({'pi':pi,'lambda':lam,'detection':d}),
            'means':fmt(m),'covariances':fmt(cov),'normalized_covariances':fmt(r),
            'recovered':fmt(got),'full_law':fmt(law)}


def check_two_season_ambiguity():
    d0=(F(1,2),F(3,4),F(2,3))
    d1=(F(2,5),F(3,5),F(1,2))
    l0=chain_law(F(2,5), F(1,3), d0)
    l1=chain_law(F(1,2), F(1,2), d1)
    marginal0={k:sum(v for bits,v in l0.items() if bits[:2]==k) for k in ('00','01','10','11')}
    marginal1={k:sum(v for bits,v in l1.items() if bits[:2]==k) for k in ('00','01','10','11')}
    assert marginal0==marginal1
    return fmt({'model_A':{'pi':F(2,5),'lambda':F(1,3),'d0':d0[0],'d1':d0[1]},
                'model_B':{'pi':F(1,2),'lambda':F(1,2),'d0':d1[0],'d1':d1[1]},
                'common_two_season_law':marginal0})


def check_false_positive_ambiguity():
    d=(F(1,2),F(3,4),F(2,3))
    baseline=chain_law(F(1,2),F(1,3),d)
    altered=chain_law(F(9,25),F(1,3),tuple(F(7,6)*x for x in d),tuple(x/8 for x in d))
    m0, c0, r0=summaries(baseline)
    m1, c1, r1=summaries(altered)
    assert m0==m1 and c0==c1 and r0==r1
    assert baseline!=altered
    return fmt({'true_zero_false_positive_model':{'pi':F(1,2),'lambda':F(1,3),'sensitivity':d},
                'alternative_false_positive_model':{'pi':F(9,25),'lambda':F(1,3),
                    'sensitivity':[F(7,6)*x for x in d], 'false_positive':[x/8 for x in d]},
                'shared_means':m0,'shared_covariances':c0,
                'three_way_event_111_first':baseline['111'],
                'three_way_event_111_second':altered['111']})


def check_lambda_zero_ambiguity():
    d=(F(1,2),F(3,4),F(2,3))
    la=chain_law(F(1,2),F(0),d)
    # Keep the three observed success probabilities fixed after changing true occupancy.
    lb=chain_law(F(3,5),F(0),tuple(F(5,6)*x for x in d))
    assert la==lb
    return fmt({'model_A_pi':F(1,2),'model_B_pi':F(3,5),
                'common_full_three_season_law':la})


if __name__=='__main__':
    examples = [
        check_example(F(2,5),F(1,3),(F(1,2),F(3,4),F(2,3))),
        check_example(F(3,5),F(-1,4),(F(1,3),F(3,4),F(1,2))),
        check_example(F(7,10),F(2,5),(F(2,3),F(1,3),F(4,5))),
    ]
    out={'schema_version':1,'method':'exact enumeration of binary hidden and observed triples',
         'positive_negative_examples':examples,
         'two_season_ambiguity':check_two_season_ambiguity(),
         'false_positive_ambiguity':check_false_positive_ambiguity(),
         'zero_temporal_memory_ambiguity':check_lambda_zero_ambiguity(),
         'outcome':'All population moments, algebraic inversions, and boundary examples verified using fractions.'}
    print(json.dumps(out,sort_keys=True,separators=(',',':'),ensure_ascii=False))
