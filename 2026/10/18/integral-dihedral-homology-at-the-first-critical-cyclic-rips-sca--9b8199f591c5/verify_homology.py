"""Independent mod-2 homology and signed simplicial Lefschetz checks."""
from itertools import combinations


def faces_by_dimension(r):
    n=3*r
    faces={()}
    for i in range(n):
        window=tuple(sorted((i+j)%n for j in range(r+1)))
        for k in range(1,r+2):
            faces.update(combinations(window,k))
    for i in range(r):
        faces.add((i,i+r,i+2*r))
    layers={}
    for f in faces:
        layers.setdefault(len(f)-1,[]).append(f)
    for k in layers:layers[k].sort()
    return layers


def rank_gf2(columns):
    pivots={}
    for c in columns:
        while c:
            p=c.bit_length()-1
            if p not in pivots:
                pivots[p]=c
                break
            c^=pivots[p]
    return len(pivots)


def ranks(layers):
    result={}
    for k in sorted(layers):
        if k<0:continue
        previous={face:i for i,face in enumerate(layers[k-1])}
        result[k]=rank_gf2(sum(1<<previous[f[:j]+f[j+1:]] for j in range(len(f))) for f in layers[k])
    return result


def permutation_sign(arr):
    return -1 if sum(a>b for i,a in enumerate(arr) for b in arr[i+1:])%2 else 1


def lefschetz(layers,perm):
    value=-1  # reduced augmentation correction
    for dim,faces in layers.items():
        if dim<0:continue
        for face in faces:
            dest=[perm[v] for v in face]
            if set(dest)==set(face):
                value+=((-1)**dim)*permutation_sign(dest)
    return value


def check(r):
    n=3*r
    layers=faces_by_dimension(r)
    d=ranks(layers)
    assert all(d.get(k,0)<=len(layers.get(k-1,[])) for k in d)
    betti={k:len(layers[k])-d.get(k,0)-d.get(k+1,0) for k in layers if k>=0}
    assert {k:b for k,b in betti.items() if b}==({2:r-1} if r>1 else {}), ('homology',r,betti)
    for j in range(n):
        perm=[(x+j)%n for x in range(n)]
        observed=lefschetz(layers,perm)
        expected=(r if j%r==0 else 0)-1 if r>1 else 0
        assert observed==expected,('rotation',r,j,observed,expected)
        perm=[(j-x)%n for x in range(n)]
        observed=lefschetz(layers,perm)
        fixed=sum((2*i-j)%r==0 for i in range(r))
        expected=1-fixed if r>1 else 0
        assert observed==expected,('reflection',r,j,observed,expected)
    return (r,n,len(layers[0]),len(layers.get(2,[])),betti.get(2,0),2*n)

if __name__=='__main__':
    for r in range(1,7): print('GF2_AND_CHARACTER',check(r))
    print('VERIFY_HOMOLOGY_OK')
