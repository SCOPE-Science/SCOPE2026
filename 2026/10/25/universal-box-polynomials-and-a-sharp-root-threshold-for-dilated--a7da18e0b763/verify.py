#!/usr/bin/env python3
"""Exact finite checks for Ehrhart and local box polynomials of dilated empty tetrahedra.
No external dependencies. The general proof is in RESULT.md."""
from fractions import Fraction
from math import comb,gcd

def predicted_h(m,r):
    u=m*r*(r*r-1)//6
    assert m*r*(r*r-1)%6==0
    return [1, u+(r-1)*(r+3), m*r*(2*r*r+1)//3-4*r+3, u-(r-1)**2]

def predicted_box(m,r):
    a=m*r*(r*r-1)//6-(r-1)**2
    b=m*r*(2*r*r+1)//3-2*r*r+2*r-1
    return [0,a,b,a]

def count_closed(m,p,r,t):
    # S=conv(0,(1,0,0),(0,1,0),(1,p,m)), dilation r*t.
    R=r*t
    if R==0:return 1
    ans=0
    for z in range(R*m+1):
        q=Fraction(z,m)
        # barycentric coefficient wrt integer-dilated simplex:
        # lambda3=z/m, lambda1=x-q, lambda2=y-p*q, lambda0=R-x-y+p*q.
        for x in range(R+1):
            if x<q:continue
            for y in range(R*p+1):
                if y<p*q:continue
                if R-x-y+p*q>=0:
                    ans+=1
    return ans

def count_box(m,p,r):
    out=[0,0,0,0]
    for z in range(1,r*m):
        q=Fraction(z,r*m)
        for x in range(0,2*r+2):
            lam1=Fraction(x,r)-q
            if not 0<lam1<1:continue
            for y in range(0,r*(p+1)+2):
                lam2=Fraction(y,r)-p*q
                if not 0<lam2<1:continue
                for height in (1,2,3):
                    lam0=height-lam1-lam2-q
                    if 0<lam0<1:out[height]+=1
    return out

def h_from_counts(m,p,r):
    f=[count_closed(m,p,r,t) for t in range(4)]
    return [sum((-1)**(j-i)*comb(4,j-i)*f[i] for i in range(j+1)) for j in range(4)]

def main():
    volume_classes=0; tested=0; cnt_box=0
    for m in range(2,11):
        for p in range(1,m):
            if gcd(p,m)!=1:continue
            volume_classes+=1
            for r in range(1,5):
                expected=predicted_h(m,r)
                observed=h_from_counts(m,p,r)
                assert observed==expected,(m,p,r,observed,expected)
                eb=predicted_box(m,r)
                ob=count_box(m,p,r)
                assert ob==eb,(m,p,r,ob,eb)
                tested+=1;cnt_box+=sum(ob)
                if r>=2:
                    a,b=eb[1],eb[2]
                    assert a>0 and b>2*a
                else:
                    assert eb==[0,0,m-1,0]
    for m in range(2,101):
        assert predicted_h(m,2)==[1,m+5,6*m-5,m-1]
        assert predicted_box(m,2)==[0,m-1,6*m-5,m-1]
    print(f'EXACT_OK parameter_cases={tested} empty_tetra_shapes={volume_classes} box_points={cnt_box} hstar_interpolation=True')
if __name__=='__main__':main()
