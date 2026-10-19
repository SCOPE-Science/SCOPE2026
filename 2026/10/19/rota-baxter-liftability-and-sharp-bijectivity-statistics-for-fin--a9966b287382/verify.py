#!/usr/bin/env python3
"""Independent finite checks for group Rota--Baxter counts on H_3(F_p)."""
from itertools import product


def group_mul(g,h,p):
    x,y,z=g; a,b,t=h
    inv2=(p+1)//2
    return ((x+a)%p,(y+b)%p,(z+t+inv2*(x*b-y*a))%p)


def group_inv(g,p):
    return tuple((-u)%p for u in g)


def construct(A,k,ell,p):
    a,b,c,d=A; u,v=ell
    inv2=(p+1)//2
    def op(g):
        x,y,z=g
        ax=(a*x+b*y)%p
        ay=(c*x+d*y)%p
        sym=(ax*y-ay*x)%p
        return (ax,ay,(k*z+u*x+v*y-k*inv2*sym)%p)
    return op


def count(p,check_identity=False):
    G=list(product(range(p),repeat=3))
    all_N=0; both=0; oneB=0; oneT=0; neither=0
    witnesses=[]
    for a,b,c,d in product(range(p),repeat=4):
        tr=(a+d)%p; det=(a*d-b*c)%p
        for k in range(p):
            if det != (k*(1+tr))%p:continue
            isB=(k!=0 and det!=0)
            isT=(k!=p-1 and (1+tr+det)%p!=0)
            all_N+=p*p
            if isB and isT:both+=p*p
            elif isB:oneB+=p*p
            elif isT:oneT+=p*p
            else:neither+=p*p
            if check_identity:
                for ell in product(range(p),repeat=2):
                    B=construct((a,b,c,d),k,ell,p)
                    for g in G:
                        Bg=B(g)
                        for h in G:
                            Bh=B(h)
                            r=group_mul(group_mul(group_mul(g,Bg,p),h,p),group_inv(Bg,p),p)
                            assert group_mul(Bg,Bh,p)==B(r), (p,(a,b,c,d),k,ell,g,h)
                    # Direct image test, without using any matrix determinant criteria.
                    im={B(g) for g in G}
                    assert (len(im)==len(G))==isB
                    Bt=lambda g:group_mul(group_inv(g,p),B(group_inv(g,p)),p)
                    assert (len({Bt(g) for g in G})==len(G))==isT
    expected=(p**6+p**4,p**6-3*p**5+4*p**3,p**5-2*p**3,p**5-2*p**3,p**5+p**4)
    measured=(all_N,both,oneB,oneT,neither)
    assert measured==expected,(p,measured,expected)
    return measured

if __name__=='__main__':
    for p in (3,5,7,11):
        print('field',p,'counts',count(p,check_identity=(p==3)))
    # Formula-check some nonconforming parameters fail the RB identity.
    for A,k in [((1,0,0,1),1),((0,1,0,0),2),((2,2,1,1),2)]:
        p=5
        det=(A[0]*A[3]-A[1]*A[2])%p
        tr=(A[0]+A[3])%p
        if det==k*(1+tr)%p:continue
        G=list(product(range(p),repeat=3))
        B=construct(A,k,(0,0),p)
        assert any(group_mul(B(g),B(h),p)!=B(group_mul(group_mul(group_mul(g,B(g),p),h,p),group_inv(B(g),p),p)) for g in G for h in G)
    print('VERIFY_OK')


def brace_counts(p):
    # Independently enumerate the entire natural p^4 family of bilinear braces,
    # the subset admitting RB lifts, their lift multiplicities, and GL2-similarity orbits.
    matrices=list(product(range(p),repeat=4))
    invertible=[P for P in matrices if (P[0]*P[3]-P[1]*P[2])%p]
    lifts={}
    for A in matrices:
        a,b,c,d=A
        tr=(a+d)%p; det=(a*d-b*c)%p
        lifts[A]=p*p*sum(det==(k*(1+tr))%p for k in range(p))
    rb=[A for A,v in lifts.items() if v]
    assert len(rb)==p**4-p**3+p*p+p
    assert sum(lifts.values())==p**6+p**4
    assert all(v==p**2 for A,v in lifts.items() if (A[0]+A[3]+1)%p)
    assert all(v==p**3 for A,v in lifts.items() if not (A[0]+A[3]+1)%p and v)
    def conj(A,P):
        a,b,c,d=P; det=(a*d-b*c)%p
        inv=pow(det,-1,p)
        Q=(d*inv%p,-b*inv%p,-c*inv%p,a*inv%p)
        def mul(X,Y):
            a,b,c,d=X; e,f,g,h=Y
            return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)
        return mul(mul(P,A),Q)
    remaining=set(rb); num=0
    while remaining:
        A=next(iter(remaining))
        orbit={conj(A,P) for P in invertible}
        assert orbit.issubset(remaining)
        remaining-=orbit
        num+=1
    assert num==p*p, (p,num)
    return len(rb),num

if __name__=='__main__':
    for p in (3,5):
        print('brace',p,brace_counts(p))
    print('BRACE_VERIFY_OK')
