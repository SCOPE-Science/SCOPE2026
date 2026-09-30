from itertools import combinations, permutations


def predicted(r, dx, ax, dy, ay):
    sx = dx>=r or ax>=r-1
    sy = dy>=r or ay>=r-1
    bx = dx==r-1 and ax<=r-2
    by = dy==r-1 and ay<=r-2
    return sx or sy or (bx and by)


def direct(r, dx, ax, dy, ay):
    # Initial colors are globally distinct; xy is a nonedge, so endpoint initial-color sets are disjoint.
    Dx=tuple(range(dx)); Dy=tuple(range(dx,dx+dy)); D=Dx+Dy
    # Complement edges: ax previous at x, ay previous at y, then current c.
    K=ax+ay+1
    edges=list(range(K))
    cur=K-1
    # Enumerate all collision patterns: a complement color either equals one distinct initial color,
    # or is a unique fresh color. Fresh identities are irrelevant.
    for j in range(min(K,len(D))+1):
        for matched_edges in combinations(edges,j):
            matched_edges=set(matched_edges)
            for toks in permutations(D,j):
                assign={e:t for e,t in zip(sorted(matched_edges),toks)}
                fresh_base=1000
                for e in edges:
                    if e not in assign:
                        assign[e]=fresh_base+e
                X=set(Dx)
                for e in range(ax): X.add(assign[e])
                X.add(assign[cur])
                Y=set(Dy)
                for e in range(ax,ax+ay): Y.add(assign[e])
                Y.add(assign[cur])
                if len(X)<r and len(Y)<r:
                    return False
    return True

for r in range(2,5):
    checked=0
    for dx in range(r+1):
      for ax in range(r):
       for dy in range(r+1):
        for ay in range(r):
            p=predicted(r,dx,ax,dy,ay)
            d=direct(r,dx,ax,dy,ay)
            checked+=1
            if p!=d:
                raise SystemExit(f'MISMATCH r={r} dx={dx} ax={ax} dy={dy} ay={ay} pred={p} direct={d}')
    print(f'r={r}: {checked} endpoint-state quadruples checked; criterion exact')
print('LOCAL_CRITERION_OK')
