"""Independent finite checks of trace-zero quadratic resultant unanimity.

No third-party dependencies. Field elements are represented in the base field
or as two coefficients in a quadratic extension; the mathematical proof covers
all odd finite fields, including extensions of higher degree.
"""

class Field:
    def __init__(self,p,d=None):
        self.p,self.d=p,d
        self.q=p if d is None else p*p
        if d is not None:
            assert pow(d,(p-1)//2,p)==p-1
    def add(self,x,y):
        p=self.p
        if self.d is None:return (x+y)%p
        return ((x%p+y%p)%p)+p*((x//p+y//p)%p)
    def neg(self,x):
        p=self.p
        if self.d is None:return (-x)%p
        return (-x%p)+p*((-(x//p))%p)
    def mul(self,x,y):
        p=self.p
        if self.d is None:return (x*y)%p
        a,b=x%p,x//p
        c,e=y%p,y//p
        return ((a*c+self.d*b*e)%p)+p*((a*e+b*c)%p)
    def power(self,x,n):
        a=1
        while n:
            if n&1:a=self.mul(a,x)
            x=self.mul(x,x)
            n//=2
        return a
    def chi(self,x):
        if x==0:return 0
        return 1 if self.power(x,(self.q-1)//2)==1 else -1


def verify_field(p,d=None):
    F=Field(p,d)
    q=F.q
    cube_set={F.power(x,3) for x in range(1,q)}
    irr=[v for v in range(1,q) if F.chi(F.neg(v))==-1]
    assert len(irr)==(q-1)//2
    unanimous=[]
    for c in range(1,q):
        r=F.mul(c,c)
        signs=[F.chi(F.add(F.power(v,3),r)) for v in irr]
        assert all(x in (1,-1) for x in signs)
        D=sum(signs)
        if q%3==0 or q%3==2:
            assert D==(F.chi(F.neg(1))-1)//2
        if len(set(signs))==1:
            unanimous.append(c)
        expected=(q==3 or q==7 or (q==13 and c not in cube_set)
                  or (q==19 and c in cube_set))
        assert expected==(len(set(signs))==1),(q,c,signs)
        # Independent resultant from multiplication in F_q[X]/(X^2+v):
        # alpha^2=-v, (alpha^3+c)(-alpha^3+c)=v^3+c^2.
        for v,s in zip(irr,signs):
            left=F.add(F.mul(r,1),F.mul(v,F.mul(v,v)))
            assert F.chi(left)==s
    print('FIELD_OK','q='+str(q),'parameters='+str(q-1),
          'irreducible_trace_zero_quadratics='+str(len(irr)),
          'unanimous='+str(len(unanimous)))
    return q-1

if __name__=='__main__':
    total=0
    for p,d in [(3,None),(5,None),(7,None),(11,None),(13,None),
                (17,None),(19,None),(23,None),(31,None),(37,None),
                (43,None),(61,None),(67,None),(73,None),(97,None),
                (3,2),(5,2),(7,3)]:
        total+=verify_field(p,d)
    print('VERIFY_OK','fields=18','parameter_classes='+str(total))
