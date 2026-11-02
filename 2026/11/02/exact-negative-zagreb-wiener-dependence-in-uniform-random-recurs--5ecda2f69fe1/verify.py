"""Independent exact-arithmetic finite checks of the displayed Zagreb--Wiener formulas.

This finite test does not establish the all-size theorem; see the analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial


def harmonic(n, power=1):
    return sum((F(1, j**power) for j in range(1, n+1)), F(0))


def closed_cov(n):
    h=harmonic(n); h2=harmonic(n, 2)
    return n*(n+1)*(4*h2 - 2*h + 1 + F(6, n+1)
                     -4*h*(F(1,n)+F(1,n+1)))


def wiener_mean(n):
    return n*(n+1)*harmonic(n) - 2*n*n


def evaluate(parents):
    n=len(parents)+1
    a=[[] for _ in range(n)]
    for v,p in enumerate(parents,start=1):
        a[v].append(p)
        a[p].append(v)
    deg=[len(neighbors) for neighbors in a]
    transmissions=[]
    for s in range(n):
        distances=[-1]*n
        distances[s]=0
        queue=[s]
        for v in queue:
            for z in a[v]:
                if distances[z] == -1:
                    distances[z]=distances[v]+1
                    queue.append(z)
        transmissions.append(sum(distances))
    z=sum(x*x for x in deg)
    w=sum(transmissions)//2
    return n, deg, transmissions, z, w


def main():
    trees=0
    checks=0
    for n in range(2,9):
        m_z=m_w=m_zw=0
        count=0
        for parents in product(*(range(v) for v in range(1,n))):
            k,deg,d,z,w=evaluate(parents)
            count+=1
            trees+=1
            assert k==n
            assert sum(x*y for x,y in zip(deg,d))==4*w-n*(n-1)
            checks+=1
            assert w<=n*(n*n-1)//6
            checks+=1
            dz=[2*x+2 for x in deg]
            dw=[n+y for y in d]
            delta_cov=(F(sum(x*y for x,y in zip(dz,dw)),n)
                      -F(sum(dz)*sum(dw),n*n))
            assert delta_cov==F(8*w,n*n)-2*(n-1)
            checks+=1
            assert delta_cov<0 if n>=3 else delta_cov==0
            checks+=1
            m_z+=z
            m_w+=w
            m_zw+=z*w
        assert count==factorial(n-1)
        checks+=1
        assert F(m_w,count)==wiener_mean(n)
        checks+=1
        assert F(m_zw,count)-F(m_z*m_w,count*count)==closed_cov(n)
        checks+=1
    for n in range(2,301):
        val=closed_cov(n)
        rhs=F(n+2,n)*val+F(8*(n+1),n)*harmonic(n)-2*n-14
        assert closed_cov(n+1)==rhs
        checks+=1
        assert val<0 if n>=4 else val==0
        checks+=1
    print(f'PASS trees={trees} exact_assertions={checks} exhaustive_orders=2..8 recurrence_orders=2..300')


if __name__ == '__main__':
    main()
