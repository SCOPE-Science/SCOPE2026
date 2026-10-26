"""Exact finite certificate for degree-matched plant-survival variance reversal.
Requires Python 3.9+ standard library only. Run: python verifier.py
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import json

def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)

def variance_overlap_polynomial(rows, pollinators):
    # The single-plant Bernoulli variance is degree-only, hence canceled
    # in every comparison with matched plant degrees.
    deg = [row.bit_count() for row in rows]
    ans = [0] * (2 * pollinators + 1)
    for i, j in combinations(range(len(rows)), 2):
        union = (rows[i] | rows[j]).bit_count()
        ans[union] += 2
        ans[deg[i] + deg[j]] -= 2
    return trim(ans)

def reduction(poly):
    a = list(poly)
    while len(a)>1 and a[0]==0:
        a.pop(0)  # remove factors of q
    while len(a)>1 and sum(a)==0:
        b = [a[0]]
        for k in range(1, len(a)-1):
            b.append(a[k]+b[-1])
        assert -b[-1] == a[-1]
        a = b  # remove factor (1-q)
    if a[0] < 0:
        a = [-x for x in a]
    g = abs(a[0])
    from math import gcd
    for x in a[1:]:
        g = gcd(g, abs(x))
    return tuple(x//g for x in a)

def enumerate_class(r,c):
    groups = defaultdict(set)
    tested=0
    for raw in range(1<<(r*c)):
        rows = tuple((raw>>(i*c)) & ((1<<c)-1) for i in range(r))
        ds=tuple(x.bit_count() for x in rows)
        if min(ds)==0 or rows!=tuple(sorted(rows)):
            continue
        cs=tuple(sorted(sum((row>>j)&1 for row in rows) for j in range(c)))
        if cs[0]==0:
            continue
        tested+=1
        groups[(tuple(sorted(ds)),cs)].add(variance_overlap_polynomial(rows,c))
    return groups,tested

def direct_variance(rows, c, q):
    e=Fraction(0);second=Fraction(0)
    for extinguished in range(1<<c):
        n=extinguished.bit_count()
        weight=q**n*(1-q)**(c-n)
        survivors=sum(1 for row in rows if row & ~extinguished)
        e+=survivors*weight
        second+=survivors*survivors*weight
    return second-e*e

def analytic_variance(rows,c,q):
    ds=[x.bit_count() for x in rows]
    v=sum((q**d)*(1-q**d) for d in ds)
    for i,j in combinations(range(len(rows)),2):
        h=(rows[i]&rows[j]).bit_count()
        v+=2*(q**(ds[i]+ds[j]-h)-q**(ds[i]+ds[j]))
    return v

def main():
    summaries=[];differences=set(); largest=0
    for r in range(2,7):
      for c in range(2,7):
        if r+c>8:continue
        groups,tested=enumerate_class(r,c)
        pair_count=0
        for polynomials in groups.values():
            for a,b in combinations(sorted(polynomials),2):
                pair_count+=1
                n=max(len(a),len(b))
                d=trim(tuple((a[k] if k<len(a) else 0)-(b[k] if k<len(b) else 0) for k in range(n)))
                if not any(d):continue
                if next(x for x in d if x)<0:d=tuple(-x for x in d)
                differences.add(d)
        summaries.append({'plants':r,'pollinators':c,'canonical_matrices':tested,
                          'degree_classes':len(groups),'distinct_curves':sum(map(len,groups.values())),
                          'curve_pairs':pair_count})
        largest+=pair_count
    allowed={(1,),(1,1),(1,2),(1,1,1)}
    reduced={reduction(d) for d in differences}
    assert reduced.issubset(allowed),(reduced-allowed)
    assert len(differences)==13,(len(differences),differences)
    A=(2,17,14,14)
    B=(16,17,7,11)
    assert sorted(map(int.bit_count,A))==sorted(map(int.bit_count,B))==[1,2,3,3]
    colseq=lambda rows: sorted(sum((row>>j)&1 for row in rows) for j in range(5))
    assert colseq(A)==colseq(B)==[1,1,2,2,3]
    # Variance(A)-Variance(B)=-2q^2(1-q)^2(1-2q).
    for q in (Fraction(1,5),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(4,5)):
      for rows in (A,B):
        assert direct_variance(rows,5,q)==analytic_variance(rows,5,q)
      delta=analytic_variance(A,5,q)-analytic_variance(B,5,q)
      assert delta==-2*q*q*(1-q)**2*(1-2*q)
    cert={'verifier':'exact_finite_certificate_v1','restricted_scope':'all simple bipartite matrices with no zero row or column and total vertex count <=8','cases':summaries,'total_pairs':largest,'distinct_nonzero_difference_polynomials':len(differences),'all_reduced_factors':sorted(map(list,reduced)),'witness_degrees_plants':[1,2,3,3],'witness_degrees_pollinators':[1,1,2,2,3],
          'witness_A_rows':[2,17,14,14],'witness_B_rows':[16,17,7,11],
          'witness_variance_A_q1_4':str(analytic_variance(A,5,Fraction(1,4))),
          'witness_variance_B_q1_4':str(analytic_variance(B,5,Fraction(1,4))),
          'witness_variance_A_q3_4':str(analytic_variance(A,5,Fraction(3,4))),
          'witness_variance_B_q3_4':str(analytic_variance(B,5,Fraction(3,4)))}
    print(json.dumps(cert,sort_keys=True,ensure_ascii=False,separators=(',',':')))

if __name__=='__main__':main()
