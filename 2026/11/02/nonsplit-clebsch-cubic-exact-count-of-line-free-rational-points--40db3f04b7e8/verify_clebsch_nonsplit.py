"""Exact elementary checks for the Clebsch cubic's nonsplit line-avoidance formula."""
from itertools import combinations, permutations, product
from fractions import Fraction


def coordinate_lines():
    out=[]
    for s in range(5):
        rem=[j for j in range(5) if j!=s]
        for a,b in combinations(rem,2):
            c,d=[j for j in rem if j not in (a,b)]
            if a<c:
                out.append((s,a,b,c,d))
    assert len(out)==15
    return out


def canonical(v,p):
    inv=pow(next(x for x in v if x%p), -1,p)
    return tuple((x*inv)%p for x in v)


def pts_on_coordinate_line(L,p):
    s,a,b,c,d=L
    points=[]
    for u in range(p):
        v=[0]*5
        v[a]=1;v[b]=-1;v[c]=u;v[d]=-u
        points.append(canonical(v,p))
    v=[0]*5;v[c]=1;v[d]=-1
    points.append(canonical(v,p))
    return set(points)


def rational_surface_points(p):
    result=set()
    for z in range(4):
        for tail in product(range(p),repeat=3-z):
            v=(0,)*z+(1,)+tail
            v=v+((-sum(v))%p,)
            if sum(x**3 for x in v)%p==0:
                result.add(v)
    return result


def rank_Q(rows):
    mat=[[Fraction(x) for x in r] for r in rows]
    m,n=len(mat),len(mat[0]);r=0
    for j in range(n):
        ii=next((i for i in range(r,m) if mat[i][j]),None)
        if ii is None:continue
        mat[ii],mat[r]=mat[r],mat[ii]
        q=mat[r][j]
        mat[r]=[a/q for a in mat[r]]
        for i in range(r+1,m):
            if mat[i][j]:
                q=mat[i][j]
                mat[i]=[a-q*b for a,b in zip(mat[i],mat[r])]
        r+=1
        if r==m:break
    return r


def verify():
    ls=coordinate_lines()
    for p in [7,11,13,17,19]:
        sets=[pts_on_coordinate_line(l,p) for l in ls]
        union=set.union(*sets)
        mult={v:sum(v in Z for Z in sets) for v in union}
        assert sorted({m for m in mult.values()})==[1,2,3]
        assert sum(m==2 for m in mult.values())==15
        assert sum(m==3 for m in mult.values())==10
        assert len(union)==15*p-20
        surf=rational_surface_points(p)
        assert union<=surf
        expected=p*p+(5 if p%5 in (2,3) else 7)*p+1
        assert len(surf)==expected
        if p%5 in (2,3):
            assert len(surf-union)==(p-3)*(p-7)
        print(f'q={p}: surface={len(surf)}, fixed_line_union={len(union)}, off_fixed={len(surf-union)}')
    p=7
    sets=[pts_on_coordinate_line(l,p) for l in ls]
    G=[[(-1 if i==j else int(bool(sets[i]&sets[j]))) for j in range(15)] for i in range(15)]
    assert rank_Q(G)==6
    assert [sum(G[i][j] for j in range(15)) for i in range(15)]==[5]*15  # each line meets six of the other fifteen
    print('COORDINATE_LINE_INTERSECTION_GRAM_RANK=6')

    # The split case p=11: the twelve remaining lines really are the S5 orbit
    # of the two-dimensional span of the Fourier characters +1 and -1.
    p=11;root=3
    assert pow(root,5,p)==1 and root!=1
    f=[[pow(root,k*j,p) for j in range(5)] for k in (1,4)]
    special=set()
    for perm in permutations(range(5)):
        a=[f[0][j] for j in perm];b=[f[1][j] for j in perm]
        pts=set()
        for t in range(p):
            pts.add(canonical([a[j]+t*b[j] for j in range(5)],p))
        pts.add(canonical(b,p))
        assert len(pts)==p+1
        special.add(frozenset(pts))
    assert len(special)==12
    combined=set.union(*[set(x) for x in special], *[pts_on_coordinate_line(x,p) for x in ls])
    assert combined==rational_surface_points(11)
    print('SPLIT_CASE_FOURIER_LINES=12; ALL_27_LINES_COVER_F11_SURFACE')
    print('VERIFY_OK')

if __name__=='__main__':verify()
