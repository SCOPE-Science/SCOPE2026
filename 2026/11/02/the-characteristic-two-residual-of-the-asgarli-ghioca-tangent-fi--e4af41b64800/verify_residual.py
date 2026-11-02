#!/usr/bin/env python3
"""Exact finite-field and polynomial checks for the characteristic-two residual curve."""
from itertools import product

IRR={4:0x7,8:0xb,16:0x13,32:0x25}
def mul(a,b,q):
    irr=IRR[q]; ret=0
    while b:
        if b&1: ret^=a
        b>>=1; a<<=1
        if a&q: a^=irr
    return ret
def power(a,n,q):
    y=1
    while n:
        if n&1:y=mul(y,a,q)
        a=mul(a,a,q);n>>=1
    return y
def poly_add(a,b):
    d=a.copy()
    for e,c in b.items():
        if c:
            d[e]=d.get(e,0)^c
            if not d[e]:del d[e]
    return d
def poly_mul(a,b):
    d={}
    for (i,j,k),ca in a.items():
        for (ii,jj,kk),cb in b.items():
            e=(i+ii,j+jj,k+kk);d[e]=d.get(e,0)^(ca&cb)
            if not d[e]:del d[e]
    return d
def mon(e):return {e:1}
def polynomial(q):
    n=q-1
    s=mon((0,0,0))
    for i in range(q.bit_length()-1):
        w=1<<i
        s=poly_mul(s,{(w,0,0):1,(0,w,0):1,(0,0,w):1})
    f=poly_add(s,{(n,0,0):1,(0,n,0):1,(0,0,n):1})
    b=poly_mul(poly_mul({(1,0,0):1,(0,1,0):1},{(0,1,0):1,(0,0,1):1}),{(1,0,0):1,(0,0,1):1})
    # Exact polynomial long division over GF(2) with lexicographic term order.
    div=f.copy();quot={}
    be=max(b)
    while div:
        e=max(div)
        assert all(e[i]>=be[i] for i in range(3)), "B does not divide F"
        m=tuple(e[i]-be[i] for i in range(3))
        quot=poly_add(quot,mon(m))
        div=poly_add(div,poly_mul(b,mon(m)))
    assert poly_mul(quot,b)==f
    return quot
def evalpoly(poly,P,q):
    ret=0
    for (i,j,k) in poly:
        v=mul(mul(power(P[0],i,q),power(P[1],j,q),q),power(P[2],k,q),q)
        ret^=v
    return ret
def deriv(poly,i):
    d={}
    for exp in poly:
        if exp[i]&1:
            f=list(exp);f[i]-=1;d[tuple(f)]=1
    return d
def projective(q):
    for x in range(q):
        for y in range(q):
            yield (x,y,1)
    for x in range(q):
        yield (x,1,0)
    yield (1,0,0)
def B(P):
    x,y,z=P;return (x^y)*(y^z)*(z^x) !=0
def singulars(q,field):
    H=polynomial(q);ds=[deriv(H,i) for i in range(3)]
    return [P for P in projective(field) if evalpoly(H,P,field)==0 and all(evalpoly(D,P,field)==0 for D in ds)]
def main():
    for q in (8,16,32):
        t=q//2;h=polynomial(q)
        assert {sum(e) for e in h}=={q-4}
        pts=[P for P in projective(q) if evalpoly(h,P,q)==0]
        assert len(pts)==(q-2)*(q-4),(q,len(pts))
        assert all(B(P) for P in pts),(q,"line rational point")
        assert not singulars(q,q),(q,"rational singular point")
        sings=singulars(q,t)
        assert len(sings)==(t-2)*(t-4),(q,t,len(sings))
        assert all(B(P) for P in sings)
        ds=[deriv(h,i) for i in range(3)]
        for i,j in ((0,1),(1,2),(0,2)):
            linepts=[P for P in projective(t) if P[i]==P[j] and evalpoly(h,P,t)==0]
            assert len(linepts)==t-2,(q,i,j,linepts)
            assert all(any(evalpoly(D,P,t)!=0 for D in ds) for P in linepts)
        print(f"q={q}: degree={q-4}; #C(F_q)={len(pts)}; #geometric cusps supported over F_{t}={len(sings)}; smooth B tangencies per line={t-2}; all checks PASS")
    # Exact characteristic-two cubic-tangent identity.
    x=mon((1,0,0));y=mon((0,1,0));z=mon((0,0,1))
    def plus(*items):
        out={}
        for v in items:out=poly_add(out,v)
        return out
    def powpoly(v,n):
        out=mon((0,0,0))
        for _ in range(n):out=poly_mul(out,v)
        return out
    lhs=plus(poly_mul(powpoly(x,4),powpoly(plus(y,z),3)),
            poly_mul(powpoly(y,4),powpoly(plus(x,z),3)),
            poly_mul(powpoly(z,4),powpoly(plus(x,y),3)))
    k=plus(poly_mul(x,y),poly_mul(x,z),poly_mul(y,z))
    rhs=poly_mul(poly_mul(poly_mul(plus(x,y),plus(x,z)),plus(y,z)),powpoly(k,2))
    assert lhs==rhs,("cusp tangent-cubic identity",lhs,rhs)
    print("Exact symbolic cusp tangent-cubic identity PASS")
if __name__=="__main__": main()
