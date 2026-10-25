"""Exact, independently replayable checks for the tree isolation--occupancy law.

Run: python verify.py
Requires: networkx >= 3.0, < 4.0.
The analytical proof, not these finite checks, establishes the all-order theorem.
"""
from collections import Counter
from fractions import Fraction
import json
import networkx as nx


def expected_and_covariance_from_degrees(degrees, p):
    q = 1 - p
    mean = sum(p * q**d for d in degrees)
    covariance = p*q*sum(q**(d-1)*(1-(d+1)*p) for d in degrees)
    return mean, covariance


def enumerate_site_states(g, p):
    n = len(g)
    nodes = list(g)
    neighbors = [[nodes.index(u) for u in g.neighbors(v)] for v in nodes]
    mean_i = Fraction(0)
    mean_s = Fraction(0)
    mean_si = Fraction(0)
    for mask in range(1<<n):
        s = mask.bit_count()
        i = sum(bool(mask & (1<<v)) and all(not mask & (1<<w) for w in neighbors[v])
                for v in range(n))
        weight = p**s * (1-p)**(n-s)
        mean_s += weight*s
        mean_i += weight*i
        mean_si += weight*s*i
    return mean_i, mean_si-mean_s*mean_i


def derivative_sum(degrees, p):
    return sum((1-p)**(d-1)*(1-(d+1)*p) for d in degrees)


def run():
    tested = 0
    tree_count = 0
    for n in range(2,9):
        for g in nx.nonisomorphic_trees(n):
            tree_count += 1
            degrees = [d for _,d in g.degree()]
            for p in (Fraction(1,5), Fraction(2,5), Fraction(3,5)):
                lhs = enumerate_site_states(g,p)
                rhs = expected_and_covariance_from_degrees(degrees,p)
                assert lhs == rhs, (n,degrees,p,lhs,rhs)
                tested += 1
            if n >= 3:
                assert derivative_sum(degrees,Fraction(1,3)) > 0
                assert derivative_sum(degrees,Fraction(1,2)) < 0
            else:
                assert derivative_sum(degrees,Fraction(1,2)) == 0
    m=15
    degrees=[m-1]*(m-1)+[m,2,1]
    sign_points=[]
    for p,sgn in ((Fraction(1,20),1),(Fraction(1,5),-1),
                  (Fraction(1,3),1),(Fraction(1,2),-1)):
        z=derivative_sum(degrees,p)
        assert z*sgn>0
        sign_points.append({'p':str(p),'sign':'positive' if sgn>0 else 'negative',
                            'value':str(z)})
    result={'schema_version':1,
            'tree_orders':'2 through 8',
            'unlabeled_trees_checked':tree_count,
            'state_sum_exact_identity_checks':tested,
            'tree_endpoint_sign_checks':tree_count,
            'non_tree_witness':'K15 with a pendant path of length two',
            'non_tree_order':17,
            'derivative_sign_certificates':sign_points,
            'all_checks_passed':True}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':
    run()
