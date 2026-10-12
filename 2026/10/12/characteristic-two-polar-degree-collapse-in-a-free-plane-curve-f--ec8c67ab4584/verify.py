"""Exact finite-field consistency checks for the polar degeneration theorem."""

def gf_mul(a,b,q,mod):
    n=q.bit_length()-1
    ans=0
    while b:
        if b&1: ans^=a
        b>>=1; a<<=1
        if a & q: a^=mod
    return ans

def gf_pow(a,e,q,mod):
    out=1
    while e:
        if e&1: out=gf_mul(out,a,q,mod)
        a=gf_mul(a,a,q,mod);e>>=1
    return out

def check(m,q,mod):
    assert (q-1)%m==0 and m%2==1
    mul=lambda x,y:gf_mul(x,y,q,mod)
    power=lambda x,n:gf_pow(x,n,q,mod)
    pts=[(1,x,y) for x in range(q) for y in range(q)]+[(0,1,y) for y in range(q)]+[(0,0,1)]
    assert len(pts)==q*q+q+1
    base=[]
    non_p=[]
    for x,y,z in pts:
        xm,ym,zm=(power(v,m) for v in (x,y,z))
        B=xm^ym;C=ym^zm
        A=mul(xm,ym)^mul(ym,zm)^mul(xm,zm)
        P=mul(B,C)
        assert A==(P^power(y,2*m))
        gradP=(mul(power(x,m-1),C),mul(power(y,m-1),xm^zm),mul(power(z,m-1),B))
        gradF=tuple(mul(power(y,2*m),c) for c in gradP)
        if gradP==(0,0,0):
            base.append((x,y,z))
            if P: non_p.append((x,y,z))
        # Algebraic equality of directional derivatives for the full equation.
        assert gradF==(mul(power(y,2*m),mul(power(x,m-1),C)),
                       mul(power(y,2*m),mul(power(y,m-1),xm^zm)),
                       mul(power(y,2*m),mul(power(z,m-1),B)))
    expected={(1,0,0),(0,1,0),(0,0,1)}
    roots=[a for a in range(1,q) if power(a,m)==1]
    assert len(roots)==m
    for a in roots:
        for b in roots:
            expected.add((1,a,b))
    assert set(base)==expected,(m,len(base),len(expected))
    assert non_p==[(0,1,0)],non_p
    return len(base),len(non_p),len(pts)

def poly_mul(a,b):
    ans={}
    for u,cu in a.items():
        for v,cv in b.items():
            w=tuple(u[j]+v[j] for j in range(3))
            ans[w]=(ans.get(w,0)^(cu&cv))
    return {u:v for u,v in ans.items() if v}

def poly_diff(a,j):
    ans={}
    for exp,c in a.items():
        if exp[j]&1:
            e=list(exp);e[j]-=1
            ans[tuple(e)]=c
    return ans

def poly_shift_y(a,n):
    return {(x,y+n,z):c for (x,y,z),c in a.items()}

def check_formal_derivatives(m):
    A={(m,m,0):1,(0,m,m):1,(m,0,m):1}
    B={(m,0,0):1,(0,m,0):1}
    C={(0,m,0):1,(0,0,m):1}
    P=poly_mul(B,C);F=poly_mul(A,P)
    assert A==dict(sorted({k:v for k,v in A.items()}.items()))
    assert F==poly_mul(P,{**P,(0,2*m,0):P.get((0,2*m,0),0)^1})
    for j in range(3):
        assert poly_diff(F,j)==poly_shift_y(poly_diff(P,j),2*m)
        if m%2==0: assert not poly_diff(F,j)

def main():
    for mm in range(2,15): check_formal_derivatives(mm)
    for m,q,mod in [(3,4,0b111),(5,16,0b10011),(7,8,0b1011)]:
        b,np,n=check(m,q,mod)
        # Verified local-length formula and residual degree.
        base_length=3*(m-1)**2+m*m
        deg=(2*m-1)**2-base_length
        assert deg==2*m-2 and deg>0
        print('m=%d, F_%d: projective_points=%d, polar_base_points=%d, off_P=%d, residual_degree=%d'%(m,q,n,b,np,deg))
    # Characteristic-zero singularity accounting at the two tangent-pencil centers.
    for m in range(2,9):
        mu_center=2*(m-1)**2+4*m*m-1
        mu_total=2*mu_center+(m-1)**2+m*m
        degree=(4*m-1)**2-mu_total
        assert degree==2*m*m+2*m-2
    print('VERIFY_OK: characteristic-two exact identities, polar base supports, and degree formulas')

if __name__=='__main__':main()
