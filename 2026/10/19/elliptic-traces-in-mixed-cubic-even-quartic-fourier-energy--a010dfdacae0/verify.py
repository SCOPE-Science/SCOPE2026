"""Exact finite-field checks for mixed cubic/quartic graph convolution energy.

All calculations use integer modular arithmetic, with quadratic extensions
represented in the basis (1, alpha), alpha**2 = nonsquare D.
"""
from collections import Counter


class Field:
    def __init__(self, p, nonsquare=None):
        self.p, self.nonsquare = p, nonsquare
        self.q = p if nonsquare is None else p*p
        if nonsquare is not None:
            assert pow(nonsquare % p, (p-1)//2, p) == p-1
        self.zero, self.one = 0, 1
        self.add_table = [[self._add(a,b) for b in range(self.q)] for a in range(self.q)]
        self.mul_table = [[self._mul(a,b) for b in range(self.q)] for a in range(self.q)]
        self.squares = {self.mul(a,a) for a in range(1,self.q)}

    def _add(self,a,b):
        if self.nonsquare is None:
            return (a+b)%self.p
        return (a%self.p+b%self.p)%self.p+self.p*((a//self.p+b//self.p)%self.p)

    def _mul(self,a,b):
        if self.nonsquare is None:
            return (a*b)%self.p
        p=self.p
        x,y=a%p,a//p
        z,w=b%p,b//p
        return (x*z+self.nonsquare*y*w)%p+p*((x*w+y*z)%p)

    def add(self,a,b): return self.add_table[a][b]
    def mul(self,a,b): return self.mul_table[a][b]
    def neg(self,a): return self._add(0,(-a)%self.p if self.nonsquare is None else (-(a%self.p))%self.p+self.p*((-(a//self.p))%self.p))
    def sub(self,a,b): return self.add(a,self.neg(b))
    def char(self,a): return 0 if a==0 else (1 if a in self.squares else -1)
    def power(self,a,n):
        v=self.one
        for _ in range(n):v=self.mul(v,a)
        return v
    def const(self,n):return n%self.p
    def inv(self,a):return self.power(a,self.q-2)


def formula(F,c):
    q=F.q
    i4=F.inv(F.const(4))
    P=lambda v:F.add(F.mul(F.const(4),F.power(v,3)),F.mul(F.mul(F.const(2),c),v))
    C=sum(F.char(P(v)) for v in range(q))
    H=sum(F.char(F.sub(v,i4)) for v in range(q) if P(v)==0 and v!=i4)
    J=F.char(P(i4))
    value=2*q*q-q+F.char(F.const(3))*(-C+q*(H+J))
    aq=-C if c!=0 else None
    if c!=0:
        points=sum(1+F.char(P(v)) for v in range(q))+1
        assert aq == q+1-points
        assert abs(aq) <= 2*q**0.5+1e-10
    if c==0:
        assert C==0
        assert H==F.char(F.neg(F.one))
        assert J==1
        assert value==2*q*q-q+q*(F.char(F.const(3))+F.char(F.neg(F.const(3))))
    return value,C,H,J,aq


def brute(F,c):
    q=F.q
    cube=[F.power(t,3) for t in range(q)]
    quartic=[F.power(t,4) for t in range(q)]
    square=[F.power(t,2) for t in range(q)]
    r=Counter()
    for t in range(q):
        for u in range(q):
            r[(F.add(t,u),F.add(cube[t],F.add(quartic[u],F.mul(c,square[u]))))]+=1
    return sum(k*k for k in r.values())


def test(F,parameters):
    for c in parameters:
        v,C,H,J,aq=formula(F,c)
        actual=brute(F,c)
        assert v==actual, (F.q,c,actual,v,C,H,J,aq)
    return len(parameters)


def main():
    total=0
    ps=(5,7,11,13,17,19,23,29,31)
    for p in ps:
        f=Field(p)
        total+=test(f,range(p))
    ext=[]
    for p in (5,7,11,13):
        nonres=next(a for a in range(2,p) if pow(a,(p-1)//2,p)==p-1)
        f=Field(p,nonres)
        cs=sorted(set((0,1,p,p+1,2*p+1,p+2)))
        total+=test(f,cs)
        ext.append(f.q)
    print('VERIFY_OK prime_fields='+str(len(ps))+' all_prime_parameters=155 quadratic_extensions='+','.join(map(str,ext))+' extension_parameters=24 total_cases='+str(total))


if __name__=='__main__':main()
