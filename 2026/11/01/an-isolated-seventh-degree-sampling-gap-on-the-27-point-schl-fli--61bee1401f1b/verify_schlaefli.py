"""Exact checks for the 27-point Schlaefli spherical harmonic sampling theorem.
Python 3 standard library only. All matrix identities are over Q.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def points():
    pts = [(F(0),)*5+(F(1),)]
    for i in range(5):
        for sig in (-1,1):
            p=[F(0)]*6
            p[i]=F(sig,2)
            p[5]=F(-1,2)
            pts.append(tuple(p))
    for signs in product((-1,1),repeat=5):
        if sum(s==-1 for s in signs)%2==0:
            pts.append(tuple([F(s,4) for s in signs]+[F(1,4)]))
    assert len(pts)==27 and len(set(pts))==27
    return pts


def dot(x,y):
    return 3*sum(x[i]*y[i] for i in range(5))+x[5]*y[5]


def gegenbauer_normalized(k,t):
    # ultraspherical parameter lambda=2 on S^5.
    if k==0: return F(1)
    c0,c1=F(1),4*t
    if k==1: return c1/F(4)
    for n in range(2,k+1):
        # n C_n^lambda = 2(n+lambda-1)t C_(n-1) - (n+2lambda-2) C_(n-2)
        cn=(2*(n+1)*t*c1-(n+2)*c0)/n
        c0,c1=c1,cn
    return c1/F(comb(k+3,3))


def rank_exact(a):
    rows=[list(map(F,r)) for r in a]
    m=len(rows);n=len(rows[0]);i=0
    for j in range(n):
        pivot=next((r for r in range(i,m) if rows[r][j]),None)
        if pivot is None:continue
        rows[i],rows[pivot]=rows[pivot],rows[i]
        a0=rows[i][j]
        rows[i]=[v/a0 for v in rows[i]]
        for r in range(i+1,m):
            p=rows[r][j]
            if p:
                rows[r]=[u-p*v for u,v in zip(rows[r],rows[i])]
        i+=1
        if i==m:break
    return i


def verify():
    pts=points();n=len(pts)
    T=[[dot(p,q) for q in pts] for p in pts]
    for i in range(n):
        assert T[i][i]==1
        assert sorted(set(T[i][:i]+T[i][i+1:]))==[F(-1,2),F(1,4)]
        assert sum(v==F(1,4) for v in T[i])==16
        assert sum(v==F(-1,2) for v in T[i])==10
    A=[[int(i!=j and T[i][j]==F(1,4)) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            a2=sum(A[i][h]*A[h][j] for h in range(n))
            assert a2==8*int(i==j)+2*A[i][j]+8
    # A has spectral sectors 16^1, 4^6, (-2)^20 by the above identity.
    table={
        0: (F(27),F(0),F(0)),
        1: (F(0),F(9,2),F(0)),
        2: (F(0),F(0),F(27,20)),
        3: (F(0),F(0),F(27,20)),
        4: (F(0),F(45,28),F(243,280)),
        5: (F(135,56),F(243,224),F(405,448)),
        6: (F(27,16),F(405,448),F(891,896)),
        7: (F(0),F(9,8),F(81,80)),
        8: (F(135,176),F(567,704),F(7533,7040)),
    }
    ranks={0:1,1:6,2:20,3:20,4:26,5:27,6:27,7:26,8:27}
    for k in range(9):
        a,b=(gegenbauer_normalized(k,F(1,4)),gegenbauer_normalized(k,F(-1,2)))
        e=(1+16*a+10*b,1+4*a-5*b,1-2*a+b)
        assert e==table[k],(k,e)
        mat=[[gegenbauer_normalized(k,T[i][j]) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                assert mat[i][j]==int(i==j)+a*A[i][j]+b*(1-int(i==j)-A[i][j])
        assert rank_exact(mat)==ranks[k]
        assert all(z>=0 for z in e)
        print(f'degree={k} eigenvalues={e} exact_rank={ranks[k]}')
    # Rigorous rational envelopes for the large-degree analytic estimate:
    assert F(16,15)**3 < F(10,9)**2
    assert F(4,3)**3 < F(8,5)**2
    assert 16*3*F(10,9)+10*3*F(8,5)==F(304,3)<110
    # k>=9: (k+1)(k+2)>=110; all spectral sectors strictly positive.
    print('SCHLAEFLI_ALL_DEGREE_CERTIFICATE_OK 27 points, 9 exact ranks')

if __name__=='__main__':verify()
