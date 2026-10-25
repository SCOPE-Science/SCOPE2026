#!/usr/bin/env python3
"""Independent deterministic numerical consistency checks; theorem proof is analytic."""
import math
import random


def spectrum(A):
    B = [list(map(float,row)) for row in A]
    n=len(B)
    for _ in range(150*n*n):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda pair:abs(B[pair[0]][pair[1]]))
        if abs(B[p][q])<2e-13: break
        theta=.5*math.atan2(2*B[p][q],B[q][q]-B[p][p])
        c,s=math.cos(theta),math.sin(theta)
        app,aqq,apq=B[p][p],B[q][q],B[p][q]
        B[p][p]=c*c*app-2*s*c*apq+s*s*aqq
        B[q][q]=s*s*app+2*s*c*apq+c*c*aqq
        B[p][q]=B[q][p]=0.
        for j in range(n):
            if j==p or j==q:continue
            apj,aqj=B[p][j],B[q][j]
            B[p][j]=B[j][p]=c*apj-s*aqj
            B[q][j]=B[j][q]=s*apj+c*aqj
    return sorted(B[i][i] for i in range(n))


def cond(n,a,b,t,d):
    u=[a]+[b]*(n-1)
    A=[[d[i]*d[j]*((1. if i==j else 0.)+t*u[i]*u[j]) for j in range(n)] for i in range(n)]
    ev=spectrum(A)
    return ev[-1]/ev[0]


def theorem(n,a,b,t):
    k=n-1;P=1+t*a*a;Q=1+t*k*b*b
    if a*a<=k*b*b: return 1.,1+t*(a*a+k*b*b)
    x=math.sqrt(Q/P)
    r=t*a*b*math.sqrt(k)/math.sqrt(P*Q)
    return x,(1+r)/(1-r)


def main():
    rng=random.Random(291013)
    total=0
    for n in range(3,9):
        for j in range(35):
            a=math.exp(rng.uniform(-1.4,2));b=math.exp(rng.uniform(-1.4,1));t=math.exp(rng.uniform(-2,1.4))
            x,k=theorem(n,a,b,t)
            got=cond(n,a,b,t,[x]+[1.]*(n-1))
            assert abs(k/got-1)<2e-9,(n,a,b,t,k,got)
            for m in range(3):
                d=[math.exp(rng.uniform(-1.3,1.3)) for _ in range(n)]
                test=cond(n,a,b,t,d)
                assert test+1e-7>=k,(n,a,b,t,k,test,d)
                total+=1
            for q in [.01,.1,.4,.9,1.,1.3,2.5,6.]:
                test=cond(n,a,b,t,[q]+[1.]*(n-1))
                assert test+1e-8>=k,(n,a,b,t,k,test,q)
                total+=1
    n,a,b,t=5.,3.,1.,1.
    x,k=theorem(int(n),a,b,t)
    assert abs(x-1/math.sqrt(2))<1e-12
    assert abs(k-(43+30*math.sqrt(2))/7)<1e-11
    assert abs(cond(5,3,1,1,[1]*5)-14.)<1e-11
    jac=cond(5,3,1,1,[1/math.sqrt(5)]+[1.]*4)
    assert abs(jac-(7+math.sqrt(189/5))/(7-math.sqrt(189/5)))<1e-10
    assert jac>14 and k<14
    print('VERIFY_OK',total)

if __name__=='__main__':main()
