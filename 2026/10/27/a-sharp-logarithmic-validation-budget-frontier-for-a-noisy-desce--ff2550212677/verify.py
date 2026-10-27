"""Standalone exact-arithmetic verification for a two-label noisy-validation search.

Uses only Python's standard library and enumerates every training and
validation sign pattern for modest batch sizes. It does not certify the
infinite-horizon large-deviation or Borel--Cantelli arguments.
"""
from fractions import Fraction
from itertools import product
from math import comb, exp, log, sqrt
import json


def f(label, x):
    return Fraction((x-label)**2, 2)


def accept(x, s, signs):
    y = s  # unit-step gradient proposal for f_s(x) = (x-s)^2/2
    return sum((f(v, y) for v in signs), Fraction(0)) < sum(
        (f(v, x) for v in signs), Fraction(0)
    )


def tail(B, lower):
    return Fraction(sum(comb(B, j) for j in range(lower, B+1)), 2**B)


def p0(B):
    return tail(B, (3*B)//4+1)


def q1(B):
    return tail(B, B//2+1)/2


def enumerate_batch(B):
    for x in (0, -1, 1):
        totals={-1:0, 0:0, 1:0}
        for s in (-1,1):
            for signs in product((-1,1), repeat=B):
                y=s if accept(x,s,signs) else x
                totals[y] += 1
        scale=2**(B+1)
        if x==0:
            assert Fraction(totals[0],scale)==1-p0(B), (x,B,totals)
            assert Fraction(totals[1],scale)==p0(B)/2, (x,B,totals)
            assert Fraction(totals[-1],scale)==p0(B)/2,(x,B,totals)
        elif x==1:
            assert Fraction(totals[-1],scale)==q1(B), (x,B,totals)
            assert Fraction(totals[1],scale)==1-q1(B), (x,B,totals)
            assert totals[0]==0
        else:
            assert Fraction(totals[1],scale)==q1(B), (x,B,totals)
            assert Fraction(totals[-1],scale)==1-q1(B), (x,B,totals)
            assert totals[0]==0
    return 3*(2**(B+1))


def transient_schedule(bs):
    d={0:Fraction(1),-1:Fraction(0),1:Fraction(0)}
    survival=Fraction(1)
    for B in bs:
        n={i:Fraction(0) for i in d}
        for state,mass in d.items():
            if state==0:
                n[0]+=mass*(1-p0(B))
                n[1]+=mass*p0(B)/2
                n[-1]+=mass*p0(B)/2
            elif state==1:
                n[1]+=mass*(1-q1(B))
                n[-1]+=mass*q1(B)
            else:
                n[-1]+=mass*(1-q1(B))
                n[1]+=mass*q1(B)
        d=n
        survival *= 1-p0(B)
        assert d[0]==survival
        assert sum(d.values())==1
        assert (d[1]+d[-1])/2==(1-survival)/2
        assert d[-1]==d[1]
    return d,survival


def log_large_deviation_check():
    I=Fraction(3,4)*log(1.5)+Fraction(1,4)*log(0.5)
    # Floating-point check only; the proof uses Stirling and bounded
    # consecutive binomial-tail ratios, not this finite sample.
    vals=[]
    for B in (20, 40, 80, 160, 320, 640):
        p=p0(B)
        scaled=float(p)*sqrt(B)*exp(float(I)*B)
        assert 0.15<scaled<4, (B,scaled)
        vals.append([B,scaled])
    return float(I),vals


def main():
    transitions=sum(enumerate_batch(B) for B in range(1,12))
    schedules=[(1,1,1,1,1),(1,2,3,4,5,6),(4,3,2,1,2,3,4),tuple((k*7)//3+1 for k in range(1,13))]
    for bs in schedules: transient_schedule(bs)
    rate,scaled=log_large_deviation_check()
    print(json.dumps({
      'status':'passed',
      'exact_enumerated_batch_sizes':list(range(1,12)),
      'exhaustive_training_validation_cases':transitions,
      'exact_fraction_schedule_checks':len(schedules),
      'relative_entropy_rate':rate,
      'critical_log_batch_multiplier':1/rate,
      'finite_sample_stirling_scale_checks':scaled,
      'scope_note':'Finite checks validate the combinatorial transition formulas; infinite-horizon thresholds require the written proof.'
    },separators=(',',':')))


if __name__=='__main__':main()
