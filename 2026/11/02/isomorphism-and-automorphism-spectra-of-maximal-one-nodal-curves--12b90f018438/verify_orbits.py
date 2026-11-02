from math import gcd

def orbit_counts(p, m):
    n=p-1
    if m==2:
        def step(v): return ((-v[0])%n,(-v[1])%n)
    elif m==4:
        def step(v): return ((-v[1])%n,v[0]%n)
    elif m==6:
        def step(v): return ((-v[1])%n,(v[0]+v[1])%n)
    else:raise ValueError(m)
    pts={(a,b) for a in range(n) for b in range(n) if (a,b)!=(0,0)}
    orbits=[]
    while pts:
        v=next(iter(pts));orbit=set();w=v
        for _ in range(m):
            orbit.add(w);w=step(w)
        assert w==v and orbit<=pts
        pts-=orbit;orbits.append(frozenset(orbit))
    if m==2: expected=(n*n+2)//2
    if m==4: expected=(n*n+4)//4
    if m==6: expected=(n*n+2)//6
    assert len(orbits)==expected, (p,m,len(orbits),expected)
    from collections import Counter
    aut_count=Counter(2*m//len(orbit) for orbit in orbits)
    if m==2:
        expected_aut={4:3,2:(n*n-4)//2}
    elif m==4:
        expected_aut={8:1,4:1,2:(n*n-4)//4}
    else:
        expected_aut={4:1,2:(n*n-4)//6}
    assert dict(aut_count)==expected_aut, (p,m,dict(aut_count),expected_aut)
    rational_elliptic_points=(p+1)**2
    degree_two_points=((p*p-1)**2-(p+1)**2)//2
    assert sum((m*rational_elliptic_points)//(2*m//len(o)) for o in orbits)==degree_two_points
    print(f'p={p}, m={m}, n={n}: {len(orbits)} orbits, sizes={dict(sorted(Counter(map(len,orbits)).items()))}')
    return orbits

for p,m in [(5,6),(7,4),(11,6),(11,4),(17,2),(19,2),(23,6),(23,4),(29,6),(31,4)]:
    if m==6: assert p%3==2
    if m==4: assert p%4==3
    orbit_counts(p,m)
print('VERIFY_OK')

def elliptic_counts_quad(p, d, a,b):
    # F_{p^2}=F_p[w]/(w^2-d), with d a nonsquare.
    residues={z*z%p for z in range(p)}
    assert d not in residues
    points=[(x,y) for x in range(p) for y in range(p)]
    def mul(u,v):
        return ((u[0]*v[0]+d*u[1]*v[1])%p, (u[0]*v[1]+u[1]*v[0])%p)
    def add(u,v):return ((u[0]+v[0])%p,(u[1]+v[1])%p)
    aa=(a,0);bb=(b,0)
    sqcount={}
    for y in points:
        yy=mul(y,y);sqcount[yy]=sqcount.get(yy,0)+1
    count=1
    for x in points:
        xx=mul(x,x)
        rhs=add(add(mul(xx,x),mul(aa,x)),bb)
        count+=sqcount.get(rhs,0)
    return count

for p,d,a,b in [(5,2,0,1),(7,3,-1,0),(11,2,0,1),(11,2,-1,0)]:
    c=elliptic_counts_quad(p,d,a,b)
    print(f'elliptic over F_{p*p}: y^2=x^3+({a})x+({b}): count={c}, bound={(p+1)**2}')
    assert c==(p+1)**2
print('FULL_VERIFY_OK')
