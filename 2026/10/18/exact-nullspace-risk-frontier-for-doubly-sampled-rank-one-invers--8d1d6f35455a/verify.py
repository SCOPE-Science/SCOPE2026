"""Direct exact-rational finite-horizon checks of rank-one doubly sampled coordinate updates."""
from fractions import Fraction as F
from itertools import product


def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))

def mean(a): return sum(a,F(0))/len(a)

def trace(M): return sum((M[i][i] for i in range(len(M))),F(0))


def checks(u,v,step,horizon=14):
    u=tuple(F(x) for x in u); v=tuple(F(x) for x in v); t=F(step)
    rows=len(u); cols=len(v)
    U2=mean([x*x for x in u]); U4=mean([x**4 for x in u]); V2=dot(v,v); V4=sum((z**4 for z in v),F(0))
    critical=2*U2*V2/(U4*V4)
    assert 0<t<critical
    rate=F(1)-2*t*U2*V2/cols+t*t*U4*V4/cols
    mu=[a/V2 for a in v]
    S=sum((v[j]**2*(F(1)-v[j]**2/V2) for j in range(cols)),F(0))
    floor=t*U4*S/(2*U2*V2-t*U4*V4)
    assert 0<=rate<1 and floor>0

    # Propagate E[X], E[XX^T] directly via each possible random affine update.
    a=[F(0)]*cols
    B=[[F(0) for _ in range(cols)] for _ in range(cols)]
    state_mse=[]
    for k in range(horizon+1):
        mse=sum((B[j][j]-2*mu[j]*a[j]+mu[j]*mu[j] for j in range(cols)),F(0))
        expected=floor*(1-rate**k)+rate**k/V2
        assert mse==expected,(u,v,t,k,mse,expected)
        state_mse.append(mse)
        if k==horizon:break
        newa=[F(0)]*cols
        newB=[[F(0) for _ in range(cols)] for _ in range(cols)]
        for ii,j in product(range(rows),range(cols)):
            coeff=t*u[ii]**2*v[j]
            L=[[F(x==y) - (coeff*v[y] if x==j else F(0)) for y in range(cols)] for x in range(cols)]
            b=[coeff if x==j else F(0) for x in range(cols)]
            m=[sum((L[x][q]*a[q] for q in range(cols)),F(0))+b[x] for x in range(cols)]
            second=[[sum((L[x][q]*B[q][r]*L[y][r] for q,r in product(range(cols),repeat=2)),F(0))+
                    sum((L[x][q]*a[q] for q in range(cols)),F(0))*b[y]+b[x]*sum((L[y][q]*a[q] for q in range(cols)),F(0))+b[x]*b[y]
                    for y in range(cols)] for x in range(cols)]
            for x in range(cols):
                newa[x]+=m[x]/(rows*cols)
                for y in range(cols):newB[x][y]+=second[x][y]/(rows*cols)
        a,B=newa,newB
    return rate,floor,critical,state_mse


def main():
    tests=[((1,2),(1,1),F(1,8)),((1,2),(1,1,1),F(1,8)),((1,3),(1,2),F(1,40)),((1,2,3),(2,1,1),F(1,80)),((1,1),(1,1,1),F(1,3)),((1,2),(1,0,2),F(1,8))]
    cnt=0
    for u,v,t in tests:
        rate,floor,critical,M=checks(u,v,t)
        cnt+=len(M)
        print('case',u,v,'eta',t,'rate',rate,'floor',floor,'critical',critical,'horizon',len(M)-1)
    # Exact sample-path enumeration to separate direct path evidence from moments recursion.
    u=(F(1),F(2));v=(F(1),F(1));t=F(1,8);mu=(F(1,2),F(1,2))
    for steps in range(1,7):
        S=F(0); paths=0
        for seq in product(range(4),repeat=steps):
            x=[F(0),F(0)]
            for z in seq:
                i,j=divmod(z,2)
                x[j]+=t*u[i]**2*v[j]*(1-dot(v,x))
            S+=sum((x[h]-mu[h])**2 for h in range(2))
            paths+=1
        Q=F(65,128);floor=F(17,126)
        target=floor*(1-Q**steps)+Q**steps/F(2)
        assert S/paths==target,(steps,S/paths,target)
        cnt+=paths
    q,fl,eta_c,ms=checks((1,2),(1,1),F(1,8))
    assert q==F(65,128) and fl==F(17,126) and eta_c==F(10,17)
    assert fl<ms[0]
    # Sharp transition of reconstruction risk in dimension 3.
    q,fl,critical,ms=checks((1,1),(1,1,1),F(1,1),6)
    assert q==0 and fl==F(2,3) and critical==2
    assert ms[0]==F(1,3) and ms[1]==F(2,3)
    # The source-motivated diagnostic can contract while reconstruction risk rises.
    q,fl,critical,ms=checks((1,2),(1,1,1),F(1,4),10)
    assert q==F(9,32) and fl==F(34,69) and ms[1]>ms[0]
    q,fl,critical,ms=checks((1,2),(1,1,1),F(5,17),10)
    assert q==F(9,34) and fl==F(2,3) and ms[1]>ms[0]
    cnt+=7+22
    print('PASS exact checked values:',cnt)

if __name__=='__main__':main()
