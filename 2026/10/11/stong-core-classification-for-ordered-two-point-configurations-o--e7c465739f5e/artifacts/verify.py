#!/usr/bin/env python3
from itertools import product


def base_points(p,q):
    return [('a',i) for i in range(p)] + [('b',j) for j in range(q)]

def base_le(x,y):
    return x == y or (x[0] == 'a' and y[0] == 'b')

def make_F2(p,q):
    B=base_points(p,q)
    pts=[(x,y) for x in B for y in B if x != y]
    def le(u,v):
        return base_le(u[0],v[0]) and base_le(u[1],v[1])
    return pts,le

def beat_kind(x,active,le):
    up=[y for y in active if y != x and le(x,y)]
    dn=[y for y in active if y != x and le(y,x)]
    up_min=[z for z in up if all(le(z,y) for y in up)]
    dn_max=[z for z in dn if all(le(y,z) for y in dn)]
    return bool(up_min), bool(dn_max)

def classify(p,q):
    pts,le=make_F2(p,q)
    out={}
    for x in pts:
        out[x]=beat_kind(x,pts,le)
    return pts,le,out

def typ(x):
    return x[0][0]+x[1][0]

def expected_beat(p,q,x):
    if typ(x) not in ('ab','ba'):
        return (False,False)
    return (q==2,p==2)  # (up,down)

def verify_case(p,q):
    pts,le,b=classify(p,q)
    assert len(pts)==(p+q)*(p+q-1)
    for x,k in b.items():
        assert k==expected_beat(p,q,x),(p,q,x,k,expected_beat(p,q,x))
    active=list(pts)
    # For p=2 use all mixed points as down beats; otherwise, if q=2, as up beats.
    if p==2:
        mixed=[x for x in list(active) if typ(x) in ('ab','ba')]
        for x in mixed:
            up,down=beat_kind(x,active,le)
            assert down,(p,q,x,'lost down-beat status')
            active.remove(x)
        AA=[x for x in active if typ(x)=='aa']
        BB=[x for x in active if typ(x)=='bb']
        assert len(AA)==2
        assert len(BB)==q*(q-1)
        assert len(active)==2+q*(q-1)
        for a in AA:
            for z in BB:
                assert le(a,z)
        for x in active:
            assert beat_kind(x,active,le)==(False,False)
    elif q==2:
        mixed=[x for x in list(active) if typ(x) in ('ab','ba')]
        for x in mixed:
            up,down=beat_kind(x,active,le)
            assert up,(p,q,x,'lost up-beat status')
            active.remove(x)
        AA=[x for x in active if typ(x)=='aa']
        BB=[x for x in active if typ(x)=='bb']
        assert len(AA)==p*(p-1)
        assert len(BB)==2
        assert len(active)==p*(p-1)+2
        for a in AA:
            for z in BB:
                assert le(a,z)
        for x in active:
            assert beat_kind(x,active,le)==(False,False)
    else:
        assert all(k==(False,False) for k in b.values())
        assert len(active)==(p+q)*(p+q-1)
    return len(pts),len(active)

rows=[]
for p in range(2,9):
    for q in range(2,9):
        rows.append((p,q,*verify_case(p,q)))
print('VERIFY_OK cases=%d range=2..8 theorem=beat_classification_and_core_formula' % len(rows))
print('samples=' + ';'.join('%dx%d:%d->%d'%r for r in rows if r[0:2] in [(2,2),(2,5),(3,3),(3,6),(5,2),(6,6)]))
