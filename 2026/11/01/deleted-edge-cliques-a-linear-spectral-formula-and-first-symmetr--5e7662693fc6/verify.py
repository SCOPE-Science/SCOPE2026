"""Exact integer spectral checks for centered graph-ball averages on K_{m+2} minus an edge.
Only m=1,2,3 are enumerated; the all-m reduction has an analytic proof.
"""
from fractions import Fraction as F
from itertools import product


def det_int(a):
    n=len(a)
    if not n:return 1
    b=[list(map(int,row)) for row in a]
    sign=1;prev=1
    for j in range(n-1):
        if b[j][j]==0:
            h=next((i for i in range(j+1,n) if b[i][j]!=0),None)
            if h is None:return 0
            b[j],b[h]=b[h],b[j]; sign=-sign
        p=b[j][j]
        for i in range(j+1,n):
            for k in range(j+1,n):
                z=b[i][k]*p-b[i][j]*b[j][k]
                assert z%prev==0
                b[i][k]=z//prev
        for i in range(j+1,n):b[i][j]=0
        prev=p
    return sign*b[n-1][n-1]


def is_pd(mat):
    return all(det_int([row[:k] for row in mat[:k]])>0 for k in range(1,len(mat)+1))


def rows(m,hv,lv):
    # Integer B = (m+1)(m+2) A. Hub selection 0=singleton, 1=whole;
    # nonadjacent-pair selection 0=singleton, 1=neighborhood, 2=whole.
    N=m+2;d=(m+1)*N;out=[]
    for i,c in enumerate(hv):
        r=[0]*N
        if c==0:r[i]=d
        else:r=[d//N]*N
        out.append(r)
    for j,c in enumerate(lv):
        r=[0]*N
        if c==0:r[m+j]=d
        if c==1:
            for i in range(m):r[i]=d//(m+1)
            r[m+j]=d//(m+1)
        if c==2:r=[d//N]*N
        out.append(r)
    return out


def verify_selection_bounds(m,q,expected):
    N=m+2;d=(m+1)*N;strict=0;exceptions=[]
    for h in product(range(2),repeat=m):
        for ell in product(range(3),repeat=2):
            b=rows(m,h,ell)
            gram=[[sum(b[z][i]*b[z][j] for z in range(N)) for j in range(N)] for i in range(N)]
            c=[[q.numerator*d*d*(i==j)-q.denominator*gram[i][j] for j in range(N)] for i in range(N)]
            if is_pd(c):strict+=1
            else:exceptions.append((h,ell))
    assert set(exceptions)==set(expected)
    assert strict==2**m*9-len(expected)
    return strict,len(exceptions)


def verify_polynomial():
    # Representative m=3, two singleton hub rows, one whole-graph hub row,
    # and two neighborhood rows: characteristic polynomial by six integer evaluations.
    m=3;d=20;N=5;b=rows(m,(0,0,1),(1,1))
    gram=[[sum(b[z][i]*b[z][j] for z in range(N)) for j in range(N)] for i in range(N)]
    p=lambda z: 400*z**3-655*z**2+126*z-1
    for z in range(6):
        mat=[[d*d*z*(i==j)-gram[i][j] for j in range(N)] for i in range(N)]
        got=F(det_int(mat),d**(2*N))
        assert got==(F(z)-1)*(16*F(z)-1)*p(F(z))/6400
    lo=F(1416,1000);hi=F(1417,1000)
    assert p(lo)<0<p(hi) and p(F(7,5))<0
    # For z>=1, p'(z)=1200z^2-1310z+126>0; exactly one root above one.
    assert 1200-1310+126>0
    # Rigorous rational interval bounds on coordinates and active averaging choices.
    blo=1-1/lo;bhi=1-1/hi
    clo=41*(3*lo-1)/(hi*(400*hi-57))
    chi=41*(3*hi-1)/(lo*(400*lo-57))
    ulo=(2+blo+2*clo)/5;uhi=(2+bhi+2*chi)/5
    vlo=(2+blo+clo)/4;vhi=(2+bhi+chi)/4
    assert 0<clo<chi<blo<bhi<ulo<uhi<vlo<vhi<1
    # Eigenvector identity (A^T A - zI)v = p(z)*r(z), checked by hand in RESULT.md.
    print('POLYNOMIAL_OK characteristic=(z-1)(16z-1)(400z^3-655z^2+126z-1)/6400')
    print('ACTIVE_OK root_interval=(1.416,1.417) positive_pattern=(1,1,b,c,c)')

if __name__=='__main__':
    c1=verify_selection_bounds(1,F(3,2),[((0,),(1,1))])
    c2=verify_selection_bounds(2,F(29,20),[((0,0),(1,1))])
    c3=verify_selection_bounds(3,F(7,5),[((0,0,1),(1,1)),((0,1,0),(1,1)),((1,0,0),(1,1))])
    verify_polynomial()
    print(f'CERTIFICATE_OK selections=126 strict={sum(c[0] for c in (c1,c2,c3))} exceptional={sum(c[1] for c in (c1,c2,c3))} m1={c1} m2={c2} m3={c3}')
