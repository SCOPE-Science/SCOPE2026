"""Exact-arithmetic and numerical consistency checks for random-step Verlet oscillator."""
from fractions import Fraction as F
from itertools import product
from math import isclose


def matmul(A, B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]


def transpose(A):
    return [list(x) for x in zip(*A)]


def det3(A):
    a,b,c=A[0];d,e,f=A[1];g,h,i=A[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def subid(A):
    return [[F(int(i==j))-A[i][j] for j in range(3)] for i in range(3)]


def verlet(h):
    a=1-h*h/2; k=1-h*h/4
    return [[a,h],[-h*k,a]]


def lift(h):
    a,b=verlet(h)[0];c,d=verlet(h)[1]
    return [[a*a,2*a*b,b*b],[a*c,a*d+b*c,b*d],[c*c,2*c*d,d*d]]


def matvec(A,v):
    return [sum(a*b for a,b in zip(row,v)) for row in A]


def mix(A,B,p):
    return [[p*a+(1-p)*b for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]


def perturb_second(h):
    a=1-h*h/2; k=1-h*h/4
    c=-h*k; cp=-1+3*h*h/4; cpp=3*h/2
    ac_second=-c-2*h*cp+a*cpp
    return [[3*h*h-2,-6*h,F(2)],
            [ac_second,6*h*h-4,-3*h],
            [2*cp*cp+2*c*cpp,2*ac_second,3*h*h-2]]


def char_poly_value(T,x):
    return det3([[x*int(i==j)-float(T[i][j]) for j in range(3)] for i in range(3)])


def top_positive_root(T):
    lo,hi=1.0,2.0
    assert char_poly_value(T,lo)<0
    while char_poly_value(T,hi)<=0: hi*=2
    for _ in range(75):
        mid=(lo+hi)/2
        if char_poly_value(T,mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2


def test():
    count=0
    for h in [F(1,5),F(1,2),F(2,3),F(1),F(3,2)]:
        a=verlet(h);k=1-h*h/4
        assert matmul(a,matmul([[F(1)/k,F(0)],[F(0),F(1)]],transpose(a))) == [[F(1)/k,F(0)],[F(0),F(1)]]
        assert matmul(transpose(a),matmul([[k,F(0)],[F(0),F(1)]],a)) == [[k,F(0)],[F(0),F(1)]]
        l=[k,F(0),F(1)];r=[F(1)/k,F(0),F(1)]
        T=lift(h)
        assert matvec(T,r)==r
        assert matvec(transpose(T),l)==l
        numerator=sum(l[i]*matvec(perturb_second(h),r)[i] for i in range(3))
        assert numerator/4==h**4/(2*(4-h*h))
        count+=1
    for u,v,p in product([F(1,5),F(1,3),F(1,2),F(3,4),F(1),F(7,5),F(9,5)],
                         [F(1,6),F(1,2),F(4,5),F(3,2)],
                         [F(1,5),F(1,2),F(4,5)]):
        T=mix(lift(u),lift(v),p)
        expected=-p*(1-p)*u*u*v*v*(u*u-v*v)**2/8
        assert det3(subid(T))==expected
        if u != v: assert expected<0
        count+=1
    # Independent finite-tree moment replay (not an infinite-time proof).
    u,v,p=F(1,2),F(3,2),F(1,3)
    T=mix(lift(u),lift(v),p)
    initial=[F(1),F(2),F(4)]
    M=initial[:]
    for n in range(1,8):
        M=matvec(T,M)
        brute=F(0)
        for bits in product([0,1],repeat=n):
            z=[F(1),F(2)]
            weight=F(1)
            for bit in bits:
                z=matvec(verlet(u if bit==0 else v),z)
                weight*=p if bit==0 else 1-p
            brute+=weight*(z[0]**2+z[1]**2)
        assert brute==M[0]+M[2]
    # Near-deterministic perturbation coefficient, checked numerically only.
    for h in [0.5,1.0,1.5]:
        predicted=h**4/(2*(4-h*h))
        ratios=[]
        for delta in [0.025,0.015,0.008]:
            T=mix(lift(h+delta),lift(h-delta),0.5)
            growth=top_positive_root(T)
            assert growth>1
            ratios.append((growth-1)/(delta*delta))
        assert abs(ratios[-1]-predicted)/predicted<0.004,(h,ratios,predicted)
        print('h',h,'perturbation-coefficient',predicted,'observed',ratios)
    print('VERIFY_OK',count,'exact determinant and invariant-form checks; 7 exhaustive path-depth checks; 9 growth-asymptotic checks')


if __name__=='__main__':
    test()
