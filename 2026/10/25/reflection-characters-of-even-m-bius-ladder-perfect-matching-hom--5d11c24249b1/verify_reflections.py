#!/usr/bin/env python3
"""Reproduce reflection traces for Möbius-ladder perfect-matching complexes.

Only Python 3 standard library is required. Graph vertices are integers 0,...,2n-1.
A perfect-matching-complex face is a subset of an actual perfect matching.
"""
from functools import lru_cache


def graph_edges(n):
    N = 2*n
    c = [tuple(sorted((i, (i+1) % N))) for i in range(N)]
    s = [tuple(sorted((i, i+n))) for i in range(n)]
    return c+s


def predicted_conflicts(n):
    # The indexed edges are c_0,...,c_{2n-1},s_0,...,s_{n-1}.
    # The extra forbidden pairs c_i,c_{i+n+-1} are the minimal
    # nonextendable matchings of Agarwal--Basak, Lemmas 13--15.
    E = graph_edges(n)
    adj = [0]*len(E)
    for i in range(len(E)):
        for j in range(i+1,len(E)):
            share = bool(set(E[i]) & set(E[j]))
            sep = i < 2*n and j < 2*n and ((j-i) % (2*n) in (n-1,n+1))
            if share or sep:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    return adj


def perfect_matchings(n):
    E=graph_edges(n)
    incident = [[] for _ in range(2*n)]
    for j,(a,b) in enumerate(E):
        incident[a].append((b,j))
        incident[b].append((a,j))
    @lru_cache(None)
    def rec(mask):
        if mask == 0: return (0,)
        a = (mask & -mask).bit_length()-1
        result=[]
        for b,j in incident[a]:
            if mask>>b&1:
                result.extend(y|(1<<j) for y in rec(mask^(1<<a)^(1<<b)))
        return tuple(result)
    return rec((1<<(2*n))-1)


def verify_pairs(n):
    pm=perfect_matchings(n)
    E=3*n
    compat=[0]*E
    for p in pm:
        for i in range(E):
            if (p>>i)&1: compat[i] |= p
    adj=predicted_conflicts(n)
    for i in range(E):
        for j in range(i+1,E):
            assert bool(adj[i]>>j&1) == (not bool(compat[i]>>j&1)), (n,i,j)
    return len(pm)


def edge_reflection(n,a):
    E=graph_edges(n); inv={e:i for i,e in enumerate(E)}
    phi=[inv[tuple(sorted(((a-u)%(2*n),(a-v)%(2*n))))] for u,v in E]
    assert all(phi[phi[i]]==i for i in range(3*n))
    return phi


def orbit_quotient(n,a):
    bad=predicted_conflicts(n)
    phi=edge_reflection(n,a)
    seen=set(); orbits=[]
    for i in range(3*n):
        if i in seen: continue
        orb=tuple(sorted({i,phi[i]})); seen.update(orb)
        if len(orb)==2 and (bad[orb[0]]>>orb[1]&1): continue
        orbits.append(orb)
    q=[0]*len(orbits)
    for i,orb in enumerate(orbits):
        for j,other in enumerate(orbits):
            if i != j and any(bad[u]>>v&1 for u in orb for v in other):
                q[i]|=1<<j
    return orbits,q


def independence_at_minus_one(adj):
    M=len(adj)
    @lru_cache(None)
    def rec(mask):
        if mask==0:return 1
        i=max((j for j in range(M) if mask>>j&1),
              key=lambda j:(mask&adj[j]).bit_count())
        rem=mask^(1<<i)
        return rec(rem)-rec(rem & ~adj[i])
    return rec((1<<M)-1)


def triangular_chain(ntri):
    # k+1 joint vertices A_0,...,A_k and k apex vertices B_1,...,B_k.
    size=2*ntri+1
    adj=[0]*size
    for i in range(1,ntri+1):
        v=(ntri+i)
        t=(i-1,i,v)
        for a in t:
            for b in t:
                if a!=b: adj[a]|=1<<b
    return adj


def verify_quotient_structure(n):
    k=n//2
    ors,Q=orbit_quotient(n,1)
    idx={o:i for i,o in enumerate(ors)}
    # A_i={c_i,c_{-i}}, i=0,...,n ; B_j={s_j,s_{1-j}}, j=1,...,k
    As=[]
    for i in range(n+1):
        o=tuple(sorted({i,(-i)%(2*n)}))
        As.append(idx[o])
    Bs=[]
    for j in range(1,k+1):
        o=tuple(sorted({2*n+j,2*n+(1-j)%n}))
        Bs.append(idx[o])
    assert len(set(As+Bs))==len(Q)==3*k+1
    for i in range(k):
        assert Q[As[i]]==Q[As[n-i]],(n,i)
    keep=As[:k+1]+Bs
    assert len(set(keep))==2*k+1
    sub=[]
    for i in keep:
        sub.append(sum(1<<j for j,v in enumerate(keep) if (Q[i]>>v)&1))
    assert sub==triangular_chain(k),(n,sub)
    val=independence_at_minus_one(Q)
    val_snake=independence_at_minus_one(sub)
    assert val==val_snake
    return val


def direct_fixed_face_sum(n,a):
    # Independent check: enumerate faces from actual perfect-matching FACETS;
    # do not use any claim about forbidden edge pairs or flagness.
    phi=edge_reflection(n,a)
    seen=set(); orbit_masks=[]
    for i in range(3*n):
        if i in seen:continue
        o={i,phi[i]};seen.update(o)
        orbit_masks.append(sum(1<<j for j in o))
    faces={0:0}
    for p in perfect_matchings(n):
        possible=[x for x in orbit_masks if (p&x)==x]
        states={0:0}
        for o in possible:
            states.update({b|o:count+1 for b,count in list(states.items())})
        faces.update(states)
    return sum(-1 if count&1 else 1 for count in faces.values())


def maximal_flag_test(n):
    # Check every maximal face of predicted clique complex equals an
    # actual perfect matching. Exhaustive for the listed small cases.
    adj=predicted_conflicts(n)
    E=len(adj)
    full=(1<<E)-1
    neigh=[full^(1<<i)^adj[i] for i in range(E)]
    actual=set(perfect_matchings(n))
    seen=[]
    def bronk(R,P,X):
        if not P and not X:
            seen.append(R)
            return
        p_x=P|X
        if p_x:
            u=(p_x&-p_x).bit_length()-1
            targets=P&~neigh[u]
        else: targets=P
        while targets:
            bit=targets&-targets;v=bit.bit_length()-1
            bronk(R|bit,P&neigh[v],X&neigh[v])
            P &= ~bit;X|=bit;targets&=~bit
    bronk(0,full,0)
    assert set(seen)==actual, (n,len(seen),len(actual))
    return len(seen)


def main():
    face_tests=0
    for n in (4,6,8,10,12,14):
        pms=verify_pairs(n)
        if n<=10:
            assert maximal_flag_test(n)==pms
        print('pair-compatibility and facets',n,pms)
    for n in range(4,34,2):
        k=n//2
        assert independence_at_minus_one(orbit_quotient(n,0)[1]) == 0
        got=verify_quotient_structure(n)
        expected=0 if k%2==0 else 2*(-1)**((k+1)//2)
        assert got==expected
        ch=(-1)**k*got
        assert ch == (0 if k%2==0 else 2*(-1)**((k-1)//2))
        print('n',n,'even-axis trace 0; odd-axis trace',ch)
    for n in (4,6,8,10):
        for a in (0,1):
            direct=direct_fixed_face_sum(n,a)
            quotient=independence_at_minus_one(orbit_quotient(n,a)[1])
            assert direct==quotient,(n,a,direct,quotient)
            face_tests+=1
    print('PASS: independent facet-face signed checks:',face_tests)
    print('PASS: all stated finite checks (unbounded formula proved in RESULT.md)')

if __name__=='__main__':main()
