from fractions import Fraction as F
from math import comb

def check(n):
    dist = {(n, 0): (F(1), F(0))}
    # accumulate expected terminal-branch waiting-time rewards jointly with cherry count
    for k in range(n,1,-1):
        nxt={}
        for (s,h),(p,w) in dist.items():
            incoming=w+p*F(2*s,k*(k-1))
            opts=[(2,comb(s,2)),(1,s*(k-s)),(0,comb(k-s,2))]
            for j,mult in opts:
                if not mult: continue
                q=F(mult,comb(k,2)); key=(s-j,h+(j==2))
                pp,ww=nxt.get(key,(F(0),F(0)))
                nxt[key]=(pp+p*q,ww+incoming*q)
        dist=nxt
    assert sum(p for p,w in dist.values())==1
    ec=sum(p*h for (s,h),(p,w) in dist.items())
    el=sum(w for p,w in dist.values())
    ecl=sum(w*h for (s,h),(p,w) in dist.items())
    vch=sum(p*h*h for (s,h),(p,w) in dist.items())-ec**2
    cv=ecl-ec*el
    assert ec==F(n,3),(n,'cherries',ec)
    assert el==2,(n,'ext',el)
    assert cv==F(-2,9),(n,'cov',cv)
    return cv,vch

if __name__=='__main__':
    for n in range(4,24):
        cv,var=check(n)
        if n>=5:assert var==F(2*n,45),(n,'var',var)
        print(f'n={n}, cov={cv}, Var(C)={var}')
    print('PASS')

def check_stage(n, target):
    d={(n,0):(F(1),F(0))}
    for k in range(n,1,-1):
        after={}
        for (s,h),(p,u) in d.items():
            marked=u+(p*s if k==target else F(0))
            for j,cnt in ((2,comb(s,2)),(1,s*(k-s)),(0,comb(k-s,2))):
                if not cnt:continue
                w=F(cnt,comb(k,2));key=(s-j,h+(j==2))
                pp,uu=after.get(key,(F(0),F(0)))
                after[key]=(pp+p*w,uu+marked*w)
        d=after
    e_sc=sum(h*u for (s,h),(p,u) in d.items())
    e_s=sum(u for p,u in d.values())
    actual=e_sc-e_s*F(n,3)
    expected=F(-target*(target-1)*(n-target)*(n-target-1),3*(n-1)*(n-2)*(n-3))
    assert actual==expected,(n,target,actual,expected)

if __name__=='__main__':
    for n in range(4,14):
        for k in range(2,n+1):check_stage(n,k)
    print('STAGE_PROFILE_PASS')
