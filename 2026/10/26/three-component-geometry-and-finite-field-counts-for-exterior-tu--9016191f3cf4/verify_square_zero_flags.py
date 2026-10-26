"""Standalone finite-field verification for square-zero anticommuting flags."""
from itertools import product
import numpy as np

def field(q):
    if q in (2,3,5,7):
        add=lambda x,y:(x+y)%q
        mul=lambda x,y:(x*y)%q
    elif q==4:
        add=lambda x,y:x^y
        def mul(x,y):
            z=0
            for i in range(2):
                for j in range(2):
                    if (x>>i)&1 and (y>>j)&1:
                        z^=1<<(i+j)
            if z&8:z^=(0b1110) # x^3=x^2+x mod x^2+x+1
            if z&4:z^=0b111 # x^2=x+1
            return z
    else:raise ValueError(q)
    return add,mul

def predicted(q,r):
    I=1+(q+1)**2*(q**r-1)+2*(q+1)*(q**r-1)*(q**r-q)
    return q**(4*r)-q**(3*r)+q**r*I

def direct(q):
    add,mul=field(q)
    zero=lambda x:x==0
    sq=[]
    for x in product(range(q),repeat=5):
        a,b,c,d,e=x
        if zero(mul(a,b)) and zero(mul(b,c)) and zero(add(mul(a,e),mul(d,c))):sq.append(x)
    n=len(sq)
    adj=np.zeros((n,n),dtype=np.int64)
    for i,x in enumerate(sq):
        a,b,c,d,e=x
        for j,y in enumerate(sq):
            A,B,C,D,E=y
            v1=add(mul(a,B),mul(A,b))
            v2=add(mul(b,C),mul(B,c))
            v3=add(add(mul(a,E),mul(A,e)),add(mul(d,C),mul(D,c)))
            if not(v1 or v2 or v3):adj[i,j]=1
    for r in (1,2,3):
        cnt= n if r==1 else int(adj.sum()) if r==2 else int(np.trace(adj@adj@adj))
        result=cnt*q**r
        exp=predicted(q,r)
        print('q',q,'r',r,'actual',result,'formula',exp,'PASS',result==exp)
        assert result==exp
    print('square-zero five-coordinate vectors',n)

for q in (2,3,4,5):direct(q)
print('VERIFY_OK_SQUARE_ZERO_ANTICOMMUTING_FLAGS')
