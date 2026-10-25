import numpy as np, math
from math import comb,pi
rng=np.random.default_rng(2121)

def count_angle(ang,b):
    ang=np.sort(np.asarray(ang)%1)
    n=len(ang)
    two=np.r_[ang,ang+1]
    c=0
    j=1
    for i in range(n):
        if j<i+1:j=i+1
        while j<i+n and two[j]-two[i] < b: j+=1
        m=j-i-1
        c+=m*(m-1)//2
    return c

def direct(ang,b):
    from itertools import combinations
    cnt=0
    for i,j,k in combinations(range(len(ang)),3):
        vals=sorted((ang[i]%1,ang[j]%1,ang[k]%1))
        gaps=(vals[1]-vals[0], vals[2]-vals[1],1+vals[0]-vals[2])
        cnt+=int(max(gaps)>1-b)
    return cnt

for b in (.09,.2,1/3,.49,.5):
    n=9; ns=25000
    v=np.fromiter((count_angle(rng.random(n),b) for _ in range(ns)),dtype=float,count=ns)
    p=3*b*b
    z=(14/3)*b**3-9*b**4
    mu=comb(n,3)*p
    va=comb(n,3)*p*(1-p)+2*comb(n,2)*comb(n-2,2)*z
    assert abs(v.mean()-mu)<0.3
    assert abs(v.var(ddof=1)-va)<max(1.,.07*va)
    for _ in range(25):
        x=rng.random(n)
        assert count_angle(x,b)==direct(x,b)
    lm=np.array([(b/(pi*k))*math.sin(2*pi*k*b)+(1-math.cos(2*pi*k*b))/(2*pi*pi*k*k) for k in range(1,7000)])
    # E kernel centered square = 2 sum(lambda_k^2)
    assert abs(2*np.dot(lm,lm)-z)<4e-6,(b,2*np.dot(lm,lm),z)
    if b<.5:
        assert lm.min()<0 and lm.max()>0
    else:
        assert lm.min()>-1e-12
    print('b',b,'mean_analytic',round(mu,6),'mean_MC',round(v.mean(),6),'var_analytic',round(va,6),'var_MC',round(v.var(ddof=1),6),'spectrumParseval',round(2*np.dot(lm,lm),8),'signed',bool(lm.min()<-1e-8))
print('CIRCULAR_STRONG_OBTUSE_COUNT_CHECKS_OK')
b=1/3;n=300;ns=2400
c=np.fromiter((count_angle(rng.random(n),b) for _ in range(ns)),dtype=float,count=ns)
zn=(c-comb(n,3)*3*b*b)/n**2
k=np.arange(1,3001,dtype=float)
lam=b*np.sin(2*pi*k*b)/(pi*k)+(1-np.cos(2*pi*k*b))/(2*pi*pi*k*k)
# limiting random Gaussian chaos with finite number of modes, one replicate per row
z=np.zeros(ns)
for q in range(0,len(k),100):
 l=lam[q:q+100]
 E=rng.exponential(size=(ns,len(l)))
 z+=(E-1)@l
print('LIMIT_LAW_CHECK n',n,'samples',ns,'finite_mean',zn.mean(),'variance',zn.var(),'theory',5/162,'positive_fraction',np.mean(zn>0),'limit_positive_fraction',np.mean(z>0))
assert abs(zn.var()-5/162)<0.007
assert abs(z.var()-5/162)<0.007
print('DEGENERATE_U_STATISTIC_GAUSSIAN_CHAOS_MOMENT_MATCH_OK')
