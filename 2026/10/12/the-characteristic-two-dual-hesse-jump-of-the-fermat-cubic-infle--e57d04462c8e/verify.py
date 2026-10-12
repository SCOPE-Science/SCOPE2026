#!/usr/bin/env python3
"""Finite-field cross-check for the Fermat-cubic inflection-tangent divisor.
Mathematical proof of the universal assertions is in RESULT.md.
No external dependencies.
"""
from collections import Counter, defaultdict

class Field:
    def __init__(self,p):
        self.p=p
        if p%3==1:
            self.w=next((a,0) for a in range(p) if (a*a+a+1)%p==0 and a!=1)
            self.extension=False
        else:
            self.w=(0,1)
            self.extension=True
        self.zero=(0,0)
        self.one=(1,0)

    def e(self,a):return (a%self.p,0)
    def add(self,a,b):return ((a[0]+b[0])%self.p,(a[1]+b[1])%self.p)
    def neg(self,a):return ((-a[0])%self.p,(-a[1])%self.p)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        p=self.p
        # omega squared = -omega-1
        return ((a[0]*b[0]-a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0]-a[1]*b[1])%p)
    def inv(self,a):
        p=self.p
        n=(a[0]*a[0]-a[0]*a[1]+a[1]*a[1])%p
        assert n
        t=pow(n,-1,p)
        return (((a[0]-a[1])*t)%p,((-a[1])*t)%p)
    def powers(self):
        w=self.w
        assert self.mul(w,self.mul(w,w))==self.one and w!=self.one
        return [self.one,w,self.mul(w,w)]
    def cross(self,a,b):
        return (self.sub(self.mul(a[1],b[2]),self.mul(a[2],b[1])),
                self.sub(self.mul(a[2],b[0]),self.mul(a[0],b[2])),
                self.sub(self.mul(a[0],b[1]),self.mul(a[1],b[0])))
    def dot(self,a,b):
        q=self.zero
        for i in range(3):q=self.add(q,self.mul(a[i],b[i]))
        return q
    def normalize(self,p):
        i=next(i for i in range(3) if p[i]!=self.zero)
        s=self.inv(p[i])
        return tuple(self.mul(s,v) for v in p)
    def rational(self,p):
        return all(v[1]==0 for v in p) if self.extension else True


def verify_prime(p):
    assert p!=3
    k=Field(p)
    z=k.zero;o=k.one
    w=k.powers()
    # The 9 tangent lines: x + w^a y, y + w^a z, z + w^a x.
    lines=([(o,t,z) for t in w]
           +[(z,o,t) for t in w]
           +[(t,z,o) for t in w])
    assert len(set(lines))==9
    incident=defaultdict(set)
    for i in range(9):
        for j in range(i+1,9):
            q=k.normalize(k.cross(lines[i],lines[j]))
            incident[q].update((i,j))
    profile=Counter(map(len,incident.values()))
    expected={3:12} if p==2 else {2:27,3:3}
    assert dict(profile)==expected,(p,profile)
    assert sum(m*(m-1)//2 for m in map(len,incident.values()))==36
    rational_line_points=sum(k.rational(q) for q in incident)
    expected_line_rational=(4 if p==2 else 30 if p%3==1 else 6)
    assert rational_line_points==expected_line_rational,(p,rational_line_points)
    flexes=([k.normalize((k.neg(t),o,z)) for t in w]
          +[k.normalize((z,k.neg(t),o)) for t in w]
          +[k.normalize((o,z,k.neg(t))) for t in w])
    assert len(set(flexes))==9
    assert all(q not in incident for q in flexes)
    for i,q in enumerate(flexes):
        assert [j for j,L in enumerate(lines) if k.dot(L,q)==z]==[i],(p,i)
        x,y,zz=q
        f=k.add(k.add(k.mul(x,k.mul(x,x)),k.mul(y,k.mul(y,y))),k.mul(zz,k.mul(zz,zz)))
        assert f==z
    rational_flexes=sum(k.rational(q) for q in flexes)
    assert rational_flexes==(3 if p%3==2 else 9)
    rational_total=rational_line_points+rational_flexes
    expected_total=7 if p==2 else (39 if p%3==1 else 9)
    assert rational_total==expected_total
    return (p,dict(profile),len(incident)+9,rational_total)

if __name__=='__main__':
    for p in (2,5,7,11,13,17,19,23,31,37,41,43):
        print(verify_prime(p))
    print('VERIFY_OK')
