"""Standalone exact finite tests for three-state excitation on open ladders.
Run: python3 VERIFY_LADDER.py (Python 3 standard library only).
"""
from itertools import product

def delta(a,b):
    return (b-a+1)%3-1

def local_winding(u,v):
    a,b=u; c,d=v
    return delta(a,c)+delta(c,d)+delta(d,b)+delta(b,a)

def run_rule(state,n):
    out=[]
    for k in range(2*n):
        s=state[k]
        if s:
            out.append((s+1)%3)
        else:
            i,j=divmod(k,2)
            neigh=[k^1]
            if i>0: neigh.append(k-2)
            if i+1<n: neigh.append(k+2)
            out.append(int(any(state[w]==1 for w in neigh)))
    return tuple(out)

def dies_out(state,n):
    seen=set()
    while state not in seen:
        if not any(state): return True
        seen.add(state)
        state=run_rule(state,n)
    return False

def expected(n):
    if n==1: return 9
    a,b=9,57
    for _ in range(3,n+1): a,b=b,7*b-4*a
    return b

assert sum(local_winding(u,v)==0 for u in product(range(3),repeat=2) for v in product(range(3),repeat=2))==57
for u in product(range(3),repeat=2):
    counts=[0,0]
    for v in product(range(3),repeat=2):
        if local_winding(u,v)==0: counts[int(v[0]!=v[1])]+=1
    assert counts==([3,4] if u[0]==u[1] else [2,4]), (u,counts)
for n in range(2,6):
    extinction=0; local=0
    for raw in product(range(3),repeat=2*n):
        cond=all(local_winding(raw[2*i:2*i+2],raw[2*i+2:2*i+4])==0 for i in range(n-1))
        got=dies_out(raw,n)
        assert cond==got,(n,raw,cond,got)
        local+=cond; extinction+=got
    assert extinction==local==expected(n),(n,extinction,local,expected(n))
    print('n=%d total=%d extinct=%d'%(n,3**(2*n),extinction))
print('LADDER_GH_EXACT_VERIFY_OK')
