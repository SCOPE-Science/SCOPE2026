"""Reproduce the commutator image checks in characteristic five.

No external packages are required.  Group-ring coordinates are powers of
truncated logarithm t; these are not nonassociative algebra powers.
"""
from itertools import product


def bracket_prime(u, v):
    # Coefficients of U(-t)V(2t)-V(-t)U(2t) modulo t^5, in F_5.
    out = []
    for m in range(1, 5):
        val = sum(((-1)**i * 2**(m-i)) * (u[i]*v[m-i]-v[i]*u[m-i])
                  for i in range(m+1))
        out.append(val % 5)
    return tuple(out)


def brute_force_f5():
    # t^4 input coefficients do not influence the bracket.
    us = list(product(range(5), repeat=4))
    outputs = set()
    for x in us:
        u = x + (0,)
        for y in us:
            outputs.add(bracket_prime(u, y + (0,)))
    square = {0, 1, 4}
    for b in product(range(5), repeat=4):
        predicted = (b[0] != 0 or (b[2]*b[2] - 2*b[1]*b[3]) % 5 in square)
        assert (b in outputs) == predicted, b
    assert len(outputs) == 585
    assert 625 - len(outputs) == 40
    k=F5()
    for b in product(range(5), repeat=4):
        w=invert_target(k,b)
        assert (w is not None)==(b in outputs), b
        if w is not None: assert wedge_value(k,*w)==b
    print('F5: 585 simple values, 40 nonsimple values; full pair search PASS')


class F5:
    """Prime field for verifying inverse commutator certificates."""
    n = 5
    def add(self,x,y): return (x+y)%5
    def neg(self,x): return (-x)%5
    def sub(self,x,y): return (x-y)%5
    def mul(self,x,y): return (x*y)%5
    def inv(self,x): return pow(x,-1,5)
    def div(self,x,y): return (x*pow(y,-1,5))%5


def check_original_basis():
    """Independent change-of-basis check: X^i is exp(i*t)."""
    inv_fact = [1,1,3,1,4]  # (k!)^{-1} modulo five for k = 0,...,4
    def exp_vec(j):
        return [pow(j,k,5)*inv_fact[k]%5 for k in range(5)]
    for i,j in product(range(5),repeat=2):
        u,v=exp_vec(i),exp_vec(j)
        prod=[]
        for m in range(5):
            prod.append(sum(((-1)**a)*(2**(m-a))*u[a]*v[m-a]
                            for a in range(m+1))%5)
        assert prod==exp_vec((2*j-i)%5), (i,j,prod)
    print('F5: all 25 basis products match dihedral quandle table')


class F25:
    """F_5[s]/(s^2-3); encode a+b*s by a+5*b."""
    n = 25
    def split(self, x):
        return x % 5, x // 5
    def add(self, x, y):
        a, b = self.split(x); c, d = self.split(y)
        return (a+c)%5 + 5*((b+d)%5)
    def neg(self, x):
        a, b = self.split(x)
        return (-a)%5 + 5*((-b)%5)
    def sub(self, x, y):
        return self.add(x, self.neg(y))
    def mul(self, x, y):
        a,b = self.split(x); c,d = self.split(y)
        return (a*c+3*b*d)%5+5*((a*d+b*c)%5)
    def inv(self, x):
        assert x
        a,b = self.split(x)
        z = pow((a*a-3*b*b)%5, -1, 5)
        return a*z%5+5*((-b*z)%5)
    def div(self, x, y):
        return self.mul(x, self.inv(y))


def quad_condition(k, target):
    b1,b2,b3,b4 = target
    d = k.sub(k.mul(b3,b3),k.mul(2,k.mul(b2,b4)))
    sqroots = {}
    for v in range(k.n):
        sqroots.setdefault(k.mul(v,v), v)
    return b1 != 0 or d in sqroots


def wedge_value(k, u, v):
    def det(i,j):
        return k.sub(k.mul(u[i],v[j]),k.mul(u[j],v[i]))
    d01=det(0,1); d02=det(0,2); d03=det(0,3)
    d12=det(1,2); d13=det(1,3)
    return (k.mul(3,d01), k.mul(3,d02),
            k.mul(4,k.add(d03,d12)), k.neg(d13))


def invert_target(k, target):
    b1,b2,c,d = target
    a=k.div(b1,3); b=k.div(b2,3)
    minors = {(i,j):0 for i in range(4) for j in range(i+1,4)}
    minors[(0,1)]=a; minors[(0,2)]=b; minors[(1,3)]=k.neg(d)
    if a:
        minors[(0,3)]=0
        minors[(1,2)]=k.mul(4,c)
        minors[(2,3)]=k.div(k.neg(k.mul(b,d)),a)
    elif b:
        disc=k.sub(k.mul(c,c),k.mul(b,d))
        roots=[x for x in range(k.n) if k.mul(x,x)==disc]
        if not roots: return None
        s=k.div(k.add(k.mul(4,c),roots[0]),2)
        minors[(0,3)]=s
        minors[(1,2)]=k.sub(k.mul(4,c),s)
    else:
        minors[(1,2)]=k.mul(4,c)
    # Construct u,v for any Pluecker-satisfying minors by one pivot.
    def det(i,j):
        return minors[(i,j)] if i<j else k.neg(minors[(j,i)])
    piv=next(((i,j) for (i,j),v in minors.items() if v),None)
    if piv is None: return (tuple([0]*4),tuple([0]*4))
    i,j=piv; z=det(i,j)
    u=[0]*4; v=[0]*4
    u[i]=1; v[j]=z
    for l in range(4):
        if l==i or l==j: continue
        v[l]=det(i,l)
        u[l]=k.neg(k.div(det(j,l),z))
    assert wedge_value(k,u,v)==target, (target,u,v)
    return (tuple(u),tuple(v))


def check_extension_field():
    k=F25(); square_roots={k.mul(x,x) for x in range(25)}
    assert len(square_roots)==13
    bad=0
    checked=0
    for x in range(25):
        for y in range(25):
            for z in range(25):
                b=(0,x,y,z)
                good=quad_condition(k,b)
                if not good:
                    bad+=1
                if (x+y+z)%11==0:
                    w=invert_target(k,b)
                    assert (w is not None)==good
                    checked+=1
    assert bad==7200,bad
    for x in range(25):
        for y in (0,1,7,13,24):
            b=(1,x,y,24)
            u,v=invert_target(k,b)
            assert wedge_value(k,u,v)==b
    print(f'F25: {bad} nonsimple values; {checked} constructive cases PASS')


if __name__=='__main__':
    check_original_basis()
    brute_force_f5()
    check_extension_field()
    print('VERIFY_OK')
