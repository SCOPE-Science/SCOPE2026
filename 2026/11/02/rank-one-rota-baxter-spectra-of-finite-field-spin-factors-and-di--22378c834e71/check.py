#!/usr/bin/env python3
"""Direct finite-field checks for rank-one weight-zero Rota--Baxter maps on spin factors."""
import itertools

class Field:
    def __init__(self,q):
        self.q=q
        if q==9:
            self.p=3
            self.add=lambda a,b: ((a%3+b%3)%3)+3*((a//3+b//3)%3)
            self.mul=lambda a,b: ((a%3)*(b%3)- (a//3)*(b//3))%3 +3*(((a%3)*(b//3)+(a//3)*(b%3))%3)
        else:
            self.p=q
            self.add=lambda a,b: (a+b)%q
            self.mul=lambda a,b: (a*b)%q
    def zero_neg(self,a):
        if self.q!=9:return (-a)%self.p
        return (-a%3)+3*((-(a//3))%3)
    def sub(self,a,b):return self.add(a,self.zero_neg(b))
    def prod(self,arr):
        t=1
        for a in arr:t=self.mul(t,a)
        return t

def projective_vectors(F,d):
    # unique representative with first nonzero entry 1, over arbitrary finite field
    q=F.q
    for pivot in range(d):
        for tail in itertools.product(range(q),repeat=d-pivot-1):
            yield (0,)*pivot+(1,)+tail

def rank_one_rb(F,n,diag,w,f):
    q=F.q
    add,mul=F.add,F.mul
    def dot(a,b):
        t=0
        for i in range(n):t=add(t,mul(diag[i],mul(a[i],b[i])))
        return t
    def times(a,b):
        return (add(mul(a[0],b[0]),dot(a[1:],b[1:])),)+tuple(add(mul(a[0],b[i]),mul(b[0],a[i])) for i in range(1,n+1))
    # independent operator check in the standard basis
    def R(x):
        s=0
        for i in range(n+1):s=add(s,mul(f[i],x[i]))
        return tuple(mul(s,z) for z in w)
    basis=[tuple(int(i==j) for i in range(n+1)) for j in range(n+1)]
    for x in basis:
        for y in basis:
            lhs=times(R(x),R(y))
            v=times(R(x),y)
            u=times(x,R(y))
            rhs=R(tuple(add(v[k],u[k]) for k in range(n+1)))
            if lhs!=rhs:return False
    return True

def predicted(F,n,diag):
    q=F.q
    add,mul=F.add,F.mul
    totalpts=0
    splitpts=[0,0]
    for w in projective_vectors(F,n+1):
        qq=0
        for j in range(n):qq=add(qq,mul(diag[j],mul(w[j+1],w[j+1])))
        if qq!=mul(w[0],w[0]):continue
        totalpts+=1
        splitpts[bool(w[0])]+=1
    return totalpts*(q**(n-1)-1),totalpts,splitpts

def exhaustive(F,n,diag):
    q=F.q
    count=0; checked=0
    for w in projective_vectors(F,n+1):
        for f in itertools.product(range(q),repeat=n+1):
            if not any(f):continue
            checked+=1
            if rank_one_rb(F,n,diag,w,f):count+=1
    return count,checked

def parametric_check(F,n,diag):
    q=F.q
    add,mul=F.add,F.mul
    positive=0
    for w in projective_vectors(F,n+1):
        qq=0
        for j in range(n):qq=add(qq,mul(diag[j],mul(w[j+1],w[j+1])))
        if qq!=mul(w[0],w[0]):continue
        witnessed=0
        for u in itertools.product(range(q),repeat=n):
            if not any(u):continue
            zz=0
            for j in range(n):zz=add(zz,mul(u[j],w[j+1]))
            if zz!=0:continue
            if witnessed<2:
                assert rank_one_rb(F,n,diag,w,(0,)+u)
                witnessed+=1
            positive+=1
    return positive

def main():
    cases=[(3,3,(1,1,1),True),(3,3,(1,1,2),True),
      (3,4,(1,1,1,1),True),(5,3,(1,1,1),False),
      (5,3,(1,1,2),False),(9,3,(1,1,1),False),
      (3,5,(1,1,1,1,1),False),(3,5,(1,1,1,1,2),False),
      (5,4,(1,1,1,1),False),(5,4,(1,1,1,2),False)]
    for q,n,diag,full in cases:
        F=Field(q)
        want,points,splits=predicted(F,n,diag)
        got,checked=(exhaustive(F,n,diag) if full else (parametric_check(F,n,diag),None))
        assert got==want,(q,n,diag,got,want)
        print(f'GF({q}) n={n} diagonal={diag} quadric_points={points} c0={splits[0]} c_nonzero={splits[1]} count={got} full_tested={checked}')
    print('SPIN_FACTOR_RANK_ONE_RB_OK 10_CASES')
if __name__=='__main__':main()
