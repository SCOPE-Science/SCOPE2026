#!/usr/bin/env python3
"""Direct finite-field verification of spin-factor zero-product counts."""
from itertools import product

class Field:
    def __init__(self,p,extension=1):
        assert p in (3,5,7)
        assert extension in (1,2)
        if extension==2: assert p==3
        self.p=p;self.extension=extension;self.q=p**extension
        def rawmul(x,y):
            if extension==1:return x*y%p
            a,b=x%p,x//p;c,d=y%p,y//p
            return (a*c+2*b*d)%p+p*((a*d+b*c)%p)
        def rawadd(x,y):
            if extension==1:return (x+y)%p
            return ((x%p+y%p)%p)+p*((x//p+y//p)%p)
        self.mul=[[rawmul(i,j) for j in range(self.q)] for i in range(self.q)]
        self.add=[[rawadd(i,j) for j in range(self.q)] for i in range(self.q)]
    def sum(self,terms):
        x=0
        for t in terms:x=self.add[x][t]
        return x

def run_case(field,diagonal):
    q=field.q;n=len(diagonal)
    vectors=list(product(range(q),repeat=n))
    qnorm={u:field.sum(field.mul[diagonal[i]][field.mul[u[i]][u[i]]] for i in range(n)) for u in vectors}
    n1=sum(norm==1 for norm in qnorm.values())
    count=0
    for a in range(q):
      for u in vectors:
       for b in range(q):
        for v in vectors:
         scalar=field.sum([field.mul[a][b]]+[field.mul[diagonal[i]][field.mul[u[i]][v[i]]] for i in range(n)])
         if scalar!=0:continue
         if any(field.add[field.mul[a][v[i]]][field.mul[b][u[i]]]!=0 for i in range(n)):continue
         count+=1
    closed=(2*q-1)*q**n+(q**n-1)*q**(n-1)+(q-1)**2*n1
    assert count==closed,(field.q,diagonal,count,closed)
    print(f'PASS q={q} n={n} form={diagonal} direct={count} N_Q(1)={n1}')
    return 1

cases=[(Field(3),[1,1]),(Field(3),[1,2]),(Field(5),[1,1]),(Field(5),[1,2]),(Field(7),[1,1]),(Field(7),[1,3]),(Field(3),[1,1,1]),(Field(3),[1,1,2]),(Field(5),[1,1,1]),(Field(3),[1,1,1,1]),(Field(3,2),[1,1]),(Field(3,2),[1,4])]
total=sum(run_case(f,d) for f,d in cases)
print('SPIN_FACTOR_ZERO_PRODUCT_OK',total)
