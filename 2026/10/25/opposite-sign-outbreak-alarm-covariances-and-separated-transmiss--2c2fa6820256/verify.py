"""Exact finite checks for pairwise outbreak-alarm covariance on star contact graphs.

Standard-library-only. An analytic proof, not this enumeration, establishes all-size claims.
"""
from fractions import Fraction
from itertools import product
import json


def analytic(m, p):
    n = m + 1
    leaf = (1+p+(m-1)*p*p)/n
    hub = (1+m*p)/n
    leaf_leaf = (3*p*p+(m-2)*p**3)/n
    hub_leaf = (2*p+(m-1)*p*p)/n
    l_poly = (m-1)**2*p**3+(m+1)*p*p-3*p-1
    h_poly = m*(m-1)*p*p+m*p-1
    assert leaf_leaf-leaf*leaf == (1-p)*l_poly/(n*n)
    assert hub_leaf-hub*leaf == (1-p)*h_poly/(n*n)
    return leaf, hub, leaf_leaf, hub_leaf


def exact_enumeration(m, p):
    n = m+1
    # Vertices 0 = hub, 1..m leaves. Source uniform among all n sites.
    prob = [Fraction(0)]*3
    for mask in product((0,1), repeat=m):
        weight = p**sum(mask)*(1-p)**(m-sum(mask))/n
        for seed in range(n):
            reached = [False]*n
            reached[seed] = True
            if seed == 0:
                for j in range(1,n):
                    reached[j] = bool(mask[j-1])
            elif mask[seed-1]:
                reached[0] = True
                for j in range(1,n):
                    if mask[j-1]:
                        reached[j] = True
            prob[0] += weight*reached[1]
            prob[1] += weight*reached[0]
            prob[2] += weight*reached[1]*reached[2]
    # Distinct ordered roles hub and leaf also require their joint moment.
    hl = Fraction(0)
    for mask in product((0,1), repeat=m):
        weight = p**sum(mask)*(1-p)**(m-sum(mask))/n
        for seed in range(n):
            both = ((seed in (0,1)) and mask[0]) or (
                (seed not in (0,1)) and mask[seed-1] and mask[0])
            hl += weight*bool(both)
    return tuple(prob)+(hl,)


def main():
    cases=0; source_edge_realizations=0
    for m in range(2,9):
        for p in (Fraction(1,7),Fraction(1,5),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(4,5)):
            assert exact_enumeration(m,p) == analytic(m,p), (m,p)
            cases += 1
            source_edge_realizations += (m+1)*2**m
    p=Fraction(1,2)
    m=3
    pl, ph, pll, phl=analytic(m,p)
    ll=pll-pl*pl
    hl=phl-ph*pl
    assert ll==Fraction(-1,32) and hl==Fraction(1,16), (ll,hl)
    # The exact covariance-polynomial ordering H_m(p)>L_m(p)
    # is algebraic on (0,1). At p=0, L_m=-1; at p=1, L_m=(m-2)(m+1).
    for m in range(2,1001):
        H=lambda v:m*(m-1)*v*v+m*v-1
        L=lambda v:(m-1)**2*v**3+(m+1)*v*v-3*v-1
        assert H(0)==-1 and H(1)==m*m-1
        assert L(0)==-1 and L(1)==(m-2)*(m+1)
        for p in (Fraction(1,101),Fraction(1,5),Fraction(1,2),Fraction(4,5),Fraction(100,101)):
            assert H(p)>L(p)
    obj={
        'method':'exact rational full bond-state and uniformly seeded component enumeration',
        'star_sizes_m':list(range(2,9)),
        'per_size_transmissibilities':['1/7','1/5','1/3','1/2','2/3','4/5'],
        'tested_analytic_enumeration_cases':cases,
        'tested_weighted_source_edge_state_cases':source_edge_realizations,
        'algebraic_coefficient_sign_samples_m_max':1000,
        'four_vertex_star_m':3,
        'four_vertex_star_p':'1/2',
        'leaf_leaf_covariance':str(ll),
        'hub_leaf_covariance':str(hl),
        'verification':'PASS',
        'scope_limit':'Exact finite checks do not establish all-m strict-root and asymptotic results.'
    }
    print(json.dumps(obj,sort_keys=True,indent=2))

if __name__=='__main__':main()
