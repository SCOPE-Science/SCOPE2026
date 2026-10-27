import math,itertools,numpy as np

def covariance(n,t,s,mu):
    a,b=sorted((t,s));k=b-a
    if a+b >= n: raise ValueError('requires t+s<n')
    return (k+1)*mu**k+2*sum(mu**(k+2*r) for r in range(1,a))-(a+b-1)*mu**(a+b)

def brute(n,t,s,p):
    mu=1-2*p
    mean=[0.0,0.0]; cross=0.0
    for z in itertools.product([-1,1],repeat=n):
        wt=math.prod(p if v==-1 else 1-p for v in z)
        m=[]
        for tt in (t,s):
            x=sum(math.prod(z[(i-j)%n] for j in range(tt)) for i in range(n))/n
            m.append(x)
        mean[0]+=wt*m[0];mean[1]+=wt*m[1];cross+=wt*m[0]*m[1]
    return mean,n*(cross-mean[0]*mean[1])

cnt=0
for n in range(6,12):
    for t in range(1,max(2,(n-1)//2)):
        for s in range(t,n-t):
            if t+s>=n: continue
            for p in (.15,.32):
                means,cov=brute(n,t,s,p)
                assert all(abs(means[i]-(1-2*p)**v)<1e-10 for i,v in enumerate((t,s)))
                assert abs(cov-covariance(n,t,s,1-2*p))<1e-10,(n,t,s,cov)
                cnt+=1
print('finite enumerations passed:',cnt)
mu=.6
for t in (6,12,24,48):
    cov=np.array([[covariance(1000,t+k,t+j,mu) for k in range(5)] for j in range(5)])
    assert np.linalg.eigvalsh(cov).min()>0
    asym=np.array([[mu**abs(j-k)*(abs(j-k)+(1+mu*mu)/(1-mu*mu)) for k in range(5)] for j in range(5)])
    print('t',t,'largest covariance error',np.max(abs(cov-asym)))
print('success')
