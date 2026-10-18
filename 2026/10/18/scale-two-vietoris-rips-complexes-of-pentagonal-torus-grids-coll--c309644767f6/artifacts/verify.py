"""Finite computational cross-check for the scale-two Rips complex of C_5 square C_n.
This is a finite cross-check of a separately stated uniform collapse proof.
Python 3, standard library only.
"""
from itertools import combinations
from collections import Counter


def v(i,j,n):
    return (i%5)*n + j%n

def dcycle(a,b,m):
    t=(a-b)%m
    return min(t,m-t)

def adjacency(n):
    return {v(i,j,n): {v(k,l,n) for k in range(5) for l in range(n)
                        if (k,l)!=(i,j) and dcycle(i,k,5)+dcycle(j,l,n)<=2}
            for i in range(5) for j in range(n)}

def actual_faces(n):
    nbr=adjacency(n)
    faces=set()
    for u in range(5*n):
        layer=[(u,)]
        while layer:
            t=layer.pop()
            faces.add(t)
            possibilities=set.intersection(*(nbr[z] for z in t)) if len(t)>1 else nbr[u]
            layer.extend(tuple(sorted(t+(w,))) for w in possibilities if w>t[-1])
    return faces

def simplices(n):
    a=[];b=[];c=[]
    for j in range(n):
        a.append(tuple(v(i,j,n) for i in range(5)))
        for i in range(5):
            # B=(L,R,M0,M1,M2)
            b.append(tuple(v(x,y,n) for x,y in
                [(i,j-1),(i,j+1),(i-1,j),(i,j),(i+1,j)]))
            # C=(a,b,c,d), counterclockwise corners
            c.append(tuple(v(x,y,n) for x,y in
                [(i,j),(i+1,j),(i+1,j+1),(i,j+1)]))
    return a,b,c

def closed_faces(facets):
    out=set()
    for f in facets:
        for z in range(1,len(f)+1):
            out.update(tuple(sorted(t)) for t in combinations(f,z))
    return out

def pair_delete(active,low,up,stage):
    lo=tuple(sorted(low));hi=tuple(sorted(up))
    assert lo in active and hi in active,(stage,'missing',lo,hi)
    assert len(hi)==len(lo)+1 and set(lo)<set(hi),(stage,'incidence')
    cofaces=[c for c in active if len(c)==len(hi) and set(lo).issubset(c)]
    assert cofaces==[hi],(stage,'not free',lo,hi,cofaces)
    active.remove(lo);active.remove(hi)

def reduce(n,verbose=False):
    f=actual_faces(n)
    A,B,C=simplices(n)
    pred=closed_faces(A+B+C)
    assert f==pred,('facet types incorrect',n,len(f),len(pred),len(f^pred))
    orig=Counter(len(z)-1 for z in f)
    assert [orig[i] for i in range(5)]==[5*n,30*n,55*n,35*n,6*n]
    # Phase 1: six free-face pairings within each length-five B.
    for j in range(n):
      for i in range(5):
        L,R,M0,M1,M2=(v(i,j-1,n),v(i,j+1,n),v(i-1,j,n),v(i,j,n),v(i+1,j,n))
        moves=[((L,R,M0,M2),(L,R,M0,M1,M2)),
               ((L,M0,M2),(L,M0,M1,M2)),
               ((R,M0,M2),(R,M0,M1,M2)),
               ((L,R,M0),(L,R,M0,M1)),
               ((L,R,M2),(L,R,M1,M2)),
               ((L,R),(L,R,M1))]
        for low,up in moves:pair_delete(f,low,up,('B',n,j,i))
    ac=closed_faces(A+C)
    assert f==ac,('phase B mismatch',n,len(f^ac))
    # Phase 2: in each C tetrahedron retain exactly two triangles
    # forming a square, with the diagonal a-c.
    for j in range(n):
      for i in range(5):
        a,b,c,d=(v(i,j,n),v(i+1,j,n),v(i+1,j+1,n),v(i,j+1,n))
        pair_delete(f,(a,b,d),(a,b,c,d),('C tetra',n,j,i))
        pair_delete(f,(b,d),(b,c,d),('C diagonal',n,j,i))
    torso=closed_faces(A)
    for j in range(n):
      for i in range(5):
        a,b,c,d=(v(i,j,n),v(i+1,j,n),v(i+1,j+1,n),v(i,j+1,n))
        torso.update(closed_faces([(a,b,c),(a,c,d)]))
    assert f==torso,('final target mismatch',n,len(f^torso))
    vec=Counter(len(z)-1 for z in f)
    assert [vec[i] for i in range(5)]==[5*n,20*n,20*n,5*n,n]
    if verbose: print('n',n,'full',dict(sorted(orig.items())),'final',dict(sorted(vec.items())),
                      'elementary collapses',40*n)
    return f


def rank_mod2(columns):
    basis={}
    for col in columns:
        while col:
            r=col.bit_length()
            if r not in basis:
                basis[r]=col
                break
            col^=basis[r]
    return len(basis)

def homology_mod2(f):
    bydim={k:sorted(x for x in f if len(x)==k+1) for k in range(5)}
    bdry={0:0,5:0}
    for k in range(1,5):
        i={s:t for t,s in enumerate(bydim[k-1])}
        cols=[sum(1<<i[face] for face in combinations(s,k)) for s in bydim[k]]
        bdry[k]=rank_mod2(cols)
    return [len(bydim[k])-bdry[k]-bdry[k+1] for k in range(5)]

if __name__=='__main__':
    for n in range(7,15):
        f=reduce(n,True)
        if n<=10:
            got=homology_mod2(f)
            assert got==[1,1,n,0,0],(n,got)
            print('mod2 Betti verified:',got)
    print('VERIFY_OK: face classification, all free pairs, final complex, homology checks')
