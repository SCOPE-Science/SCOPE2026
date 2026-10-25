from itertools import product
from fractions import Fraction as F

def harmonic(m,p):return sum((F(1,i**p) for i in range(1,m+1)),F(0))

def verify(n):
    total=0;sr=sg=srg=0
    for seq in product(*(range(1,j) for j in range(2,n+1))):
        p=[0,0]+list(seq)
        dep=[0]*(n+1)
        for j in range(2,n+1):dep[j]=1+dep[p[j]]
        children=[0]*(n+1)
        for j in range(2,n+1):children[p[j]]+=1
        r=children[1];g=sum(dep[j]==2 and children[j]==0 for j in range(2,n+1))
        sr+=r;sg+=g;srg+=r*g;total+=1
    c=F(srg,total)-F(sr*sg,total*total)
    formula=harmonic(n-2,1)-harmonic(n-2,2)-F((n-2)**2,(n-1)**2)
    assert c==formula,(n,c,formula)
    return n,total,str(c)

if __name__=='__main__':
    for n in range(3,10):print('EXACT',*verify(n))
    for n in range(3,1000):
        m=n-2
        c=harmonic(m,1)-harmonic(m,2)-F(m*m,(m+1)*(m+1))
        assert (c<0 if n<=5 else c>0)
    print('VERIFY_OK')
