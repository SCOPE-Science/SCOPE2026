from itertools import product
from collections import Counter
from fractions import Fraction

class Field:
    def __init__(self,q):
        self.q=q
        assert q in (2,3,4), "checker supports q=2,3,4"
    def add(self,a,b):
        if self.q==4:
            return a ^ b
        return (a+b)%self.q
    def neg(self,a):
        if self.q==4:
            return a
        return (-a)%self.q
    def sub(self,a,b):
        return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=4:
            return (a*b)%self.q
        # bits encode a0+a1*t over F2, with t^2=t+1.
        a0,a1=a&1,(a>>1)&1
        b0,b1=b&1,(b>>1)&1
        c0=(a0*b0) ^ (a1*b1)
        c1=(a0*b1) ^ (a1*b0) ^ (a1*b1)
        return c0 | (c1<<1)

def build(q,r):
    F=Field(q)
    vecs=list(product(range(q),repeat=r))
    elems=[(a,v,c) for a in range(q) for v in vecs for c in range(q)]
    def vadd(v,w):
        return tuple(F.add(x,y) for x,y in zip(v,w))
    def vneg(v):
        return tuple(F.neg(x) for x in v)
    def smul(a,v):
        return tuple(F.mul(a,x) for x in v)
    def mul(x,y):
        a,v,c=x
        d,w,f=y
        return (F.mul(a,d), vadd(smul(a,w),smul(f,v)), F.mul(c,f))
    def sub(x,y):
        return (F.sub(x[0],y[0]),vadd(x[1],vneg(y[1])),F.sub(x[2],y[2]))
    def comm(x,y):
        return sub(mul(x,y),mul(y,x))
    return F,vecs,elems,mul,comm

def check(q,r):
    F,vecs,elems,mul,comm=build(q,r)
    n=len(elems)
    assert n==q**(r+2)

    # Multiplication sanity: identity and associativity.
    one=(1,(0,)*r,1)
    assert all(mul(one,x)==x and mul(x,one)==x for x in elems)
    for x in elems:
        for y in elems[:min(len(elems),17)]:
            for z in elems[:min(len(elems),11)]:
                assert mul(mul(x,y),z)==mul(x,mul(y,z))

    # Exact centralizers from multiplication.
    cents=[]
    for x in elems:
        C=frozenset(i for i,y in enumerate(elems) if mul(x,y)==mul(y,x))
        cents.append(C)
    distinct=set(cents)
    assert len(distinct)==q**r+2

    size_profile=Counter(map(len,distinct))
    expected=Counter({n:1, q**(r+1):1, q**2:q**r})
    if q**(r+1)==q**2:
        expected=Counter({n:1,q**2:q**r+1})
    assert size_profile==expected, (q,r,size_profile,expected)

    # Exact commutator fibers from multiplication.
    fibers=Counter()
    for x in elems:
        for y in elems:
            z=comm(x,y)
            assert z[0]==0 and z[2]==0
            fibers[z[1]]+=1

    zero=(0,)*r
    zero_expected=q**(2*r+2)+(q*q-1)*q**(r+2)
    nonzero_expected=q**(r+2)*(q*q-1)
    assert fibers[zero]==zero_expected
    assert set(fibers)==set(vecs)
    assert all(fibers[z]==nonzero_expected for z in vecs if z!=zero)
    assert sum(fibers.values())==n*n

    pr=Fraction(fibers[zero],n*n)
    expected_pr=Fraction(1,q*q)+Fraction(q*q-1,q**(r+2))
    assert pr==expected_pr
    return len(distinct),pr,size_profile

rows={}
for case in [(2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(4,2)]:
    rows[case]=check(*case)
    print(case, rows[case])

assert rows[(2,2)][0]==rows[(4,1)][0]==6
assert rows[(2,2)][1]==Fraction(7,16)
assert rows[(4,1)][1]==Fraction(19,64)
assert rows[(2,2)][1]!=rows[(4,1)][1]

print("VERIFY_OK")
