from fractions import Fraction as F
from collections import defaultdict
from math import comb,pi,sqrt

def q(n):
    m=n-2
    return F(comb(2*m,m),4**m)

def exact_formula(N):
    c=F(0)
    for n in range(2,N):
        r=q(n)
        c+=r*F(n-3,3*(n-1))+r*r*F(2*n-3,3*(n-1)**2)
    return c

def exhaustive(limit=9):
    states={(1,1): F(1)}
    for n in range(2,limit+1):
        ed=el=edl=ed2=el2=eq=F(0)
        for deg,pr in states.items():
            assert sum(deg)==2*(n-1)
            D=deg[0];L=sum(x==1 for x in deg)
            ed+=pr*D;el+=pr*L;edl+=pr*D*L
            ed2+=pr*D*D;el2+=pr*L*L
            eq+=pr*(D==1)
        c=edl-ed*el
        assert c==exact_formula(n),(n,c,exact_formula(n))
        assert ed==F(2*n-3)*q(n),(n,'ed',ed)
        assert el==F(2*(n-1),3)+F(4,3)*q(n),(n,'el',el)
        assert eq==q(n),(n,'q',eq)
        assert ed2==2*(n-1)-ed,(n,'ed2',ed2)
        if n>=4: assert c>0
        else: assert c==0
        print('EXACT_ENUM_PASS',n,len(states),'cov',c,'meanD',ed,'meanL',el)
        if n==limit:break
        more=defaultdict(F)
        for deg,pr in states.items():
            for i,d in enumerate(deg):
                a=list(deg);a[i]+=1;a.append(1)
                more[tuple(a)]+=pr*F(d,2*(n-1))
        states=more
        assert sum(states.values())==1

if __name__=='__main__':
    exhaustive(9)
    for n in range(2,250):
        assert exact_formula(n)>=0
    for n in [1000,10000,100000]:
        total=0.0
        qn=1.0
        for j in range(2,n):
            total+=qn*((j-3)/(3*(j-1))+(2*j-3)*qn/(3*(j-1)**2))
            qn*=1-1/(2*(j-1))
        scaled=total/sqrt(n)
        print('ASYMPTOTIC_DIAGNOSTIC',n,scaled, 'target',2/(3*sqrt(pi)))
    print('VERIFY_OK')
