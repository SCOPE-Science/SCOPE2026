"""Exact finite checks for two-step sampling of simultaneous binary updates.

Requires Python 3.10+ standard library only.
Set beta=log(9), so every tested normalized field on degree-one/two
networks yields rational logistic probabilities.
"""
from fractions import Fraction as F
from itertools import product

def configs(n):
    return list(product((-1, 1), repeat=n))

def prob_plus(field_num, degree):
    # logistic(beta * field_num/degree), beta=log 9, degree=1 or 2.
    assert degree in (1, 2)
    assert field_num in range(-degree, degree+1, 2)
    power = 2 * field_num // degree
    assert (2 * field_num) % degree == 0
    if power >= 0:
        x = F(3**power, 1)
    else:
        x = F(1, 3**(-power))
    return x / (1 + x)

def one_step(G):
    n = len(G)
    X = configs(n)
    out = {}
    for s in X:
        ps = [prob_plus(sum(s[j] for j in G[i]), len(G[i])) for i in range(n)]
        for t in X:
            x = F(1)
            for z, p in zip(t, ps):
                x *= p if z == 1 else 1-p
            out[(s, t)] = x
        assert sum(out[(s,t)] for t in X) == 1
    return X, out

def twice(G):
    X, P = one_step(G)
    Q = {(s,t):sum(P[(s,m)]*P[(m,t)] for m in X) for s in X for t in X}
    return X,Q

def edge_marginal_cov(X,Q,s,v,w):
    ev=sum(Q[(s,t)]*t[v] for t in X)
    ew=sum(Q[(s,t)]*t[w] for t in X)
    evw=sum(Q[(s,t)]*t[v]*t[w] for t in X)
    return evw-ev*ew

def matching_check(G):
    X,Q=twice(G)
    assert all(len(neigh)==1 for neigh in G)
    t2=F(16,25) # tanh(log(9)/2)^2 = (4/5)^2
    for s in X:
        for t in X:
            expected=F(1)
            for i in range(len(G)):
                expected *= (1+t[i]*s[i]*t2)/2
            assert Q[(s,t)]==expected,(G,s,t,Q[(s,t)],expected)
    return len(X)**2

def nonmatching_check(G):
    X,Q=twice(G)
    chosen=None
    for u, neigh in enumerate(G):
        if len(neigh)>=2:
            chosen=(neigh[0],neigh[1]);break
    assert chosen
    v,w=chosen
    covs=[edge_marginal_cov(X,Q,s,v,w) for s in X]
    assert all(c>0 for c in covs),(G,covs)
    return min(covs),max(covs)

if __name__=='__main__':
    edge=[[1],[0]]
    pair_edges=[[1],[0],[3],[2]]
    path3=[[1],[0,2],[1]]
    cycle4=[[1,3],[0,2],[1,3],[0,2]]
    # 2-spin and 4-spin matching: exact conditional two-step kernels.
    assert matching_check(edge)==16
    assert matching_check(pair_edges)==256
    # Nonmatching: every starting state gives strict common-parent covariance.
    c3=nonmatching_check(path3)
    c4=nonmatching_check(cycle4)
    X,Q=twice(path3)
    # For path leaves 0,2, if their original opinions disagree, their
    # shared parent at the intermediate step is unbiased.
    for s in X:
        c=edge_marginal_cov(X,Q,s,0,2)
        target=F(16,25) if s[0]!=s[2] else F(144,625)
        assert c==target,(s,c,target)
    print('PASS: 272 exact matching-kernel entries; positive covariance for all 8+16 nonmatching initial states.')
    print('Path 3 conditional covariance interval:',c3)
    print('Cycle 4 conditional covariance interval:',c4)
