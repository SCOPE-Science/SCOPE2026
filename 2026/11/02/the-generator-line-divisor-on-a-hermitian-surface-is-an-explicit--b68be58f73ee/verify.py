"""Independent exact finite-field checks for the Hermitian generator divisor.
Runs with Python 3 standard library and no external resources.
"""
from itertools import combinations, product


def check(q):
    if q == 2:
        p, nonsquare = 2, 1  # a^2+a+1=0
        def plus(x, y): return x ^ y
        def times(x, y):
            a,b=x&1,x>>1
            c,d=y&1,y>>1
            return (a*c ^ b*d) | (((a*d ^ b*c ^ b*d)&1)<<1)
    elif q == 3:
        p, nonsquare = 3, 2  # a^2+1=0
        def plus(x, y):return ((x%3+y%3)%3) + 3*((x//3+y//3)%3)
        def times(x,y):
            a,b=x%3,x//3
            c,d=y%3,y//3
            return ((a*c+2*b*d)%3)+3*((a*d+b*c)%3)
    else:raise ValueError('Only small test fields implemented.')
    n=q*q
    def power(x,k):
        z=1
        while k:
            if k&1:z=times(z,x)
            x=times(x,x);k>>=1
        return z
    assert all(power(x,n)==x for x in range(n))
    def zero_sum(values):
        z=0
        for a in values:z=plus(z,a)
        return z==0
    # Every vector in F_(q^2)^4, normalized by leading coordinate 1.
    points=[]
    for lead in range(4):
        for tail in product(range(n),repeat=3-lead):
            v=tuple([0]*lead+[1]+list(tail))
            if zero_sum(power(x,q+1) for x in v):
                points.append(v)
    want_points=(q**3+1)*(q**2+1)
    assert len(points)==want_points,(q,len(points),want_points)
    # Enumerate all row-reduced 2 by 4 F_(q^2)-matrices.
    lines=[]
    for i,j in combinations(range(4),2):
        slots=[(r,c) for r,piv in enumerate((i,j)) for c in range(piv+1,4) if c not in (i,j)]
        for vals in product(range(n),repeat=len(slots)):
            uv=[[0]*4 for _ in range(2)]
            uv[0][i]=1;uv[1][j]=1
            for (r,c),z in zip(slots,vals):uv[r][c]=z
            u,v=uv
            # Hermitian isotropic iff three pairings vanish.
            if not zero_sum(power(x,q+1) for x in u):continue
            if not zero_sum(power(x,q+1) for x in v):continue
            if not zero_sum(times(power(x,q),y) for x,y in zip(u,v)):continue
            lines.append((u,v))
            # The second high-degree equation vanishes identically on this line.
            # Over F_(q^2), high Frobenius agrees with q-Frobenius.
            for s,t in product(range(n),repeat=2):
                coords=[plus(times(s,x),times(t,y)) for x,y in zip(u,v)]
                assert zero_sum(power(x,q**3+1) for x in coords)
    want_lines=(q+1)*(q**3+1)
    assert len(lines)==want_lines,(q,len(lines),want_lines)
    # Count the incidences at every rational point from all generator lines.
    def canon(v):
        lead=next(x for x in v if x)
        inv=power(lead,n-2)
        return tuple(times(inv,x) for x in v)
    counts={pt:0 for pt in points}
    for u,v in lines:
        line_pts={canon([plus(times(s,x),times(t,y)) for x,y in zip(u,v)])
                  for s,t in product(range(n),repeat=2) if s or t}
        assert len(line_pts)==n+1
        for pt in line_pts:counts[pt]+=1
    assert set(counts.values())=={q+1}
    degree=want_lines
    genus=1+degree*(q**3+q-2)//2
    assert genus=={2:109,3:1569}[q]
    print('q=%d FIELD=%d RATIONAL_POINTS=%d GENERATOR_LINES=%d GENERATORS_PER_POINT=%d DEGREE=%d ARITHMETIC_GENUS=%d' %
          (q,n,len(points),len(lines),q+1,degree,genus))

if __name__=='__main__':
    check(2)
    check(3)
    print('VERIFY_OK')
