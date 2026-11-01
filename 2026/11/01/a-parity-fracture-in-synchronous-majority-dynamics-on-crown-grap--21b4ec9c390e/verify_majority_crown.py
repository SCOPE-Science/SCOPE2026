"""Exact finite checks for synchronous strict-majority dynamics on crown graphs.

No nonstandard dependencies; run: python verify_majority_crown.py
"""
from collections import Counter
from math import comb, factorial


def analytic(n):
    if n % 2 == 0:
        m = n // 2
        c = comb(n,m)
        low = sum(comb(n,j) for j in range(m))
        fixed = 2 + c
        periodic_two = (c+1)*(c+2)
        basin_two = 2*low*low + 4*low*c + c*c-c
        sharp_transient = 0 if n == 2 else 1
    elif n == 1:
        fixed,periodic_two,basin_two,sharp_transient = 4,0,0,0
    else:
        m = (n-1)//2
        c = comb(n,m)
        fixed = 2+2*(m+2)*c
        periodic_two = 2
        basin_two = (4**n)//2 - 2*c*(2*(m+2)*2**m - (m*m+3*m+3))
        sharp_transient = 2 if n==3 else 3
    return fixed,periodic_two,basin_two,sharp_transient


def next_profile(mapping,z,n):
    total_left=sum(z[j] for j in range(4) if mapping[j]//2)
    total_right=sum(z[j] for j in range(4) if mapping[j]%2)
    nxt=[]
    for pair in mapping:
        if pair == -1:
            nxt.append(-1)
            continue
        a,b=(pair//2,pair%2)
        left_ones=total_right-b
        right_ones=total_left-a
        aa=int(2*left_ones>n-1) if 2*left_ones!=n-1 else a
        bb=int(2*right_ones>n-1) if 2*right_ones!=n-1 else b
        nxt.append(2*aa+bb)
    return tuple(nxt)


def profile_check(n):
    fact=[factorial(i) for i in range(n+1)]
    fixed=period2=basin2=0
    max_t=0
    transient_tally=Counter()
    for a in range(n+1):
        for b in range(n-a+1):
            for c in range(n-a-b+1):
                d=n-a-b-c
                z=(a,b,c,d)
                state=tuple(j if z[j] else -1 for j in range(4))
                weight=fact[n]//(fact[a]*fact[b]*fact[c]*fact[d])
                timeline={};s=state
                while s not in timeline:
                    timeline[s]=len(timeline)
                    s=next_profile(s,z,n)
                    if len(timeline)>8: raise AssertionError((n,state,'long orbit'))
                tran=timeline[s];p=len(timeline)-tran
                assert p in (1,2),(n,state,p)
                max_t=max(max_t,tran)
                transient_tally[(tran,p)]+=weight
                if tran==0 and p==1:fixed+=weight
                if tran==0 and p==2:period2+=weight
                if p==2:basin2+=weight
    got=(fixed,period2,basin2,max_t)
    expect=analytic(n)
    assert got==expect, (n,got,expect)
    assert sum(transient_tally.values()) == 4**n
    return transient_tally


def microscopic_next(state,n):
    # Independent adjacency-based simulator: each vertex explicitly votes over n-1 neighbors.
    bits=[(state>>k)&1 for k in range(2*n)]
    updated=[]
    for i in range(2*n):
        if i<n:
            neighborhood=[j+n for j in range(n) if j!=i]
        else:
            neighborhood=[j for j in range(n) if j!=i-n]
        ones=sum(bits[j] for j in neighborhood)
        updated.append(1 if 2*ones>n-1 else (0 if 2*ones<n-1 else bits[i]))
    return sum(x<<i for i,x in enumerate(updated))


def micro_check(n):
    got_fixed=got_period2=got_basin2=0
    max_t=0
    for initial in range(4**n):
        trail={};x=initial
        while x not in trail:
            trail[x]=len(trail)
            x=microscopic_next(x,n)
            assert len(trail)<=8, (n,initial)
        t=trail[x];p=len(trail)-t
        assert p in (1,2)
        max_t=max(max_t,t)
        got_fixed+=(t==0 and p==1)
        got_period2+=(t==0 and p==2)
        got_basin2+=(p==2)
    assert (got_fixed,got_period2,got_basin2,max_t)==analytic(n), (n,(got_fixed,got_period2,got_basin2,max_t),analytic(n))


def main():
    for n in range(1,51):
        profile_check(n)
        if n<=7: micro_check(n)
        if n<=10 or n in (20,30,40,50):
            f,p,b,t=analytic(n)
            print(f'n={n}: fixed={f}, primitive_period2_orbits={p//2}, basin2={b}, max_transient={t}; MATCH')
    print('CROWN_MAJORITY_PARITY_VERIFY_OK')

if __name__=='__main__':main()
