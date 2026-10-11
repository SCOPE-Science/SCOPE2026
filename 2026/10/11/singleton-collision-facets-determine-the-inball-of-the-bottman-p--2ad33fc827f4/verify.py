#!/usr/bin/env python3
from fractions import Fraction

def runs(mask, length):
    out=[]
    i=0
    while i<length:
        if (mask>>i)&1:
            j=i
            while j<length and ((mask>>j)&1):
                j+=1
            out.append(j-i)
            i=j
        else:
            i+=1
    return out

checks=0
for m in range(3,10):
    for n in range(3,10):
        H=n-1
        K=m-1
        d=H+K
        C=(n*(n-1)//2)*(m*(m-1)//2)+n*(n-1)//2+m*(m-1)//2
        r2=Fraction((C-d)*(C-d), d*(d-1))

        for length in range(1,H):
            h=length*(length+1)//2
            t=length
            slack=Fraction(t*C,d)-h
            norm2=Fraction(t*(d-t),d)
            d2=slack*slack/norm2
            assert d2>=r2
            assert (d2==r2)==(length==1)
            checks+=1

        for length in range(1,K):
            h=length*(length+1)//2
            t=length
            slack=Fraction(t*C,d)-h
            norm2=Fraction(t*(d-t),d)
            d2=slack*slack/norm2
            assert d2>=r2
            assert (d2==r2)==(length==1)
            checks+=1

        for hm in range(1,1<<H):
            hr=runs(hm,H)
            R=sum(hr)
            U=sum(r*(r+1)//2 for r in hr)
            for vm in range(1,1<<K):
                vr=runs(vm,K)
                Q=sum(vr)
                if R==H and Q==K:
                    continue
                V=sum(q*(q+1)//2 for q in vr)
                t=R+Q
                h=U+V+U*V
                slack=Fraction(t*C,d)-h
                norm2=Fraction(t*(d-t),d)
                d2=slack*slack/norm2
                assert d2>r2,(m,n,hm,vm,hr,vr,d2,r2)
                checks+=1

        singleton_slack=Fraction(C,d)-1
        singleton_norm2=Fraction(d-1,d)
        assert singleton_slack*singleton_slack/singleton_norm2==r2

print(f"VERIFY_OK Bottman-Poliakova-constrainahedron m,n=3..9 facet_checks={checks} exact=yes")
