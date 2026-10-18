"""Exhaustive finite-field checks for gcd/lcm cycle-algebra decomposition and division."""
from itertools import product
from math import gcd, lcm


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]


def valunit(n,p):
    v=0
    while n%p==0:
        v+=1;n//=p
    return v,n


def normalized_product(i,j,p):
    return (0,None) if valunit(i,p)[0] and valunit(j,p)[0] else (1,lcm(i,j))


def multiply(A,B,indices,p,q):
    pos={d:k for k,d in enumerate(indices)}
    z=[0]*len(indices)
    for i,a in zip(indices,A):
        if not a:continue
        for j,b in zip(indices,B):
            if not b:continue
            c,k=normalized_product(i,j,p)
            if c:z[pos[k]]=(z[pos[k]]+a*b)%q
    return tuple(z)


def phi(A,indices,p,m,q):
    a,u=valunit(m,p)
    divs=divisors(u)
    out=[]
    for r in divs:
        z=[0]*(a+1)
        for n,c in zip(indices,A):
            k,v=valunit(n,p)
            if r%v==0:z[k]=(z[k]+c)%q
        out.append(tuple(z))
    return tuple(out)


def component_product(U,V,q):
    z=[U[0]*V[0]%q]
    z.extend((U[0]*V[i]+V[0]*U[i])%q for i in range(1,len(U)))
    return tuple(z)


def rho_basis(n,m,p):
    a,u=valunit(m,p);k,v=valunit(n,p)
    if k and not a:return None
    return (p**min(k,a) if k else 1)*gcd(u,v)


def test(p,m):
    q=p; ds=divisors(m); a,u=valunit(m,p); s=len(divisors(u))
    assert len(ds)==(a+1)*s
    space=list(product(range(q),repeat=len(ds)))
    projected={X:phi(X,ds,p,m,q) for X in space}
    assert len(set(projected.values()))==len(space),('not injective',p,m)
    # Verify all pairs and exact division counts through image sets.
    count=0
    for X in space:
        im=set()
        for Y in space:
            Z=multiply(X,Y,ds,p,q)
            im.add(Z)
            PX,PY,PZ=projected[X],projected[Y],projected[Z]
            assert PZ==tuple(component_product(V,W,q) for V,W in zip(PX,PY)), ('product',p,m,X,Y)
        count+=len(im)
    expected=((q-1)*q**(2*a+1)+(q**a-1)*q+1)**s
    assert count==expected,('division',p,m,count,expected)
    # A retraction to the divisor-truncated ring really fixes products and its domain.
    for i in range(1,3*m+1):
        for j in range(1,3*m+1):
            c,k=normalized_product(i,j,p)
            lt=rho_basis(k,m,p) if c else None
            ri=rho_basis(i,m,p);rj=rho_basis(j,m,p)
            cr,kr=normalized_product(ri,rj,p) if ri and rj else (0,None)
            rt=kr if cr else None
            assert lt==rt,('retraction',p,m,i,j,lt,rt)
    print('PASS',f'p={p},m={m},dimension={len(ds)},elements={len(space)},solvable_pairs={count}')


if __name__=='__main__':
    for p,m in [(2,1),(2,2),(2,4),(2,6),(2,12),(3,1),(3,3),(3,6),(3,9),(5,5),(5,10),(7,7)]:
        test(p,m)
    print('ALL_CHECKS_PASS')
