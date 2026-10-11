#!/usr/bin/env python3
"""Exact rational Euclidean minimum-ball witnesses for near-block oriented even cycles."""
from fractions import Fraction as F
from itertools import product


def roots(s):
    n=len(s)
    out=[]
    for i,sign in enumerate(s):
        v=[0]*n; v[i]=sign;v[(i+1)%n]=-sign;out.append(tuple(v))
    return out

def dot(a,b):return sum(x*y for x,y in zip(a,b))

def weighted_center(v,w):
    return tuple(sum(w[i]*v[i][j] for i in range(len(w))) for j in range(len(v)))

def check():
    instances=0
    for k in range(3,71):
        L=k-1;n=2*k
        s=[1]*L+[-1,1]+[-1]*L
        v=roots(s)
        if k==3:
            w=list(map(lambda t:F(t,34),[7,9,1,1,9,7]))
            alpha=F(6,17)
        else:
            alpha=F(3*(2*L+1),L*(L+1)*(L*L+L+1))
            a=F(2*L*L+2*L+1,2*L+1)
            outward=[alpha*F((L+1-j),2)*(a-(L+1-j)) for j in range(1,L+1)]
            w=outward+[F(0),F(0)]+outward[::-1]
            assert all(x>0 for x in outward)
            assert sum(outward)==F(1,2)
        assert len(w)==n
        assert sum(w)==1 and all(x>=0 for x in w)
        c=weighted_center(v,w)
        assert dot(c,c)==alpha
        vals=[dot(c,x) for x in v]
        assert all(x>=alpha for x in vals)
        assert all(vals[i]==alpha for i in range(n) if w[i]>0)
        assert F(2)-dot(c,c)==(F(28,17) if k==3 else
                 F(2)-F(3*(2*k-1),(k-1)*k*(k*k-k+1)))
        if k==3:
            assert all(x==alpha for x in vals)
        else:
            assert [i for i,t in enumerate(vals) if t>alpha]==[L,L+1]
            assert vals[L]==vals[L+1]==w[L-1]
            gap=F(6*(L*L-2*L-1),L*(L+1)*(L*L+L+1))
            assert gap>0 and 2*(vals[L]-alpha)==gap
        # Independent complete distance-radius arithmetic, not just Gram comparisons.
        rs=[dot(tuple(x-y for x,y in zip(z,c)),tuple(x-y for x,y in zip(z,c))) for z in v]
        assert max(rs)==F(2)-alpha
        if k>=4:
            assert [i for i,t in enumerate(rs) if t<max(rs)]==[L,L+1]
        instances+=1
    print('VERIFY_OK nearblock_dimensions=',instances,'exact_rational=True')
if __name__=='__main__':check()
