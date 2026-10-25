#!/usr/bin/env python3
"""Exact rational supplementary checks for a discrete second-difference endpoint theorem.

The general theorem is proved analytically; these tests verify finite examples only.
"""
from fractions import Fraction as F


def data(d):
    if not isinstance(d, int) or d < 1:
        raise ValueError('d must be a positive integer')
    N = d + 2
    k = N // 4
    u, v = k + 1, N - k
    L = v-u
    tau = F(N-4*k-2, 2)
    b = [F(0)] * (N+1)
    for r in range(1, N+1):
        b[r] = F(1) if r < u or r > v else tau if r in (u,v) else F(-1)
    a = [sum((j-r+1)*b[r] for r in range(1,j+1)) for j in range(1,d+1)]
    return N,k,u,v,L,tau,b,a


def quartic_cases(d):
    m, s = divmod(d,4)
    return [F(m*(m+1)*(2*m+1)), F((m+1)**2*(4*m+1),2),
            F(2*(m+1)**3), F((m+1)**2*(4*m+7),2)][s]


def verify(max_dimension=160):
    checks=0
    for d in range(1, max_dimension+1):
        N,k,u,v,L,tau,b,a=data(d)
        assert -1<=tau<=1 and L>=1
        assert sum(b)==0
        assert sum(r*b[r] for r in range(1,N+1))==0
        checks+=3
        ext = [F(0)]*2+a+[F(0)]*2
        # ext index 0 and 1 represent j=-1 and j=0.
        for r in range(1,N+1):
            assert ext[r+1]-2*ext[r]+ext[r-1]==b[r]
            checks+=1
        assert a == a[::-1] and all(x>0 for x in a)
        checks+=1
        for j in range(1,d+1):
            h=lambda r:max(j-r+1,0)
            chord=lambda r:F((v-r)*h(u)+(r-u)*h(v),v-u)
            assert sum(abs(h(r)-chord(r)) for r in range(1,N+1))==a[j-1]
            checks+=1
        P=lambda r:(r-u)*(r-v)
        poly_norm=F(sum(abs(P(r)) for r in range(1,N+1)),2)
        direct=F(k*(k+1)*(2*k+1),6)+F(L*k*(k+1),2)+F(L*(L*L-1),12)
        assert sum(a)==poly_norm==direct==quartic_cases(d)
        checks+=1
    print('PASS: dimensions=1..%s, exact rational assertions=%d'%(max_dimension,checks))


if __name__ == '__main__':
    verify()
