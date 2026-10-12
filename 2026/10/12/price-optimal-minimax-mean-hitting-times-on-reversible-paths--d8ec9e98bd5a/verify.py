"""Separate finite checks for price-optimal worst-pair hitting time on paths.
Run with python3 verify.py. Finite tests supplement, never establish, universal claims.
"""
from fractions import Fraction as F
from random import Random
from math import sqrt,isclose

def solve(a,b):
    n=len(b); a=[list(map(F,row))+[F(b[i])] for i,row in enumerate(a)]
    for k in range(n):
        j=next(j for j in range(k,n) if a[j][k]);a[k],a[j]=a[j],a[k]
        q=a[k][k];a[k]=[v/q for v in a[k]]
        for j in range(n):
            if j==k:continue
            q=a[j][k]
            a[j]=[x-q*y for x,y in zip(a[j],a[k])]
    return [row[n] for row in a]

def exact_hittings(pi, w):
    n=len(pi);q=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,x in enumerate(w):
        q[i][i+1]+=x/pi[i];q[i+1][i]+=x/pi[i+1]
        q[i][i]-=x/pi[i];q[i+1][i+1]-=x/pi[i+1]
    ans=[]
    for target in range(n):
        ix=[i for i in range(n) if i!=target]
        h=solve([[-q[i][j] for j in ix] for i in ix],[F(1)]*len(ix))
        ans.append([F(0) if i==target else h[ix.index(i)] for i in range(n)])
    return ans

def avalues(pi):
    result=[];s=F(0)
    for p in pi[:-1]:s+=p;result.append(s)
    return result

def theory(pi,c):
    p=avalues(pi);d=[float(2*x-1) for x in p];p=[float(x) for x in p];c=list(map(float,c))
    def der(lam):return sum(sqrt(t)*v/sqrt(1-x+lam*v) for t,v,x in zip(c,d,p))
    if der(0)<=0: lam=0.
    elif der(1)>=0:lam=1.
    else:
        lo,hi=0.,1.
        for _ in range(85):
            mid=(lo+hi)/2
            if der(mid)>0:lo=mid
            else:hi=mid
        lam=(lo+hi)/2
    a=[1-x+lam*v for x,v in zip(p,d)]
    s=sum(sqrt(x*y) for x,y in zip(a,c));w=[sqrt(x/y)/s for x,y in zip(a,c)]
    plus=sum(x/z for x,z in zip(p,w))
    minus=sum((1-x)/z for x,z in zip(p,w))
    return lam,s*s,w,plus,minus

def main():
    rand=Random(150876); exact_cases=0;exact_pairs=0
    for n in range(3,8):
        for _ in range(44):
            masses=[F(rand.randint(1,10)) for j in range(n)];s=sum(masses);pi=[a/s for a in masses]
            raw=[F(rand.randint(1,10)) for j in range(n-1)];prices=[F(rand.randint(1,8)) for j in range(n-1)]
            s=sum(a*b for a,b in zip(raw,prices));w=[a/s for a in raw];p=avalues(pi)
            h=exact_hittings(pi,w)
            f=sum(x/y for x,y in zip(p,w));g=sum((1-x)/y for x,y in zip(p,w))
            assert h[n-1][0]==f and h[0][n-1]==g
            assert max(max(row) for row in h)==max(f,g)
            exact_cases+=1;exact_pairs+=n*n
    numeric=0
    for n in range(3,11):
        for _ in range(100):
            masses=[F(rand.randint(1,50)) for j in range(n)];s=sum(masses);pi=[a/s for a in masses]
            prices=[rand.randint(1,20)/rand.randint(1,20) for j in range(n-1)]
            lam,v,w,plus,minus=theory(pi,prices)
            assert isclose(sum(x*y for x,y in zip(prices,w)),1,rel_tol=5e-13)
            assert isclose(max(plus,minus),v,rel_tol=2e-12,abs_tol=1e-11)
            if 1e-5<lam<1-1e-5:assert isclose(plus,minus,rel_tol=1e-12)
            for _ in range(10):
                raw=[w[i]*(.05+rand.random()*2) for i in range(n-1)]
                cost=sum(x*y for x,y in zip(raw,prices));z=[x/cost for x in raw]
                p=list(map(float,avalues(pi)))
                val=max(sum(x/y for x,y in zip(p,z)),sum((1-x)/y for x,y in zip(p,z)))
                assert val>=v-1e-8
            numeric+=1
    pi=[F(1,4),F(1,2),F(1,4)]
    for r in [F(1,10),F(1,3),F(1,2),F(1),F(2),F(3),F(4),F(10)]:
        lam,v,w,plus,minus=theory(pi,[r,F(1)])
        if F(1,3)<=r<=F(3):
            assert isclose(w[0],w[1],rel_tol=1e-12)
            assert isclose(v,float(r+1),rel_tol=1e-12)
    print(f'VERIFY_OK {exact_cases} independent exact generator/hitting-time cases; {exact_pairs} ordered hitting entries; {numeric} arbitrary-mass/price optimizer cases; {numeric*10} feasible perturbations; eight exact three-state phase probes')
if __name__=='__main__':main()
