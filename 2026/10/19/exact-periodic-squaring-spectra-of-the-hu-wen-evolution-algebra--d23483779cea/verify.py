"""Direct finite-field tests for the squaring dynamics of the Hu--Wen evolution algebra family."""
from math import gcd


class Field:
    def __init__(self, p, degree=1, nonresidue=None):
        self.p, self.degree, self.q = p, degree, p**degree
        self.nr = nonresidue
        if degree == 2:
            assert nonresidue not in {pow(x,2,p) for x in range(p)}

    def pair(self, a):
        return a % self.p, a // self.p

    def add(self, x, y):
        p = self.p
        if self.degree == 1:
            return (x + y) % p
        a,b = self.pair(x)
        c,d = self.pair(y)
        return (a+c)%p + p*((b+d)%p)

    def neg(self, x):
        return self.sub(0,x)

    def sub(self, x, y):
        p=self.p
        if self.degree==1:
            return (x-y)%p
        a,b=self.pair(x)
        c,d=self.pair(y)
        return (a-c)%p + p*((b-d)%p)

    def mul(self, x, y):
        p=self.p
        if self.degree==1:
            return (x*y)%p
        a,b=self.pair(x)
        c,d=self.pair(y)
        return (a*c + self.nr*b*d)%p + p*((a*d+b*c)%p)

    def const(self, v):
        return v % self.p

    def pow(self, x, n):
        z=1
        while n:
            if n&1:
                z=self.mul(z,x)
            x=self.mul(x,x)
            n//=2
        return z

    def inv(self,x):
        assert x
        return self.pow(x,self.q-2)


def square_original(E, lam, v):
    """Evaluate with the original three-square multiplication table, not in square coordinates."""
    x,y,z=v
    x2,y2,z2=E.mul(x,x),E.mul(y,y),E.mul(z,z)
    a=E.sub(E.sub(z2,x2),E.mul(E.const(2),y2))
    b=E.mul(lam,y2)
    c=E.add(E.sub(z2,x2),E.mul(E.sub(lam,E.const(2)),y2))
    return (a,b,c)


def predicted_count(E, lam, m):
    q,p=E.q,E.p
    g=gcd(2**m-1,q-1)
    if lam==E.const(2):
        return 1+q*g if m%p==0 else 1
    t=E.mul(E.const(2),E.inv(lam))
    return 1+g*(q if E.pow(t,m)==1 else 1)


def direct_count(E,lam,m):
    # Every point fixed by a positive iterate belongs to the two-dimensional square E^2.
    total=0
    for a in range(E.q):
        for b in range(E.q):
            start=(a,b,E.add(a,b))
            x=start
            for _ in range(m):
                x=square_original(E,lam,x)
            total += (x==start)
    return total


def number_periodic(E, lam):
    visited=set()
    periodic=set()
    for a in range(E.q):
        for b in range(E.q):
            start=(a,b,E.add(a,b))
            if start in visited:
                continue
            index={}
            orbit=[]
            x=start
            while x not in index and x not in visited:
                index[x]=len(orbit)
                orbit.append(x)
                x=square_original(E,lam,x)
            if x in index:
                periodic.update(orbit[index[x]:])
            visited.update(orbit)
    return len(periodic)


def main():
    fields=[Field(p) for p in (3,5,7,11,13)] + [Field(3,2,2),Field(5,2,2)]
    total=0
    for E in fields:
        q=E.q
        # Choose the full parameter space for small fields and representative parameters for F_25.
        params=list(range(1,q)) if q<=13 else [E.const(1),E.const(2),E.const(3),1+E.p]
        ms=list(range(1,18 if q<=9 else 13))
        if q==25:
            ms=list(range(1,9))
        h=q-1
        while h%2==0:
            h//=2
        for lam in params:
            assert lam
            for m in ms:
                got=direct_count(E,lam,m)
                want=predicted_count(E,lam,m)
                assert got==want,(q,lam,m,got,want)
                total+=1
            got_periodic=number_periodic(E,lam)
            assert got_periodic==1+q*h,(q,lam,got_periodic,1+q*h)
        print('FIELD',q,'PARAMETERS',len(params),'FIXED_ITERATES',len(ms),'PERIODIC_SET_OK')
    # Nonzero exceptional periodic points have no least period prime to the characteristic.
    for E in fields:
        lam=E.const(2)
        if E.q==25:
            continue
        for m in range(1,16):
            if m%E.p:
                assert direct_count(E,lam,m)==1
    print('DIRECT_MULTIPLICATION_PERIODIC_FORMULAE_OK',total)
    print('VERIFY_OK')


if __name__=='__main__':
    main()
