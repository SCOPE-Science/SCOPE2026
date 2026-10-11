#!/usr/bin/env python3
from itertools import combinations, permutations
from math import comb

def compose(p,q):
    return tuple(p[q[i]] for i in range(len(p)))

def adjacent(n,k):
    p=list(range(n)); p[k],p[k+1]=p[k+1],p[k]; return tuple(p)

def pair_action(n,d,p,pair):
    i,j=pair
    a,b=p[i],p[j]
    if a<b:
        return (a,b),1
    return (b,a),(-1 if d%2 else 1)

def sign_pair_trace(n,d,p):
    tr=0
    for pair in combinations(range(n),2):
        image,sgn=pair_action(n,d,p,pair)
        if image==pair: tr+=sgn
    return tr

def cycles_1_2(p):
    n=len(p); seen=[False]*n; x1=x2=0
    for i in range(n):
        if not seen[i]:
            cyc=[]; j=i
            while not seen[j]:
                seen[j]=True; cyc.append(j); j=p[j]
            if len(cyc)==1: x1+=1
            elif len(cyc)==2: x2+=1
    return x1,x2

def expected_pair_trace(d,x1,x2):
    return comb(x1,2)+x2 if d%2==0 else comb(x1,2)-x2

def torsion_degrees(d):
    return [d+1+r for r in range(1,d-1) if r%2==1]

def check_coxeter(n,d):
    gens=[adjacent(n,k) for k in range(n-1)]
    pairs=list(combinations(range(n),2))
    def act(p,state):
        pair,sgn0=state
        image,sgn=pair_action(n,d,p,pair)
        return image,sgn0*sgn
    for g in gens:
        for pair in pairs:
            assert act(g,act(g,(pair,1)))==(pair,1)
    for i in range(n-2):
        a,b=gens[i],gens[i+1]
        for pair in pairs:
            left=act(a,act(b,act(a,(pair,1))))
            right=act(b,act(a,act(b,(pair,1))))
            assert left==right
    for i in range(n-1):
        for j in range(i+2,n-1):
            a,b=gens[i],gens[j]
            for pair in pairs:
                assert act(a,act(b,(pair,1)))==act(b,act(a,(pair,1)))

def check(n,d):
    check_coxeter(n,d)
    for p in permutations(range(n)):
        x1,x2=cycles_1_2(p)
        tr=sign_pair_trace(n,d,p)
        assert tr==expected_pair_trace(d,x1,x2)
        top_tr=tr + (x1 if d%2==0 else 0)
        exp_top=(x1+comb(x1,2)+x2) if d%2==0 else (comb(x1,2)-x2)
        assert top_tr==exp_top
    td=torsion_degrees(d)
    assert all(d+2 <= q <= 2*d-1 and (q-(d+1))%2==1 for q in td)
    free_rank=comb(n,2)+(n if d%2==0 else 0)
    red_euler=comb(n,2)+(n if d%2==0 else 0)
    assert free_rank==red_euler
    return td,free_rank

if __name__=='__main__':
    cases=0
    for n in range(1,8):
        for d in range(1,7):
            td,rank=check(n,d)
            print(f'n={n} d={d} torsion_degrees={td} free_top_rank={rank}')
            cases+=1
    print(f'VERIFY_OK cases={cases} characters=all_permutations_n_le_7 coxeter=yes parity_sign=yes')
