"""Self-contained finite-field checks for automorphisms of a six-dimensional
quantum complete intersection. Run with Python 3 (no dependencies)."""
from itertools import product

BASIS = ((0,0),(1,0),(0,1),(1,1),(0,2),(1,2))
INDEX = {a:i for i,a in enumerate(BASIS)}

class Field:
    def __init__(self,p,extension=False):
        self.p=p
        self.q=4 if extension else p
        self.extension=extension
    def add(self,a,b):
        return a^b if self.extension else (a+b)%self.p
    def mul(self,a,b):
        if not self.extension:return a*b%self.p
        out=0
        while b:
            if b&1:out^=a
            b>>=1
            a<<=1
            if a&4:a^=7
        return out
    def power(self,a,n):
        out=1
        for _ in range(n):out=self.mul(out,a)
        return out


def multiply(A,B,twist,F):
    C=[0]*6
    q=F.q
    powers=[1,twist,F.mul(twist,twist)]
    for r,(i,j) in enumerate(BASIS):
        if not A[r]:continue
        for s,(I,J) in enumerate(BASIS):
            if not B[s] or i+I>1 or j+J>2:continue
            term=F.mul(F.mul(A[r],B[s]),powers[j*I])
            index=INDEX[(i+I,j+J)]
            C[index]=F.add(C[index],term)
    return C

def is_hom(X,Y,twist,F):
    xx=multiply(X,X,twist,F)
    yy=multiply(Y,Y,twist,F)
    yyy=multiply(yy,Y,twist,F)
    yx=multiply(Y,X,twist,F)
    xy=multiply(X,Y,twist,F)
    return not any(xx) and not any(yyy) and all(yx[i]==F.mul(twist,xy[i]) for i in range(6))

def map_is_invertible(X,Y,t,F):
    one=(1,0,0,0,0,0)
    Y2=multiply(Y,Y,t,F)
    images=[one,X,Y,multiply(X,Y,t,F),Y2,multiply(X,Y2,t,F)]
    rows=[[images[col][row] for col in range(6)] for row in range(6)]
    rank=0
    for col in range(6):
        pivot=next((r for r in range(rank,6) if rows[r][col]),None)
        if pivot is None:continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        piv=rows[rank][col]
        inv=next(a for a in range(1,F.q) if F.mul(a,piv)==1)
        rows[rank]=[F.mul(a,inv) for a in rows[rank]]
        for r in range(6):
            if r==rank or not rows[r][col]:continue
            factor=rows[r][col]
            rows[r]=[F.add(rows[r][j],F.mul(factor,rows[rank][j]))
                     if F.p==2 else (rows[r][j]-F.mul(factor,rows[rank][j]))%F.p
                     for j in range(6)]
        rank+=1
    return rank==6

def predicted_twist_dim(F,t):
    one=1
    if t==one:
        return 6 if F.p in (2,3) else 5
    if F.power(t,3)==one or F.add(one,F.power(t,2))==0:
        return 5
    return 4

def verify(F,t):
    # Scaling X and Y by independent nonzero scalars preserves all
    # relations, so the count for a=g=1 multiplies by (Q-1)^2.
    accepted=0
    # Variables c,d,e,f,h,i,j; x=a*x+c*xy+d*y²+e*xy²,
    # y=f*x+g*y+h*xy+i*y²+j*xy².
    for c,d,e,f,h,i,j in product(range(F.q),repeat=7):
        X=(0,1,0,c,d,e)
        Y=(0,f,1,h,i,j)
        if is_hom(X,Y,t,F):
            accepted+=1
            if accepted%29==1:
                assert map_is_invertible(X,Y,t,F),(F.q,t,X,Y)
    dim=predicted_twist_dim(F,t)
    assert accepted==F.q**dim,(F.q,t,accepted,dim)
    print('OK', 'F4' if F.extension else f'F{F.p}', 'twist',t,
          'normalized',accepted,'automorphisms',(F.q-1)**2*accepted)

if __name__=='__main__':
    verify(Field(2),1)
    verify(Field(3),1)
    verify(Field(3),2)
    verify(Field(2,True),1)
    verify(Field(2,True),2)
    verify(Field(5),1)
    verify(Field(5),2)
    verify(Field(5),4)
    verify(Field(7),2)
    print('VERIFY_OK')
