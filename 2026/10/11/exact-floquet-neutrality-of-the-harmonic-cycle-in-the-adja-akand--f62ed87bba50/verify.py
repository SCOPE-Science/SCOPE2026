from fractions import Fraction as F

def add(a,b):
    c=dict(a)
    for k,v in b.items():
        c[k]=c.get(k,F(0))+v
        if c[k]==0: del c[k]
    return c

def mul(a,b):
    c={}
    for i,ai in a.items():
        for j,bj in b.items():
            c[i+j]=c.get(i+j,F(0))+ai*bj
    return {k:v for k,v in c.items() if v}

def scale(a,s): return {k:v*s for k,v in a.items() if v*s}

ONE={0:F(1)}; X={1:F(1)}; X2={2:F(1)}

def xn(k): return {k:F(1)}

for n in range(65):
    S={2*l:F(1) for l in range(n+1)}
    geom=add(add(mul(add(ONE,scale(X2,F(-1))),S),xn(2*n+2)),scale(ONE,F(-1)))
    assert geom=={}, (n,geom)
    # Polynomial ring Q[x,y], encoded exponent pair -> coefficient.
    def A(a,b): return {(a,b):F(1)}
    def add2(p,q):
        r=dict(p)
        for k,v in q.items():
            r[k]=r.get(k,F(0))+v
            if r[k]==0: del r[k]
        return r
    def mul2(p,q):
        r={}
        for (i,j),a in p.items():
            for (k,l),b in q.items():
                z=(i+k,j+l); r[z]=r.get(z,F(0))+a*b
        return {k:v for k,v in r.items() if v}
    def sc2(p,s): return {k:v*s for k,v in p.items() if v*s}
    s2={(2*l,0):F(1) for l in range(n+1)}
    R=add2(add2(A(2,0),A(0,2)),{(0,0):F(-1)})
    h=mul2(A(1,0),add2(R,mul2(A(0,1),s2)))
    ydot=add2(sc2(mul2(h,A(0,1)),F(-1)),{(2*n+3,0):F(-1)})
    rdot=add2(sc2(mul2(A(1,0),A(0,1)),F(2)),sc2(mul2(A(0,1),ydot),F(2)))
    rhs=sc2(mul2(mul2(mul2(A(1,0),A(0,1)),add2(A(0,1),s2)),R),F(-2))
    assert add2(rdot,sc2(rhs,F(-1)))=={}, n
print('VERIFY_OK')
