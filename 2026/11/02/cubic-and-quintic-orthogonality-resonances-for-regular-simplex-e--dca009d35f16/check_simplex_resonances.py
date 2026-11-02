"""Exact checks of cubic/quintic harmonic interpolation on simplex-edge directions.

No external packages. These tests check finite formulas; proof covers every n>=4
and the infinite n=5 degree ladder without relying on finite extrapolation.
"""
from fractions import Fraction as F
from itertools import combinations


def P(n, degree, t):
    if degree == 0:
        return F(1)
    a, b = F(1), t
    for j in range(1, degree):
        a, b = b, ((2*j+n-3)*t*b-j*a)/(j+n-3)
    return b


def edges(n):
    return list(combinations(range(n), 2))


def incidence_dot(e, f):
    i,j=e; k,l=f
    return int(i==k)-int(i==l)-int(j==k)+int(j==l)


def verify(n, degree, projectors=False):
    E=edges(n); N=len(E)
    w = P(n,degree,F(1,2))
    if degree==3:
        assert w == F(n-11,8*(n-2))
        av=F(n-3,8)
        ac=F(3*(n+1),4*(n-2))
    elif degree==5:
        assert w == F((n-5)*(n-27),32*n*(n-2))
        av=F(n*n+135,32*n)
        ac=F(15*(n*n-9),16*n*(n-2))
    else:
        av=1+(n-2)*w
        ac=1-2*w
    assert av>0 and ac>0
    H=[]
    for e in E:
        row=[]
        for f in E:
            q=incidence_dot(e,f)
            direct=P(n,degree,F(q,2))
            predicted=(1 if e==f else q*w)
            assert direct==predicted
            projection=F(q,n)
            two_level=ac*(e==f)+(av-ac)*projection
            assert direct==two_level
            row.append(direct)
        H.append(row)
    assert (all(H[i][j]==(i==j) for i in range(N) for j in range(N)))==(w==0)
    if projectors:
        B=[[F(incidence_dot(e,f),n) for f in E] for e in E]
        assert all(sum(B[i][k]*B[k][j] for k in range(N))==B[i][j] for i in range(N) for j in range(N))
        assert sum(B[i][i] for i in range(N))==n-1
        y=[F((i*i+7*i+13)%17-8) for i in range(N)]
        Py=[sum(B[i][j]*y[j] for j in range(N)) for i in range(N)]
        c=[y[i]/ac+(1/av-1/ac)*Py[i] for i in range(N)]
        assert [sum(H[i][j]*c[j] for j in range(N)) for i in range(N)]==y
    return av,ac

if __name__=='__main__':
    for n in range(4,16):
        print(n,'cubic',verify(n,3,True),'quintic',verify(n,5,True))
    for n in [16,20,27,29]:
        print(n,'quintic',verify(n,5,False))
    for degree in range(0,121):
        # n=5 means dimension 4, so normalized Gegenbauer=U_degree/(degree+1).
        assert P(5,degree,F(1,2)) == F((1,1,0,-1,-1,0)[degree%6],degree+1)
        if degree%2:
            assert (P(5,degree,F(1,2))==0)==(degree%6==5)
            if degree>=3:
                assert 1+3*P(5,degree,F(1,2))>0
                assert 1-2*P(5,degree,F(1,2))>0
        else:
            assert P(5,degree,F(0))!=0
    print('PASS: exact n-by-degree spectra, cardinal interpolation, and n=5 periodic resonance')
