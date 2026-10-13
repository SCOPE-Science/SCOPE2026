from itertools import combinations, product
from math import comb, factorial

assertions = 0

def partitions(n):
    if n == 0:
        yield []
        return
    blocks=[]
    def rec(i):
        if i==n:
            yield [b[:] for b in blocks]
            return
        for j in range(len(blocks)):
            blocks[j].append(i)
            yield from rec(i+1)
            blocks[j].pop()
        blocks.append([i])
        yield from rec(i+1)
        blocks.pop()
    yield from rec(0)

def formula(t,e):
    total=0
    for pi in partitions(t):
        k=len(pi)
        mu=(-1)**(k-1)*factorial(k-1)
        allowed=t+sum(comb(len(B),2) for B in pi)
        total += mu*(allowed**e)
    return total

def connected_assignment(t, assn):
    if t==1:
        return True
    parent=list(range(t))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb: parent[rb]=ra
    for S in assn:
        if len(S)==2:
            union(S[0],S[1])
    r=find(0)
    return all(find(i)==r for i in range(t))

def brute(t,e):
    opts=[(i,) for i in range(t)] + list(combinations(range(t),2))
    c=0
    for a in product(opts, repeat=e):
        if connected_assignment(t,a): c+=1
    return c

# Exact brute-force comparison for a substantial finite grid.
for t in range(1,5):
    maxe={1:7,2:7,3:6,4:5}[t]
    for e in range(0,maxe+1):
        b=brute(t,e)
        f=formula(t,e)
        assertions += 1
        if b!=f:
            raise SystemExit(("brute/formula mismatch",t,e,b,f))

# Independent connected-component recurrence (the bivariate exponential formula).
# A(t,e)=q_t^e counts all incidence systems; C(t,e)=formula(t,e) counts connected ones.
def A(t,e):
    if t==0:
        return 1 if e==0 else 0
    q=t*(t+1)//2
    return q**e

for t in range(1,9):
    for e in range(0,11):
        rhs=0
        for i in range(1,t+1):
            for j in range(0,e+1):
                rhs += comb(t-1,i-1)*comb(e,j)*formula(i,j)*A(t-i,e-j)
        lhs=A(t,e)
        assertions += 1
        if lhs!=rhs:
            raise SystemExit(("EGF recurrence mismatch",t,e,lhs,rhs))

# Structural corollaries and first total labeled rooted-frame values.
for e in range(0,12):
    assertions += 1
    if formula(2,e) != 3**e-2**e:
        raise SystemExit(("t=2 mismatch",e))

expected_R={2:2,3:6,4:34,5:255,6:2541,7:31948,8:482308}
for m,want in expected_R.items():
    got=sum(comb(m,t)*formula(t,m-t) for t in range(1,m))
    assertions += 1
    if got!=want:
        raise SystemExit(("R mismatch",m,got,want))

print("N(t,e) rows (e=1..7 where shown):")
for t in range(1,6):
    print(t, [formula(t,e) for e in range(1,8)])
print("R_m (distinguished root; m labeled nonroot points):")
print([expected_R[m] for m in sorted(expected_R)])
print(f"VERIFY_OK {assertions} exact formula/recurrence assertions; exhaustive assignment grid through t=4")
