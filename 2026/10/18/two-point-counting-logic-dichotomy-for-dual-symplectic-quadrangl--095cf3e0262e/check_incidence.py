#!/usr/bin/env python3
"""Finite incidence construction checks for a two-landmark generalized-quadrangle theorem.
Uses only the Python standard library; outputs deterministic line-oriented summaries.
"""
from itertools import product, combinations
from collections import Counter


def make_symplectic(q):
    assert q in (3,5,7,11), 'This executable uses prime fields; the theorem covers all odd prime powers.'
    def normalize(v):
        u = next(a for a in v if a % q)
        inv = pow(u, -1, q)
        return tuple(inv*a % q for a in v)
    points = sorted({normalize(v) for v in product(range(q), repeat=4) if any(v)})
    ids = {p:i for i,p in enumerate(points)}
    def B(u,v):
        return (u[0]*v[1]-u[1]*v[0]+u[2]*v[3]-u[3]*v[2])%q
    lines = set()
    for a,b in combinations(range(len(points)),2):
        if B(points[a], points[b]):
            continue
        L=frozenset(ids[normalize(tuple((x*points[a][k]+y*points[b][k])%q for k in range(4)))]
                    for x,y in product(range(q), repeat=2) if x or y)
        lines.add(L)
    lines = sorted(lines,key=lambda x:tuple(sorted(x)))
    assert len(lines) == len(points) == (q+1)*(q*q+1)
    assert all(len(L) == q+1 for L in lines)
    return len(points), lines


def transpose_incidence(n,lines):
    return len(lines), [frozenset(j for j,L in enumerate(lines) if i in L) for i in range(n)]


def neighbour_sets(n,lines):
    adj = [set() for _ in range(n)]
    for line in lines:
        for a,b in combinations(line,2):
            adj[a].add(b);adj[b].add(a)
    return adj


def center_spectrum(n,lines,anchors):
    a,b=anchors
    near=neighbour_sets(n,lines)
    assert b not in near[a]
    centers = near[a] & near[b]
    assert len(centers)==len(lines[0])
    valid=[x for x in range(n) if x not in near[a] and x not in near[b] and x!=a and x!=b]
    return Counter(len(near[x] & centers) for x in valid)


def wl_pair(n1,lines1,marks1,n2,lines2,marks2):
    assert len(marks1)==len(marks2)
    def graph(n,lines):
        A=[set() for _ in range(n+len(lines))]
        for j,L in enumerate(lines):
            for x in L: A[x].add(n+j); A[n+j].add(x)
        return A
    A=graph(n1,lines1); B=graph(n2,lines2)
    nA=len(A); adj=A + [{nA+j for j in x} for x in B]
    init=[]
    for n,lines,marks in ((n1,lines1,marks1),(n2,lines2,marks2)):
        D={x:i for i,x in enumerate(marks)}
        init += [(0, D[x]+1 if x in D else 0) for x in range(n)] + [(1,0) for _ in lines]
    colors=[{c:i for i,c in enumerate(sorted(set(init)))}[x] for x in init]
    dseq=[]
    for step in range(12):
        C1=Counter(colors[:nA]); C2=Counter(colors[nA:]); eq=(C1==C2)
        dseq.append(eq)
        keys=[(colors[i],tuple(sorted(Counter(colors[j] for j in adj[i]).items()))) for i in range(len(adj))]
        codes={k:i for i,k in enumerate(sorted(set(keys)))}
        new=[codes[x] for x in keys]
        if len(set(new)) == len(set(colors)):
            # old colors are included in signatures, so equal number of cells means stability
            colors=new
            C1=Counter(colors[:nA]); C2=Counter(colors[nA:]);dseq.append(C1==C2)
            break
        colors=new
    return dseq,Counter(colors[:nA]),Counter(colors[nA:])


def test(q):
    n,W=make_symplectic(q)
    nD,D=transpose_incidence(n,W)
    assert n==nD
    for typ,ls in (('W',W),('dual',D)):
        nbs=neighbour_sets(n,ls)
        a,b=next((i,j) for i,j in combinations(range(n),2) if j not in nbs[i])
        hist=center_spectrum(n,ls,(a,b))
        expected=(Counter({q+1:q-1,1:(q-1)*(q*q-1)}) if typ=='W' else
                  Counter({2:q*(q*q-1)//2,0:q*(q-1)*(q-1)//2}))
        assert hist==expected,(q,typ,hist,expected)
        print('CENTER',q,typ,dict(sorted(hist.items())))
    nw=neighbour_sets(n,W);nd=neighbour_sets(n,D)
    a,b=next((i,j) for i,j in combinations(range(n),2) if j not in nw[i])
    c,d=next((i,j) for i,j in combinations(range(n),2) if j not in nd[i])
    seq,_,_=wl_pair(n,W,[a,b],n,D,[c,d])
    assert not seq[-1], (q,seq)
    print('WL_OPPOSITE',q,seq)
    for r in sorted(set((2,3,q,q+1))):
        Lw=sorted(W[0]); Ld=sorted(D[0]);
        seq,h1,h2=wl_pair(n,W,Lw[:r],n,D,Ld[:r])
        assert all(seq),(q,r,seq)
        delta=int(r < q+1)
        # if r=q, the remaining unmarked point is a singleton so class count same as full marked line
        predicted=3*r+3*delta+2
        assert len(h1)==predicted,(q,r,len(h1),predicted)
        assert sorted(h1.values())==sorted(h2.values())
        print('WL_COLLINEAR',q,r,'cells',len(h1),'equal_through_rounds',len(seq),'hist',sorted(h1.values()))
    print('OK',q)

if __name__=='__main__':
    for q in (3,5,7): test(q)
