"""Exact-rational checks of cyclic-shift controllability Gramian identities.

Run with Python 3, with no external dependencies. General results require the proof.
"""
from fractions import Fraction as F
from itertools import product


def shift(v, k):
    n = len(v)
    return [v[(i-k) % n] for i in range(n)]


def dots(a,b):
    return sum((x*y for x,y in zip(a,b)), F(0))


def mat_gram(n, b, r, horizon):
    out = [[F(0) for _ in range(n)] for _ in range(n)]
    if horizon is None:
        phases = [[(r*r)**j/(1-(r*r)**n) for j in range(n)]]
        terms = [(j, phases[0][j]) for j in range(n)]
    else:
        terms = [(j % n, (r*r)**j) for j in range(horizon)]
    for j,w in terms:
        col = shift(b,j)
        for i in range(n):
            for k in range(n):
                out[i][k] += w*col[i]*col[k]
    return out


def phase_weights(n,r,horizon):
    rr=r*r
    if horizon is None:
        return [rr**j/(1-rr**n) for j in range(n)]
    return [sum((rr**k for k in range(j,horizon,n)),F(0)) for j in range(n)]


def determinant(mat):
    n=len(mat)
    a=[row[:] for row in mat]
    out=F(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None: return F(0)
        if pivot != j:
            a[j],a[pivot]=a[pivot],a[j]
            out=-out
        q=a[j][j]
        out*=q
        for k in range(j+1,n):
            factor=a[k][j]/q
            for l in range(j+1,n):
                a[k][l]-=factor*a[j][l]
            a[k][j]=F(0)
    return out


def inverse_trace(mat):
    n=len(mat)
    a=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(mat)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None:return None
        a[j],a[pivot]=a[pivot],a[j]
        q=a[j][j]
        a[j]=[v/q for v in a[j]]
        for i in range(n):
            if i==j:continue
            q=a[i][j]
            a[i]=[a[i][k]-q*a[j][k] for k in range(2*n)]
    return sum((a[i][n+i] for i in range(n)),F(0))


def assert_gramian(n,b,r,horizon):
    assert dots(b,b)==1
    d=phase_weights(n,r,horizon)
    assert all(d[j]>d[j+1] for j in range(n-1))
    C=[[shift(b,j)[i] for j in range(n)] for i in range(n)]
    W=mat_gram(n,b,r,horizon)
    W2=[[sum(C[i][j]*d[j]*C[k][j] for j in range(n))
        for k in range(n)] for i in range(n)]
    assert W==W2
    assert sum(W[i][i] for i in range(n))==sum(d)
    dc=determinant(C)
    assert determinant(W)==dc*dc*__import__('math').prod(d)
    assert abs(dc)<=1
    if dc:
        assert inverse_trace(W)>=sum(1/x for x in d)
    autocorr=[dots(b,shift(b,j)) for j in range(1,n)]
    if not any(autocorr):
        assert abs(dc)==1
        assert inverse_trace(W)==sum(1/x for x in d)
    return (W,d,autocorr)


def main():
    cases=0
    vectors={
      2:[[F(1),F(0)],[F(3,5),F(4,5)]],
      3:[[F(1),F(0),F(0)], [F(2,3),F(2,3),F(-1,3)], [F(3,5),F(4,5),F(0)]],
      4:[[F(1),F(0),F(0),F(0)], [F(1,2),F(1,2),F(1,2),F(-1,2)]],
      5:[[F(1),F(0),F(0),F(0),F(0)]],
      6:[[F(1),F(0),F(0),F(0),F(0),F(0)]],
    }
    for n,vecs in vectors.items():
      for b,r,h in product(vecs,[F(1,2),F(2,3),F(3,4)], [n,n+1,2*n+3,None]):
        assert_gramian(n,b,r,h)
        cases+=1
    b=[F(2,3),F(2,3),F(-1,3)]
    W,d,corr=assert_gramian(3,b,F(1,2),None)
    assert d==[F(64,63),F(16,63),F(4,63)]
    assert corr==[F(0),F(0)]
    assert determinant(W)==F(4096,63**3)
    assert inverse_trace(W)==F(1323,64)
    print('VERIFY_OK',cases,'exact-rational Gramian, determinant, and inverse-trace cases')

if __name__=='__main__': main()
