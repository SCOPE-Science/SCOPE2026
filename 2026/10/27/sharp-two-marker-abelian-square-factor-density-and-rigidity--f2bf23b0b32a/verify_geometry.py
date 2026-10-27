#!/usr/bin/env python3
"""Independent exact-rational polygon check of the strip area identity.
This is corroboration, not a substitute for the written all-parameter proof.
"""
from fractions import Fraction

def clip(poly, f):
    out=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        fp=f(p); fq=f(q)
        if fp<=0: out.append(p)
        if (fp<0 and fq>0) or (fp>0 and fq<0):
            t=fp/(fp-fq)
            out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
    return out

def reference_area(a,b,c):
    a,b,c=map(Fraction,(a,b,c))
    poly=[(Fraction(0),Fraction(0)),(a,Fraction(0)),(a,c),(Fraction(0),c)]
    poly=clip(poly,lambda p:p[0]-p[1]-b)
    poly=clip(poly,lambda p:p[1]-p[0]-b)
    if len(poly)<3:return Fraction(0)
    return abs(sum(x*y2-x2*y for (x,y),(x2,y2) in zip(poly,poly[1:]+poly[:1])))/2

def expression(a,b,c):
    if a>c:a,c=c,a
    assert b<=a
    s=a+b+c;h=c-a
    return Fraction(b*s-2*b*b,1)-Fraction(h*h,2)+Fraction(max(h-b,0)**2,2)

def main():
    tested=0
    for a in range(21):
        for b in range(21):
            for c in range(21):
                area=reference_area(a,b,c)
                s=a+b+c
                assert 8*area<=s*s,(a,b,c,area)
                if b<=min(a,c): assert area==expression(a,b,c),(a,b,c,area,expression(a,b,c))
                if s>0 and 8*area==s*s:
                    assert 8*a==3*s and 4*b==s and 8*c==3*s,(a,b,c)
                tested+=1
    print(f'GEOMETRIC AREA CORROBORATED on {tested} nonnegative triples')
    print('SUCCESS')
if __name__=='__main__':main()
