"""Numerical corroboration of the stated exact endpoint formula and peak sharpness.
All infinite assertions are established in RESULT.md, not by these tests.
"""
import math
import random
from scipy.integrate import quad
from scipy.special import gammainc, gammaln

def eigen(k, intervals):
    return sum(gammainc(k+1,b)-gammainc(k+1,a) for a,b in intervals)

def delta(k, intervals):
    def pdf(t):
        if t<=0:return 0.
        return math.exp((k+1)*math.log(t)-t-gammaln(k+2))
    return sum(pdf(a)-pdf(b) for a,b in intervals)

count=0
random.seed(253716)
for m in range(1,6):
    for trial in range(25):
        x=random.uniform(1,3)
        intervals=[]
        for j in range(m):
            a=x; b=a+random.uniform(0.1,1.8)
            intervals.append((a,b)); x=b+random.uniform(1.0,5.0)
        for k in range(0,2+math.ceil(intervals[-1][1])):
            left=eigen(k+1,intervals)-eigen(k,intervals)
            right=delta(k,intervals)
            assert abs(left-right)<3.e-13, (m,trial,k,left,right)
            count+=1
        signs=[delta(k,intervals) for k in range(math.ceil(intervals[-1][1])+15)]
        peaks=sum((k==0 or signs[k-1]>0) and signs[k]<0 for k in range(len(signs)))
        assert peaks<=m, (intervals,peaks)
        count+=1
for m in range(1,7):
    L=75
    ints=[(j*L,j*L+1) for j in range(1,m+1)]
    for j in range(1,m+1):
        a=j*L
        assert delta(a-2,ints)>0,(m,j,'rise')
        assert delta(a+2,ints)<0,(m,j,'fall')
        count+=2
    signs=[delta(k,ints) for k in range(m*L+20)]
    peaks=sum((k==0 or signs[k-1]>0) and signs[k]<0 for k in range(len(signs)))
    assert peaks==m, (m,peaks)
    count+=1
print(f'PASS: {count} numerical endpoint-identity, mode-ceiling, and sharpness checks.')
print('Numerical tests are not proofs; see analytic Descartes and large-separation arguments.')
