"""Exact-rational reproducibility checks for the Sel'kov max-plus survival polygon.

Only finite certificates are checked here; the infinite-time area and exit laws
follow from the matrix identity and the induction in RESULT.md.
"""
from fractions import Fraction as Q

A = ((Q(2), Q(1)), (Q(-2), Q(0)))
I = ((Q(1), Q(0)), (Q(0), Q(1)))


def mm(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def mv(a, v):
    return tuple(sum(a[i][k]*v[k] for k in range(2)) for i in range(2))


def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]


def area2(verts):
    return sum(cross(verts[i], verts[(i+1)%len(verts)]) for i in range(len(verts)))


def rows(n):
    p=I
    ans=[]
    for _ in range(n+1):
        ans.append(p[0]);p=mm(p,A)
    return ans


def polygon(n,B=Q(1)):
    """Intersect halfplanes r_j dot u >= -B by enumerating exact vertices."""
    h=rows(n)
    vs=set()
    for i,(a,b) in enumerate(h):
        for c,d in h[i+1:]:
            den=a*d-b*c
            if not den:
                continue
            x=B*(b-d)/den
            y=B*(c-a)/den
            if all(p*x+q*y>=-B for p,q in h):
                vs.add((x,y))
    if not vs:
        raise AssertionError('no vertices')
    center=(sum(x for x,y in vs)/len(vs), sum(y for x,y in vs)/len(vs))
    import functools
    def cmp(v,w):
        a=(v[0]-center[0],v[1]-center[1]);b=(w[0]-center[0],w[1]-center[1])
        def half(z): return 0 if z[1]>0 or z[1]==0 and z[0]>=0 else 1
        ha,hb=half(a),half(b)
        if ha!=hb:return -1 if ha<hb else 1
        c=cross(a,b)
        return -1 if c>0 else (1 if c<0 else 0)
    ordered=sorted(vs,key=functools.cmp_to_key(cmp))
    assert area2(ordered)>0
    return ordered


if __name__=='__main__':
    p=I
    for _ in range(8): p=mm(p,A)
    assert p==((Q(16),Q(0)),(Q(0),Q(16)))
    assert rows(7)==[(Q(1),Q(0)),(Q(2),Q(1)),(Q(2),Q(2)),(Q(0),Q(2)),(Q(-4),Q(0)),(Q(-8),Q(-4)),(Q(-8),Q(-8)),(Q(0),Q(-8))]
    expected={(Q(-1),Q(9,8)),(Q(-1),Q(1)),(Q(-1,2),Q(0)),(Q(0),Q(-1,2)),(Q(1,4),Q(-1,2)),(Q(1,4),Q(-1,4)),(Q(1,8),Q(0))}
    assert set(polygon(6))==expected
    assert area2(polygon(6))==Q(79,64)
    assert area2(polygon(5))==Q(5,2)
    inv=((Q(0),Q(-1,2)),(Q(1),Q(1)))
    assert mm(inv,A)==I
    for n in range(6,19):
        v=polygon(n)
        assert area2(v)==Q(79,64)*Q(1,2)**(n-6)
        next_v=set(polygon(n+1))
        assert {mv(inv,x) for x in v}==next_v,(n, v, next_v)
    for B in [Q(1,7),Q(1),Q(11,3)]:
        assert set(polygon(6,B))=={(B*x,B*y) for x,y in expected}
        assert area2(polygon(6,B))==Q(79,64)*B*B
    witness=(Q(-11,10),Q(121,100))
    assert all(a*witness[0]+b*witness[1]>-1 for a,b in rows(6)[1:])
    assert witness[0]<=-1
    assert {mv(inv,x) for x in polygon(5)} != set(polygon(6))
    # Test strict branch predicates against their centered halfplanes.
    for u in [(Q(0),Q(0)),(Q(1,10),Q(-1,10)),(Q(3,4),Q(1,4)),(Q(-1,4),Q(0))]:
        x,y=Q(1)+u[0],-Q(1)+u[1]
        stay=True
        for j in range(16):
            stay=stay and x>0
            if j in (7,8,12,15):
                assert stay==all(a*u[0]+b*u[1]>-1 for a,b in rows(j))
            oldx=x
            x=y+max(Q(0),2*x)
            y=Q(1)-max(Q(0),2*oldx)
    print('EXACT_SELVKOV_SURVIVOR_CERTIFICATE_OK')
