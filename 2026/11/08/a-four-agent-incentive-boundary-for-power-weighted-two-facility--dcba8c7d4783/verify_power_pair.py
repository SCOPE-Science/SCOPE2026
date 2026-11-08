"""Exact checks for a four-agent power-weighted pair-location witness.

Requires only Python 3 standard library. Finite checks support, but do not
replace, the continuous-exponent and all-reports proofs in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def cost(reports, i, alpha):
    """Expected distance to nearer facility, with integer alpha."""
    truth = F(0)
    weights = []
    for a in range(len(reports)):
        for b in range(a + 1, len(reports)):
            w = abs(reports[a] - reports[b]) ** alpha
            weights.append((w, min(abs(truth-reports[a]),abs(truth-reports[b]))))
    den = sum(w for w, _ in weights)
    assert den
    return sum(w*c for w,c in weights)/den


def run():
    assert cost([F(0),F(1),F(1),F(-1)],0,3)==F(16,19)
    assert cost([F(-1,5),F(1),F(1),F(-1)],0,3)==F(164,195)
    assert F(16,19)-F(164,195)==F(4,3705)
    total = 0
    for alpha in (1,2,3,4,5):
        for k in range(-80,81):
            r=F(k,40)
            actual=cost([r,F(1),F(1),F(-1)],0,alpha)
            t=abs(r)
            if t<=1:
                A=F(2)**(alpha+1)
                S=2*abs(1-r)**alpha+abs(1+r)**alpha
                expected=(A+t*S)/(A+S)
                assert actual==expected
            if alpha in (1,2):
                assert actual>=cost([F(0),F(1),F(1),F(-1)],0,alpha)
            total+=1
    P=lambda t: -9+87*t-155*t*t-19*t*t*t
    assert P(F(0))<0 and P(F(1,4))>0 and P(F(1))<0
    assert P(F(1,10))<0 and P(F(1,5))>0 and P(F(1,2))<0
    # Exact positive-r branch exclusion for every tested rational report.
    for j in range(0,1001):
        t=F(j,1000)
        branch= -105+201*t-187*t*t+19*t**3
        assert branch<0
    print('PASS: 805 exact direct/closed-form evaluations, 322 local non-manipulability checks, cubic signs, 1001 positive-report exclusions')

if __name__=='__main__':
    run()
