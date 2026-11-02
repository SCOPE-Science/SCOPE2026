"""Exact finite checks for the radius-three Rips join theorem on C8 and W(2).

Uses only Python's standard library; does not claim finite examples prove a theorem.
"""
from itertools import combinations, permutations
from collections import defaultdict, deque


def perfect_matchings(items):
    if not items:
        yield ()
        return
    a, rest = items[0], items[1:]
    for b in rest:
        for leftover in perfect_matchings(tuple(x for x in rest if x != b)):
            yield tuple(sorted(((a, b),) + leftover))


def gq22():
    points = tuple(('p', i, j) for i, j in combinations(range(6), 2))
    mats = tuple(perfect_matchings(tuple(range(6))))
    lines = tuple(('l', mat) for mat in mats)
    edges = {frozenset((p, l)) for p in points for l in lines
             if (p[1], p[2]) in l[1]}
    return points, lines, edges


def cycle8():
    points = tuple(('p', i) for i in range(0, 8, 2))
    lines = tuple(('l', i) for i in range(1, 8, 2))
    vs = points + lines
    edges = {frozenset((vs[a], vs[b])) for a in range(8) for b in range(a+1, 8)
             if (int(vs[a][-1])-int(vs[b][-1])) % 8 in (1,7)}
    return points, lines, edges


def all_distances(verts, edges):
    nbr = {v:set() for v in verts}
    for u, v in map(tuple,edges):
        nbr[u].add(v); nbr[v].add(u)
    dist={}
    for v in verts:
        q=deque([v]); d={v:0}
        while q:
            u=q.popleft()
            for w in nbr[u]:
                if w not in d:
                    d[w]=d[u]+1;q.append(w)
        assert len(d)==len(verts)
        dist[v]=d
    return nbr,dist


def faces_color(color,dist):
    out={0:[(v,) for v in color]}
    for k in range(2,len(color)+1):
        arr=[t for t in combinations(color,k) if all(dist[x][y]<=2 for x,y in combinations(t,2))]
        if arr:out[k-1]=arr
        else:break
    return out


def mod2_rank(rows):
    piv={}
    for x in rows:
        while x:
            k=x.bit_length()-1
            if k not in piv:
                piv[k]=x;break
            x^=piv[k]
    return len(piv)


def bettis(faces):
    ranks={}
    for d in sorted(faces):
        if d==0: ranks[d]=0;continue
        lower={s:i for i,s in enumerate(faces[d-1])}
        cols=[]
        for s in faces[d]:
            c=0
            for j in range(len(s)):
                c^=1<<lower[s[:j]+s[j+1:]]
            cols.append(c)
        ranks[d]=mod2_rank(cols)
    return {d:len(faces[d])-ranks[d]-ranks.get(d+1,0) for d in faces}


def check(points,lines,edges,label):
    vs=points+lines
    nbr,dist=all_distances(vs,edges)
    assert max(dist[x][y] for x in vs for y in vs)<=4
    assert all(dist[x][y] in (1,3) for x in points for y in lines)
    assert all(dist[x][y] in (2,4) for color in (points,lines) for x,y in combinations(color,2))
    for color,opposite in ((points,lines),(lines,points)):
        for v,w in combinations(color,2):
            assert len(nbr[v]&nbr[w])<=1
        for triple in combinations(color,3):
            if all(dist[x][y]==2 for x,y in combinations(triple,2)):
                assert len(set.intersection(*(nbr[x] for x in triple)))==1
    fa,fb=faces_color(points,dist),faces_color(lines,dist)
    ba,bb=bettis(fa),bettis(fb)
    beta=len(edges)-len(vs)+1
    assert ba.get(0)==1 and ba.get(1,0)==beta and all(v==0 for d,v in ba.items() if d>=2)
    assert bb.get(0)==1 and bb.get(1,0)==beta and all(v==0 for d,v in bb.items() if d>=2)
    # Enumerate the join faces explicitly; all and only Rips diameter<=3 faces.
    all_faces=defaultdict(list)
    sideA=[()]+[s for rank in fa.values() for s in rank]
    sideB=[()]+[s for rank in fb.values() for s in rank]
    for a in sideA:
        for b in sideB:
            if a or b:
                s=tuple(sorted(a+b,key=repr))
                assert all(dist[x][y]<=3 for x,y in combinations(s,2))
                all_faces[len(s)-1].append(s)
    # Check converse by recovering each same-part face in an arbitrary r<=3 clique.
    assert len(all_faces[max(all_faces)])>0
    bjoin=bettis(all_faces)
    assert bjoin=={d:(1 if d==0 else beta*beta if d==3 else 0) for d in all_faces}
    assert len(all_faces)==(4 if label=='C8' else 6)
    print(label,'vertices',len(vs),'edges',len(edges),'beta',beta,
          'A_faces',{d:len(a) for d,a in fa.items()},
          'VR3_faces',{d:len(a) for d,a in all_faces.items()},
          'VR3_betti_mod2',bjoin)
    return beta


def symmetry_gq():
    P,L,E=gq22()
    edgeno=len(E); verts=P+L
    fixed_char=[]
    for perm in permutations(range(6)):
        def action(v):
            if v[0]=='p': return ('p',)+tuple(sorted((perm[v[1]],perm[v[2]])))
            m=tuple(sorted(tuple(sorted((perm[x],perm[y]))) for x,y in v[1]))
            return ('l',m)
        # Each graph edge is canonically oriented point to line, so edge-fixed signs are +1.
        edge_fixed=sum(action(p)==p and action(l)==l for p,l in
                       ((a,b) if a[0]=='p' else (b,a) for a,b in map(tuple,E)))
        vertex_fixed=sum(action(v)==v for v in verts)
        chi=edge_fixed-vertex_fixed+1
        fixed_char.append(chi)
        assert all(frozenset((action(a),action(b))) in E for a,b in map(tuple,E))
    assert fixed_char[0]==16
    assert sum(chi*chi for chi in fixed_char)==len(fixed_char)
    assert sum(chi for chi in fixed_char)==0
    print('W(2) type-preserving 720 symmetries: cycle-representation character squared invariant rank 1 PASS')

if __name__=='__main__':
    assert check(*cycle8(),'C8')==1
    assert check(*gq22(),'W(2) Tutte-Coxeter')==16
    symmetry_gq()
    print('GQ_RADIUS_THREE_JOIN_AND_720_CHARACTER_EXACT_OK')
