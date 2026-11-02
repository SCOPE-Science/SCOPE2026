"""Independent exact checks for total mutual-visibility counting in three-factor Hamming graphs.

Run with Python 3.9+ standard library: python verify.py
"""
from functools import lru_cache
from itertools import product, combinations, permutations
from math import comb
from random import Random


def add_shift(dst, src, factor, shift):
    for j, v in enumerate(src):
        if j + shift >= len(dst):
            dst.extend([0] * (j + shift + 1 - len(dst)))
        dst[j + shift] += factor * v


@lru_cache(None)
def coefficients(a, b, c):
    if min(a, b, c) == 0:
        return (1,)
    ans = list(coefficients(a - 1, b, c))
    for length in range(1, a + 1):
        add_shift(ans, coefficients(a-length, b-1, c-1),
                  comb(a-1, length-1) * b * c, length)
    for length in range(2, b + 1):
        add_shift(ans, coefficients(a-1, b-length, c-1),
                  comb(b, length) * c, length)
    for length in range(2, c + 1):
        add_shift(ans, coefficients(a-1, b-1, c-length),
                  b * comb(c, length), length)
    while len(ans) > 1 and ans[-1] == 0:
        ans.pop()
    return tuple(ans)


def exhaustive_distance_two(a,b,c):
    vertices = list(product(range(a),range(b),range(c)))
    n = len(vertices)
    forbidden = [0]*n
    for i in range(n):
        for j in range(i+1,n):
            if sum(x!=y for x,y in zip(vertices[i],vertices[j]))==2:
                forbidden[i] |= 1 << j
                forbidden[j] |= 1 << i
    # Independent-set enumerator by branching on least-index vertex.
    @lru_cache(None)
    def poly(mask):
        if not mask:
            return (1,)
        bit = mask & -mask
        i = bit.bit_length()-1
        rem = mask^bit
        x = poly(rem)
        y = poly(rem & ~forbidden[i])
        res = [0]*max(len(x),len(y)+1)
        for k,v in enumerate(x): res[k]+=v
        for k,v in enumerate(y): res[k+1]+=v
        while len(res)>1 and res[-1]==0: res.pop()
        return tuple(res)
    return poly((1<<n)-1),poly.cache_info()


def original_geodesic_property(vertices, chosen):
    # Reconstruct all shortest paths by permuting the coordinates where endpoints differ.
    # This verifies the definition without using the distance-two characterization.
    for u,v in combinations(vertices,2):
        delta = [i for i in range(3) if u[i]!=v[i]]
        possible = False
        for order in permutations(delta):
            cur = list(u)
            ok = True
            for axis in order[:-1]:
                cur[axis] = v[axis]
                if tuple(cur) in chosen:
                    ok = False
                    break
            if ok:
                possible=True
                break
        if not possible:
            return False
    return True


def check_original_small(a,b,c):
    vertices = list(product(range(a),range(b),range(c)))
    cnt = [0]*(len(vertices)+1)
    for mask in range(1<<len(vertices)):
        X={vertices[i] for i in range(len(vertices)) if mask>>i&1}
        if original_geodesic_property(vertices,X):
            cnt[len(X)]+=1
    while cnt and cnt[-1]==0:cnt.pop()
    assert tuple(cnt)==coefficients(a,b,c),(a,b,c,cnt,coefficients(a,b,c))
    return tuple(cnt)


def check_extrema():
    # All three factor sizes >=5: unique three-axis-component type.
    for a,b,c in [(5,5,5),(6,5,5),(7,6,5),(7,7,7)]:
        x=coefficients(a,b,c)
        assert len(x)-1==a+b+c-6,(a,b,c,len(x)-1)
        assert x[-1]==a*(a-1)*b*(b-1)*c*(c-1),(a,b,c,x[-1])
    # Thin third factor with other factors >=3.
    for a,b in [(3,3),(4,3),(5,5),(8,4)]:
        x=coefficients(a,b,2)
        assert len(x)-1==a+b-2,(a,b,x)
        assert x[-1]==2*a*b,(a,b,x[-1])
    # Boundary size four permits both two- and three-component optima.
    for a,b,c in [(4,4,4),(5,4,4),(6,5,4)]:
        x=coefficients(a,b,c)
        pairs=a*b*c*(c-1)
        if b==c:pairs+=a*c*b*(b-1)
        if a==b==c:pairs+=b*c*a*(a-1)
        expected=a*(a-1)*b*(b-1)*c*(c-1)+pairs
        assert len(x)-1==a+b-2 and x[-1]==expected,(a,b,c,x[-1],expected)


def main():
    print('BASE', coefficients(2,2,2), coefficients(2,2,3))
    for dims in [(2,2,2),(2,2,3)]:
        v=check_original_small(*dims)
        print('ORIGINAL_GEODESICS_OK',dims,len(v)-1,sum(v))
    for dims in [(2,2,2),(2,2,3),(2,3,3),(3,3,3),(3,3,4)]:
        p,stats=exhaustive_distance_two(*dims)
        assert p==coefficients(*dims),(dims,p,coefficients(*dims))
        print('DISTANCE_TWO_INDEPENDENT_SETS_OK',dims,len(p)-1,sum(p),stats)
    # Independent random geodesic and distance-two checks for larger small graphs.
    rng=Random(26047)
    for dims in [(2,3,3),(3,3,3)]:
        verts=list(product(*(range(d) for d in dims)))
        for t in range(200):
            chosen={v for v in verts if rng.randrange(3)==0}
            avoids=all(sum(x!=y for x,y in zip(u,v))!=2
                       for u,v in combinations(chosen,2))
            assert original_geodesic_property(verts,chosen)==avoids,(dims,chosen)
        print('GEODESIC_EQUIVALENCE_OK',dims)
    check_extrema()
    print('EXTREMAL_COUNTS_OK')
    print('VERIFY_OK')


if __name__=='__main__':main()
