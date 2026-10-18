"""Modular chain-complex verification of the dihedral character for cycle independence complexes.

This independently constructs augmented simplicial boundary matrices and computes
traces on boundary spaces by sparse reduced-echelon linear algebra. The field
characteristic is larger than every group order tested; finite-field agreement
is a consistency test, not a proof of the integral infinite-family theorem.
"""
from itertools import combinations
from math import gcd

P = 1_000_003


def faces(n):
    out = {}
    for size in range(n + 1):
        out[size] = [f for f in combinations(range(n), size)
                     if all((abs(a - b) not in (1, n-1)) for a, b in combinations(f, 2))]
        if not out[size] and size > 0:
            break
    return out


def eliminate(a, b, scalar):
    for k, v in b.items():
        val = (a.get(k, 0) - scalar * v) % P
        if val:
            a[k] = val
        else:
            a.pop(k, None)


def echelon_basis(columns):
    basis = {}
    for col in columns:
        v = dict(col)
        for p in sorted(basis):
            c = v.get(p, 0)
            if c:
                eliminate(v, basis[p], c)
        if not v:
            continue
        p = min(v)
        scale = pow(v[p], P-2, P)
        v = {i:(a*scale)%P for i, a in v.items()}
        for bp, bv in basis.items():
            if v_p := bv.get(p, 0):
                eliminate(bv, v, v_p)
        basis[p] = v
        for q,bv in basis.items():
            assert bv[q] == 1 and all(bv.get(o,0)==0 for o in basis if o!=q)
    return basis


def parity(values):
    return -1 if sum(a > b for i,a in enumerate(values) for b in values[i+1:])%2 else 1


def transform_face(n, f, j, reflect):
    mapped = [((j-v) if reflect else (j+v)) % n for v in f]
    return tuple(sorted(mapped)), parity(mapped)


def boundary_columns(faces_by_size, s):
    if s == 0:
        return []
    lower = {face:i for i,face in enumerate(faces_by_size[s-1])}
    columns = []
    for face in faces_by_size[s]:
        col = {}
        for j in range(s):
            lower_face = face[:j] + face[j+1:]
            col[lower[lower_face]] = (1 if j%2 == 0 else P-1)
        columns.append(col)
    return columns


def image_trace(n, faces_by_size, basis, s, j, reflect):
    """Trace on im(boundary from s-sets to (s-1)-sets)."""
    if not basis:
        return 0
    lower = faces_by_size[s-1]
    lower_index = {f:i for i, f in enumerate(lower)}
    total = 0
    for p, vec in basis.items():
        image = {}
        for i, val in vec.items():
            moved, sign = transform_face(n,lower[i],j,reflect)
            q = lower_index[moved]
            image[q] = (image.get(q,0)+sign*val)%P
        # Basis vectors are reduced at all other pivot positions.
        for z,bvec in basis.items():
            if z == p:
                total += image.get(p,0)
        # Image belongs to the boundary space.
        residual = dict(image)
        for z,bvec in basis.items():
            if c:=residual.get(z,0):
                eliminate(residual,bvec,c)
        assert not residual,(n,s,j,reflect,len(residual))
    return total%P


def chain_trace(n, fset, j, reflect):
    return sum(sign for f in fset
               for mapped,sign in [transform_face(n,f,j,reflect)]
               if mapped==f)%P


def pred(n,j,refl):
    sign=(-1)**(((n-2)//3)+1)
    if not refl:
        g=gcd(n,j)
        if g==1:
            return sign
        return sign*([2,1,-1,-2,-1,1][g%6])
    def pf(k):
        a,b=1,0
        for _ in range(2,k+1):a,b=b,b-a
        return a if k==0 else b
    if n%2:
        return sign*pf((n-1)//2)
    if j%2:
        return sign*pf(n//2-2)
    return sign*pf(n//2+1)


def test(n):
    f=faces(n)
    max_size=max(f)
    boundary={s:echelon_basis(boundary_columns(f,s)) for s in range(1,max_size+1)}
    rank={s:len(b) for s,b in boundary.items()}
    Betti={s-1:len(f[s])-rank.get(s,0)-rank.get(s+1,0) for s in range(max_size+1)}
    expect={(n-2)//3:2 if n%3==0 else 1}
    assert {k:v for k,v in Betti.items() if v}==expect, (n,Betti)
    for reflect in (False,True):
        for j in range(n):
            for s in range(max_size+1):
                ct=chain_trace(n,f[s],j,reflect)
                down=image_trace(n,f,boundary.get(s,{}),s,j,reflect) if s>0 else 0
                up=image_trace(n,f,boundary.get(s+1,{}),s+1,j,reflect) if s+1<=max_size else 0
                hc=(ct-down-up)%P
                expected=(pred(n,j,reflect) if s-1==(n-2)//3 else 0)%P
                assert hc==expected,(n,j,reflect,s,hc,expected)
    return sum(len(v) for v in f.values()),sum(rank.values())


def main():
    for n in range(3,13):
        f,r=test(n)
        print('CHAIN_CASE',n,'faces',f,'rank_sum',r,'group_elements',2*n)
    print('CHAIN_REPRESENTATIONS_OK')

if __name__=='__main__':
    main()
