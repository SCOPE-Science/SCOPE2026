"""Exact rational independent checks of one-element metric-star L2 projectors.
Run with standard Python 3, no third-party packages required.
"""
from fractions import Fraction as F
import random


def inverse(A):
    n = len(A)
    W = [list(row) + [F(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for k in range(n):
        z = next(i for i in range(k, n) if W[i][k])
        W[k], W[z] = W[z], W[k]
        c = W[k][k]
        W[k] = [v / c for v in W[k]]
        for i in range(n):
            if i != k:
                t = W[i][k]
                W[i] = [a-t*b for a, b in zip(W[i], W[k])]
    return [row[n:] for row in W]


def integ_abs(a, b):
    """Integral 0..1 of |(1-t)a+tb| exactly."""
    if a*b >= 0:
        return (abs(a)+abs(b))/2
    return (a*a+b*b)/(2*abs(b-a))


def evaluate(lengths):
    m=len(lengths)
    S=sum(lengths)
    M=[[F(0) for _ in range(m+1)] for _ in range(m+1)]
    M[0][0]=S/3
    for j,h in enumerate(lengths, 1):
        M[0][j]=M[j][0]=h/6
        M[j][j]=h/3
    B=inverse(M)
    # Reconstruction check of all entries against independent inverse.
    for i in range(m+1):
      for j in range(m+1):
        predicted=(F(4,S) if i==j==0 else
          F(-2,S) if 0 in (i,j) else
          (F(3,1)/lengths[i-1] if i==j else F(0)) + F(1,S))
        assert B[i][j]==predicted,(lengths,i,j,B[i][j],predicted)
    row_norms=[]
    for i in range(m+1):
        value=F(0)
        for j,h in enumerate(lengths,1):
            # Two endpoints of a kernel with x fixed to a vertex.
            a=B[i][0]
            b=B[i][j]
            value += h*integ_abs(a,b)
        row_norms.append(value)
    expected=[F(5,3)] + [F(7*S+3*h,3*(S+h)) for h in lengths]
    assert row_norms==expected,(lengths,row_norms,expected)
    assert max(row_norms)==F(7*S+3*min(lengths),3*(S+min(lengths)))
    assert max(row_norms)>row_norms[0] if m>=2 else True
    return 1


def run():
    rng=random.Random(20261017)
    n=0
    for m in range(2,13):
        for _ in range(180):
            vals=[F(rng.randrange(1,200),rng.randrange(1,100)) for j in range(m)]
            n+=evaluate(vals)
    assert evaluate([F(1),F(1),F(1)])==1
    assert F(7*3+3, 3*(3+1))==2
    assert F(7*4+3,3*(4+1))>2
    print('PASS',n+2,'exact rational star systems; matrix inverse, integrated absolute kernel and sharp norm')
if __name__=='__main__':run()
