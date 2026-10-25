"""Exact checks of a three-voter synchronous plurality poll oscillation.

Computes expected utility directly from all tremble outcomes, using only
rational arithmetic; no symbolic formula from the proof is assumed.
"""
from fractions import Fraction as Q
from itertools import product

A, B, C = range(3)
RANKS = ((A,B,C), (B,A,C), (C,A,B))
TRUTH = (A,B,C)
UNANIMOUS = (A,A,A)

def multiply_poly(x,y):
    v = [Q(0)]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            v[i+j] += a*b
    return tuple(v)

def outcome_prob(original,dest):
    return (Q(1),Q(-1)) if original==dest else (Q(0),Q(1,2))

def payoff(counts,ballot,rank,rho):
    counts = list(counts)
    counts[ballot] += 1
    high = max(counts)
    winners = [c for c in range(3) if counts[c]==high]
    utility = {rank[0]:Q(1),rank[1]:rho,rank[2]:Q(0)}
    return sum((utility[c] for c in winners),Q(0))/len(winners)

def margin_polynomial(profile,who,rho):
    rank=RANKS[who]
    others=[profile[j] for j in range(3) if j!=who]
    result=[Q(0)]*3
    for dests in product(range(3),repeat=2):
        prob = multiply_poly(outcome_prob(others[0],dests[0]),outcome_prob(others[1],dests[1]))
        counts=tuple(dests.count(c) for c in range(3))
        delta=payoff(counts,rank[0],rank,rho)-payoff(counts,rank[1],rank,rho)
        for k,c in enumerate(prob):result[k]+=c*delta
    return tuple(result)

def first_nonzero(seq):
    return next(((k,x) for k,x in enumerate(seq) if x),None)

def chosen(profile,rhos):
    ans=[]
    for i,rho in enumerate(rhos):
        lead=first_nonzero(margin_polynomial(profile,i,rho))
        assert lead is not None
        ans.append(RANKS[i][0 if lead[1]>0 else 1])
    return tuple(ans)

def check():
    assert outcome_prob(A,A)==(Q(1),Q(-1))
    assert outcome_prob(A,B)==(Q(0),Q(1,2))
    # Compare affine coefficient of top-minus-middle to direct enumeration.
    # For general rho, coefficient = constant + rho * slope.
    for profile in (TRUTH,UNANIMOUS):
        for i in range(3):
            at_zero=margin_polynomial(profile,i,Q(0))
            at_one=margin_polynomial(profile,i,Q(1))
            aff=((at_zero[k],at_one[k]-at_zero[k]) for k in range(3))
            aff=tuple(aff)
            if profile==TRUTH:
                assert aff[0]==(Q(1,3),Q(-2,3)),(profile,i,aff)
            else:
                assert aff[0]==(Q(0),Q(0)),(profile,i,aff)
                if i==0:
                    assert aff[1]==(Q(5,3),Q(-4,3)),(profile,i,aff)
                else:
                    assert aff[1]==(Q(4,3),Q(-5,3)),(profile,i,aff)
    rhos=(Q(1,4),Q(3,4),Q(3,4))
    assert chosen(TRUTH,rhos)==UNANIMOUS
    assert chosen(UNANIMOUS,rhos)==TRUTH
    assert chosen(chosen(TRUTH,rhos),rhos)==TRUTH
    assert tuple(TRUTH.count(c) for c in range(3))==(1,1,1)
    assert tuple(UNANIMOUS.count(c) for c in range(3))==(3,0,0)
    tests=0
    for r1 in (Q(1,10),Q(1,4),Q(49,100)):
        for r2 in (Q(51,100),Q(3,4),Q(79,100)):
            for r3 in (Q(51,100),Q(3,4),Q(79,100)):
                params=(r1,r2,r3)
                assert chosen(TRUTH,params)==UNANIMOUS
                assert chosen(UNANIMOUS,params)==TRUTH
                tests+=1
    print('Exact independent tremble-outcome checks PASSED; 6 affine margin identities,',tests,'open-region sample parameter triples, strict cycle.')

if __name__=='__main__':check()
