class BinaryField:
    def __init__(self,f,modulus):
        self.f=f
        self.q=1<<f
        self.modulus=modulus
        assert modulus>>(f)==1
    def add(self,a,b):
        return a^b
    def mul(self,a,b):
        out=0
        x=a
        y=b
        while y:
            if y&1:
                out^=x
            y>>=1
            x<<=1
            if x&(1<<self.f):
                x^=self.modulus
        return out & (self.q-1)
    def pow(self,a,n):
        r=1
        while n:
            if n&1:
                r=self.mul(r,a)
            a=self.mul(a,a)
            n//=2
        return r
    def inv(self,a):
        assert a
        return self.pow(a,self.q-2)
    def sigma(self,a):
        return self.mul(a,a)

def radd(F,x,y):
    return (F.add(x[0],y[0]),F.add(x[1],y[1]))

def rmul(F,x,y):
    a,b=x
    c,d=y
    return (
        F.mul(a,c),
        F.add(F.mul(a,d),F.mul(b,F.sigma(c))),
    )

def rinv(F,x):
    a,b=x
    ai=F.inv(a)
    # In characteristic two, minus equals plus.
    d=F.mul(ai,F.mul(b,F.sigma(ai)))
    y=(ai,d)
    assert rmul(F,x,y)==(1,0)
    assert rmul(F,y,x)==(1,0)
    return y

def agl_mul(F,x,y):
    t,a=x
    s,c=y
    return (F.add(t,F.mul(a,s)),F.mul(a,c))

def phi(F,x):
    t,a=x
    ai=F.inv(a)
    return (ai,F.mul(t,F.sigma(ai)))

fields=[
    BinaryField(1,0b11),       # x+1
    BinaryField(2,0b111),      # x^2+x+1
    BinaryField(3,0b1011),     # x^3+x+1
    BinaryField(4,0b10011),    # x^4+x+1
]

for F in fields:
    q=F.q
    ring=[(a,b) for a in range(q) for b in range(q)]
    units=[x for x in ring if x[0]!=0]
    assert len(units)==q*(q-1)

    # Verify every displayed inverse.
    for x in units:
        rinv(F,x)

    agl=[(t,a) for t in range(q) for a in range(1,q)]
    images={phi(F,x) for x in agl}
    assert images==set(units)

    # Exhaustive homomorphism check.
    for x in agl:
        for y in agl:
            assert phi(F,agl_mul(F,x,y))==rmul(F,phi(F,x),phi(F,y))

    # Check inverse-scalar conjugation on the radical.
    for a in range(1,q):
        aa=(a,0)
        aainv=rinv(F,aa)
        for b in range(q):
            lhs=rmul(F,rmul(F,aa,(1,b)),aainv)
            rhs=(1,F.mul(b,F.inv(a)))
            assert lhs==rhs

    print({
        "q":q,
        "ring_order":q*q,
        "unit_order":len(units),
        "agl_order":len(agl),
    })

print("VERIFY_OK")
