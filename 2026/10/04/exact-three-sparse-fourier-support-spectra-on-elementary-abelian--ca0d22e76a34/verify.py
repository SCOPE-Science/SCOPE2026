#!/usr/bin/env python3
from itertools import combinations, product

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def scale(a,n): return tuple(n*x for x in a)
def zeta(p,e):
    v=[0]*p; v[e%p]=1; return tuple(v)
def shift(a,k):
    p=len(a); k%=p
    out=[0]*p
    for i,x in enumerate(a): out[(i+k)%p]+=x
    return tuple(out)
def iszero(a): return all(x==a[0] for x in a)
def isum(*xs):
    z=(0,)*len(xs[0])
    for x in xs: z=add(z,x)
    return z

def local_col(p,u,v,coeffs):
    vals=[]
    for t in range(p):
        a,b,c=coeffs
        vals.append(isum(a,shift(b,u*t),shift(c,v*t)))
    return sum(iszero(x) for x in vals)

def local_plane(p,coeffs):
    out=0
    a,b,c=coeffs
    for x in range(p):
        for y in range(p):
            if iszero(isum(a,shift(b,x),shift(c,y))): out+=1
    return out

def const(p,n): return scale(zeta(p,0),n)

def run():
    checked_col=checked_plane=box_cases=0
    for p in (3,5,7,11):
        # Every normalized collinear support {0,u,v}.
        for u,v in combinations(range(1,p),2):
            w0=(const(p,3),const(p,1),const(p,1))
            w1=(const(p,-2),const(p,1),const(p,1))
            # (zeta^u-zeta^v, zeta^v-1, -(zeta^u-1))
            w2=(add(zeta(p,u),neg(zeta(p,v))), add(zeta(p,v),neg(zeta(p,0))), neg(add(zeta(p,u),neg(zeta(p,0)))))
            assert [local_col(p,u,v,w) for w in (w0,w1,w2)]==[0,1,2]
            checked_col+=1
            # Exact finite coefficient-box corroboration of the <=2 bound.
            for aa,bb,cc in product((-2,-1,1,2), repeat=3):
                z=local_col(p,u,v,(const(p,aa),const(p,bb),const(p,cc)))
                assert z<=2
                box_cases+=1
        # Noncollinear normalized support {0,e1,e2}.
        w0=(const(p,3),const(p,1),const(p,1))
        w1=(const(p,-2),const(p,1),const(p,1))
        w2=(zeta(p,1), neg(add(zeta(p,0),zeta(p,1))), const(p,1))
        assert [local_plane(p,w) for w in (w0,w1,w2)]==[0,1,2]
        checked_plane+=1
        for aa,bb,cc in product((-2,-1,1,2), repeat=3):
            assert local_plane(p,(const(p,aa),const(p,bb),const(p,cc)))<=2
            box_cases+=1
        for d in (2,3,5):
            assert sorted({(p-j)*p**(d-1) for j in (0,1,2)}) == sorted([(p-2)*p**(d-1),(p-1)*p**(d-1),p**d])
            assert sorted({(p*p-j)*p**(d-2) for j in (0,1,2)}) == sorted([p**d-p**(d-2),p**d-2*p**(d-2),p**d])
    print(f"collinear_supports={checked_col} plane_types={checked_plane} exact_box_cases={box_cases}")
    print("VERIFY_OK")

if __name__=='__main__': run()
