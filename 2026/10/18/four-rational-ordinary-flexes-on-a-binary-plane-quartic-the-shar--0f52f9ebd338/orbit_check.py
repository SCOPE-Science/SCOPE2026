#!/usr/bin/env python3
"""Exact PGL3(F2) orbit and four-cap incidence check for binary quartics."""
from itertools import product
from collections import Counter
from check_flexes import MON, TANGENTS, smooth
MON_INDEX={m:i for i,m in enumerate(MON)}

def times(a,b):
    out=set()
    for x in a:
        for y in b:
            z=tuple(x[i]+y[i] for i in range(3))
            if z in out:out.remove(z)
            else:out.add(z)
    return out

def mon_image(m,columns):
    p={(0,0,0)}
    for i,e in enumerate(m):
        f={tuple(int(j==k) for j in range(3)) for k in range(3) if columns[i]>>k&1}
        for _ in range(e):p=times(p,f)
    return sum(1<<MON_INDEX[w] for w in p)

def transform(f,columns):
    masks=[mon_image(m,columns) for m in MON]
    return __import__('functools').reduce(lambda v,j:v^(masks[j] if f>>j&1 else 0),range(15),0)

def ordinary_flex_points(f):
    pts=[]
    for p,others in TANGENTS:
        if any(all((f&row).bit_count()%2==int(k==3) for k,row in enumerate(rows)) for q,rows in others):pts.append(p)
    return tuple(pts)

if __name__=='__main__':
    gens=((3,2,4),(2,4,1))
    orbit={4418};queue=[4418]
    for f in queue:
        for g in gens:
            z=transform(f,g)
            if z not in orbit:orbit.add(z);queue.append(z)
    assert len(orbit)==168
    assert all(smooth(f) and len(ordinary_flex_points(f))==4 for f in orbit)
    # Every rational point is one of the four ordinary flexes.
    def on_curve(f,p):
        return sum((f>>i&1) for i,m in enumerate(MON) if all(e==0 or (p>>j&1) for j,e in enumerate(m)))%2==0
    assert all(tuple(p for p in range(1,8) if on_curve(f,p))==ordinary_flex_points(f) for f in orbit)
    caps=Counter(ordinary_flex_points(f) for f in orbit)
    assert len(caps)==7 and set(caps.values())=={24},caps
    for cap in caps:
        assert all(p^q not in cap for i,p in enumerate(cap) for q in cap[i+1:])
    print('ORBIT_SIZE',len(orbit))
    print('FOUR_CAPS',len(caps),'CURVES_PER_CAP',sorted(set(caps.values())))
    print('ALL_ORBIT_CURVES_GEOMETRICALLY_SMOOTH_AND_FOUR_FLEX',True)
    print('SUCCESS')
