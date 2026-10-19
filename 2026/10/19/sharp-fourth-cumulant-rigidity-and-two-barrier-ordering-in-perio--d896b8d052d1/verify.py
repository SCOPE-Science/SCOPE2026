from fractions import Fraction as Q
from itertools import combinations
import sympy as s

def independent(n,cs):
    L=[s.zeros(n) for _ in range(5)]
    for i in range(n):
        ip=(i+1)%n;im=(i-1)%n
        for j,delta in ((ip,1),(im,-1)):
            rate=s.Rational(cs[i]) if delta==1 else s.Rational(cs[im])
            L[0][i,j]+=rate
            for h in range(1,5):L[h][i,j]+=rate*delta**h
            L[0][i,i]-=rate
    fs=[s.ones(n,1)];lamb=[0]
    for h in range(1,5):
        rhs=s.zeros(n,1)
        for j in range(1,h+1):rhs+=L[j]*fs[h-j]/s.factorial(j)
        coef=sum(rhs)/n
        lamb.append(s.factor(coef))
        forcing=coef*s.ones(n,1)
        for j in range(1,h):forcing+=lamb[j]*fs[h-j]
        forcing-=rhs
        aa=L[0].copy(); b=forcing.copy()
        for j in range(n):aa[n-1,j]=1
        b[n-1]=0
        f=aa.inv()*b
        fs.append(f)
    return s.factor(2*lamb[2]),s.factor(24*lamb[4]),s.factor(lamb[1]),s.factor(lamb[3])

def predicted(n,cs):
    rs=[s.Rational(1)/s.Rational(c) for c in cs]
    R=sum(rs);B=sum(rs[i]*rs[j]*(j-i)*(n-j+i) for i,j in combinations(range(n),2))
    return 2*n/R,s.factor(2*n**3/R-24*n*B/R**3),B,R

num=0
for n in range(3,9):
    for t in range(7):
        cs=[s.Integer([1,2,3,4,5,7,9,11,13][(j*j+3*t+j*t+n)%9]) for j in range(n)]
        k2,k4,o1,o3=independent(n,cs)
        p2,p4,B,R=predicted(n,cs)
        assert o1==o3==0,(n,cs,'odd',o1,o3)
        assert k2==p2 and k4==p4,(n,cs,k2,p2,k4,p4)
        num+=1
print('PASS independent tilted full-generator exact perturbation comparisons:',num)
for n in range(3,8):
  c=[s.Integer(1)]*n
  k2,k4,_,_=independent(n,c)
  assert k2==2 and k4==2
print('PASS homogeneous cumulants')

# Independent finite exact checks for the cyclic primitive-energy identity.
identity_checks=0
for n in range(3,13):
    for t in range(9):
        rs=[s.Rational((j*j+3*t*j+7*t+5)%17+1, (3*j+5*t)%11+1) for j in range(n)]
        R=sum(rs)
        B=sum(rs[i]*rs[j]*(j-i)*(n-j+i) for i,j in combinations(range(n),2))
        us=[q-R/n for q in rs]
        Ss=[sum(us[:j]) for j in range(n)]
        avg=sum(Ss)/n
        E=sum((z-avg)**2 for z in Ss)
        assert s.factor((n*n-1)*R*R/s.Integer(12)-B-n*E)==0
        assert s.factor((2*n**3/R-24*n*B/R**3)/(2*n/R)-(1+12*n*E/R**2))==0
        assert E >= 0
        identity_checks += 1
print('PASS exact independent cyclic primitive-energy identities:',identity_checks)

# Two-defect separation: closed form and strict ordering where distances differ.
layout_checks=0
for n in range(3,19):
    for delta in (s.Rational(1,7),s.Integer(2),s.Integer(9)):
        arr=[]
        for d in range(1,n//2+1):
            rs=[s.Integer(1)+ (delta if j==0 or j==d else 0) for j in range(n)]
            R=sum(rs)
            B=sum(rs[i]*rs[j]*(j-i)*(n-j+i) for i,j in combinations(range(n),2))
            F=s.factor((2*n**3/R-24*n*B/R**3)/(2*n/R))
            want=1+4*delta**2*(n*n-1-3*d*(n-d))/(n+2*delta)**2
            assert s.factor(F-want)==0
            arr.append(F)
            layout_checks+=1
        assert all(arr[i]>arr[i+1] for i in range(len(arr)-1))
print('PASS exact two-defect formulas and all-separation ordering:',layout_checks)
