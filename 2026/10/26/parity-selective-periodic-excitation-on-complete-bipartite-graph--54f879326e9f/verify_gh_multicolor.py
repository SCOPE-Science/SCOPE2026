"""Independent finite-state tests of periodic-point classification for multicolor GHM on complete bipartite graphs.
No external packages required. Run: python verify_gh_multicolor.py
"""
from itertools import product
from math import comb, factorial

def update(state, a, q):
    active_left = 1 in state[:a]
    active_right = 1 in state[a:]
    return tuple((v+1)%q if v else int(active_right) for v in state[:a]) + tuple((v+1)%q if v else int(active_left) for v in state[a:])

def surj(n,k):
    return sum((-1)**j * comb(k,j) * (k-j)**n for j in range(k+1))

def predicted_period(state,a,q):
    A=set(state[:a]); B=set(state[a:]);m=(q+1)//2
    allc=set(range(q))
    if A=={0} and B=={0}: return 1
    if A==allc and B==allc: return q
    even=set(range(0,q,2))
    if q%2: other={0}|set(range(1,q,2))
    else: other=set(range(1,q,2))
    if (A==even and B==other) or (A==other and B==even):return 2*m
    return 0

def check(a,b,q):
    # Independent full functional-graph cycle detection, not predicated on a period bound.
    states=list(product(range(q),repeat=a+b))
    succ={s:update(s,a,q) for s in states}
    assigned=set(); observed={}
    for st in states:
        if st in assigned:continue
        walk=[];pos={};x=st
        while x not in assigned and x not in pos:
            pos[x]=len(walk);walk.append(x);x=succ[x]
        if x in pos:
            for c in walk[pos[x]:]:observed[c]=len(walk)-pos[x]
        assigned.update(walk)
    expected={1:1, q:surj(a,q)*surj(b,q)}
    L=2*((q+1)//2)
    expected[L]=expected.get(L,0)+2*surj(a,(q+1)//2)*surj(b,(q+1)//2)
    found={}
    for s,period in observed.items():
        assert period==predicted_period(s,a,q),('period mismatch',q,a,b,s,period,predicted_period(s,a,q))
        found[period]=found.get(period,0)+1
    assert {k:v for k,v in found.items() if v}=={k:v for k,v in expected.items() if v},(q,a,b,found,expected)
    return len(states),found

def forcing_q(q):
    # 2-step return maps: even-time stimulation A and odd-time stimulation B.
    def step(x,stim):return (x+1)%q if x else int(stim)
    G={x:step(step(x,1),0) for x in range(q)}
    H={x:step(step(x,0),1) for x in range(q)}
    def recurrent_states(mp):
        good=set()
        for x in mp:
            seen={};track=[];y=x
            while y not in seen:
                seen[y]=len(track);track.append(y);y=mp[y]
            good.update(track[seen[y]:])
        return good
    E=set(range(0,q,2))
    O=({0}|set(range(1,q,2))) if q%2 else set(range(1,q,2))
    assert recurrent_states(G)==E,(q,'G')
    assert recurrent_states(H)==O,(q,'H')
    m=(q+1)//2
    def cyclen(mp,st):
        x=st
        for j in range(1,q+2):
            x=mp[x]
            if x==st:return j
        raise AssertionError('no cycle')
    assert {cyclen(G,x) for x in E}=={m}
    assert {cyclen(H,x) for x in O}=={m}

if __name__=='__main__':
    total=0;cases=0;details=[]
    for q in range(3,8):
        for a in range(1,5):
            for b in range(1,5):
                if q**(a+b)>150000: continue
                N,r=check(a,b,q);total+=N;cases+=1
                if a==b and a in (2,3,4):details.append((q,a,b,N,r))
    for q in range(3,65):forcing_q(q)
    # Non-exhaustive but independent direct long-wave witnesses beyond brute force sizes.
    for q in range(7,16):
        m=(q+1)//2
        E=sorted(set(range(0,q,2)))
        O=sorted(({0}|set(range(1,q,2))) if q%2 else set(range(1,q,2)))
        for st in (tuple(E+O),tuple(O+E)):
            x=st; seen={}
            while x not in seen:
                seen[x]=len(seen); x=update(x,m,q)
            assert x==st and len(seen)==2*m,(q,st,len(seen))
    print('OK exhaustive state-space configurations:',total,'parameter triples:',cases)
    print('OK single-site forced maps for all kappa 3..64')
    print('OK direct long-wave witness cycles for kappa 7..15')
    print('Selected counts:',details)
