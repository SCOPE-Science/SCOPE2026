"""Reproduce finite-state absorption probabilities of biased synchronous majority on bicliques.

Requires Python 3 and sympy. Run: python biclique_biased_verifier.py
All calculations are exact rational arithmetic. No floating point is used.
"""
from fractions import Fraction as Q
from math import comb
import sympy as sp


def binomial(n, p):
    return [Q(comb(n, k)) * p**k * (1-p)**(n-k) for k in range(n+1)]


def majority_probabilities(n, p):
    distribution = binomial(n, p)
    positive = sum(distribution[n//2+1:], Q(0))
    tie = distribution[n//2] if n % 2 == 0 else Q(0)
    return positive, tie


def formula(a,b,p_u,p_v,i,j):
    alpha_u,beta_u=majority_probabilities(a,p_u)
    alpha_v,beta_v=majority_probabilities(b,p_v)
    den=1-beta_u*beta_v
    tie_out_u=(alpha_v+beta_v*alpha_u)/den
    tie_out_v=(alpha_u+beta_u*alpha_v)/den
    u=Q(1) if 2*i>a else Q(0) if 2*i<a else tie_out_u
    v=Q(1) if 2*j>b else Q(0) if 2*j<b else tie_out_v
    return (u*v,(1-u)*(1-v),u*(1-v)+(1-u)*v)


def update_distribution(n, opposing_size, opposing_blue, p):
    if 2*opposing_blue < opposing_size:
        return [Q(1)]+[Q(0)]*n
    if 2*opposing_blue > opposing_size:
        return [Q(0)]*n+[Q(1)]
    return binomial(n,p)


def markov_absorption(a,b,p_u,p_v):
    """Solve the exact count-state absorbing chain; independent of theorem formula."""
    states=[(i,j) for i in range(a+1) for j in range(b+1)]
    final={(0,0):1,(a,b):0,(0,b):2,(a,0):2}
    transient=[s for s in states if s not in final]
    index={s:i for i,s in enumerate(transient)}
    matrix=sp.eye(len(transient))
    rhs=sp.zeros(len(transient),3)
    for z,(i,j) in enumerate(transient):
        p1=update_distribution(a,b,j,p_u)
        p2=update_distribution(b,a,i,p_v)
        for ni,pi in enumerate(p1):
            for nj,pj in enumerate(p2):
                weight=pi*pj
                if weight==0:continue
                w=sp.Rational(weight.numerator, weight.denominator)
                s=(ni,nj)
                if s in index:
                    matrix[z,index[s]]-=w
                else:
                    rhs[z,final[s]]+=w
    solved=matrix.inv()*rhs
    def rational(q):return Q(int(q.p),int(q.q))
    return {s:tuple(rational(solved[index[s],i]) for i in range(3)) if s in index else
            tuple(Q(int(i==final[s])) for i in range(3)) for s in states}


def check(a,b,p_u,p_v):
    computed=markov_absorption(a,b,p_u,p_v)
    for (i,j),triple in computed.items():
        expect=formula(a,b,p_u,p_v,i,j)
        assert expect==triple,(a,b,p_u,p_v,i,j,expect,triple)
    return len(computed)


def main():
    tests=0;states=0
    for a in range(1,5):
        for b in range(1,5):
            for p_u,p_v in [(Q(1,3),Q(1,3)),(Q(1,2),Q(1,2)),
                            (Q(2,3),Q(1,3)),(Q(1,3),Q(2,3)),
                            (Q(2,3),Q(3,4))]:
                states+=check(a,b,p_u,p_v)
                tests+=1
    # Test the inequalities used in the universal tail bound.
    for n in range(1,101):
        for p in [Q(1,10),Q(1,3),Q(1,2),Q(2,3),Q(9,10)]:
            _,beta=majority_probabilities(n,p)
            assert beta <= Q(1,2)
    print('PASS: %s exact absorbing chains, %s state/parameter comparisons; %s tie-mass checks' % (tests,states,500))
    print('Nontrivial example K_4,4, U tie biased 3/4, V tie biased 1/4, both initial counts tied:')
    print(formula(4,4,Q(3,4),Q(1,4),2,2))

if __name__=='__main__':main()
