from math import comb

def mul(a,b,N):
    out=[0]*(N+1)
    for i,x in enumerate(a):
        if x:
            lim=min(N-i,len(b)-1)
            for j in range(lim+1):
                y=b[j]
                if y: out[i+j]+=x*y
    return out

def factor_power(step,e,N):
    f=[0]*(N+1)
    for k in range(0,N//step+1):
        f[k*step]=(-1)**k*comb(e,k)
    return f

def A_power(e,N,scale=1):
    out=[1]+[0]*N
    m=1
    while m*scale<=N:
        out=mul(out,factor_power(m*scale,e,N),N)
        m+=1
    return out

def partitions(N):
    p=[0]*(N+1); p[0]=1
    for m in range(1,N+1):
        for n in range(m,N+1): p[n]+=p[n-m]
    return p

def coeffs(p,a,N):
    t=p**a
    F=A_power(t*t-1,N)
    num=A_power(t,N,scale=t)
    inv=partitions(N)
    C=mul(num,inv,N)
    return F,C

def vp(z,p):
    if z==0:return 10**9
    z=abs(z); r=0
    while z%p==0:r+=1;z//=p
    return r

cases=[(2,1,24),(2,2,24),(2,3,24),(3,1,24),(3,2,24),(5,1,24),(7,1,24)]
rows=[]
for p,a,N in cases:
    F,C=coeffs(p,a,N)
    mod=p**(a+1)
    assert all((F[n]-C[n])%mod==0 for n in range(N+1))
    n0=p**(a-1)
    d=F[n0]-C[n0]
    assert vp(d,p)==a+1,(p,a,n0,d,vp(d,p))
    rows.append((p,a,n0,d,vp(d,p)))
print('VERIFY_OK cases=%d sharp=%s'%(len(cases),rows))
