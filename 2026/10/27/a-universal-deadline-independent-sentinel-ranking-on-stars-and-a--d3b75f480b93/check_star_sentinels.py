"""Exact checks for optimal finite-deadline SI monitoring on star graphs.

Run: python check_star_sentinels.py
No third-party dependencies. The transition enumeration is independent of the
closed two-placement formulas and uses Fraction throughout.
"""
from fractions import Fraction as Q
from itertools import combinations


def independent_state_transition(n, state, p):
    q = 1-p
    if state & 1:
        susceptible = [j for j in range(1,n) if not (state >> j) & 1]
        for mask in range(1<<len(susceptible)):
            out = state
            for i,j in enumerate(susceptible):
                if (mask >> i) & 1:
                    out |= 1<<j
            count = mask.bit_count()
            yield out, p**count*q**(len(susceptible)-count)
    else:
        infected_leaves = (state>>1).bit_count()
        infection_prob = 1-q**infected_leaves
        yield state, 1-infection_prob
        if infection_prob:
            yield state|1, infection_prob


def exact_probabilities(n, p, t):
    results=[]
    for seed in range(n):
        states={1<<seed:Q(1)}
        for _ in range(t):
            nxt={}
            for state,pr in states.items():
                for state2,rate in independent_state_transition(n,state,p):
                    nxt[state2]=nxt.get(state2,Q(0))+pr*rate
            states={s:v for s,v in nxt.items() if v}
            assert sum(states.values())==1
        results.append(states)
    return results


def detection(n, sensor_mask, state_probs):
    return sum((pr for states in state_probs for s,pr in states.items()
                if s & sensor_mask),Q(0))/n


def closed(n,k,p,t):
    q=1-p
    r=n-k
    gam=q**k
    c=1-((1-gam)*q**t-(1-q)*gam**t)/(q-gam)
    hub=(k+r*(1-q**t))/n
    leaf=(k+(1-gam**t)+(r-1)*c)/n
    common=(1-q)*(q**t-gam**t)/(q-gam)
    delta=(r-sum(q**j for j in range(k)))*common/n
    return hub,leaf,delta


def run():
    assertions=0
    for n in range(4,8):
        for k in range(2,n):
            hub_mask=sum(1<<j for j in range(k-1)) + (1<<(k-1)) # 0..k-1
            # hub index 0, leaves 1..n-1; leaf-only set is 1..k
            leaf_mask=sum(1<<j for j in range(1,k+1))
            for p in [Q(1,3),Q(2,5),Q(3,4)]:
                for t in range(0,7):
                    byseed=exact_probabilities(n,p,t)
                    a=detection(n,hub_mask,byseed)
                    b=detection(n,leaf_mask,byseed)
                    x,y,d=closed(n,k,p,t)
                    assert (a,b,a-b)==(x,y,d),(n,k,p,t,a,b,x,y,d)
                    assertions+=3
                    # Every k-subset reduces by symmetry to hub/leaf case.
                    vals=set()
                    for combo in combinations(range(n),k):
                        mask=sum(1<<j for j in combo)
                        v=detection(n,mask,byseed)
                        expected=a if 0 in combo else b
                        assert v==expected
                        vals.add(v)
                        assertions+=1
                    assert vals <= {a,b}
                    assertions+=1
    # Exact golden-ratio switch witnesses at two rational probabilities.
    for p,positive in [(Q(2,5),True),(Q(1,3),False)]:
        for t in range(1,9):
            a,b,d=closed(5,3,p,t)
            assert (a>b)==positive
            assertions+=1
    # Expected-time gaps derived by summing the finite-deadline identity.
    for n in range(4,14):
        for k in range(2,n):
            for p in [Q(1,3),Q(2,5),Q(3,4)]:
                q=1-p; r=n-k
                gap=(r-sum(q**j for j in range(k)))/(n*(1-q**k))
                partial=sum((closed(n,k,p,t)[2] for t in range(1,50)),Q(0))
                # Remainder geometric, bounded by a decaying power.
                assert abs(partial-gap) < Q(1,10**7)
                assertions+=1
    print(f'PASS: {assertions} exact checks; all monitored-subset symmetry classes verified.')

if __name__=='__main__': run()
