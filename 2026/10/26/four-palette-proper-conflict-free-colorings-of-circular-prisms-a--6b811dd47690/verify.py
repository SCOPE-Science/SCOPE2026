"""Exact verification of proper conflict-free colorings of circular prisms.
Run: python3 verify.py. Uses only the Python standard library.
"""
from itertools import product
from math import comb


def transfer(k):
    cols = [(x, y) for x in range(k) for y in range(k) if x != y]
    states = [(a, b) for a in cols for b in cols
              if a[0] != b[0] and a[1] != b[1]]
    ids = {state: i for i, state in enumerate(states)}
    nxt = [[] for _ in states]
    for i, (a, b) in enumerate(states):
        for c in cols:
            if (b[0] != c[0] and b[1] != c[1] and
                len({a[0], c[0], b[1]}) >= 2 and
                len({a[1], c[1], b[0]}) >= 2):
                nxt[i].append(ids[(b, c)])
    return states, nxt


def traces(k, steps):
    states, adj = transfer(k)
    m = len(states)
    out = [m] + [0]*steps
    for s in range(m):
        state = [0]*m
        state[s] = 1
        for n in range(1, steps+1):
            new = [0]*m
            for i, x in enumerate(state):
                if x:
                    for j in adj[i]:
                        new[j] += x
            state = new
            out[n] += state[s]
    return out


def mul(a, b):
    z = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i+j] += x*y
    return z


def expected_denominator():
    factors = [([1,-1],6),([1,1],2),([1,-2],1),
               ([1,1,2],3), ([1,-1,0,-2],2),
               ([1,-4,-6,4],1),([1,3,6,-2,4],3)]
    d = [1]
    for f, exponent in factors:
        for _ in range(exponent):
            d = mul(d, f)
    return d


def direct_count(n,k):
    cols = [(x,y) for x in range(k) for y in range(k) if x != y]
    count=0
    def rec(seq):
        nonlocal count
        if len(seq)==n:
            if seq[-1][0]==seq[0][0] or seq[-1][1]==seq[0][1]:
                return
            for i,(x,y) in enumerate(seq):
                prev=seq[(i-1)%n]; nxt=seq[(i+1)%n]
                if len({prev[0],nxt[0],y})<2 or len({prev[1],nxt[1],x})<2:
                    return
            count+=1
            return
        for c in cols:
            if not seq or (seq[-1][0]!=c[0] and seq[-1][1]!=c[1]):
                rec(seq+[c])
    rec([])
    return count


def main():
    states3, adj3 = transfer(3)
    states4, adj4 = transfer(4)
    assert (len(states3),sum(map(len,adj3))) == (18,12)
    assert (len(states4),sum(map(len,adj4))) == (84,384)
    # Strong connectivity and aperiodicity of the four-palette transfer graph.
    def reachable(g, start):
        seen={start}; todo=[start]
        for x in todo:
            for y in g[x]:
                if y not in seen:
                    seen.add(y); todo.append(y)
        return seen
    rev=[[] for _ in states4]
    for i, targets in enumerate(adj4):
        for j in targets: rev[j].append(i)
    assert len(reachable(adj4,0)) == len(states4)
    assert len(reachable(rev,0)) == len(states4)
    tr3 = traces(3,15)
    assert all(tr3[n]==(12 if n%3==0 else 0) for n in range(3,16))
    tr4 = traces(4,84)
    assert tr4[1]==0 and tr4[2]==24
    assert tr4[3:12]==[264,384,3600,17472,75936,427152,2071632,10365504,52961568]
    # Newton identities reconstruct det(I-tA), verifying every coefficient.
    d=[1]
    for n in range(1,len(states4)+1):
        v=-sum(d[n-i]*tr4[i] for i in range(1,n+1))
        assert v%n == 0, (n,v)
        d.append(v//n)
    target=expected_denominator()
    assert d[:len(target)]==target
    assert all(c==0 for c in d[len(target):])
    assert len(target)==37
    # Independent vertex-level enumeration verifies cyclic transfer encoding.
    for n in (3,4,5):
        assert direct_count(n,4)==tr4[n]
    for n in (3,4,5,6):
        assert direct_count(n,3)==tr3[n]
    # Three based closed walks of lengths 3,4,5 give four-palette solutions.
    examples=[[(0,1),(1,0),(2,3)],
              [(0,1),(1,0),(2,3),(3,2)],
              [(0,1),(1,0),(2,3),(0,1),(2,3)]]
    for example in examples:
        n=len(example)
        for i,(x,y) in enumerate(example):
            prev=example[(i-1)%n];nxt=example[(i+1)%n]
            assert x!=y and x!=nxt[0] and y!=nxt[1]
            assert len({prev[0],nxt[0],y})>=2
            assert len({prev[1],nxt[1],x})>=2
        assert example[:2]==[(0,1),(1,0)]
    print('VERIFY_OK: transfer, exact determinant, direct counts, constructions')
    print('four-label counts n=3..11:',tr4[3:12])
    print('denominator degree:',len(target)-1,'state count:',len(states4))

if __name__=='__main__': main()
