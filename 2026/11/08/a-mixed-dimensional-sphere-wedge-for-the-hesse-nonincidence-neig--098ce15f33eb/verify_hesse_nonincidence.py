"""Finite verification of a neighborhood-complex homotopy type in the nine-point affine plane."""
from collections import Counter,deque,defaultdict
from itertools import combinations

def affine():
    pts=[(x,y) for x in range(3) for y in range(3)]
    forms=[(1,0,v) for v in range(3)]+[(0,1,v) for v in range(3)]+[(1,m,v) for m in (1,2) for v in range(3)]
    ls=[frozenset(i for i,(x,y) in enumerate(pts) if (a*x+b*y-c)%3==0) for a,b,c in forms]
    assert len(set(ls))==12 and all(len(l)==3 for l in ls)
    assert all(sum(i in l for l in ls)==4 for i in range(9))
    return ls

def subsets(facets):
    x={0}
    for facet in facets:
        a=facet
        while a:
            x.add(a);a=(a-1)&facet
    return x

def membership_direct(ls,n,side):
    if side=='points':
        return {s for s in range(1<<9) if any(all(not(s>>i&1) for i in L) for L in ls)}
    return {s for s in range(1<<12) if any(all(not(s>>j&1) for j,L in enumerate(ls) if i in L) for i in range(9))}

def getcomplexes():
    ls=affine()
    point_facets=[sum(1<<i for i in range(9) if i not in L) for L in ls]
    line_facets=[sum(1<<j for j,L in enumerate(ls) if i not in L) for i in range(9)]
    p=subsets(point_facets);l=subsets(line_facets)
    assert p==membership_direct(ls,9,'points') and l==membership_direct(ls,12,'lines')
    return (p,point_facets),(l,line_facets)

def boundary(face):
    verts=[i for i in range(face.bit_length()) if face>>i&1]
    return {face^(1<<i):(-1 if j%2 else 1) for j,i in enumerate(verts)}

def morse(faces,n,order):
    remaining=set(faces-{0});pairs=[]
    for i in order:
        bit=1<<i
        for s in sorted((s for s in remaining if not(s&bit)),key=lambda s:(s.bit_count(),s)):
            if s in remaining and s|bit in remaining:
                t=s|bit;remaining.remove(s);remaining.remove(t);pairs.append((s,t))
    # oriented Hasse directed downward for unmatched, upwards for matched
    mapping={f:g for f,g in pairs};verts=faces-{0}
    out={s:[] for s in verts};indeg={s:0 for s in verts}; m=0
    for s in verts:
        bits=s
        while bits:
            b=bits&-bits;bits-=b;t=s^b
            if not t:continue
            if mapping.get(t)==s: src,dst=t,s
            else:src,dst=s,t
            out[src].append(dst);indeg[dst]+=1;m+=1
    todo=deque(s for s in verts if indeg[s]==0);num=0
    while todo:
        v=todo.popleft();num+=1
        for w in out[v]:
            indeg[w]-=1
            if indeg[w]==0:todo.append(w)
    assert num==len(verts),(num,len(verts))
    return pairs,remaining,m

def morse_top_boundary(pairs,critical,topdim):
    basis={lo:hi for lo,hi in pairs if lo.bit_count()==topdim}
    answers=[]
    for c in sorted(s for s in critical if s.bit_count()==topdim+1):
        cur=defaultdict(int,boundary(c));count=0
        while True:
            matched=next((s for s,v in cur.items() if v and s in basis),None)
            if matched is None:break
            hi=basis[matched];bs=boundary(hi);sgn=bs[matched];coef=cur[matched]//sgn
            for s,v in bs.items():cur[s]-=coef*v
            count+=1
            assert count<100000
        assert all(v==0 or s in critical for s,v in cur.items())
        answers.append({s:v for s,v in cur.items() if v})
    return answers

def main():
 for (name,n),(faces,facets) in zip([('point',9),('line',12)],getcomplexes()):
    fvec=Counter(s.bit_count()-1 for s in faces if s)
    print(name,'faces',len(faces),'facets',len(facets),'fvec',sorted(fvec.items()))
    for order in (tuple(range(n)),tuple(reversed(range(n)))):
        pairs,crit,inc=morse(faces,n,order)
        cv=Counter(x.bit_count()-1 for x in crit)
        print(name,'morse',len(pairs),dict(cv),'incidences',inc)
        assert cv==Counter({0:1,3:11,4:1})
        bd=morse_top_boundary(pairs,crit,4)
        print(name,'critical 4-to-3 map',bd)
        assert len(bd)==1 and not bd[0]
 print('AFFINE_NONINCIDENCE_VERIFIED')
if __name__=='__main__':main()
