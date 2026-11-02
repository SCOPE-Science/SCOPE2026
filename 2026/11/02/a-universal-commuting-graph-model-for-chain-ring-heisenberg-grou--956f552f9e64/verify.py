#!/usr/bin/env python3
"""Direct commuting-tuple censuses for Heisenberg groups over small chain rings.

The census constructs multiplication tables, tests every determinant directly,
and counts ordered cliques in the resulting commutation relation. No valuation
partition is used in the census.
"""
from functools import lru_cache


class Ring:
    def __init__(self, model, q, length):
        self.model, self.q, self.length = model, q, length
        self.size = q ** length
        if model == 'mod':
            assert q in (2, 3, 5)
            self.mul = tuple(tuple((a*b) % self.size for b in range(self.size)) for a in range(self.size))
            self.neg = tuple((-a) % self.size for a in range(self.size))
        else:
            assert model == 'trunc'
            assert q in (2, 3, 4)
            fm = [[0]*q for _ in range(q)]
            for a in range(q):
                for b in range(q):
                    if q == 4:
                        v = 0
                        if a & 1:
                            v ^= b
                        if a & 2:
                            v ^= b << 1
                        if v & 8: v ^= 0b1110
                        if v & 4: v ^= 0b0111
                        fm[a][b] = v
                    else:
                        fm[a][b] = a*b % q
            def coeff(x):
                out=[]
                for i in range(length):
                    out.append(x % q); x //=q
                return out
            cs=[coeff(i) for i in range(self.size)]
            def product(a,b):
                c=[0]*length
                for i,aa in enumerate(cs[a]):
                    for j,bb in enumerate(cs[b][:length-i]):
                        v=fm[aa][bb]
                        c[i+j]=(c[i+j]^v) if q == 4 or q == 2 else (c[i+j]+v)%q
                return sum(x*q**i for i,x in enumerate(c))
            self.mul=tuple(tuple(product(a,b) for b in range(self.size)) for a in range(self.size))
            self.neg=tuple(sum(((-x)%q)*q**i for i,x in enumerate(cs[a])) for a in range(self.size))
        self.zero = 0

    def detzero(self, a,b,c,d):
        t=self.mul[a][d]
        s=self.mul[b][c]
        return t == s


def direct_counts(ring, max_k):
    n=ring.size
    vectors=[(a,b) for a in range(n) for b in range(n)]
    total=len(vectors)
    masks=[]
    for a,b in vectors:
        bits=0
        for j,(c,d) in enumerate(vectors):
            if ring.detzero(a,b,c,d):
                bits|=1<<j
        masks.append(bits)
    # Recursion uses the original candidate mask at each branch, not its residual.
    @lru_cache(maxsize=None)
    def count(mask, remaining):
        if remaining == 0:
            return 1
        z=0
        todo=mask
        while todo:
            bit=todo & -todo
            i=bit.bit_length()-1
            todo-=bit
            z+=count(mask & masks[i], remaining-1)
        return z
    full=(1<<total)-1
    return [count(full, k) for k in range(1,max_k+1)]


def expected(q,ell,k):
    return q**(2*k*(ell//2))+sum(q**(2*k*s)*(q**(ell-2*s)+q**(ell-2*s-1))*(q**((ell-2*s)*k)-q**((ell-2*s-1)*k)) for s in range((ell+1)//2))



def direction(ring, a, b, j):
    """Normalized primitive line over R/(pi^j)."""
    n=ring.q**j
    a%=n; b%=n
    assert a%ring.q or b%ring.q
    if a%ring.q:
        pivot=a; other=b; flag=0
    else:
        pivot=b; other=a; flag=1
    value=next(t for t in range(n) if ring.mul[pivot][t]%n==other)
    return (flag,value)


def canonical_paths(ring):
    q=ring.q; ell=ring.length
    nodes={j:set() for j in range(1,ell+1)}
    for j in range(1,ell+1):
        for a in range(q**j):
            for b in range(q**j):
                if a%q or b%q:
                    nodes[j].add(direction(ring,a,b,j))
        assert len(nodes[j]) == (q+1)*q**(j-1)
    paths={1:{x:(i,) for i,x in enumerate(sorted(nodes[1]))}}
    for j in range(2,ell+1):
        children={par:[] for par in nodes[j-1]}
        for x in nodes[j]:
            parent=(x[0],x[1] % (q**(j-1)))
            assert parent in nodes[j-1]
            children[parent].append(x)
        assert all(len(c)==q for c in children.values())
        paths[j]={}
        for par in sorted(children):
            for idx,x in enumerate(sorted(children[par])):
                paths[j][x]=paths[j-1][par]+(idx,)
    return paths


def vector_signatures(ring):
    """Build a canonical vertex set without comparing ring operations."""
    q=ring.q; ell=ring.length; n=ring.size
    paths=canonical_paths(ring)
    buckets={}
    vecs=[(a,b) for a in range(n) for b in range(n)]
    for a,b in vecs:
        if (a,b)==(0,0): continue
        s=next(i for i in range(ell) if a%(q**(i+1)) or b%(q**(i+1)))
        j=ell-s
        d=direction(ring,a//(q**s),b//(q**s),j)
        key=(s,paths[j][d])
        buckets.setdefault(key,[]).append((a,b))
    table={(0,0):('center',)}
    for key,group in buckets.items():
        assert len(group)==(q-1)*q**(ell-key[0]-1)
        for rank,v in enumerate(sorted(group)):
            table[v]=key+(rank,)
    assert len(set(table.values()))==len(vecs)
    return {v:s for v,s in table.items()}


def cross_ring_graph_check(q,ell):
    """Explicitly compare every pair of Heisenberg vector classes."""
    a=Ring('mod',q,ell); b=Ring('trunc',q,ell)
    sig_a=vector_signatures(a); sig_b=vector_signatures(b)
    lookup_b={sig:v for v,sig in sig_b.items()}
    assert set(sig_a.values())==set(sig_b.values())
    pairs=[(v,lookup_b[sig]) for v,sig in sig_a.items()]
    for (a1,b1),(a2,b2) in pairs:
        for (c1,d1),(c2,d2) in pairs:
            assert a.detzero(a1,b1,c1,d1)==b.detzero(a2,b2,c2,d2)
    if (q,ell)==(2,3):
        # Expand the complete 512-vertex graph; the central coordinate is
        # carried bijectively and every ordered pair of vertices is tested.
        expanded=[(v,w,z) for v,w in pairs for z in range(a.size)]
        assert len(expanded)==512
        for (a1,b1),(a2,b2),z1 in expanded:
            for (c1,d1),(c2,d2),w1 in expanded:
                assert a.detzero(a1,b1,c1,d1)==b.detzero(a2,b2,c2,d2)
    return len(pairs), len(pairs)**2


def main():
    specs=[('mod',2,1,4),('mod',2,2,4),('mod',2,3,3),
           ('mod',3,1,4),('mod',3,2,3),('mod',5,1,3),
           ('trunc',2,2,4),('trunc',2,3,3),
           ('trunc',3,2,3),('trunc',4,1,3),('trunc',4,2,2)]
    record=[]
    for model,q,ell,max_k in specs:
        ring=Ring(model,q,ell)
        obs=direct_counts(ring,max_k)
        pred=[expected(q,ell,k) for k in range(1,max_k+1)]
        assert obs==pred,(model,q,ell,obs,pred)
        record.append((model,q,ell,max_k,obs))
    # Check the exact linear recurrence in the ring length independently
    # of the direct finite censuses.
    for q in (2,3,4,5):
        for k in range(1,7):
            for ell in range(1,9):
                a=expected(q,ell+4,k)
                b=(q**(2*k)+q**(2*k+2))*expected(q,ell+2,k)
                c=q**(4*k+2)*expected(q,ell,k)
                assert a-b+c == 0, (q,ell,k)
    graph_checks=[]
    for q,ell in [(2,2),(2,3),(2,4),(3,2),(3,3)]:
        graph_checks.append((q,ell,cross_ring_graph_check(q,ell)))
    for x in record: print('CHECK',*x)
    for x in graph_checks: print('GRAPH_ISOMORPHISM',*x)
    print('VERIFY_OK 11 exact commuting-tuple censuses and 5 exhaustive cross-ring graph-isomorphism maps')

if __name__=='__main__':
    main()
