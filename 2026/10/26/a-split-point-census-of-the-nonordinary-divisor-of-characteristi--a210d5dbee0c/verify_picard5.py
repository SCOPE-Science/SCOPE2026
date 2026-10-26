#!/usr/bin/env python3
"""Exact finite-field checks for Picard quartic nonordinary strata (public reproducibility)."""
from itertools import product

def field_tables(n):
    p=5; q=p**n
    mod={1:(0,1),2:(2,0,1),3:(1,1,0,1)}[n]
    def vec(x):
        return [(x//(p**j))%p for j in range(n)]
    vals=[vec(i) for i in range(q)]
    def enc(v):
        return sum((v[j]%p)*p**j for j in range(n))
    add=[[enc([(vals[i][t]+vals[j][t])%p for t in range(n)]) for j in range(q)] for i in range(q)]
    mul=[]
    for i in range(q):
        row=[]
        for j in range(q):
            poly=[0]*(2*n-1)
            for s,vs in enumerate(vals[i]):
                for t,vt in enumerate(vals[j]):
                    poly[s+t]=(poly[s+t]+vs*vt)%p
            for d in range(2*n-2,n-1,-1):
                k=poly[d]
                for t in range(n):
                    poly[d-n+t]=(poly[d-n+t]-k*mod[t])%p
            row.append(enc(poly[:n]))
        mul.append(row)
    assert all(mul[a][1]==a for a in range(q))
    assert all(any(mul[a][b]==1 for b in range(1,q)) for a in range(1,q)), "extension modulus must be irreducible"
    return add,mul,q

def check(n):
    add,mul,q=field_tables(n)
    def A(*xs):
        s=0
        for x in xs:s=add[s][x]
        return s
    def M(x,y):return mul[x][y]
    def neg(x):return mul[4][x]
    def sq(x):return mul[x][x]
    def cube(x):return mul[x][sq(x)]
    def pow4(x):return sq(sq(x))
    Np=0; Np_smooth=0; total_smooth=0
    # Mod-5 quartic discriminant, computed over Z then reduced:
    # Delta=a^4 c + a^3 b^2 +2a^2 c^2 -a b^2 c-2b^4+c^3.
    for a in range(q):
        a2=sq(a); a3=M(a2,a);a4=sq(a2)
        for b in range(q):
            b2=sq(b); b4=sq(b2)
            ab2=M(a,b2)
            for c in range(q):
                c2=sq(c); c3=M(c2,c)
                P=A(c2,M(a2,c),ab2)
                D=A(M(a4,c), M(a3,b2), M(2,M(a2,c2)),
                    neg(M(ab2,c)),neg(M(2,b4)),c3)
                if D!=0:total_smooth+=1
                if P==0:
                    Np+=1
                    if D!=0:
                        Np_smooth+=1
                        assert b!=0
                        assert A(M(2,M(a,c)),b2)!=0 or M(2,M(a,b))!=0 or A(M(2,c),a2)!=0
    assert Np==q*q,(n,q,'P count',Np,q*q)
    assert total_smooth==q**3-q**2,(n,q,'U count',total_smooth,q**3-q**2)
    assert Np_smooth==(q-1)**2,(n,q,'p-rank0 count',Np_smooth,(q-1)**2)
    print('GF(5^%d): q=%d P=%d smooth=%d rank0=%d rank2=%d' %
          (n,q,Np,total_smooth,Np_smooth,total_smooth-Np_smooth))

def check_cartier_coefficient_and_squarefree():
    p=5
    def cv(f,g):
        out=[0]*(len(f)+len(g)-1)
        for i,x in enumerate(f):
            for j,y in enumerate(g):out[i+j]=(out[i+j]+x*y)%p
        return out
    def degree(f):
        while len(f)>1 and f[-1]==0:f.pop()
        return len(f)-1
    def remainder(f,g):
        f=f[:];g=g[:];dg=degree(g)
        while degree(f)>=dg and any(f):
            k=degree(f)-dg;factor=f[-1]*pow(g[-1],-1,p)%p
            for j in range(len(g)):f[j+k]=(f[j+k]-factor*g[j])%p
            degree(f)
        return f
    def sqfree(f):
        derivative=[(j*f[j])%p for j in range(1,len(f))]
        while any(derivative):f,derivative=derivative,remainder(f,derivative)
        return degree(f)==0
    for a,b,c in product(range(p),repeat=3):
        f=[c,b,a,0,1]
        f3=cv(cv(f,f),f)
        P=(c*c+a*a*c+a*b*b)%5
        D=(a**4*c+a**3*b*b+2*a*a*c*c-a*b*b*c-2*b**4+c**3)%5
        assert f3[4]==3*P%5
        assert f3[9]==3*b%5
        assert sqfree(f[:])==(D!=0)
    print('GF(5): independent coefficient-extraction and squarefree checks passed')

if __name__=='__main__':
    check_cartier_coefficient_and_squarefree()
    for n in (1,2,3):check(n)
    print('VERIFY_OK')
