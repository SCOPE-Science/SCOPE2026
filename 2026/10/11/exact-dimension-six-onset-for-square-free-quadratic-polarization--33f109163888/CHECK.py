"""Exact finite-dimensional coefficient certificates, independently of input matrix values."""
from fractions import Fraction as F
from itertools import combinations, product


def signs(n):
    return product((-1, 1), repeat=n)


def edges(n):
    return tuple(combinations(range(n), 2))


def q_coeff(s, ee):
    # q_A(s)=2*sum_(i,j) A_ij*s_i*s_j; coefficients relative to 2*A_ij.
    return tuple(s[i] * s[j] for i, j in ee)


def b_coeff(x, y, ee):
    # B_A(x,y)=sum_(i,j) A_ij*(x_i*y_j+x_j*y_i).
    return tuple(F(x[i]*y[j]+x[j]*y[i], 2) for i,j in ee)


def certificate(x,y):
    n=len(x)
    u=tuple(i for i in range(n) if x[i]==y[i])
    v=tuple(i for i in range(n) if x[i]!=y[i])
    if min(len(u),len(v))<=2:
        small=u if len(u)<=2 else v
        large=v if len(u)<=2 else u
        relative=[1]*n
        if len(small)==2:
            relative[small[0]]=-1
        s=tuple(a*b for a,b in zip(x,relative))
        s2=tuple(-a if i in large else a for i,a in enumerate(s))
        coeff=F(-1 if small==u else 1,2)
        return ((coeff,s),(coeff,s2))
    assert n==6 and len(u)==len(v)==3
    ans=[]
    for flipped in v:
        rel=[1]*n;rel[flipped]=-1
        s=tuple(a*b for a,b in zip(x,rel))
        s2=tuple(-a if i in v else a for i,a in enumerate(s))
        ans.extend(((F(1,8),s),(F(1,8),s2)))
    for flipped in u:
        rel=[1]*n;rel[flipped]=-1
        s=tuple(a*b for a,b in zip(x,rel))
        s2=tuple(-a if i in u else a for i,a in enumerate(s))
        ans.extend(((F(-1,8),s),(F(-1,8),s2)))
    return tuple(ans)


def verify(n):
    ee=edges(n); ss=list(signs(n)); cnt=0; maxmass=0
    for x in ss:
        for y in ss:
            cert=certificate(x,y)
            mass=sum(abs(w) for w,_ in cert)
            maxmass=max(maxmass,mass)
            assert mass<= (F(3,2) if n==6 else F(1))
            coeff=tuple(sum(w*q_coeff(s,ee)[k] for w,s in cert) for k in range(len(ee)))
            assert coeff==b_coeff(x,y,ee),(n,x,y,coeff,b_coeff(x,y,ee))
            cnt+=1
    print(f'n={n}: {cnt} sign pairs, all coefficient identities exact; maximal coefficient mass {maxmass}')


for n in range(2,7):
    verify(n)
n=6
A=[[0]*n for _ in range(n)]
for lo,sgn in ((0,1),(3,-1)):
    for i,j in combinations(range(lo,lo+3),2):
        A[i][j]=A[j][i]=sgn
SS=list(signs(6))
quad=max(abs(sum(A[i][j]*x[i]*x[j] for i in range(n) for j in range(n))) for x in SS)
bilin=max(abs(sum(A[i][j]*x[i]*y[j] for i in range(n) for j in range(n))) for x in SS for y in SS)
assert (quad,bilin)==(8,12)
print('six-dimensional extremizer: polynomial norm 8, bilinear norm 12; ratio 3/2')
