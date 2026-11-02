#!/usr/bin/env python3
"""Exact finite-field and integral cycle-lattice checks for translation actions
on affine-plane incidence graph scale-two Rips homology.

Uses only Python's standard library. The all-prime-power theorem is proved
in the accompanying mathematical text; the computations test small fields.
"""
from collections import deque
from itertools import product, combinations
from math import prod


def ff(q):
    if q == 4:
        def add(a, b): return a ^ b
        def mul(a, b):
            ans = 0
            while b:
                if b & 1: ans ^= a
                b >>= 1
                a <<= 1
                if a & 4: a ^= 7  # t^2+t+1
            return ans
    elif q in (3, 5):
        def add(a, b): return (a + b) % q
        def mul(a, b): return (a * b) % q
    else:
        raise ValueError('only verification fields GF(3), GF(4), GF(5)')
    neg = lambda x: next(a for a in range(q) if add(x, a) == 0)
    return add, mul, neg


def data(q):
    add, mul, neg = ff(q)
    P = list(product(range(q), repeat=2))
    dirs = list(range(q)) + ['vertical']
    L = list(product(dirs, range(q)))
    line_id = {l:i for i,l in enumerate(L)}
    point_id = {p:i for i,p in enumerate(P)}
    def on_line(p, line):
        (x,y), (d,b) = p, line
        return x==b if d=='vertical' else y==add(mul(d,x),b)
    E = [(i,j) for i,p in enumerate(P) for j,l in enumerate(L) if on_line(p,l)]
    e_id = {edge:i for i,edge in enumerate(E)}
    return add,mul,neg,P,L,dirs,point_id,line_id,E,e_id


def graph_basis(q, ctx):
    _,_,_,P,L,_,_,_,E,_ = ctx
    n = len(P)+len(L)
    adj = [[] for _ in range(n)]
    for eid,(pi,lj) in enumerate(E):
        v=pi; w=len(P)+lj
        adj[v].append((w,eid,+1))
        adj[w].append((v,eid,-1))
    parent={0:(None,None,None)}
    todo=deque([0]); tree=set()
    while todo:
        v=todo.popleft()
        for w,eid,sgn in adj[v]:
            if w not in parent:
                parent[w]=(v,eid,sgn)
                tree.add(eid)
                todo.append(w)
    assert len(parent)==n, 'incidence graph disconnected'
    chords=[e for e in range(len(E)) if e not in tree]
    def route(v,w):
        # Traversal from v to w through the spanning tree,
        # with orientation from point to line.
        seen={};u=v
        while u is not None:
            seen[u]=True; u=parent[u][0]
        u=w; dw=[]
        while u not in seen:
            prev,eid,sgn = parent[u]
            dw.append((eid,-sgn)) # traversing u -> prev
            u=prev
        lca=u; u=v; dv=[]
        while u!=lca:
            prev,eid,sgn=parent[u]
            dv.append((eid,-sgn)) # u -> prev
            u=prev
        return dv + [(eid,-sgn) for eid,sgn in reversed(dw)]
    basis=[]
    for chord in chords:
        pi,lj=E[chord]; end=len(P)+lj
        z={chord:1}
        # chord points from pi to line, so return from line to pi.
        for eid,sgn in route(end,pi):z[eid]=z.get(eid,0)+sgn
        assert all(v in (-1,1) for v in z.values()), 'non-simple fundamental cycle'
        boundary=[0]*n
        for eid,sgn in z.items():
            a,b=E[eid];boundary[a]-=sgn;boundary[len(P)+b]+=sgn
        assert not any(boundary)
        basis.append(z)
    assert len(chords)==(q-1)**2*(q+1)
    return chords,basis


def examine(q):
    ctx=data(q);add,mul,neg,P,L,dirs,pid,lid,E,eid=ctx
    chords,cycles=graph_basis(q,ctx)
    dims2=(q-1)**2*(q+1)
    dimsq=(q-1)**(q+1)
    traces2=[];tracesq=[]
    perms={}
    for a,c in P:
        pperm=[pid[(add(x,a),add(y,c))] for x,y in P]
        lperm=[]
        for d,b in L:
            shift=a if d=='vertical' else add(c,neg(mul(d,a)))
            lperm.append(lid[(d,add(b,shift))])
        eperm=[eid[(pperm[i],lperm[j])] for i,j in E]
        assert sorted(eperm)==list(range(len(E)))
        # Compute integral action on the fundamental-cycle basis.
        diag=0
        for col,(ch,z) in enumerate(zip(chords,cycles)):
            m={eperm[k]:v for k,v in z.items()}
            diag+=m.get(ch,0)
            # Coefficients in the chord basis reproduce the transported cycle.
            coeffs=[m.get(ch2,0) for ch2 in chords]
            actual=[0]*len(E)
            for z2,fac in zip(cycles,coeffs):
                for edge,sign in z2.items():actual[edge]+=fac*sign
            assert all(actual[k]==m.get(k,0) for k in range(len(E)))
        traces2.append(diag)
        # Integral augmentation bases e_i - e_(q-1) in each class.
        factors=[]
        for d in dirs:
            lineperm=[]
            for b in range(q):
                old=lid[(d,b)]; nd,nb=L[lperm[old]]
                assert nd==d
                lineperm.append(nb)
            assert sorted(lineperm)==list(range(q))
            trace=0
            for i in range(q-1):
                trace+= (1 if lineperm[i]==i else 0)
                trace-= (1 if lineperm[q-1]==i else 0)
            assert trace==sum(lineperm[i]==i for i in range(q))-1
            factors.append(trace)
        tracesq.append(prod(factors))
        perms[(a,c)] = (pperm,lperm)
    tau=(q-1)*(-1)**q
    assert traces2[0]==dims2 and all(x==1-q for x in traces2[1:])
    assert tracesq[0]==dimsq and all(x==tau for x in tracesq[1:])
    # Fixed dimensions and augmentation-regular multiplicities over Q.
    assert sum(traces2)==0
    assert sum(tracesq)%q**2==0
    bq=sum(tracesq)//q**2
    aq=(dimsq-tau)//q**2
    assert bq>=0 and aq>=0 and bq+aq*(q*q-1)==dimsq
    assert bq== (dimsq+(q*q-1)*tau)//(q*q)
    print('q',q,'T',q*q,'H2_dim',dims2,'Hq_dim',dimsq,
          'H2_nontrivial_trace',1-q,'Hq_nontrivial_trace',tau,
          'H2_fixed',0,'Hq_fixed',bq,'Hq_augmentation_copies',aq)
    return bq



def explicit_scale_two_homology_q3():
    """Independently enumerate all Rips cliques and exact mod-101 boundaries."""
    q=3
    ctx=data(q);_,_,_,P,L,dirs,_,_,_,_=ctx
    nP=len(P)
    adjacent=lambda p,l: ((p[0]==l[1]) if l[0]=='vertical' else
                          p[1]==(l[0]*p[0]+l[1])%q)
    facets=[tuple(range(nP))]
    facets += [tuple(nP+L.index((d,b)) for d,b in zip(dirs,choices))
               for choices in product(range(q),repeat=q+1)]
    facets += [tuple([i]+[nP+j for j,l in enumerate(L) if adjacent(p,l)])
               for i,p in enumerate(P)]
    facets += [tuple([nP+j]+[i for i,p in enumerate(P) if adjacent(p,l)])
               for j,l in enumerate(L)]
    faces=set()
    for f in facets:
        f=sorted(f)
        for k in range(1,len(f)+1):
            faces.update(combinations(f,k))
    bydim={k:sorted(f for f in faces if len(f)==k+1)
           for k in range(max(map(len,faces)))}
    assert [len(bydim[k]) for k in range(9)]==[21,126,282,255,135,84,36,9,1]
    def rank(rows,p=101):
        piv={}
        for row in rows:
            row={k:v%p for k,v in row.items() if v%p}
            while row:
                k=min(row)
                if k not in piv:
                    inv=pow(row[k],-1,p)
                    piv[k]={j:(v*inv)%p for j,v in row.items()}
                    break
                coef=row[k]
                for j,v in piv[k].items():
                    row[j]=(row.get(j,0)-coef*v)%p
                    if not row[j]:del row[j]
        return len(piv)
    ranks={0:0}
    for d in range(1,len(bydim)):
        last={face:i for i,face in enumerate(bydim[d-1])}
        rows=[{last[f[:j]+f[j+1:]]: (-1)**j for j in range(len(f))}
              for f in bydim[d]]
        ranks[d]=rank(rows)
    betti=[len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0)
           for d in bydim]
    assert betti==[1,0,16,16,0,0,0,0,0]
    print('q3_explicit_Rips2_face_vector',[len(bydim[k]) for k in bydim],
          'mod101_Betti',betti)

if __name__=='__main__':
    explicit_scale_two_homology_q3()
    assert [examine(q) for q in (3,4,5)]==[0,18,160]
    print('AFFINE_TRANSLATION_INTEGRAL_CYCLES_AND_ALL_ACTIONS_OK')
