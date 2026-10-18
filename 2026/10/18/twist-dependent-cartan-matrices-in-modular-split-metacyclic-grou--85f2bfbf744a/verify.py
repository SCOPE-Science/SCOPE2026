"""Exact finite-prime-field checks for twisted metacyclic algebra radical layers."""
from itertools import product
from math import comb


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


def mul(a, b, p):
    if not a or not b:
        return ()
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % p
    return trim(c)


def divmodp(a, b, p):
    a, b = list(trim(a)), trim(b)
    if not b:
        raise ZeroDivisionError
    q = [0]*max(0,len(a)-len(b)+1)
    ib = pow(b[-1], -1, p)
    while len(a)>=len(b):
        k=len(a)-len(b)
        v=a[-1]*ib%p
        q[k]=v
        for j, bj in enumerate(b):
            a[k+j]=(a[k+j]-v*bj)%p
        while a and a[-1]==0:
            a.pop()
    return trim(q),trim(a)


def factors(f,p):
    f=trim(f)
    out=[]
    while len(f)>1:
        found=False
        for d in range(1,len(f)):
            for prefix in product(range(p),repeat=d):
                g=tuple(prefix)+(1,)
                q,r=divmodp(f,g,p)
                if not r:
                    out.append(g)
                    f=q
                    found=True
                    break
            if found:
                break
        if not found:
            out.append(f)
            break
    return out


def scale_root_factor(f,s,p):
    """Monic polynomial of s*beta when beta is a root of monic f."""
    d=len(f)-1
    return tuple(f[i]*pow(s,d-i,p)%p for i in range(d+1))


def ppow(a,k,p):
    z=(1,)
    for _ in range(k):
        z=mul(z,a,p)
        z=z[:p]
    return trim(z)


def oneprod(i,j,k,l,p,m,r,a):
    """Product of two basis monomials t^i y^j and t^k y^l."""
    # compute ((1+t)^{r^j}-1)^k more efficiently
    exponent=pow(r,j,p)
    z=trim([(0 if v==0 else comb(exponent,v)%p) if v>0 else 0
            for v in range(exponent+1)])
    v=ppow(z,k,p)
    ans={}
    for h,c in enumerate(v):
        if c and i+h<p:
            key=(i+h,(j+l)%m)
            ans[key]=(ans.get(key,0)+c*(a if j+l>=m else 1))%p
    return {key:c for key,c in ans.items() if c}


def product_linear(A,B,p,m,r,a):
    ans={}
    for (i,j),x in A.items():
        for (k,l),y in B.items():
            for key,c in oneprod(i,j,k,l,p,m,r,a).items():
                ans[key]=(ans.get(key,0)+x*y*c)%p
    return {key:c for key,c in ans.items() if c}


def check(p,m,r,a):
    assert pow(r,m,p)==1 and all(pow(r,j,p)!=1 for j in range(1,m))
    q_poly=tuple([-a%p]+[0]*(m-1)+[1])
    ff=factors(q_poly,p)
    assert len(set(ff))==len(ff)
    d=next(iter(map(lambda x:len(x)-1,ff)))
    assert all(len(x)-1==d for x in ff)
    c=pow(a,(p-1)//m,p)
    assert c!=0 and pow(c,m,p)==1
    assert d==next(k for k in range(1,m+1) if pow(c,k,p)==1)
    h=m//d
    assert len(ff)==h
    idx={f:i for i,f in enumerate(ff)}
    perm=[]
    for f in ff:
        g=scale_root_factor(f,r,p)
        assert g in idx
        perm.append(idx[g])
    assert set(perm)==set(range(h))
    orbit=[]
    j=0
    for k in range(h):
        assert j not in orbit
        orbit.append(j)
        j=perm[j]
    assert j==0 and len(orbit)==h
    C=[[0]*h for _ in range(h)]
    for j in range(h):
        i=j
        for _ in range(p):
            C[i][j]+=1
            i=perm[i]
    predicted=[[((p-1)//h)+(i==j) for j in range(h)]for i in range(h)]
    assert C==predicted
    # exact basis associativity in representative examples
    if p*m<=20:
        basis={(i,j):{(i,j):1} for i in range(p) for j in range(m)}
        for akey,bkey,ckey in product(basis,repeat=3):
            A,B,C0=basis[akey],basis[bkey],basis[ckey]
            assert product_linear(product_linear(A,B,p,m,r,a),C0,p,m,r,a)==product_linear(A,product_linear(B,C0,p,m,r,a),p,m,r,a)
    print(f'p={p} m={m} r={r} twist={a} c={c} d={d} h={h} factors={ff} Cartan={C}')


if __name__=='__main__':
    for params in [(3,2,2,1),(3,2,2,2),(5,4,2,1),(5,4,2,4),(5,4,2,2),(7,3,2,1),(7,3,2,2),(7,3,2,3),(7,6,3,1),(7,6,3,6),(7,6,3,2),(7,6,3,3)]:
        check(*params)
    print('ALL CHECKS PASS')
