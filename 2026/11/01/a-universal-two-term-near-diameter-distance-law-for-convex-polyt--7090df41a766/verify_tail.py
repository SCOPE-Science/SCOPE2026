#!/usr/bin/env python3
"""Exact local-cone moment identities for two-point distance tails.

This verifies algebraic specializations and independently evaluates the
near-diameter planar square integral.  The all-polytope theorem uses its
analytic localization and radial-integration proof, not finite testing.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial, sqrt


def box_t_formula(lengths):
    """Two-term ratio from the independent coordinate-difference density."""
    d = len(lengths)
    sq_d = sum((L*L for L in lengths), F(0))
    inv_sq = sum((1/(L*L) for L in lengths), F(0))
    return (3*sq_d*inv_sq - d*(2*d+1)) / F(2*d+1)


def box_t_from_cone_moments(lengths):
    """The numerator of D times T from uniform height-one sections."""
    d=len(lengths)
    sq_d=sum((L*L for L in lengths), F(0))
    inv_sq=sum((1/(L*L) for L in lengths), F(0))
    squared_mean_transverse=sq_d*inv_sq/F(d*d)-1
    second_transverse=2*sq_d*inv_sq/F(d*(d+1))-1
    # The inward section at the opposite corner is the negative of this one.
    cross=-squared_mean_transverse
    return (d*(d+1)*2*second_transverse-2*d*d*cross)/F(2*(2*d+1))


def cone_section_ratios_simplex(d):
    """Obtain D*T for a standard regular d-simplex via Gram matrices."""
    # Work in R^(d+1), P=conv(e_0,...,e_d), D=sqrt(2).
    D=sqrt(2.)
    dim=d+1
    e=[-1/D,1/D]+[0.]*(d-1)
    def directions(apex,other):
        vectors=[]
        for j in range(dim):
            if j==apex:continue
            v=[0.]*dim
            v[j]=1.;v[apex]=-1.
            h=sum(ei*vi for ei,vi in zip(e,v))
            if apex==1:h=-h
            assert h>0
            vectors.append([vi/h for vi in v])
        return vectors
    def mom(vecs):
        S=[sum(v[i] for v in vecs) for i in range(dim)]
        mean=[x/d for x in S]
        # height is +1 at apex a, -1 at apex b; tangent projected mean
        proj=sum(ei*mi for ei,mi in zip(e,mean))
        transmean=[mi-proj*ei for ei,mi in zip(e,mean)]
        m2=(sum(sum(x*x for x in v) for v in vecs)+sum(x*x for x in S))/(d*(d+1))-1
        return transmean,m2
    mu_a,M_a=mom(directions(0,1))
    mu_b,M_b=mom(directions(1,0))
    dot=sum(x*y for x,y in zip(mu_a,mu_b))
    T=(d*(d+1)*(M_a+M_b)-2*d*d*dot)/(2*D*(2*d+1))
    return T*D


def square_direct_integral_tail(t, n=8000):
    """Independent numerical quadrature using triangular coordinate densities.

    Unit square, distance D=sqrt(2); near maximal-distance corners.
    Integrate alpha_1 alpha_2, with 0<=alpha_i<=1 and
    (1-alpha_1)^2+(1-alpha_2)^2>(sqrt(2)-t)^2.
    """
    from math import sqrt
    D=sqrt(2.)
    limit=(D-t)**2
    # integrate alpha_1 in [0, 1-(D-t-1)] and alpha_2 in [0,threshold]
    hi=max(0.,min(1.,2-D+t))
    def fun(alpha):
        rhs=limit-(1-alpha)**2
        cap=1.-sqrt(max(0.,rhs))
        cap=max(0.,min(1.,cap))
        # alpha_1 density times integral alpha_2 d alpha_2
        return alpha*cap*cap/2
    h=hi/n
    integ=(fun(0)+fun(hi)+4*sum(fun((i+.5)*h) for i in range(n)) + 2*sum(fun(i*h) for i in range(1,n)))*h/6
    return 4*integ  # four diameter-corner sign pairs


def main():
    total=0
    for d in range(2,12):
        for lengths in product([F(1),F(2),F(3,2)],repeat=min(d,5)):
            if d>5:
                lengths=tuple(lengths)+(F(1),)*(d-5)
            a=box_t_formula(lengths)
            b=box_t_from_cone_moments(lengths)
            assert a==b,(d,lengths,a,b)
            assert a>=F(d*(d-1),2*d+1)
            equality=(a==F(d*(d-1),2*d+1))
            assert equality==(len(set(lengths))==1)
            total+=1
    for d in range(2,18):
        value=cone_section_ratios_simplex(d)
        target=3*(d-1)/(2*d+1)
        assert abs(value-target)<4e-13,(d,value,target)
        total+=1
    # Independent spatial integration checks the universal coefficient for
    # the square, despite the main novel theorem being formulated for d>=3.
    D=sqrt(2.)
    c0=F(2,3) # 2^2 D^4/(4)! for [0,1]^2
    T=float(F(2,5))/D
    for t in [0.05,0.025,0.0125,0.00625]:
        direct=square_direct_integral_tail(t)
        predicted=float(c0)*t**4*(1+T*t)
        rel_error=abs(direct-predicted)/(float(c0)*t**4)
        # The uncomputed remainder is O(t^2) as t -> 0.
        assert rel_error < 0.7*t*t,(t,rel_error)
        total+=1
    print('PASS exact cone/box identities, rigidity, simplex benchmark, square direct integration:',total,'instances')

if __name__=='__main__':main()
