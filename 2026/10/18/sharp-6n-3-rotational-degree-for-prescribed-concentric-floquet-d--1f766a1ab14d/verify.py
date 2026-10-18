#!/usr/bin/env python3
"""Exact polynomial identity checks for prescribed concentric periodic orbits."""
from fractions import Fraction as F
from math import factorial


def add(p,q):
    r=[F(0)]*max(len(p),len(q))
    for i,v in enumerate(p):r[i]+=v
    for i,v in enumerate(q):r[i]+=v
    return trim(r)


def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p


def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return trim(r)


def scale(p,c): return trim([c*v for v in p])

def evaluate(p,x):
    v=F(0)
    for a in reversed(p):v=v*x+a
    return v


def derivative(p):return trim([i*p[i] for i in range(1,len(p))] or [F(0)])


def interpolate_square(nodes,values):
    out=[F(0)]
    bas=[]
    for i,s in enumerate(nodes):
        numerator=[F(1)]
        denom=F(1)
        for j,t in enumerate(nodes):
            if j!=i:
                numerator=mul(numerator,[-t,F(1)])
                denom*=s-t
        l=scale(numerator, F(1)/denom)
        bas.append(l)
        out=add(out,scale(mul(l,l),values[i]))
    for i,s in enumerate(nodes):
        assert all(evaluate(b,s)==(j==i) for j,b in enumerate(bas))
        assert evaluate(out,s)==values[i]
    return out,bas


def check(nodes, periods, target_h):
    n=len(nodes)
    assert n and all(s>0 for s in nodes)
    assert all(nodes[i]<nodes[i+1] for i in range(n-1))
    A=[F(1)]
    for s in nodes:A=mul(A,[-s,F(1)])
    H,_=interpolate_square(nodes,target_h)
    Omega,_=interpolate_square(nodes,[F(1)/t for t in periods])
    Q=mul(A,H)
    assert len(Q)-1<=3*n-2
    assert len(Omega)-1<=2*n-2
    for i,s in enumerate(nodes):
        assert evaluate(Q,s)==0
        assert evaluate(Omega,s)==1/periods[i]
        # omega is 2*pi times Omega; period physical T_i=1/Omega(s_i)
        exponent_scaled=2*s*evaluate(derivative(Q),s)*periods[i]
        expected=2*s*evaluate(derivative(A),s)*target_h[i]*periods[i]
        assert exponent_scaled==expected and exponent_scaled!=0
        assert (exponent_scaled>0)==(((-1)**(n-i-1))>0)
    # sum of positive squares is nonzero on all real points, not a proof for all points.
    for x in [F(k,4) for k in range(-30,71)]:
        assert evaluate(H,x)>0 and evaluate(Omega,x)>0
    return Q,H,Omega


def test_lower_n2():
    # With nodes s1=1,s2=4 and h=(1,1/10), an affine H exists
    # but has negative leading coefficient and is negative for sufficiently large s.
    nodes=[F(1),F(4)]
    h1,h2=F(1),F(1,10)
    slope=(h2-h1)/(nodes[1]-nodes[0])
    assert slope==-F(3,10)
    root=nodes[0]-h1/slope
    assert root==F(13,3)>nodes[1]


def main():
    for n in range(1,7):
        nodes=[F((i+1)**2) for i in range(n)]
        periods=[F(2*i+3, i+1) for i in range(n)]
        h=[F(i+1,i+3) for i in range(n)]
        check(nodes,periods,h)
        check(nodes,periods,[F(1)]+[F(1,10**n)]*(n-1))
    test_lower_n2()
    print('VERIFY_OK')


if __name__=='__main__':main()
