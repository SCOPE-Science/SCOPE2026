"""Independent direct-state verification of finite deterministic traffic evacuation."""
import itertools
import math

def step(word):
    n = len(word)
    after = [0] * n
    for i in range(n):
        if not word[i]:
            continue
        if i == n - 1:
            continue
        if word[i+1] == 0:
            after[i+1] = 1
        else:
            after[i] = 1
    return tuple(after)

def first_empty(word):
    state = tuple(word)
    for t in range(2 * len(state) + 1):
        if not any(state):
            return t
        state = step(state)
    raise AssertionError('No extinction within the predicted bound')

def walk_stat(word):
    height = 0
    highest_up = None
    for b in word:
        if b == 1:
            highest_up = height if highest_up is None else max(highest_up, height)
        height += 2 * b - 1
    return 0 if highest_up is None else len(word) + highest_up

def shell(n,t):
    if t == 0: return 1
    if 1 <= t <= n:
        return math.comb(t,(t-1)//2) if t & 1 else math.comb(t, t//2 - 1)
    if n < t <= 2*n-1:
        return math.comb(n, (2*n-t-1)//2)
    return 0

def restricted(m,a,p_num,q_num):
    total = 0
    R = (m+a)//2
    for k in range(R+1):
        good = math.comb(m,k) - (math.comb(m,k-a-1) if 0<=k-a-1<=m else 0)
        total += good * p_num**k * q_num**(m-k)
    return total

states_total = 0
for n in range(1,16):
    counts = [0]*(2*n)
    for word in itertools.product((0,1),repeat=n):
        t=first_empty(word)
        assert t==walk_stat(word),(n,word,t,walk_stat(word))
        counts[t]+=1
    assert counts == [shell(n,t) for t in range(2*n)],(n,counts)
    assert sum(counts)==2**n
    for p,q in ((1,2),(2,1),(1,1)):
        weighted=[0]*(2*n)
        for word in itertools.product((0,1),repeat=n):
            weighted[walk_stat(word)]+=p**sum(word)*q**(n-sum(word))
        acc=0
        for t,v in enumerate(weighted):
            acc+=v
            if t<n:
                predicted=q**(n-t)*restricted(t,1,p,q)
            else:
                predicted=restricted(n,t-n+1,p,q)
            assert acc==predicted,(n,p,q,t,acc,predicted)
    states_total+=2**n
print(f'PYTHON_VERIFIED n=1..15, unweighted trajectories={states_total}, exact shells and p:q=1:2,2:1,1:1 weighted CDF verified')
