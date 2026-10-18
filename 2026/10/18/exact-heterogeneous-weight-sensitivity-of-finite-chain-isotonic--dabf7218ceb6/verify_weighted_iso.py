"""Finite consistency checks for weighted least-squares isotonic sensitivity.
Only public mathematical checks, not a substitute for the analytic proof.
"""
import itertools, math, random


def iso(y,w):
    blocks=[]
    for i,(yi,wi) in enumerate(zip(y,w)):
        blocks.append([i,i,wi,wi*yi])
        while len(blocks)>=2 and blocks[-2][3]/blocks[-2][2]>blocks[-1][3]/blocks[-1][2]:
            b=blocks.pop();a=blocks.pop();blocks.append([a[0],b[1],a[2]+b[2],a[3]+b[3]])
    z=[0.0]*len(y)
    for a,b,W,V in blocks:
        for i in range(a,b+1):z[i]=V/W
    return z


def norm(x,p):
    if p==float('inf'):return max(abs(t) for t in x)
    return sum(abs(t)**p for t in x)**(1./p)


def interval_constant(w,p):
    n=len(w); out=(1.,0,0)
    for a in range(n):
        for b in range(a,n):
            B=w[a:b+1]; k=len(B);W=sum(B)
            if p==float('inf'): val=1.
            elif p==1:val=k*max(B)/W
            else:
                q=p/(p-1)
                val=k**(1./p)*(sum((v/W)**q for v in B))**(1./q)
            if val>out[0]:out=(val,a,b)
    return out


def witness(w,p,a,b):
    n=len(w); B=list(range(a,b+1));alpha=sum(w[i]*i for i in B)/sum(w[i] for i in B)
    base=[-20.*(a-i) for i in range(a)]+[alpha-i for i in B]+[20.*(i-b) for i in range(b+1,n)]
    h=[0.]*n
    if p==float('inf'):
        for i in B:h[i]=1.
    elif p==1:
        h[max(B,key=lambda i:w[i])]=1.
    else:
        q=p/(p-1)
        for i in B:h[i]=w[i]**(q-1.)
    e=1.e-5
    u=iso(base,w);v=iso([base[i]+e*h[i] for i in range(n)],w)
    return norm([v[i]-u[i] for i in range(n)],p)/(e*norm(h,p))


def envelope(n,p,kappa):
    out=(1.,0,0)
    for k in range(1,n+1):
        for r in range(k+1):
            if p==1:val=k*kappa/(r*kappa+k-r) if r else 1.
            elif p==float('inf'):val=1.
            else:
                q=p/(p-1.)
                val=k**(1/p)*(r*kappa**q+k-r)**(1/q)/(r*kappa+k-r)
            if val>out[0]:out=(val,k,r)
    return out


def continuum(p,kappa):
    q=p/(p-1.)
    A=kappa**q-1;B=kappa-1
    theta=(A-q*B)/((q-1)*A*B)
    C=((q-1)**(1-1/q)/q)*A/(B**(1/q)*(A-B)**(1-1/q))
    return theta,C


def main():
    random.seed(240417)
    checks=0
    for n in range(2,9):
      for j in range(26):
        w=[10**random.uniform(-1,1) for _ in range(n)]
        for p in (1,1.5,2,3,4,11,float('inf')):
            c,a,b=interval_constant(w,p)
            ratio=witness(w,p,a,b)
            assert abs(c-ratio)<5.e-5,(n,p,w,c,ratio,a,b)
            checks+=1
            for _ in range(3):
                x=[random.uniform(-5,5) for _ in range(n)]
                y=[random.uniform(-5,5) for _ in range(n)]
                u=iso(x,w);v=iso(y,w)
                R=norm([ui-vi for ui,vi in zip(u,v)],p)/norm([xi-yi for xi,yi in zip(x,y)],p)
                assert R<=c+1.e-8,(n,p,R,c)
                checks+=1
    for p in (1.1,1.5,2,3,4,9):
        for kappa in (1.1,2,4,25):
            theta,C=continuum(p,kappa)
            assert 0<theta<1
            q=p/(p-1)
            F=(1+theta*(kappa**q-1))**(1/q)/(1+theta*(kappa-1))
            assert abs(F-C)<1.e-11
            previous=0.0
            for n in (100,300,800):
                m=envelope(n,p,kappa)[0]
                assert previous<=m+1.e-10<=C+2.e-10,(n,p,kappa,C,m)
                previous=m
                checks+=1
            assert C-previous<0.02,(p,kappa,C,previous)
            checks+=3
    for kappa in (1.2,2,10):
        for n in (2,3,8,55):
            C=envelope(n,1,kappa)[0]
            assert abs(C-n*kappa/(kappa+n-1))<1.e-9
            checks+=1
    print('WEIGHTED_ISOTONIC_VERIFY_OK',checks)

if __name__=='__main__':main()
