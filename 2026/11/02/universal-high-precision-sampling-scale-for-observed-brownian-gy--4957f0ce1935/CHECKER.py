"""Deterministic checks for a two-time Gaussian irreversibility theorem.
Public model parameters only. Python 3 standard library; no external packages.
Run: python CHECKER.py
"""
from math import exp, sqrt


def trans(a):
    return [list(x) for x in zip(*a)]


def add(a,b):
    return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def sub(a,b):
    return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(a,s):
    return [[s*x for x in row] for row in a]


def mul(a,b):
    bt=trans(b)
    return [[sum(x*y for x,y in zip(row,col)) for col in bt] for row in a]


def inv(a):
    n=len(a)
    s=[[float(x) for x in row]+[float(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        k=max(range(j,n),key=lambda i:abs(s[i][j]))
        s[k],s[j]=s[j],s[k]
        pivot=s[j][j]
        if abs(pivot)<1e-20: raise ArithmeticError('singular matrix')
        s[j]=[x/pivot for x in s[j]]
        for i in range(n):
            if i==j:continue
            c=s[i][j]
            s[i]=[x-c*y for x,y in zip(s[i],s[j])]
    return [row[n:] for row in s]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def blocks(a,b,c,d):
    return [a[i]+b[i] for i in range(len(a))]+[c[i]+d[i] for i in range(len(c))]


def model(k,u,tx,ty,t,h):
    assert k>0 and 0<abs(u)<k and tx>0 and ty>0 and tx!=ty and t>0 and h>=0
    a=k-u;b=k+u
    d=(tx+ty)/2;e=(tx-ty)/2
    diffus=[[d,e],[e,d]]
    c=[[d/a,2*e/(a+b)],[2*e/(a+b),d/b]]
    f=[[exp(-a*t),0],[0,exp(-b*t)]]
    v=add(c,scale(diffus,h))
    z=mul(c,f)
    p=add(v,scale(add(z,trans(z)),0.5))
    q=sub(v,scale(add(z,trans(z)),0.5))
    j=scale(sub(z,trans(z)),0.5)
    g=mul(mul(trans(j),inv(p)),j)
    w=sub(q,g)
    kl=2*tr(mul(inv(w),g))
    # Direct four-dimensional stationary forward/reverse normal KL.
    sf=blocks(v,z,trans(z),v)
    perm=[2,3,0,1]
    sr=[[sf[perm[i]][perm[j]] for j in range(4)] for i in range(4)]
    brute=(tr(mul(inv(sr),sf))-4)/2
    pp=exp(-a*t);qq=exp(-b*t);cross=c[0][1]
    denom=c[0][0]*c[1][1]*(1-pp*pp)*(1-qq*qq)-cross*cross*(1-pp*qq)**2
    noiseless=cross*cross*(pp-qq)**2*(1-pp*qq)/denom
    sig=u*u*(tx-ty)**2/(2*k*tx*ty)
    return kl,brute,noiseless,sig


def golden_max(fun,lo,hi):
    gr=(sqrt(5)-1)/2
    c=hi-gr*(hi-lo);d=lo+gr*(hi-lo)
    fc=fun(c);fd=fun(d)
    for _ in range(130):
        if fc>fd:
            hi=d;d=c;fd=fc;c=hi-gr*(hi-lo);fc=fun(c)
        else:
            lo=c;c=d;fc=fd;d=lo+gr*(hi-lo);fd=fun(d)
    x=(lo+hi)/2
    return x,fun(x)


def close(x,y,rtol=1e-7,atol=1e-12):
    assert abs(x-y)<=atol+rtol*max(abs(x),abs(y)),(x,y)


def run():
    cases=[(1.,.4,1.,3.),(2.,.5,4.,1.),(.75,-.22,1.,2.2),(3.,-1.2,2.,8.)]
    cnt=0
    for case in cases:
        for t in (.015,.11,.55,2.3):
            for h in (0.,.002,.07):
                kl,brute,plain,sig=model(*case,t,h)
                close(kl,brute,rtol=2e-8,atol=5e-11)
                if h==0:close(kl,plain,rtol=2e-8,atol=5e-11)
                assert kl>=0
                assert kl/t <sig
                cnt+=1
    # The limiting detection horizon and information-loss coefficient.
    for k,u,tx,ty in cases:
        for h in (1e-4,1e-5):
            function=lambda t:model(k,u,tx,ty,t,h)[0]/t
            start=sqrt(h/k)
            opt,value=golden_max(function,0.35*start,1.8*start)
            target= sqrt(h/k)
            assert abs(opt/target-1)<.045,(opt,target)
            sig=model(k,u,tx,ty,.05,h)[3]
            asym=1-2*sqrt(k*h)
            assert abs(value/sig-asym)<.004
            # Broad comparison: no fixed small or large horizon beats optimum.
            assert value>max(function(x) for x in (0.1*start,0.2*start,3*start,8*start,.5,2.,10.))
            cnt+=1
    # Exact noiseless continuous-time limiting coefficient.
    for case in cases:
        for t in (.002,.001):
            kl,_,_,sig=model(*case,t,0.)
            assert abs(kl/t/sig - (1-case[0]*t))<5e-5
            cnt+=1
    print('PASS:',cnt,'Gaussian KL/direct covariance checks and sharp high-precision optimum tests')


if __name__=='__main__':
    run()
