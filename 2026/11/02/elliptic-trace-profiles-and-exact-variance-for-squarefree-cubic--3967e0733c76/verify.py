"""Independent finite-field checks for the cubic/quadratic squarefree-shift theorem.

Run with Python 3 (standard library only): python verify.py.
Constructs repeated-root cubics by factorization and compares their shifted
intersection against the quadratic-character expression, including shift
means and exact variance. Computation is finite supporting evidence.
"""
from itertools import product


class Field:
    def __init__(self, p, modulus):
        self.p = p
        self.modulus = tuple(modulus)  # monic degree-r irreducible over F_p
        self.r = len(modulus) - 1
        self.q = p ** self.r
        self.zero = 0
        self.one = 1
        self.digits = []
        for a in range(self.q):
            z = a
            v = []
            for _ in range(self.r):
                v.append(z % p)
                z //= p
            self.digits.append(v)
        self.add_table = [[self.pack([(a+b) % p for a,b in zip(self.digits[x], self.digits[y])])
                          for y in range(self.q)] for x in range(self.q)]
        self.neg_table = [self.pack([(-a) % p for a in self.digits[x]]) for x in range(self.q)]
        self.mul_table = [[self.multiply_raw(x,y) for y in range(self.q)] for x in range(self.q)]
        self.squares = {self.mul(a,a) for a in range(1,self.q)}

    def pack(self, v):
        return sum(a*self.p**i for i,a in enumerate(v))

    def multiply_raw(self,x,y):
        p,r = self.p,self.r
        a,b = self.digits[x], self.digits[y]
        c = [0]*(2*r-1)
        for i in range(r):
            for j in range(r):
                c[i+j]=(c[i+j]+a[i]*b[j])%p
        for k in range(2*r-2,r-1,-1):
            coeff=c[k]
            for j in range(r):
                c[k-r+j]=(c[k-r+j]-coeff*self.modulus[j])%p
        return self.pack(c[:r])

    def add(self,x,y):return self.add_table[x][y]
    def neg(self,x):return self.neg_table[x]
    def sub(self,x,y):return self.add_table[x][self.neg_table[y]]
    def mul(self,x,y):return self.mul_table[x][y]
    def sq(self,x):return self.mul_table[x][x]
    def chi(self,x):return 0 if x==0 else (1 if x in self.squares else -1)
    def inv(self,x):
        if not x:raise ZeroDivisionError
        for y in range(1,self.q):
            if self.mul(x,y)==1:return y
        raise AssertionError('not a field')
    def num(self,n):return n%self.p


def repeated_cubics(F):
    # (T-r)^2(T-s) = T^3 -(2r+s)T^2 + (r^2+2rs)T-r^2s
    res=set()
    for r in range(F.q):
        r2=F.sq(r)
        for s in range(F.q):
            a=F.neg(F.add(F.add(r,r),s))
            b=F.add(r2,F.mul(F.add(r,r),s))
            c=F.neg(F.mul(r2,s))
            res.add((a,b,c))
    assert len(res)==F.q*F.q
    return res


def run():
    fields=[(3,[0,1]),(5,[0,1]),(7,[0,1]),(9,[1,0,1]),
            (11,[0,1]),(13,[0,1]),(25,[2,0,1]),(27,[2,2,0,1]),
            (49,[1,0,1])]
    tested=0
    for q,poly in fields:
        if q in (3,9,27):p=3
        elif q==25:p=5
        elif q==49:p=7
        else:p=q
        F=Field(p,poly)
        assert F.q==q
        repeated=repeated_cubics(F)
        u_choices=[1]+([2] if q<14 else [])
        v_choices=[0]+([1] if q<14 else [])
        for u in u_choices:
            for v in v_choices:
                u4=F.sq(F.sq(u))
                inv_u4=F.inv(u4)
                four=F.num(4)
                B=[]
                for w in range(q):
                    delta=F.sub(F.sq(v),F.mul(four,F.mul(u,w)))
                    t=F.mul(four,F.mul(delta,inv_u4))
                    # Independent count using complete sets of nonsquarefree cubic factorizations
                    actual=sum((F.add(a,u),F.add(b,v),F.add(c,w)) in repeated
                               for (a,b,c) in repeated)
                    # Predicted from a one-variable quadratic-character sum
                    charsum=sum(F.chi(F.add(F.add(F.mul(F.sq(z),z),F.sq(z)),t))
                                for z in range(1,q))
                    predicted=q-1+charsum+(q if t==0 else 0)
                    assert actual==predicted,(q,u,v,w,t,actual,predicted)
                    B.append(actual)
                    tested+=1
                # As w varies, t is a bijection of the field
                assert sum(B)==q*q,(q,u,v,sum(B))
                var_sum=sum((b-q)**2 for b in B)
                expected=q*(2*q-F.chi(F.neg(F.num(3)))-6+(1 if p==3 else 0))-1
                assert var_sum==expected,(q,u,v,var_sum,expected)
    print(f'VERIFY_OK fields={len(fields)} shifts={tested} independent_repeated_cubic_sets=yes means_variances=exact')

if __name__=='__main__':run()
