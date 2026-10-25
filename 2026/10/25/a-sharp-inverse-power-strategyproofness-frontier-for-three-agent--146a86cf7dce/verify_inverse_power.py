"""Exact small-metric checks for a three-agent inverse-power omission theorem.

This program is ancillary evidence; general claims use the written proof.
Run: python3 verify_inverse_power.py
"""
from itertools import product
from fractions import Fraction
from decimal import Decimal, getcontext


def distances(edge_lengths):
    d = [[0]*4 for _ in range(4)]
    pairs = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    for (i,j),w in zip(pairs,edge_lengths): d[i][j]=d[j][i]=w
    for k in range(4):
        for i in range(4):
            for j in range(4): d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d


def omit_weights(dists,p):
    if p==0:
        return [Fraction(1,3)]*3
    wi=[Fraction(1, z**p) for z in dists]
    z=sum(wi)
    return [w/z for w in wi]


def compare_truth_deviation(D,p):
    # True reports: x0,x1,x2; x0 instead reports x3.
    a,b,h = D[0][1],D[0][2],D[0][3]
    r = min(a,b)
    before=[r,min(a,D[1][2]),min(b,D[1][2])]
    after=[min(D[3][1],D[3][2]),min(D[3][1],D[1][2]),min(D[3][2],D[1][2])]
    w=omit_weights(before,p)
    wp=omit_weights(after,p)
    truth=w[0]*r
    dev=wp[0]*r+wp[1]*min(h,b)+wp[2]*min(h,a)
    return truth,dev


def witness(epsilon=Fraction(1,100),h=Fraction(1,1000),p=4):
    # Three true reports (-1, 0, 1+epsilon); the central report is changed to h.
    u=1+h; v=1+epsilon-h
    # 0<h<epsilon/2: nearest-neighbour distances after deviation are (u,u,v).
    pre=Fraction(1,1+1+(1+epsilon)**(-p))
    post=Fraction(1,1+1+(u/v)**p)
    truth=pre
    dev=h+(1-h)*post
    return truth,dev


def main():
    checked=0
    for lens in product(range(1,6),repeat=6):
        D=distances(lens)
        for exponent in (0,1,2,3):
            truth,dev=compare_truth_deviation(D,exponent)
            assert dev>=truth,(lens,exponent,truth,dev)
            checked+=1
    before,after=witness()
    assert after < before
    # Cubic stationarity t^3+6t=4 has a unique root between the rational bounds.
    lo=Fraction(6258,10000);hi=Fraction(6259,10000)
    poly=lambda q:q**3+6*q-4
    assert poly(lo)<0<poly(hi)
    print('PASS exact comparisons:',checked,'across 15625 weighted 4-point complete graphs')
    print('PASS four-agent-free p=4 manipulation on a 3-agent line:')
    print(' truthful cost:',before,' deviating cost:',after, 'strict gain:',before-after)
    getcontext().prec=22
    z=Decimal('0.6258168189584641')
    print('p=3 worst-case social-cost ratio:',(Decimal(2)+z*z)/(Decimal(2)+z**3))
    print('PASS unique stationary root bracket:',lo,hi)

if __name__=='__main__':main()
