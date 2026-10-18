"""Exact-rational checks for complete-bipartite symmetric-edge incenter classification.
The graph facet classification is taken as an analytical input from the cited primary source.
This finite program checks its ensuing norm and contact-span calculations only.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def rank(rows):
    if not rows: return 0
    M=[list(map(F,row)) for row in rows]
    h,w=len(M),len(M[0]); i=0
    for j in range(w):
        piv=next((k for k in range(i,h) if M[k][j]),None)
        if piv is None:continue
        M[i],M[piv]=M[piv],M[i]
        c=M[i][j];M[i]=[x/c for x in M[i]]
        for k in range(h):
            if k!=i and M[k][j]:
                t=M[k][j];M[k]=[a-t*b for a,b in zip(M[k],M[i])]
        i+=1
        if i==h:break
    return i


def facets(p,q):
    n=p+q
    for side,size in [('A',p),('B',q)]:
        for signs in product((-1,1),repeat=size):
            v=(signs+(0,)*q) if side=='A' else ((0,)*p+signs)
            s=sum(signs)
            norm_sq=F(size)-F(s*s,n)
            yield side,v,norm_sq


def test(p,q):
    n=p+q
    t=F(q)-F(q%2,n)
    fv=list(facets(p,q))
    observed=max(v for _,_,v in fv)
    assert observed==t,(p,q,t,observed)
    active=[f for s,f,v in fv if v==t]
    expected=(comb(q,q//2) if q%2==0 else 2*comb(q,(q-1)//2))*(2 if p==q else 1)
    assert len(active)==expected,(p,q,len(active),expected)
    # Facet equations are tested on H; projected normals have the same row rank on H.
    # A vector z is in H iff sum z_i=0.
    expected_dim=(p if q%2==0 else p-1) if p<q else (1 if q%2==0 else 0)
    rr=rank(active+[(1,)*n])
    assert n-rr==expected_dim,(p,q,n-rr,expected_dim)
    basis=[]
    if p<q:
        for i in range(p-1):
            row=[F(0)]*n;row[i]=1;row[p-1]=-1;basis.append(row)
        if q%2==0:
            basis.append([-F(q,p)]*p+[F(1)]*q)
    elif q%2==0:
        basis.append([F(1)]*p+[-F(1)]*q)
    assert len(basis)==expected_dim
    for v in basis:
        assert sum(v)==0
        assert all(sum(a*b for a,b in zip(f,v))==0 for f in active)
        for direction in (1,-1):
            # Check the ball constraints in exact rational arithmetic by squaring
            # nonnegative sides. This only corroborates the local feasible dimension.
            center=[direction*z/F(1000000) for z in v]
            for side,f,nsq in fv:
                x=abs(sum(a*b for a,b in zip(f,center)))
                assert x<=1 and (1-x)**2>=nsq/t,(p,q,side,x,nsq,t)
    return len(fv),len(active),expected_dim


def main():
    profiles=0; facets_checked=0; touches=0; nontrivial=0
    for p in range(2,9):
        for q in range(p,12):
            f,a,d=test(p,q)
            profiles+=1;facets_checked+=f;touches+=a
            if d:nontrivial+=1
    print('VERIFY_OK profiles=%d facets=%d tangent_facets=%d positive_dim_profiles=%d'%(profiles,facets_checked,touches,nontrivial))

if __name__=='__main__':main()

# Additional strict endpoint-contact check for balanced even bicliques. This is
# a finite numerical cross-check only; the analytic proof handles every m.
def endpoint_checks():
    from math import sqrt, isclose
    summary=[]
    for m in (2,4,6,8):
        n=2*m
        a=(1-sqrt(1-F(2,m*m)))/2
        z=[a]*m+[-a]*m
        seen=set();tangent=0
        for _,f,nsq in facets(m,m):
            s=sum(f); proj=tuple(F(t)-F(s,n) for t in f)
            if proj in seen:continue
            seen.add(proj)
            dot=sum(float(t)*u for t,u in zip(f,z))
            margin=1-dot-sqrt(float(nsq)/m)
            assert margin>-1e-11,(m,margin)
            if isclose(margin,0,abs_tol=1e-11):tangent+=1
        expect=2*comb(m,m//2)+(1 if m==2 else 2*comb(m,m//2-1))
        assert tangent==expect,(m,tangent,expect)
        summary.append((m,tangent))
    return summary

if __name__=='__main__':
    print('VERIFY_ENDPOINTS_OK',endpoint_checks())
