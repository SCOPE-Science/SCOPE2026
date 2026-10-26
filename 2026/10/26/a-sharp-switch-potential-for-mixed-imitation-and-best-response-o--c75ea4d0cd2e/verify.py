#!/usr/bin/env python3
"""Exact finite-state regression for two-strategy complete-graph hybrid updates."""
import itertools, random, math
from fractions import Fraction

def step(n, state, active, kinds, payoff):
    R,S,T,P=payoff
    k=state.bit_count()
    bit=(state>>active)&1
    if kinds[active]=='B':
        # Best response uses neighbors only, opposite strategy payoff evaluated counterfactually.
        num_A=k-bit
        num_B=n-1-num_A
        uA=num_A*R+num_B*S
        uB=num_A*T+num_B*P
        new=bit if uA==uB else int(uA>uB)
    else:
        # Compare current payoffs of all neighbors; ties between strategies retain current choice.
        candidates=[]
        for j in range(n):
            if j==active: continue
            jbit=(state>>j)&1
            aj=k-jbit; bj=n-1-aj
            u=(aj*R+bj*S) if jbit else (aj*T+bj*P)
            candidates.append((u,jbit))
        m=max(u for u,_ in candidates)
        strategies={s for u,s in candidates if u==m}
        new=next(iter(strategies)) if len(strategies)==1 else bit
    return (state&~(1<<active))|(new<<active)

def validate(n,payoff,kinds):
    R,S,T,P=payoff
    assert min(R,P)>max(S,T)
    a=R-T;b=P-S
    t=Fraction((n-1)*b,a+b)
    h=t.numerator//t.denominator+1
    max_phi=max(h,n-h)
    actual_eq=[]
    for state in range(1<<n):
        k=state.bit_count(); phi=abs(k-h)
        successors=[step(n,state,i,kinds,payoff) for i in range(n)]
        for nxt in successors:
            if nxt!=state:
                assert abs(nxt.bit_count()-h)>phi,(n,payoff,kinds,state,nxt,h)
        if all(nxt==state for nxt in successors):
            actual_eq.append(state)
            intended=(k in (0,n) or (all(z=='I' for z in kinds) and 2<=k<=n-2 and
                     (k-1)*R+(n-k)*S==k*T+(n-k-1)*P))
            assert intended,(n,payoff,kinds,state,'unexpected equilibrium')
        elif 0<k<n:
            assert not (all(z=='I' for z in kinds) and 2<=k<=n-2 and
                        (k-1)*R+(n-k)*S==k*T+(n-k-1)*P),(n,payoff,kinds,state,'missed eq')
    # Dynamic longest-change path: Phi forces DAG, verify actual longest count <=n-1.
    lens={}
    for state in sorted(range(1<<n),key=lambda s:abs(s.bit_count()-h),reverse=True):
        nexts=[step(n,state,i,kinds,payoff) for i in range(n)]
        lens[state]=max([1+lens[y] for y in nexts if y!=state] or [0])
        assert lens[state]<=n-1
    return len(actual_eq),max(lens.values())

def main():
    rng=random.Random(20261020)
    cases=0; states=0; switch_checks=0
    for n in range(2,9):
        for i in range(120):
            R=rng.randint(1,9);P=rng.randint(1,9)
            S=rng.randrange(-5,min(R,P))
            T=rng.randrange(-5,min(R,P))
            kinds=tuple(rng.choice('IB') for _ in range(n))
            validate(n,(R,S,T,P),kinds)
            cases+=1;states+=(1<<n);switch_checks+=n*(1<<n)
        if n<=5:
            for R,P in itertools.product([2,3,4],repeat=2):
                for S,T in itertools.product([-1,0,1],repeat=2):
                    if min(R,P)<=max(S,T):continue
                    for mask in range(1<<n):
                        kinds=tuple('I' if mask>>j&1 else 'B' for j in range(n))
                        validate(n,(R,S,T,P),kinds)
                        cases+=1;states+=(1<<n);switch_checks+=n*(1<<n)
    # Non-symmetric coexistence witness: all imitators, n=4, equal payoff at k=2.
    kinds='IIII';p=(4,-1,0,2)
    assert step(4,0b0011,0,kinds,p)==0b0011
    for j in range(4):assert step(4,0b0011,j,kinds,p)==0b0011
    # Sharp n-1 switches, with BOTH behavioral types present.
    for n in range(2,15):
        p=(n,0,0,1);kinds='I'+'B'*(n-1)
        state=1
        for j in range(1,n):
            after=step(n,state,j,kinds,p)
            assert after==state|(1<<j),(n,j,state,after)
            state=after
        assert state==(1<<n)-1
    print('PASS exact complete graph tests',cases,'parameter/type cases;',states,'states;',switch_checks,'activation checks; mixed sharpness n=2..14.')

if __name__=='__main__':main()
