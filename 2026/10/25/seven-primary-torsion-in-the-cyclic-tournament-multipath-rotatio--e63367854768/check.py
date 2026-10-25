"""Exact integral chain computation for the seven-vertex cyclic tournament multipath complex.

Requires Python 3.10+ and SymPy (tested with SymPy 1.14.0).
Run: python check.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
import itertools
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

N = 7
ARCS = [(a, (a+d) % N) for a in range(N) for d in (1,2,3)]
ARCPOS = {a:i for i,a in enumerate(ARCS)}

def valid(bits):
    """Independent predicate: in/out-degree <=1 and no directed cycle."""
    succ={}; targets=set()
    for j,(u,v) in enumerate(ARCS):
        if bits>>j&1:
            if u in succ or v in targets: return False
            succ[u]=v; targets.add(v)
    for v in succ:
        seen=set();w=v
        while w in succ:
            if w in seen: return False
            seen.add(w);w=succ[w]
    return True

def enumerate_faces():
    """Enumerates every edge subset, without assuming its cardinality."""
    F=defaultdict(list)
    for s in range(1<<len(ARCS)):
        if valid(s): F[s.bit_count()-1].append(s)
    return dict(F)

def boundary(s):
    ids=[i for i in range(len(ARCS)) if s>>i&1]
    return [(s^(1<<j),(-1 if k%2 else 1)) for k,j in enumerate(ids)]

def smith(M):
    D=smith_normal_form(M,domain=ZZ)
    return Counter(abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i])

def original_morse(F):
    allfaces=set().union(*(set(v) for v in F.values()))
    remaining=set(allfaces);pairs=[]
    for j in range(len(ARCS)):
        for s in sorted(remaining):
            t=s|(1<<j)
            if not(s>>j&1) and t in remaining:
                remaining.remove(s); remaining.remove(t);pairs.append((s,t))
    lower_to_upper=dict(pairs);uppers={t for _,t in pairs}
    # Acyclicity certificate: the modified face-poset Hasse digraph is a DAG.
    degrees={s:0 for s in allfaces};out=defaultdict(list)
    P=set(pairs)
    for d,fs in F.items():
        if d<0:continue
        for t in fs:
            for s,_ in boundary(t):
                u,v=(s,t) if (s,t) in P else (t,s)
                out[u].append(v);degrees[v]+=1
    q=deque(s for s,v in degrees.items() if v==0);visited=0
    while q:
        s=q.popleft();visited+=1
        for v in out[s]:
            degrees[v]-=1
            if degrees[v]==0:q.append(v)
    assert visited==len(allfaces),"Morse matching is not acyclic"
    @lru_cache(None)
    def project(s):
        if s in remaining:return {s:1}
        if s in uppers:return {}
        t=lower_to_upper[s]
        sign=next(z for f,z in boundary(t) if f==s)
        result=defaultdict(int)
        for f,z in boundary(t):
            if f==s:continue
            for c,k in project(f).items():result[c]-=sign*z*k
        return {x:v for x,v in result.items() if v}
    critical={d:sorted(s for s in remaining if s.bit_count()-1==d) for d in range(-1,6)}
    B={}
    for d in range(0,6):
        if not critical[d] or not critical[d-1]:continue
        ix={s:i for i,s in enumerate(critical[d-1])}
        M=sp.zeros(len(ix),len(critical[d]))
        for j,s in enumerate(critical[d]):
            for f,z in boundary(s):
                for c,k in project(f).items():M[ix[c],j]+=z*k
        B[d]=M
    assert len(pairs)==1416
    assert [len(critical[d]) for d in range(3,6)]==[24,54,17]
    assert all(not critical[d] for d in [-1,0,1,2])
    assert smith(B[4])==Counter({1:11})
    assert not any(B[5])
    return [13,43,17]

def quotient(F):
    trans=[[ARCPOS[((a+t)%N,(b+t)%N)] for a,b in ARCS] for t in range(N)]
    @lru_cache(None)
    def normalize(s):
        original=[j for j in range(len(ARCS)) if s>>j&1]
        best=None;sign=1
        for perm in trans:
            image=[perm[j] for j in original]
            mask=sum(1<<j for j in image)
            if best is None or mask<best:
                best=mask
                inversions=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
                sign=(-1 if inversions%2 else 1)
        return best,sign
    # Every nonempty simplex has <7 vertices; translations have orbits of size 7.
    for d,fs in F.items():
        if d>=0:
            assert len(fs)%N==0
            assert max(s.bit_count() for s in fs)<N
    Q={d:sorted({normalize(s)[0] for s in fs}) for d,fs in F.items()}
    B={}
    for d in range(1,6):
        index={x:i for i,x in enumerate(Q[d-1])}
        M=sp.zeros(len(Q[d-1]),len(Q[d]))
        for j,s in enumerate(Q[d]):
            for low,sign in boundary(s):
                rep,orient=normalize(low)
                M[index[rep],j]+=sign*orient
        B[d]=M
    # A quotient simplicial orbit complex is a cellular chain complex.
    for d in range(2,6):assert B[d-1]*B[d]==sp.zeros(B[d-1].rows,B[d].cols)
    expected={1:{1:2},2:{1:21,7:1},3:{1:68},4:{1:88,7:2},5:{1:20}}
    for d,M in B.items():
        assert dict(smith(M))==expected[d],(d,smith(M))
    ranks={d:sum(expected[d].values()) for d in expected}
    betti={d:len(Q[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(6)}
    assert [len(Q[d]) for d in range(6)]==[3,24,90,159,117,25]
    assert betti=={0:1,1:0,2:0,3:1,4:7,5:5}
    return betti,expected

def modular_rank(columns,p):
    """Independent sparse column-echelon rank computation over a prime field."""
    pivots={}
    for c in columns:
        c={i:v%p for i,v in c.items() if v%p}
        while c:
            k=min(c)
            if k in pivots:
                z=c[k]
                for i,v in pivots[k].items():
                    w=(c.get(i,0)-z*v)%p
                    if w:c[i]=w
                    else:c.pop(i,None)
            else:
                z=pow(c[k],-1,p)
                pivots[k]={i:v*z%p for i,v in c.items()}
                break
    return len(pivots)

def independent_full_chain_ranks(F):
    expected=[20,148,482,618,158]
    for prime in (7,101):
        for degree in range(1,6):
            idx={s:i for i,s in enumerate(F[degree-1])}
            columns=[{idx[t]:v for t,v in boundary(s)} for s in F[degree]]
            assert modular_rank(columns,prime)==expected[degree-1]

if __name__=='__main__':
    F=enumerate_faces()
    counts=[len(F[d]) for d in range(6)]
    assert counts==[21,168,630,1113,819,175]
    assert len(F[-1])==1
    assert sum(counts)+1==2927
    independent_full_chain_ranks(F)
    b=original_morse(F)
    q,sm=quotient(F)
    # For C7 the nontrivial rational representation has dimension six.
    multiplicities={d:((b[d-3]-q[d])//6,q[d]) for d in (3,4,5)}
    assert multiplicities=={3:(2,1),4:(6,7),5:(2,5)}
    print('PASS: face counts',counts)
    print('PASS: integral reduced homology of the original in degrees 3,4,5:',b)
    print('PASS: orbit-cell Smith diagonals:',sm)
    print('PASS: quotient Betti numbers:',q)
    print('PASS: (cyclotomic,trivial) rational multiplicities:',multiplicities)
    print('PASS: quotient H1=Z/7 and H3=Z + (Z/7)^2; H4=Z^7, H5=Z^5.')
