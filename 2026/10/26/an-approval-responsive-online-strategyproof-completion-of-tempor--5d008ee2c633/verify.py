"""Reproducibility checks for approval-responsive completion of temporal MES.
No external dependencies. All arithmetic is exact."""
from fractions import Fraction as F
from itertools import product

def price(budgets, supporters, p):
    a = sorted(budgets[i] for i in supporters)
    if sum(a, F(0)) < p:
        return None
    s = F(0)
    for j in range(len(a)):
        r = (p - s) / (len(a)-j)
        if r <= a[j]:
            return r
        s += a[j]
    raise AssertionError('unreachable')

def choice(budgets, ballots, p, m):
    # fixed priority = increasing candidate index. Candidate scores are separable.
    support = [tuple(i for i, v in enumerate(ballots) if (v >> c) & 1) for c in range(m)]
    rho = [price(budgets, support[c], p) for c in range(m)]
    feasible = [c for c in range(m) if rho[c] is not None]
    if feasible:
        c = min(feasible, key=lambda c:(rho[c],c))
        return c, tuple(budgets[i]-min(budgets[i],rho[c]) if i in support[c] else budgets[i] for i in range(len(budgets))), True
    c = min(range(m),key=lambda c:(-sum((budgets[i] for i in support[c]), F(0)),c))
    return c,tuple(budgets),False

def all_ballots(n,m):
    return product(range(1,1<<m),repeat=n)

# Exhaustive one-round OIIA and OSP, including all frozen budget vectors
count_profile=0
count_o_iia=0
count_o_sp=0
for n,m,levels,Ts in [(2,2,(0,1,2,4),(1,2,3)),(3,3,(0,1,2,4),(2,3,4))]:
    levels = tuple(F(v,4) for v in levels)
    for b in product(levels, repeat=n):
        for T in Ts:
            p=F(n,T)
            for votes in all_ballots(n,m):
                winner, _, _ = choice(b,votes,p,m)
                count_profile+=1
                # Removing a losing alternative leaves the winner invariant.
                for i in range(n):
                    for c in range(m):
                        if c!=winner and (votes[i]>>c)&1:
                            v=list(votes); v[i]^=(1<<c)
                            # OIIA holds even at empty reported ballots
                            assert choice(b,v,p,m)[0] == winner, (n,m,b,p,votes,i,c)
                            count_o_iia+=1
                    for lie in range(1,1<<m):
                        if lie==votes[i]: continue
                        v=list(votes);v[i]=lie
                        alt=choice(b,v,p,m)[0]
                        assert not ((votes[i]>>winner)&1==0 and (votes[i]>>alt)&1 == 1), (n,m,b,p,votes,i,lie,winner,alt)
                        count_o_sp+=1

# Enumerate actual dynamic two-round histories including all admissible deviations
count_hist=0
for n,m,T in [(2,2,2),(3,2,2),(2,3,2),(3,2,3)]:
    p=F(n,T)
    options=range(1,1<<m)
    for allround in product(tuple(product(options,repeat=n)),repeat=T):
        b=tuple(F(1) for _ in range(n))
        halted=False
        winners=[]
        for t,votes in enumerate(allround):
            def step(v):
                if halted:
                    # A frozen-budget approval-weighted continuation.
                    c=min(range(m),key=lambda c:(-sum((b[i] for i in range(n) if (v[i]>>c)&1),F(0)),c))
                    return c,b,False
                return choice(b,v,p,m)
            w,next_b,aff=step(votes)
            for i in range(n):
                for lie in options:
                    v=list(votes);v[i]=lie
                    alt=step(v)[0]
                    assert not ((votes[i]>>w)&1 == 0 and (votes[i]>>alt)&1 ==1)
            winners.append(w)
            if not halted and not aff: halted=True
            b=next_b
        # Explicit verification of wEJR at these small horizons.
        for group in range(1,1<<n):
            idx=[i for i in range(n) if group>>i&1]
            if not all(any(all((v[i]>>c)&1 for i in idx) for c in range(m)) for v in allround):
                continue
            ell=(T*len(idx))//n
            if ell:
                assert any(sum(bool((allround[t][i]>>winners[t])&1) for t in range(T))>=ell for i in idx)
        count_hist+=1

# The completion really fills an MES early-stop case with a supported winner.
p=F(2,2)
b=(F(1),F(1))
w,b,aff=choice(b,(1,1),p,2)
assert (w,b,aff)==(0,(F(1,2),F(1,2)),True)
w,b,aff=choice(b,(1,2),p,2)
assert (w,b,aff)==(0,(F(1,2),F(1,2)),False)
# A superficially similar but decreasing-support fallback can be manipulated.
bad=lambda votes: min(range(2),key=lambda c:(sum((b[i] for i in range(2) if votes[i]>>c&1),F(0)),c))
assert bad((1,2))==0 and bad((1,3))==1
print('PASS: fixed-budget profiles',count_profile,'loser-deletion checks',count_o_iia,'OSP checks',count_o_sp,'dynamic histories',count_hist,'safe and unsafe fallback witnesses verified')
