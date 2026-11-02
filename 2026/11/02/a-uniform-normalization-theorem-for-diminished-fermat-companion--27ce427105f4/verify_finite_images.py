"""Independent finite-field check for the companion morphism's boundary fibers.

Finite-field images cannot prove geometric birationality; this routine checks
coordinate formulas and uniqueness at ordinary prime-field boundary points.
"""
p=101
for m in range(3,8):
    d=2*m-1
    def map_image(a,b,c):
        A,B,C=pow(a,m,p),pow(b,m,p),pow(c,m,p)
        v=(pow(a,m-1,p)*(d*C-A),
           pow(b,m-1,p)*(B-d*C),
           pow(c,m-1,p)*(C-d*A),
           pow(c,m-1,p)*(d*B-C),
           d*pow(b,m-1,p)*(A-C),
           d*pow(a,m-1,p)*(C-B))
        v=tuple(x%p for x in v)
        assert any(v), (m,a,b,c)
        lead=next(z for z in v if z)
        inv=pow(lead,-1,p)
        return tuple(z*inv%p for z in v)
    # P^2(Fp): (1,b,c), (0,1,c), (0,0,1).
    buckets={}
    for b in range(p):
        for c in range(p):
            key=map_image(1,b,c)
            buckets.setdefault(key, []).append((1,b,c))
    for c in range(p):
        key=map_image(0,1,c)
        buckets.setdefault(key,[]).append((0,1,c))
    key=map_image(0,0,1)
    buckets.setdefault(key,[]).append((0,0,1))
    checked=0
    for t in range(1,p):
        if pow(t,m,p)==1: continue
        key=map_image(1,t,0)
        assert buckets[key]==[(1,t,0)], (m,t,buckets[key])
        checked+=1
    print('m',m,'boundary_unique_fibers',checked,'image_points',len(buckets))
print('FINITE_IMAGE_CHECK_OK')
