"""Exact reproducible checks for the six-entry 3x3 determinant fibers."""
from itertools import product
from hashlib import sha256

class Field:
    def __init__(self, q):
        if q not in (3, 5, 7, 9, 11):
            raise ValueError('Only supported test fields')
        self.q = q
        self.items = list(range(q))
        if q == 9:
            self.add = lambda x, y: (x % 3 + y % 3) % 3 + 3*((x//3+y//3)%3)
            self.mul = lambda x,y: (((x%3)*(y%3) - (x//3)*(y//3)) % 3
                       + 3*(((x%3)*(y//3) + (x//3)*(y%3))%3))
            self.neg = lambda x: ((-(x%3))%3) + 3*((-(x//3))%3)
        else:
            self.add = lambda x,y: (x+y)%q
            self.mul = lambda x,y: (x*y)%q
            self.neg = lambda x: (-x)%q
        self.sub = lambda x,y: self.add(x,self.neg(y))
        self.squares = {self.mul(x,x) for x in range(1,q)}
    def chi(self,x):
        if x == 0: return 0
        return 1 if x in self.squares else -1


def count_exact(F, a,b,c,u,v,w):
    A,M,S=F.add,F.mul,F.sub
    out=[0]*F.q
    for x,y,z in product(F.items, repeat=3):
        det = A(A(A(M(M(a,b),c),M(M(u,v),w)),M(M(x,y),z)),
                S(0,A(A(M(M(a,v),z),M(M(u,c),y)), M(M(b,w),x))))
        out[det]+=1
    return out


def count_formula(F,a,b,c,u,v,w):
    A,M,S=F.add,F.mul,F.sub
    D=M(M(a,b),c); T=M(M(u,v),w)
    discriminants=[]
    out=[]
    for t in F.items:
        value=S(S(A(D,T),t),0)
        discr=S(M(value,value),M(A(A(1,1),A(1,1)),M(D,T)))
        discriminants.append(discr)
        out.append(F.q**2+1+F.q*F.chi(discr))
    return out,discriminants


def run():
    n_checks=0; cases=0; sumchecks=0
    for q in (3,5,7,9,11):
        F=Field(q)
        nonzero=list(range(1,q))
        tuples=product(nonzero, repeat=6) if q in (3,5) else (
            tuple(nonzero[(7*j*j+11*j*i+i*i+3*i+2*j)%len(nonzero)] for j in range(6))
            for i in range(128))
        for params in tuples:
            true=count_exact(F,*params)
            pred,disc=count_formula(F,*params)
            assert true==pred, (q,params,true,pred,disc)
            assert sum(true)==q**3
            assert len({v for v in true})<=3
            cases+=1
            n_checks+=q
            sumchecks+=1
        print(f'F_{q}: verified')
    print('PASS', cases,'six-entry choices;', n_checks,'determinant fibers;',sumchecks,'total-count checks')
if __name__=='__main__':run()
