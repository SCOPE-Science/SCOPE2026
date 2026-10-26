"""Self-contained exact-arithmetic checks for a three-dimensional SPAI pattern barrier."""
from fractions import Fraction as F
from itertools import product

def det(a):
    n=len(a)
    if n==1: return a[0][0]
    return sum((-1)**j*a[0][j]*det([r[:j]+r[j+1:] for r in a[1:]]) for j in range(n))

def solve(a,b):
    n=len(b)
    aug=[list(map(F,a[i]))+[F(b[i])] for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n) if aug[k][j])
        aug[j],aug[k]=aug[k],aug[j]
        u=aug[j][j]; aug[j]=[x/u for x in aug[j]]
        for k in range(n):
            if k==j: continue
            t=aug[k][j]; aug[k]=[x-t*y for x,y in zip(aug[k],aug[j])]
    return [r[-1] for r in aug]

def matmul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0)) for j in range(len(b[0]))] for i in range(len(a))]

def spaifit(a,pattern):
    n=len(a); m=[[F(0) for j in range(n)] for i in range(n)]
    for j in range(n):
        cols=[i for i in range(n) if (i,j) in pattern]
        gram=[[sum(a[k][u]*a[k][v] for k in range(n)) for v in cols] for u in cols]
        rhs=[a[j][u] for u in cols]
        x=solve(gram,rhs)
        for i,y in zip(cols,x): m[i][j]=y
    return m

def err(a,m):
    am=matmul(a,m); n=len(a)
    return sum(((F(int(i==j))-am[i][j])**2 for i in range(n) for j in range(n)),F(0))

j0={(0,0),(1,1),(2,2)}
j1=j0|{(0,1)}
a0=[[F(1),F(1),F(1)], [F(1),F(3),F(5)], [F(1),F(5),F(10)]]
m0=spaifit(a0,j0);m1=spaifit(a0,j1)
assert [det([r[:k] for r in a0[:k]]) for k in range(1,4)]==[F(1),F(2),F(2)]
assert m0==[[F(1,3),F(0),F(0)],[F(0),F(3,35),F(0)],[F(0),F(0),F(5,63)]]
assert m1==[[F(1,3),F(1,3),F(0)],[F(0),F(0),F(0)],[F(0),F(0),F(5,63)]]
assert det(m0)>0 and det(m1)==0 and det(matmul(a0,m1))==0
assert err(a0,m0)==F(509,315)
assert err(a0,m1)==F(97,63)
assert err(a0,m0)-err(a0,m1)==F(8,105)

cnt=7
for denom in [10,20,25,30,50,100,200,1000,10000]:
    e=F(1,denom)
    a=[[F(1),F(1),F(1)],[F(1),F(3),F(5)+e],[F(1),F(5)+e,F(10)]]
    u=spaifit(a,j0);v=spaifit(a,j1)
    assert det(a)==2-8*e-e*e>0
    assert v[0][1]==(8+7*e+e*e)/(24+12*e+2*e*e)
    assert v[1][1]==-e/(24+12*e+2*e*e)
    assert det(v)==(-5*e)/(3*(e*e+6*e+12)*(e*e+10*e+126))
    assert det(u)>0 and det(v)<0 and err(a,u)>err(a,v)
    cnt+=6

# In dimension two, the diagonal-plus-one-entry preconditioner is triangular
# and its diagonal coefficients remain positive for any SPD test.
for a,b,c in product([F(1),F(2),F(3),F(5)],repeat=3):
    if a*b<=c*c: continue
    aa=[[a,c],[c,b]]
    for off in [(0,1),(1,0)]:
        base={(0,0),(1,1)}
        u=spaifit(aa,base)
        v=spaifit(aa,base|{off})
        assert det(u)>0 and det(v)>0 and err(aa,v)<=err(aa,u)
        cnt+=1
print(f'PASS exact-SPAI verification: {cnt} independently evaluated assertion groups')
