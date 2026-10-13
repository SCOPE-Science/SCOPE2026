"""Finite-field spot checks for a plane-filling pencil's rational singularities.

This is independent finite evidence, not a replacement for the general proof.
Only prime fields are enumerated.  No third-party dependencies are needed.
"""
from math import comb, gcd

PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43, 71, 113)

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1

def f(p,k,x,y,z):
    return (x*x*(pow(x,p,p)*y-x*pow(y,p,p))+
            y*y*(pow(y,p,p)*z-y*pow(z,p,p))+
            (z*z+k*x*x)*(pow(z,p,p)*x-z*pow(x,p,p))) % p

def grad(p,k,x,y,z):
    return ((2*pow(x,p+1,p)*y-3*x*x*pow(y,p,p)+
             2*k*x*(pow(z,p,p)*x-z*pow(x,p,p))+
             (z*z+k*x*x)*pow(z,p,p)) % p,
            (pow(x,p+2,p)+2*pow(y,p+1,p)*z-
             3*y*y*pow(z,p,p)) % p,
            (pow(y,p+2,p)+2*z*(pow(z,p,p)*x-z*pow(x,p,p))-
             (z*z+k*x*x)*pow(x,p,p)) % p)

def jet(p,k,a,b):
    # Coefficients of F_k(a+u,b+v,1), through total degree three.
    out = {}
    def term(i,j,c):
        for r in range(min(i,3)+1):
            for s in range(min(j,3-r)+1):
                out[r,s] = (out.get((r,s),0) + c*comb(i,r)*comb(j,s)*
                            pow(a,i-r,p)*pow(b,j-s,p)) % p
    term(p+2,1,1); term(3,p,-1)
    term(0,p+2,1); term(0,3,-1)
    term(1,0,1); term(p,0,-1)
    term(3,0,k); term(p+2,0,-k)
    return out

for p in PRIMES:
    cusps = nodes = split = nonsplit = 0
    by_k = {k: set() for k in range(p)}
    for t in range(1,p):
        a,b = pow(t,2,p),pow(t,3,p)
        # Formula k=t^3-t^{-4}; negative powers always modular inverse.
        k = (pow(t,3,p)-pow(pow(t,4,p),-1,p))%p
        by_k[k].add((a,b))
        assert f(p,k,a,b,1)==0 and grad(p,k,a,b,1)==(0,0,0)
        T=jet(p,k,a,b)
        assert T.get((0,0),0)==T.get((1,0),0)==T.get((0,1),0)==0
        A,B,C=(T.get((2,0),0),T.get((1,1),0),T.get((0,2),0))
        assert (A,B,C)==((-2*pow(t,-2,p))%p,(2*pow(t,4,p))%p,(-2*pow(t,3,p))%p)
        disc=(B*B-4*A*C)%p
        assert disc == 4*t*(pow(t,7,p)-4)%p
        if disc==0:
            cusps+=1
            assert (256*pow(k,7,p)-pow(3,7,p))%p==0
            slope=t*pow(2,-1,p)%p
            cubic=sum(T.get((3-j,j),0)*pow(slope,j,p) for j in range(4))%p
            assert cubic==pow(2,-1,p)*pow(t,-4,p)%p
        else:
            nodes+=1
            if legendre(disc,p)==1: split+=1
            else: nonsplit+=1
    c=sum(pow(t,7,p)==4%p for t in range(1,p))
    S=sum(legendre(t*(pow(t,7,p)-4),p) for t in range(1,p))
    assert cusps==c and nodes==p-1-c
    assert split==(p-1-c+S)//2 and nonsplit==(p-1-c-S)//2
    if gcd(7,p-1)==1:
        assert (cusps,split,nonsplit)==(1,(p-3)//2,(p-1)//2)
    else:
        # Even-degree monic hyperelliptic model has two rational infinities.
        affine_count=sum(1+legendre(t*(pow(t,7,p)-4),p) for t in range(p))
        assert affine_count+2==p+2+S
    if p<=19:
        # Exhaustive full projective singular support, including infinity.
        for k in range(p):
            actual=set()
            for x in range(p):
                for y in range(p):
                    if f(p,k,x,y,1)==0 and grad(p,k,x,y,1)==(0,0,0):
                        actual.add((x,y))
            for y in range(p):
                assert grad(p,k,1,y,0)!=(0,0,0)
            assert grad(p,k,0,1,0)!=(0,0,0)
            assert actual==by_k[k],(p,k,actual,by_k[k])
    print(f"p={p}: cusp={c}, split_nodes={split}, nonsplit_nodes={nonsplit}, S={S}")
print('VERIFY_OK: rational node/cusp, branch splitting, and finite-field census tests')
