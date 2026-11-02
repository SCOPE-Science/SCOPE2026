"""Exact finite-field checks for simultaneous irreducibility of quadratic-composition quartics.

Requires only Python 3 standard library. Run: python verify.py
"""

class Field:
    def __init__(self, p, delta=None):
        self.p = p
        self.delta = delta
        self.q = p if delta is None else p*p
        if delta is not None:
            assert pow(delta, (p-1)//2, p) == p-1

    def add(self, x, y):
        p = self.p
        if self.delta is None:
            return (x+y) % p
        return ((x%p+y%p)%p) + p*((x//p+y//p)%p)

    def neg(self, x):
        p = self.p
        if self.delta is None:
            return (-x)%p
        return (-x%p) + p*((-(x//p))%p)

    def sub(self, x, y):
        return self.add(x,self.neg(y))

    def mul(self, x, y):
        p = self.p
        if self.delta is None:
            return x*y%p
        a,b=x%p,x//p
        c,d=y%p,y//p
        return (a*c+self.delta*b*d)%p + p*((a*d+b*c)%p)

    def power(self, x, e):
        out=1
        while e:
            if e&1: out=self.mul(out,x)
            x=self.mul(x,x)
            e>>=1
        return out

    def inv(self, x):
        assert x
        return self.power(x,self.q-2)

    def chi(self, x):
        if not x: return 0
        return 1 if self.power(x,(self.q-1)//2)==1 else -1


def trim(a):
    while a and a[-1]==0: a.pop()
    return a

def padd(F,a,b):
    return trim([F.add(a[i] if i<len(a) else 0,b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def psub(F,a,b):
    return trim([F.sub(a[i] if i<len(a) else 0,b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def pmul(F,a,b):
    if not a or not b: return []
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            z[i+j]=F.add(z[i+j],F.mul(x,y))
    return trim(z)

def premainder(F,a,b):
    assert b
    a=a[:]
    inv=F.inv(b[-1])
    while len(a)>=len(b):
        factor=F.mul(a[-1],inv)
        offset=len(a)-len(b)
        for i,z in enumerate(b):
            a[i+offset]=F.sub(a[i+offset],F.mul(factor,z))
        trim(a)
    return a

def pgcd(F,a,b):
    while b:
        a,b=b,premainder(F,a,b)
    return a

def ppowmod(F,a,e,m):
    z=[1]
    while e:
        if e&1: z=premainder(F,pmul(F,z,a),m)
        a=premainder(F,pmul(F,a,a),m)
        e>>=1
    return z

def quartic(F,a,b,c):
    h=[b,a,1]
    return padd(F,pmul(F,h,h),[c])

def irreducible_quartic(F,poly):
    # A reducible degree-4 polynomial has a factor of degree 1 or 2.
    # These are exactly the irreducible factors of X^(q^2)-X.
    xp=ppowmod(F,[0,1],F.q**2,poly)
    test=psub(F,xp,[0,1])
    return len(pgcd(F,poly,test))==1

def elliptic_order(F,c,d):
    # Count affine pairs directly, then add one point at infinity.
    sqr=[F.mul(y,y) for y in range(F.q)]
    total=1
    for x in range(F.q):
        rhs=F.mul(x,F.mul(F.add(x,c),F.add(x,d)))
        total += sqr.count(rhs)
    return total

def exact_count(F,c,d):
    cnt=0
    for a in range(F.q):
        for b in range(F.q):
            first=irreducible_quartic(F,quartic(F,a,b,c))
            second=irreducible_quartic(F,quartic(F,a,b,d))
            if first and second:
                cnt+=1
    return cnt

def expected(F,c,d):
    if c==0 or d==0 or F.chi(F.neg(c))!=-1 or F.chi(F.neg(d))!=-1:
        return 0,None
    if c==d:
        return F.q*(F.q+1)//2,None
    E=elliptic_order(F,c,d)
    assert E%4==0
    return F.q*(E//4),E

def run():
    fields=[Field(3),Field(5),Field(7),Field(11),Field(13),Field(17),Field(19),Field(3,2),Field(5,2),Field(7,3)]
    cases=0
    tested_quartics=0
    examples=[]
    for F in fields:
        ok=[c for c in range(1,F.q) if F.chi(F.neg(c))==-1]
        pairs=[]
        if len(ok)>1:
            pairs.extend((ok[0],c) for c in ok[1:4])
        pairs.append((ok[0],ok[0]))
        pairs.extend([(0,ok[0]),(ok[0],0)])
        non=[c for c in range(1,F.q) if F.chi(F.neg(c))==1]
        if non: pairs.extend([(non[0],ok[0]),(ok[0],non[0])])
        for c,d in pairs:
            actual=exact_count(F,c,d)
            wanted,E=expected(F,c,d)
            assert actual==wanted,(F.q,c,d,actual,wanted,E)
            if E is not None:
                assert abs(E-(F.q+1))**2<=4*F.q,(F.q,E)
            cases+=1
            tested_quartics+=2*F.q*F.q
            if E is not None and len(examples)<12:
                examples.append((F.q,c,d,actual,E))
    print('VERIFY_OK fields=%d cases=%d direct_quartic_tests=%d' % (len(fields),cases,tested_quartics))
    print('Sample (q,c,d,count,elliptic_order):',examples)

if __name__=='__main__': run()
