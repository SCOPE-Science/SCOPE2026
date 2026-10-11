#!/usr/bin/env python3
"""Independent finite checks of shortest-path Rips complexes for equal-length three-arm families.
Python 3 standard library only; no proof of the all-parameter result is asserted by these checks.
"""
import itertools
from collections import deque, defaultdict


def graph(m):
    assert m >= 2
    n = 2 + 2*m
    adj = [set() for _ in range(n)]
    def add(x,y):
        adj[x].add(y); adj[y].add(x)
    for i in range(m):
        a=2+i; b=2+m+i
        add(0,a); add(a,b); add(b,1)
    return adj


def distances(adj):
    dist=[]
    for s in range(len(adj)):
        d=[-1]*len(adj); d[s]=0
        todo=deque([s])
        while todo:
            v=todo.popleft()
            for w in adj[v]:
                if d[w]<0:
                    d[w]=d[v]+1;todo.append(w)
        assert -1 not in d
        dist.append(d)
    return dist


def all_faces(dist, threshold):
    n=len(dist); levels=defaultdict(list)
    def walk(prefix, poss):
        for ix,v in enumerate(poss):
            nxt=prefix+(v,)
            levels[len(nxt)-1].append(nxt)
            remain=[w for w in poss[ix+1:] if dist[v][w]<=threshold]
            walk(nxt,remain)
    walk((),list(range(n)))
    return dict(levels)


def rank_f2(cols):
    piv={}
    for x in cols:
        while x:
            bit=x.bit_length()-1
            if bit in piv:x ^= piv[bit]
            else:piv[bit]=x;break
    return len(piv)


def betti_mod2(faces):
    rank={}
    for k in range(1,max(faces)+1):
        lows={x:i for i,x in enumerate(faces.get(k-1,[]))}
        cols=[]
        for s in faces.get(k,[]):
            bits=0
            for j in range(len(s)):
                bits ^= 1 << lows[s[:j]+s[j+1:]]
            cols.append(bits)
        rank[k]=rank_f2(cols)
    out={}
    for k,chain in faces.items():
        value=len(chain)-rank.get(k,0)-rank.get(k+1,0)-(k==0)
        if value:out[k]=value
    return out


def inversion_sign(values):
    inversions=sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))
    return 1 if inversions%2==0 else -1


def lefschetz_reduced(faces, mapping):
    tr=-1 # subtract trace on augmented chain in dimension -1
    for dim,ss in faces.items():
        chaintrace=0
        for s in ss:
            images=tuple(mapping[x] for x in s)
            if set(images)==set(s):
                chaintrace+=inversion_sign(images)
        tr+=(-1)**dim*chaintrace
    return tr


def transformed(m,perm,flip):
    v=list(range(2+2*m));v[0]=1 if flip else 0;v[1]=0 if flip else 1
    for i,j in enumerate(perm):
        v[2+i]=2+m+j if flip else 2+j
        v[2+m+i]=2+j if flip else 2+m+j
    return v


def verify():
    total_traces=0
    for m in range(2,9):
        D=distances(graph(m))
        assert max(max(d) for d in D)==3
        for i in range(m):
            for j in range(m):
                assert D[2+i][2+m+j]==(1 if i==j else 3)
                if i!=j:
                    assert D[2+i][2+j]==2 and D[2+m+i][2+m+j]==2
        assert D[0][1]==3
        assert all(D[0][v]<=2 and D[1][v]<=2 for v in range(2,2+2*m))
        f1=all_faces(D,1); f2=all_faces(D,2)
        assert betti_mod2(f1)=={1:m-1},(m,betti_mod2(f1))
        assert betti_mod2(f2)=={2:m-1},(m,betti_mod2(f2))
        # The two singleton pole vertices join the induced internal complex.
        # Its facets are precisely the two all-a/all-b simplices and m bridge edges.
        inner=all_faces([row[2:] for row in D[2:]],2)
        ia=tuple(range(m));ib=tuple(range(m,2*m))
        faceset=set(x for level in inner.values() for x in level)
        expected=set()
        for big in (ia,ib):
            for l in range(1,len(big)+1):
                expected.update(itertools.combinations(big,l))
        expected.update((i,m+i) for i in range(m))
        assert faceset==expected,(m,len(faceset),len(expected))
        for r,fs in ((1,f1),(2,f2)):
            if m<=5:
                for perm in itertools.permutations(range(m)):
                    fixed=sum(perm[i]==i for i in range(m))
                    for flip in (False,True):
                        L=lefschetz_reduced(fs,transformed(m,perm,flip))
                        expected_trace=(-1 if r==1 else 1)*(fixed-1)*((-1 if flip else 1) if r==1 else 1)
                        assert L==expected_trace,(m,r,perm,flip,L,expected_trace)
                        total_traces+=1
        print('m=%d, vertices=%d, scale1=%s, scale2=%s, faces2=%d' % (
              m,len(D),betti_mod2(f1),betti_mod2(f2),sum(map(len,f2.values()))))
    print('VERIFY_OK; complete equivariant Lefschetz traces=%d' % total_traces)

if __name__=='__main__':verify()
