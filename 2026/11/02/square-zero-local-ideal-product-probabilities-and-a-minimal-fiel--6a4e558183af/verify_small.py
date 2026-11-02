#!/usr/bin/env python3
"""Independent small-ring ideal enumeration for the minimality bound."""
from fractions import Fraction

def ideals(n,add,mul):
    found=[]
    for mask in range(1,1<<n):
        if not (mask&1): continue
        I=[i for i in range(n) if mask&(1<<i)]
        if any(not mask&(1<<add(a,b)) for a in I for b in I): continue
        if any(not mask&(1<<mul(r,a)) for r in range(n) for a in I): continue
        found.append(tuple(I))
    return found

def run(title,n,add,mul,expected):
    assert all(add(add(a,b),c)==add(a,add(b,c)) for a in range(n) for b in range(n) for c in range(n))
    assert all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a in range(n) for b in range(n) for c in range(n))
    li=ideals(n,add,mul)
    z=sum(all(mul(x,y)==0 for x in I for y in J) for I in li for J in li)
    v=Fraction(z,len(li)**2)
    assert v==expected,(title,v,expected)
    print(title,'ideals',len(li),'zero pairs',z,'total pairs',len(li)**2,'probability',str(v))

def main():
    run('Z/4',4,lambda a,b:(a+b)%4,lambda a,b:(a*b)%4,Fraction(2,3))
    def dualmul(a,b):
        x,y=a&1,a>>1
        u,v=b&1,b>>1
        return x*u+2*((x*v+y*u)%2)
    run('F2[t]/t^2',4,lambda a,b:a^b,dualmul,Fraction(2,3))
    run('F2xF2',4,lambda a,b:a^b,lambda a,b:a&b,Fraction(9,16))
    run('Z/6',6,lambda a,b:(a+b)%6,lambda a,b:(a*b)%6,Fraction(9,16))
    print('VERIFY_OK')

if __name__=='__main__': main()
