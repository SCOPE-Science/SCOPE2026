#!/usr/bin/env python3
"""Exact projective-join/meet closure from a point frame over prime fields."""

def normalize(v, p):
    v = tuple(x % p for x in v)
    if not any(v):
        raise ValueError('zero vector')
    inv = pow(next(x for x in v if x), -1, p)
    return tuple(x*inv % p for x in v)


def cross(a, b, p):
    return normalize((a[1]*b[2]-a[2]*b[1],
                      a[2]*b[0]-a[0]*b[2],
                      a[0]*b[1]-a[1]*b[0]), p)


def all_pts(p):
    return {normalize((x,y,z),p) for x in range(p) for y in range(p)
            for z in range(p) if (x,y,z)!=(0,0,0)}


def close_frame(p):
    pts = {normalize(x,p) for x in ((1,0,0),(0,1,0),(0,0,1),(1,1,1))}
    lines = set()
    rounds = 0
    while True:
        np = set(pts)
        nl = set(lines)
        pv = sorted(pts)
        for i, a in enumerate(pv):
            for b in pv[i+1:]:
                nl.add(cross(a,b,p))
        lv = sorted(nl)
        for i, a in enumerate(lv):
            for b in lv[i+1:]:
                np.add(cross(a,b,p))
        rounds += 1
        if np == pts and nl == lines:
            return pts, lines, rounds
        pts, lines = np, nl

if __name__=='__main__':
    for p in (2,3,5,7,11,13):
        pts, lines, rounds = close_frame(p)
        allp = all_pts(p)
        assert pts == allp and lines == allp
        print(f'PASS p={p} closure_points={len(pts)} closure_lines={len(lines)} '
              f'construction_passes={rounds}')
    print('VERIFY_CLOSURE_OK')
