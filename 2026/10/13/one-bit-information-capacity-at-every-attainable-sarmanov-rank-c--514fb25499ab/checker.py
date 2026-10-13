from fractions import Fraction as F
from itertools import product

def model(r):
    assert -F(3,4) <= r <= F(3,4)
    t=F(1,4)-r/3
    U=[(F(0),t,1),(t,t+F(1,2),-1),(t+F(1,2),F(1),1)]
    V=[(F(0),F(1,2),-1),(F(1,2),F(1),1)]
    cells=[]
    for i,(a,b,sa) in enumerate(U):
        for j,(c,d,sb) in enumerate(V):
            density=1+sa*sb
            mass=F(density)*(b-a)*(d-c)
            cells.append((i,j,a,b,c,d,F(density),mass))
    assert sum(z[-1] for z in cells)==1
    for i,(a,b,sa) in enumerate(U):
        assert sum(z[-1] for z in cells if z[0]==i)==b-a
    for j,(c,d,sb) in enumerate(V):
        assert sum(z[-1] for z in cells if z[1]==j)==d-c
    euv=sum(m*(a+b)*(c+d)/4 for i,j,a,b,c,d,dens,m in cells)
    rho=12*euv-3
    tau=sum(m*n*((i>k)-(i<k))*((j>l)-(j<l)) for i,j,a,b,c,d,dens,m in cells for k,l,e,f,g,h,dens2,n in cells)
    assert rho==r,(r,rho)
    assert tau==F(2,3)*r,(r,tau)
    assert {x[-2] for x in cells}.issubset({0,2})
    assert sum(x[-1] for x in cells if x[-2]==2)==1
    return t,rho,tau

rs=[F(-3,4),F(-5,8),F(-1,2),F(-1,3),F(-1,10),F(0),F(1,24),F(1,4),F(1,3),F(1,2),F(5,8),F(3,4)]
for r in rs:
    print(r,model(r))
print('Exact rectangular-copula rank and MI coefficient checks PASS:',len(rs),'parameters')
