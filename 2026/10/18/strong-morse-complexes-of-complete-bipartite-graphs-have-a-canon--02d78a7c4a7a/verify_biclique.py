#!/usr/bin/env python3
"""Independent finite checks for strong discrete-Morse matching complexes of bicliques.

No external dependencies. The input graph is a one-dimensional simplicial complex.
Every strict vertex order determines pairs v--(v,w) precisely when v has one
previous neighbor w. We compare this direct construction with a predicted cover,
then calculate homology and equivariant Lefschetz numbers from all faces.
"""
from itertools import combinations, permutations, product
from math import factorial


def arcs(m,n):
    A=range(m); B=range(m,m+n)
    return tuple([(a,b) for a in A for b in B]+[(b,a) for b in B for a in A])


def generators(m,n):
    A=range(m); B=range(m,m+n)
    g=[]
    for b in B:
        base=frozenset((a,b) for a in A)
        g.append(base)
        for a in A:
            g.append((base-{(a,b)})|{(b,a)})
    for a in A:
        base=frozenset((b,a) for b in B)
        g.append(base)
        for b in B:
            g.append((base-{(b,a)})|{(a,b)})
    return g


def directly_generated(m,n):
    vs=tuple(range(m+n))
    res=set()
    for order in permutations(vs):
        sa=[];sb=[];picked=[]
        for v in order:
            if v<m:
                if len(sb)==1: picked.append((v,sb[0]))
                sa.append(v)
            else:
                if len(sa)==1: picked.append((v,sa[0]))
                sb.append(v)
        res.add(frozenset(picked))
    return res


def closure(g):
    fs={frozenset()}
    for facet in g:
        t=tuple(facet)
        for k in range(len(t)+1):
            fs.update(frozenset(s) for s in combinations(t,k))
    return fs


def b2_ranks(faces):
    bydim={}
    for f in faces:
        if f: bydim.setdefault(len(f)-1,[]).append(tuple(sorted(f)))
    maxd=max(bydim)
    ranks={-1:0}
    for d in range(1,maxd+1):
        lower={f:i for i,f in enumerate(bydim[d-1])}
        pivot={}
        for f in bydim[d]:
            col=0
            for i in range(len(f)):
                col^=1<<lower[f[:i]+f[i+1:]]
            while col:
                lead=col.bit_length()-1
                if lead not in pivot:
                    pivot[lead]=col
                    break
                col^=pivot[lead]
        ranks[d]=len(pivot)
    betti={d:len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0)
           for d in range(maxd+1)}
    betti[0]-=1
    return tuple(len(bydim[d]) for d in range(maxd+1)), {d:b for d,b in betti.items() if b}


def perm_sign_on_vertices(perm):
    count=sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
    return -1 if count%2 else 1


def trace_h1_from_complex(faces,m,n,pa,pb,swap=False):
    def action(arc):
        v,w=arc
        if not swap:
            act=lambda x:pa[x] if x<m else m+pb[x-m]
        else:
            # m=n and pa,pb specify images of A in B and B in A.
            act=lambda x:m+pa[x] if x<m else pb[x-m]
        return act(v),act(w)
    total=0
    for f in faces:
        if not f:continue
        t=tuple(sorted(f))
        moved=tuple(action(x) for x in t)
        if set(moved)!=set(t):continue
        index={x:i for i,x in enumerate(t)}
        induced=[index[x] for x in moved]
        sign=perm_sign_on_vertices(induced)
        total+=((-1)**(len(t)-1))*sign
    return 1-total


def predicted_trace(m,n,pa,pb,swap=False):
    if swap:
        return 1
    a=sum(pa[i]==i for i in range(m)); b=sum(pb[i]==i for i in range(n))
    return 2*a*b-a-b+1


def run(m,n,lefschetz=False):
    g=generators(m,n)
    direct=directly_generated(m,n)
    assert all(any(g0<=M for M in direct) for g0 in g), 'predicted generator unrealizable'
    assert all(any(M<=g0 for g0 in g) for M in direct), 'some direct gradient outside cover'
    faces=closure(g)
    assert closure(direct)==faces, 'face closure mismatch'
    fv,bt=b2_ranks(faces)
    loops=2*m*n-m-n+1
    assert bt=={1:loops},(m,n,bt,loops)
    if lefschetz:
        pas=list(permutations(range(m)))
        pbs=list(permutations(range(n)))
        for pa,pb in product(pas,pbs):
            got=trace_h1_from_complex(faces,m,n,pa,pb)
            exp=predicted_trace(m,n,pa,pb)
            assert got==exp,(m,n,pa,pb,got,exp)
        if m==n:
            for pa,pb in product(pas,pbs):
                got=trace_h1_from_complex(faces,m,n,pa,pb,True)
                assert got==1,(m,pa,pb,got)
    print('K_%d,%d orders=%d direct_gradients=%d cover_generators=%d faces=%d f_vector=%s reduced_betti=%s%s PASS'%(
          m,n,factorial(m+n),len(direct),len(g),len(faces)-1,fv,bt,
          (' group_character_checks='+str(factorial(m)*factorial(n)*(2 if m==n else 1))) if lefschetz else ''))

if __name__=='__main__':
    for m,n in [(2,2),(2,3),(3,3),(3,4),(3,5),(4,4),(4,5)]:
        run(m,n,lefschetz=(m,n) in {(2,2),(3,3),(3,4)})
    print('ALL INDEPENDENT FINITE CHECKS PASSED')
