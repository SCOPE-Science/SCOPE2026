"""Independent finite checks for sharp tetrahedral volumes in regular prisms.

Only Python standard library needed. Computations check finite n and do not prove the
all-n result (proved by symmetric strict concavity in RESULT.md).
"""
from itertools import combinations
from math import pi, sin, cos


def det2(a,b):
    return a[0]*b[1]-a[1]*b[0]


def sub(a,b):
    return a[0]-b[0],a[1]-b[1]


def chord_max_and_count(n):
    p=[(cos(2*pi*j/n),sin(2*pi*j/n)) for j in range(n)]
    chords=[(i,j,sub(p[j],p[i])) for i,j in combinations(range(n),2)]
    best=-1.0; optimal=[]
    for ix,(a,b,v) in enumerate(chords):
        for jx in range(ix+1,len(chords)):
            c,d,w=chords[jx]
            value=abs(det2(v,w))
            if value>best+1.e-9:
                best=value;optimal=[(a,b,c,d)]
            elif abs(value-best)<1.e-9:
                optimal.append((a,b,c,d))
    x=pi/n
    if n%4==0:
        expected=4.0
        pairs=n//4
    elif n%2:
        expected=4*cos(pi/(2*n))**3
        pairs=n if n>=5 else 3
    else:
        expected=4*cos(x)
        pairs=3*n//2
    assert abs(best-expected)<1.e-8,(n,best,expected)
    assert len(optimal)==pairs,(n,len(optimal),pairs)
    if n>=4:
        for a,b,c,d in optimal:
            assert len({a,b,c,d})==4,(n,a,b,c,d)
            order=sorted([a,b,c,d]); p0,p1,p2,p3=order
            gaps=[p1-p0,p2-p1,p3-p2,n-(p3-p0)]
            assert max(gaps)-min(gaps)<=1,(n,order,gaps)
    return best,len(optimal)


def tetra_full_check(n):
    p=[(cos(2*pi*j/n),sin(2*pi*j/n)) for j in range(n)]
    verts=[(*q,z) for z in (0.0,1.0) for q in p]
    def vdet(a,b,c,d):
        ax,ay,az=verts[a];bx,by,bz=verts[b];cx,cy,cz=verts[c];dx,dy,dz=verts[d]
        u=(bx-ax,by-ay,bz-az);v=(cx-ax,cy-ay,cz-az);w=(dx-ax,dy-ay,dz-az)
        return abs(u[0]*(v[1]*w[2]-v[2]*w[1])-u[1]*(v[0]*w[2]-v[2]*w[0])+u[2]*(v[0]*w[1]-v[1]*w[0]))
    values=[(vdet(*v),v) for v in combinations(range(2*n),4)]
    best=max(v for v,_ in values)
    hits=[idx for v,idx in values if abs(v-best)<1.e-9]
    expected=chord_max_and_count(n)[0]
    assert abs(best-expected)<1.e-8,(n,best,expected)
    count=(2*(n//4) if n%4==0 else 2*n if n%2 else 3*n) if n>=4 else 12
    assert len(hits)==count,(n,len(hits),count)
    return len(values)


def run():
    tot=0
    for n in range(3,21):
        tot+=tetra_full_check(n)
    for n in range(21,49):
        chord_max_and_count(n)
    print('PRISM_TETRAHEDRON_CHECK_OK tetra_subsets=',tot,'tested_orders=',46)

if __name__=='__main__':run()

# Endpoint-supported optimizer-cell dimension check. This is finite diagnostic
# evidence only; the proof for every n uses balanced gap vectors.
def cell_dimension_check():
    from itertools import product
    for n in range(4,18):
        choices=set()
        for a,b,c,d in combinations(range(n),4):
            g=(b-a,c-b,d-c,n-d+a)
            if max(g)-min(g)==(0 if n%4==0 else 1):
                choices.add((frozenset((a,c)),frozenset((b,d))))
                choices.add((frozenset((b,d)),frozenset((a,c))))
        best=0
        for bot,top in choices:
            indices=tuple(sorted(bot))+tuple(sorted(top))
            for free in product((0,1),repeat=4):
                if sum(free)<=best: continue
                valid=True
                for endpoints in product(*((0,1) if enabled else (0,) for enabled in free)):
                    v=[(indices[i]+endpoints[i])%n for i in range(4)]
                    if (frozenset(v[:2]),frozenset(v[2:])) not in choices:
                        valid=False; break
                if valid:best=sum(free)
        expected=(0 if n%4==0 else 2 if n%4==2 else 1)
        assert best==expected,(n,best,expected)
    print('OPTIMIZER_FACE_DIMENSION_OK orders=14')

if __name__=='__main__':
    cell_dimension_check()
