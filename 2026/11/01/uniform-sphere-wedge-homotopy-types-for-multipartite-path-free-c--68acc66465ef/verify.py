#!/usr/bin/env python3
"""Independent finite tests for path-free complexes of complete multipartite graphs.
Only finite examples are checked; the universal theorem is established by the proof.
"""
from math import comb
from collections import Counter, deque


def choose(n,k):
    return comb(n,k) if 0<=k<=n else 0


def model(parts,t):
    N=sum(parts)
    blocks=[];bits=[];offset=0
    for a in parts:
        b=((1<<a)-1)<<offset
        blocks.append(b);bits.append(1<<offset);offset+=a
    s=(t-2)//2
    faces=set();high=set(); matched={}; lower=set();upper=set()
    counts=Counter()
    for w in range(1,1<<N):
        k=w.bit_count()
        occ=[(w&block).bit_count() for block in blocks]
        b=k-max(occ)
        if k<t or b<=s:
            faces.add(w); counts[k-1]+=1
            if k>=t:
                high.add(w)
                i=occ.index(max(occ))
                assert b<=s
                p=bits[i]
                u=w if w&p else w|p
                l=u^p
                assert l in faces or l.bit_count()==t-1, (parts,t,w,u,l)
                # The upper partner might not have been enumerated yet.
                if l in matched: assert matched[l]==u
                matched[l]=u
    # Check every matched upper has valid high face and lower face.
    for l,u in matched.items():
        assert l in faces and u in faces and u in high
        assert u.bit_count()==l.bit_count()+1
        assert l not in upper and u not in lower
        upper.add(u);lower.add(l)
    assert high <= (upper|lower), (parts,t, len(high),len(upper|lower))
    assert len(upper)==len(lower)
    assert not (upper&lower)
    critical=faces-(upper|lower)
    assert all(w.bit_count()<=t-1 for w in critical)
    B=choose(N-1,t-1)-sum(choose(N-a,b)*choose(a-1,t-b-1)
             for a in parts for b in range(0,s+1))
    assert B>=0
    euler=sum((-1)**(k)*n for k,n in counts.items())-1
    assert euler==(-1)**(t-2)*B,(parts,t,euler,B)
    # Directed Hasse orientation: matching edges upward; other edges downward.
    # Every directed cycle would contain an alternating Morse path.
    idx={w:i for i,w in enumerate(faces)}
    edges=[[] for _ in faces]; indeg=[0]*len(faces); incidence=0
    for w in faces:
        for j in range(N):
            bit=1<<j
            if not w&bit or w==bit:continue
            v=w^bit
            assert v in faces
            incidence+=1
            if matched.get(v)==w: x,y=v,w
            else: x,y=w,v
            ix=idx[x];iy=idx[y]
            edges[ix].append(iy);indeg[iy]+=1
    dq=deque(i for i,d in enumerate(indeg) if d==0)
    visited=0
    while dq:
        i=dq.popleft();visited+=1
        for j in edges[i]:
            indeg[j]-=1
            if indeg[j]==0:dq.append(j)
    assert visited==len(faces),(parts,t,'Hasse cycle!')
    # Independent graph path-existence test for all subsets at small N.
    if N<=9:
        col=[]
        for i,a in enumerate(parts):col.extend([i]*a)
        nbr=[sum(1<<j for j in range(N) if col[j]!=col[i]) for i in range(N)]
        def has_path(w,t):
            if w.bit_count()<t:return False
            paths=set((1<<i,i) for i in range(N) if w>>i&1)
            for k in range(1,t):
                new=set()
                for used,last in paths:
                    avail=(nbr[last]&w)&~used
                    while avail:
                        bit=avail&-avail;avail-=bit
                        new.add((used|bit,bit.bit_length()-1))
                paths=new
                if not paths:return False
            return bool(paths)
        for w in range(1,1<<N):
            assert (w in faces)==(not has_path(w,t)),(parts,t,w)
    if N<=9:
        bydim={d:sorted(w for w in faces if w.bit_count()==d+1)
               for d in range(max(counts)+1)}
        ranks={}
        for d,facets in bydim.items():
            old={w:j for j,w in enumerate(bydim.get(d-1,[]))}
            pivots={}
            for w in facets:
                v=1 if d==0 else 0
                if d>0:
                    for j in range(N):
                        if w>>j&1:v^=1<<old[w^(1<<j)]
                while v:
                    bit=v.bit_length()-1
                    if bit in pivots:v^=pivots[bit]
                    else:pivots[bit]=v;break
            ranks[d]=len(pivots)
        for d,facets in bydim.items():
            beta=len(facets)-ranks[d]-ranks.get(d+1,0)
            assert beta==(B if d==t-2 else 0),(parts,t,d,beta,B)
    print('VERIFY_OK', 'parts='+str(parts), 'threshold='+str(t),
          'faces='+str(len(faces)),'high='+str(len(high)),
          'pairs='+str(len(matched)),'incidences='+str(incidence),
          'dag='+str(visited), 'B='+str(B),
          'critical_dimensions='+str(dict(sorted(Counter(w.bit_count()-1 for w in critical).items()))))
    return B


def main():
    for parts,t in [((2,2,2),5), ((2,2,2),6), ((2,3,3),5),
       ((2,3,3),6),((3,3,3),5),((3,3,3),6),((3,3,4),5),
       ((3,3,4),6),((3,3,4),7),((2,4,5),8), ((4,4,4),5),
       ((4,4,4),6),((1,1,7),5), ((1,2,3,4),5),
       ((2,2,2),7),((1,1,1),5)]:
        model(parts,t)
    print('ALL_VERIFY_OK complete face enumeration, independent path DP (N<=9), explicit matching and Hasse DAG, Euler and formula')
if __name__=='__main__':main()
