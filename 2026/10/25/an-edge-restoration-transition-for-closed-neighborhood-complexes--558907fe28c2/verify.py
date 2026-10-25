#!/usr/bin/env python3
"""Finite checks for closed-neighborhood complexes of bipartite graphs."""
import itertools
import random
from collections import defaultdict


def subsets(mask):
    sub = mask
    while sub:
        yield sub
        sub = (sub - 1) & mask


def simplex_faces(vertices):
    out = {0}
    for v in vertices:
        out |= {s | (1 << v) for s in list(out)}
    return out


def complexes(a, b, edges):
    N = a + b
    nbs = [set() for _ in range(N)]
    for x, y in edges:
        assert 0 <= x < a <= y < N
        nbs[x].add(y)
        nbs[y].add(x)
    X = {0}
    Y = {0}
    for u in range(a):
        Y.update(simplex_faces({u} | nbs[u]))
    for v in range(a, N):
        X.update(simplex_faces({v} | nbs[v]))
    return X, Y, X | Y, X & Y, nbs


def groups(faces):
    out=defaultdict(list)
    for x in faces:
        if x: out[x.bit_count()-1].append(x)
    for d in out:
        out[d].sort()
    return out


def boundary_cols(low, high):
    idx={x:i for i,x in enumerate(low)}
    for face in high:
        col=0
        for k in range(face.bit_length()):
            if face>>k&1:
                col ^= 1 << idx[face^(1<<k)]
        yield col


def insert(vec,pivots):
    while vec:
        p=vec.bit_length()-1
        if p in pivots: vec ^= pivots[p]
        else:
            pivots[p]=vec
            return True
    return False


def betti(faces):
    g=groups(faces)
    ranks={0:0}
    for d in sorted(g):
        if d==0:continue
        piv={}
        for c in boundary_cols(g[d-1],g[d]):insert(c,piv)
        ranks[d]=len(piv)
    return {d:len(v)-ranks.get(d,0)-ranks.get(d+1,0)-(d==0) for d,v in g.items()}


def relative_cone_collapse(faces, apex, base):
    fs=set(faces)
    base=set(base)
    assert apex not in base and len(base)>0
    x=1<<apex
    root=1<<min(base)
    other=sum(1<<v for v in base if v!=min(base))
    # All apex faces disappear, paired with the same face after adjoining root.
    pairs=[]
    choices=list(subsets(other))+[0]
    choices.sort(key=lambda t:(-t.bit_count(),-t))
    for t in choices:
        lower=x|t
        upper=lower|root
        assert lower in fs and upper in fs
        higher=[z for z in fs if z!=lower and z & lower==lower]
        assert higher==[upper], ('not-free',apex,lower,higher)
        fs.remove(lower);fs.remove(upper)
        pairs.append((lower,upper))
    return fs,pairs


def check_hemi(a,b,edges,X,Y,nbs):
    final_X=set(X)
    final_Y=set(Y)
    cnt=0
    for v in range(a,a+b):
        final_X,pairs=relative_cone_collapse(final_X,v,nbs[v])
        cnt+=len(pairs)
    for u in range(a):
        final_Y,pairs=relative_cone_collapse(final_Y,u,nbs[u])
        cnt+=len(pairs)
    maskA=(1<<a)-1
    maskB=((1<<b)-1)<<a
    assert all((f&~maskA)==0 for f in final_X)
    assert all((f&~maskB)==0 for f in final_Y)
    return final_X,final_Y,cnt


def kernel_vectors(cols):
    piv={}
    ker=[]
    for j,b0 in enumerate(cols):
        v=1<<j; b=b0
        while b:
            p=b.bit_length()-1
            if p in piv:
                bb,vv=piv[p];b^=bb;v^=vv
            else:piv[p]=(b,v);break
        if not b:ker.append(v)
    return ker


def h2_map_rank(src,dst):
    s=groups(src);t=groups(dst)
    if 2 not in s:return 0
    src2=s[2];dst2=t[2];src1=s[1]
    ker=kernel_vectors(list(boundary_cols(src1,src2)))
    idx2={x:i for i,x in enumerate(dst2)}
    borders={}
    for c in boundary_cols(dst2,t.get(3,[])):insert(c,borders)
    indep=dict(borders)
    rank=0
    for c in ker:
        lifted=0
        for i,x in enumerate(src2):
            if c>>i&1:lifted ^=1<<idx2[x]
        if insert(lifted,indep):rank+=1
    return rank


def test_partial(n,j):
    missing=set(range(n-j))
    edges={(i,n+k) for i in range(n) for k in range(n) if i!=k or i not in missing}
    X,Y,K,I,nbs=complexes(n,n,edges)
    expI={0}|{1<<i for i in range(2*n)}|{(1<<u)|(1<<v) for u,v in edges}
    assert I==expI
    XA,YB,count=check_hemi(n,n,edges,X,Y,nbs)
    maskA=(1<<n)-1; maskB=maskA<<n
    if j==0:
        assert XA==simplex_faces(range(n))-{maskA}
        assert YB==simplex_faces(range(n,2*n))-{maskB}
    else:
        assert XA==simplex_faces(range(n))
        assert YB==simplex_faces(range(n,2*n))
    b=betti(K)
    pred={}
    if j==0:
        pred[2]=n*n-3*n+1
        pred[n-2]=pred.get(n-2,0)+2
    else: pred[2]=n*n-3*n+1+j
    got={k:v for k,v in b.items() if v}
    assert got==pred,(n,j,len(K),got,pred)
    return K,len(K),count,got


def test_random(seed=24681357):
    rng=random.Random(seed)
    checks=0
    for a in range(2,6):
        for b in range(2,6):
            for rep in range(4):
                # 0 and a are opposite-side universal vertices; other edges random.
                edges={(i,a+j) for i in range(a) for j in range(b)
                       if i==0 or j==0 or rng.getrandbits(1)}
                X,Y,K,I,nbs=complexes(a,b,edges)
                expectedI={0}|{1<<u for u in range(a+b)}|{(1<<u)|(1<<v) for u,v in edges}
                assert I==expectedI
                XA,YB,pairs=check_hemi(a,b,edges,X,Y,nbs)
                assert XA==simplex_faces(range(a))
                assert YB==simplex_faces(range(a,a+b))
                B={d:v for d,v in betti(K).items() if v}
                assert B==({2:len(edges)-(a+b)+1} if len(edges)>a+b-1 else {}),(a,b,rep,B)
                checks+=1
    return checks


def main():
    total_faces=0;total_pairs=0;maps=0
    for n in range(4,8):
        previous=None
        for j in range(n+1):
            K,num,pairs,b=test_partial(n,j)
            total_faces+=num-1
            total_pairs+=pairs
            if previous is not None and n<=5:
                rank=h2_map_rank(previous,K)
                expect=n*n-3*n+1+j-1
                assert rank==expect,(n,j,rank,expect)
                maps+=1
            previous=K
    rand=test_random()
    print('VERIFY_OK', 'partial_cases',sum(n+1 for n in range(4,8)),
          'random_graphs',rand,'faces',total_faces,'hemisphere_collapse_pairs',total_pairs,
          'mod2_inclusion_checks',maps)

if __name__=='__main__':main()
