"""Finite-extension geometric check of degree-three base-point orbits."""

def gf_mul(a,b,m,poly):
    val=0
    for i in range(m):
        if b & (1<<i): val ^= a<<i
    for i in range(2*m-2,m-1,-1):
        if val & (1<<i): val ^= poly<<(i-m)
    return val

def gf_pow(a,n,m,poly):
    x=1
    while n:
        if n&1:x=gf_mul(x,a,m,poly)
        a=gf_mul(a,a,m,poly)
        n>>=1
    return x

def det3(a,b,c,m,p):
    # determinant in characteristic two
    prod=lambda u,v,w:gf_mul(gf_mul(u,v,m,p),w,m,p)
    return (prod(a[0],b[1],c[2])^prod(a[0],b[2],c[1])^
            prod(a[1],b[0],c[2])^prod(a[1],b[2],c[0])^
            prod(a[2],b[0],c[1])^prod(a[2],b[1],c[0]))

def orbit_count(q):
    if q==2: m,poly=3,0b1011
    elif q==4:m,poly=6,0b1000011
    else:raise ValueError
    n=1<<m
    pts={(1,a,b) for a in range(n) for b in range(n)}|{(0,1,a) for a in range(n)}|{(0,0,1)}
    def proj(v):
        for lead in v:
            if lead:
                inv=gf_pow(lead,n-2,m,poly)
                return tuple(gf_mul(u,inv,m,poly) for u in v)
        raise AssertionError
    def frob(p): return proj(tuple(gf_pow(a,q,m,poly) for a in p))
    seen=set();tot=col=noncol=0
    for p in pts:
        if p in seen:continue
        p1=frob(p);p2=frob(p1)
        orbit={p,p1,p2}
        assert frob(p2)==p
        seen.update(orbit)
        if len(orbit)==1:continue
        tot+=1
        if det3(p,p1,p2,m,poly)==0:col+=1
        else:noncol+=1
    return n,len(pts),tot,col,noncol

if __name__=='__main__':
    for q in (2,4):
        n,pts,tot,col,noncol=orbit_count(q)
        formula=q**3*(q-1)**2*(q+1)//3
        print(f'q={q}: field F_{n}, points={pts}, degree3 closed points={tot}, collinear triples={col}, noncollinear triples={noncol}, expected={formula}')
        assert noncol==formula
