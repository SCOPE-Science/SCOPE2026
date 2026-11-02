"""Independent finite checks of the stopped-pattern border sign theorem.

No external modules or network are required. The theorem is proved in RESULT.md;
finite enumeration here is supplementary and is not a proof for all lengths.
"""
from itertools import product
from math import isclose

def borders(w):
    return [(j, sum(map(int, w[:j]))) for j in range(1,len(w)+1) if w[:j]==w[-j:]]

def expected_sign(w):
    bs = borders(w)
    deviations = [(j,2*c-j) for j,c in bs if 2*c!=j]
    if not deviations: return 0
    return (deviations[-1][1]>0)-(deviations[-1][1]<0)

def kernel_integral(w, samples=1024):
    k = len(w)
    data = borders(w)
    def f(x):
        if x == 0: return (2*data[-1][1]-k)/4 if k==1 else 0.0
        if x == 1: return 0.0
        z=x/2
        h = z**k + (1-x)*sum(z**(k-j) for j,_ in data)
        num = sum((2*c-j)*z**(2*k-j) for j,c in data)
        return (1-x)*num/(2*x*h*h)
    n=samples
    assert n%2==0
    return (f(0)+f(1)+4*sum(f(i/n) for i in range(1,n,2))+2*sum(f(i/n) for i in range(2,n,2)))/(3*n)

def stopped_dp(w, steps):
    k=len(w)
    states=[('',0.,0.)]
    masses=[0.]*k; moments=[0.]*k; masses[0]=1.
    q=0.
    for t in range(1,steps+1):
        nxt=[0.]*k; nxt_m=[0.]*k
        for i in range(k):
            if masses[i]==0: continue
            for bit in '01':
                v=w[:i]+bit
                # All old suffixes have length <= i, sufficient for KMP automaton
                j=max((s for s in range(k+1) if v.endswith(w[:s])),default=0)
                mass=masses[i]/2; ones=(moments[i]+int(bit)*masses[i])/2
                if j==k: q+=ones/t
                else: nxt[j]+=mass; nxt_m[j]+=ones
        masses,moments=nxt,nxt_m
    return q,sum(masses)

if __name__=='__main__':
    checked=0; nonzero=0
    for k in range(1,10):
        for tup in product('01',repeat=k):
            w=''.join(tup)
            bs=borders(w)
            s=expected_sign(w)
            for T in (2.,3.,5.,10.):
                Q=sum((2*c-j)*(T**j) for j,c in bs)
                got=(Q>0)-(Q<0)
                assert got==s,(w,T,s,got)
                checked+=1
                if s: nonzero+=1
    print('Border polynomial sign checks:',checked,'including',nonzero,'nonzero signs; lengths 1..9')
    for w in ('0','1','00','11','01','10','1001','0110','1010','100011110001'):
        integral=kernel_integral(w,2048)
        s=(integral>1e-12)-(integral<-1e-12)
        assert s==expected_sign(w),(w,integral,s,expected_sign(w))
        if len(w)<=4:
            estimate,tail=stopped_dp(w,400)
            assert abs((estimate-.5)-integral)<tail+1e-8,(w,estimate,integral,tail)
            print(w,'q-1/2 integral',round(integral,10),'DP',round(estimate-.5,10),'tail',round(tail,12))
        else: print(w,'q-1/2 integral',round(integral,10))
    print('All verification checks passed.')
