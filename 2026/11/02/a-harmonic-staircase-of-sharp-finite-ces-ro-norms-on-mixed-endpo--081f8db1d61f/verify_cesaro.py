"""Exact-rational finite checks of sharp generalized Cesaro norm formulas.
Scientific validation aid; the proof of the unrestricted result is analytic.
"""
from fractions import Fraction as F
from itertools import combinations

def weighted_cesaro(x,t):
    s=F(0); y=[]
    for i,z in enumerate(x,1):
        s=t*s+z
        y.append(s/i)
    return y

def norm(x,eps):
    a=[abs(z) for z in x]
    return (1-eps)*max(a)+eps*sum(a)

def pred(n,t,eps):
    c=[sum((t**(i-j)/i for i in range(j,n+1)),F(0)) for j in range(1,n+1)]
    vals=[((1-eps)+eps*sum(c[:k]))/((1-eps)+eps*k) for k in range(1,n+1)]
    return max(vals),vals

def run():
    cases=0; support_tests=0; phase_tests=0
    for n in range(2,10):
        for t in [F(0),F(1,3),F(2,3),F(1)]:
            for eps in [F(1,100),F(1,7),F(1,2),F(1)]:
                target,vals=pred(n,t,eps)
                best=F(0)
                for k in range(1,n+1):
                    for S in combinations(range(n),k):
                        x=[F(int(i in S)) for i in range(n)]
                        rate=norm(weighted_cesaro(x,t),eps)/norm(x,eps)
                        assert rate<=target,(n,t,eps,S,rate,target)
                        best=max(best,rate)
                        support_tests+=1
                assert best==target,(n,t,eps,best,target)
                cases+=1
    for n in range(4,41):
        h=[F(0)]
        for i in range(1,n+1):h.append(h[-1]+F(1,i))
        B=[F(0)]+[k*(h[n]-h[k]) for k in range(1,n+1)]
        # The exact thresholds decrease strictly whenever positive.
        th=[(h[n]-h[k]-1)/(h[n]-h[k]+k-1) for k in range(1,n) if h[n]-h[k]>1]
        assert all(th[j]>th[j+1] for j in range(len(th)-1))
        for eps in [F(1,10000),F(1,100),F(1,7),F(1,2),F(1)]:
            _,actual=pred(n,F(1),eps)
            symbolic=[1+eps*B[k]/(1+eps*(k-1)) for k in range(1,n+1)]
            assert actual==symbolic
            for k in range(1,n):
                d=(h[n]-h[k]-1)-eps*(h[n]-h[k]+k-1)
                assert (actual[k]>actual[k-1])==(d>0)
                assert (actual[k]==actual[k-1])==(d==0)
                phase_tests+=1
    assert pred(4,F(1),F(1,13))[1][0] == pred(4,F(1),F(1,13))[1][1]
    print('PASS',cases,'complete exact-rational support/candidate cases;',support_tests,'support evaluations;',phase_tests,'phase adjacent-sign checks')
if __name__=='__main__':run()
