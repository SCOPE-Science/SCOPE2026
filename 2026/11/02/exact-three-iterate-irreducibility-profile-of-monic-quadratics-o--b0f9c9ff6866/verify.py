#!/usr/bin/env python3
"""Independent finite-field checks of the depth-three quadratic-iterate count.

Only Python standard library is required.  In prime fields, a separate
polynomial-gcd irreducibility test checks the degree-2, 4, and 8 iterates
without using the critical-orbit criterion.
"""


def trim(f):
    f = list(f)
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    return f


def add(a, b, p):
    return trim([( (a[i] if i < len(a) else 0) +
                    (b[i] if i < len(b) else 0)) % p
                 for i in range(max(len(a), len(b)))])


def subtract(a, b, p):
    return add(a, [(-x) % p for x in b], p)


def multiply(a, b, p):
    r = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            r[i+j] = (r[i+j] + ai * bj) % p
    return trim(r)


def remainder(a, divisor, p):
    a, divisor = trim(a), trim(divisor)
    d = len(divisor)-1
    while len(a)-1 >= d and a != [0]:
        shift = len(a)-1-d
        mult = a[-1] * pow(divisor[-1], -1, p) % p
        for j in range(d+1):
            a[shift+j] = (a[shift+j]-mult*divisor[j])%p
        a=trim(a)
    return a


def pgcd(a, b, p):
    a, b = trim(a), trim(b)
    while b != [0]:
        a,b=b,remainder(a,b,p)
    if a == [0]:return a
    return [(c*pow(a[-1],-1,p))%p for c in a]


def powmod(a, e, mod, p):
    out=[1]
    while e:
        if e&1:out=remainder(multiply(out,a,p),mod,p)
        a=remainder(multiply(a,a,p),mod,p)
        e>>=1
    return out


def compose(f,g,p):
    out=[0]
    for a in f[::-1]:
        out=add(multiply(out,g,p),[a],p)
    return out


def directly_irreducible(f,p):
    n=len(f)-1
    assert n in (2,4,8)
    xp=[0,1]
    for k in range(1,n+1):
        xp=powmod(xp,p,f,p)
        if k==n//2 and pgcd(f,subtract(xp,[0,1],p),p)!=[1]:
            return False
    return xp==[0,1]


class Field:
    def __init__(self,p,mod=None):
        self.p=p
        self.mod=mod
        self.degree=(len(mod)-1) if mod is not None else 1
        self.q=p**self.degree

    def digits(self,x):
        return [(x//(self.p**i))%self.p for i in range(self.degree)]

    def encode(self,coeffs):
        return sum((c%self.p)*(self.p**i) for i,c in enumerate(coeffs))

    def add(self,x,y):
        return self.encode([a+b for a,b in zip(self.digits(x),self.digits(y))])

    def neg(self,x):
        return self.encode([-a for a in self.digits(x)])

    def sub(self,x,y):
        return self.add(x,self.neg(y))

    def mul(self,x,y):
        if self.mod is None:return x*y%self.p
        prod=multiply(self.digits(x),self.digits(y),self.p)
        return self.encode(remainder(prod,self.mod,self.p))

    def power(self,x,n):
        acc=1
        while n:
            if n&1:acc=self.mul(acc,x)
            x=self.mul(x,x)
            n>>=1
        return acc

    def chi(self,x):
        if x==0:return 0
        ans=self.power(x,(self.q-1)//2)
        if ans==1:return 1
        assert ans==self.neg(1)
        return -1


def test_field(F,poly_check=False):
    q=F.q
    e=F.chi(F.neg(1))
    c1=c2=c3=0
    triple=ab=ac=bc=0
    for a in range(q):
        for b in range(q):
            d=F.sub(b,a)
            db=F.mul(d,d)
            B=F.add(db,b)
            C=F.add(F.mul(F.add(db,d),F.add(db,d)),b)
            signs=(F.chi(F.neg(b)),F.chi(B),F.chi(C))
            if signs[0]==-1:
                c1+=1
                if signs[1]==-1:
                    c2+=1
                    if signs[2]==-1:c3+=1
            if poly_check:
                # f(X)=(X-a)^2+b over the prime field.
                p=F.p
                f=[(a*a+b)%p,(-2*a)%p,1]
                g=f
                depth=0
                for k in range(3):
                    if not directly_irreducible(g,p):break
                    depth+=1
                    if k<2:g=compose(g,f,p)
                assert depth==sum(signs[0:j]==(-1,)*j for j in (1,2,3)), (p,a,b,depth,signs)
    assert c1==q*(q-1)//2, (q,c1)
    assert c2==(q*q-1)//4, (q,c2)
    assert c3==(q-1)*(q+2+e)//8, (q,c3)
    # Independently test the character-correlation reductions for all (t,x).
    # These are not necessary to run the direct finite-field count above.
    for t in range(q):
        t2=F.mul(t,t)
        tp1=F.add(t,1)
        c=F.mul(t2,F.mul(tp1,tp1))
        for x in range(q):
            A=x;B=F.add(x,t2);C=F.add(x,c)
            aa,bb,cc=F.chi(A),F.chi(B),F.chi(C)
            ab+=aa*bb;ac+=aa*cc;bc+=bb*cc
            triple+=aa*bb*cc
    assert (ab,ac,bc,triple)==(0,q,q,1+e),(q,ab,ac,bc,triple)
    print(f'q={q:<3} char={F.p:<2} e={e:+d} depths={c1},{c2},{c3} correlations=OK'+(' irreducibility=OK' if poly_check else ''))
    return q*q


def main():
    fields=[Field(p) for p in (3,5,7,11,13,17,19,23,29,31)]
    fields += [Field(3,[1,0,1]),Field(5,[2,0,1]),Field(3,[2,2,0,1]),Field(7,[1,0,1])]
    cases=0
    for F in fields:
        cases+=test_field(F,poly_check=F.degree==1 and F.p<=11)
    print(f'VERIFY_OK fields={len(fields)} coefficient_pairs={cases} direct_prime_iterates=4 degree_bound=8')

if __name__=='__main__':
    main()
