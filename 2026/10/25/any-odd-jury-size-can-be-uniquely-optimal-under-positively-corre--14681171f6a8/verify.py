"""Exact rational checks for majority-jury gain and moment-law separation."""
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path

def majority(p, m):
    n=2*m+1
    return sum(F(comb(n,k))*p**k*(1-p)**(n-k) for k in range(m+1,n+1))

def meanvar(law):
    mu=sum(w*p for p,w in law)
    return mu,sum(w*p*p for p,w in law)-mu*mu

def gain_formula(law,m):
    return F(comb(2*m+1,m))*sum(w*(2*p-1)*(p*(1-p))**(m+1) for p,w in law)

def j(law,m): return sum(w*majority(p,m) for p,w in law)

def fmt(x): return str(x)

cases=0
for pp in (F(3,5),F(2,3),F(3,4),F(9,10)):
    for qq in (F(1,10),F(1,4),F(2,5)):
        for w in (F(1,7),F(1,3),F(1,2),F(7,10),F(9,10)):
            law=[(pp,w),(qq,1-w)]
            for m in range(12):
                assert j(law,m+1)-j(law,m)==gain_formula(law,m)
                cases+=1

pair_a=[(F(1,2),F(21,46)),(F(24,25),F(25,46))]
pair_b=[(F(9,10),F(7,10)),(F(2,5),F(3,10))]
assert meanvar(pair_a)==meanvar(pair_b)==(F(3,4),F(21,400))
assert sum(w*p*p for p,w in pair_a)==sum(w*p*p for p,w in pair_b)
assert [j(pair_b,m) for m in range(4)]==[F(3,4),F(393,500),F(19731,25000),F(196257,250000)]
assert j(pair_a,100)>j(pair_a,1)>j(pair_a,0)
assert j(pair_b,2)>j(pair_b,3) and j(pair_b,2)>j(pair_b,1)

opt_cases=0
for target in range(41):
    r=F(8,3)
    H=(r**target+r**(target+1))/2
    w=H/(H+4)
    law=[(F(9,10),w),(F(2,5),1-w)]
    mu,cov=meanvar(law)
    assert mu>F(1,2) and cov>0
    assert r**target<H<r**(target+1)
    for m in range(46):
        # sign law is algebraic, not inferred from finite search
        factor=w*F(4,5)*F(9,100)**(m+1)-(1-w)*F(1,5)*F(6,25)**(m+1)
        if m<target: assert factor>0
        else: assert factor<0
        opt_cases+=1

cert={
 'arithmetic':'Python Fraction exact rationals',
 'identity_cases':cases,
 'target_index_values_checked':41,
 'target_delta_cases':opt_cases,
 'pairwise_law':{'marginal_mean':fmt(F(3,4)),'latent_variance':fmt(F(21,400)), 'pairwise_vote_correlation':fmt(F(7,25))},
 'finite_optimum_example':{'odd_size':5, 'majority_accuracy_n_1_3_5_7':[fmt(j(pair_b,m)) for m in range(4)]},
 'always_improving_example':{'majority_accuracy_n_1_3_5_7':[fmt(j(pair_a,m)) for m in range(4)]},
 'result':'all assertions passed; analytical proof required for all sizes'
}
if __name__=='__main__':
    print(json.dumps(cert,sort_keys=True,separators=(',',':')))
