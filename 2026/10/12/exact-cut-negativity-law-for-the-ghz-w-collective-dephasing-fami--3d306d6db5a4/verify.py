#!/usr/bin/env python3
import math

def formula(e,s): return (math.sqrt(41*e*e-18*e+9)-3*(1-e))/12+(math.sqrt(e*e+9*(1-e)*(1-e)*s*s)-e)/6

def jacobi(a):
    n=len(a); a=[r[:] for r in a]
    for _ in range(200*n*n):
        p=q=0; m=0.0
        for i in range(n):
            for j in range(i+1,n):
                if abs(a[i][j])>m: m=abs(a[i][j]); p=i; q=j
        if m<1e-13: break
        tau=(a[q][q]-a[p][p])/(2*a[p][q]); t=(1 if tau>=0 else -1)/(abs(tau)+math.sqrt(1+tau*tau)) if tau else 1.0
        c=1/math.sqrt(1+t*t); s=t*c; app=a[p][p]; aqq=a[q][q]; apq=a[p][q]
        for k in range(n):
            if k!=p and k!=q:
                x,y=a[k][p],a[k][q]; a[k][p]=a[p][k]=c*x-s*y; a[k][q]=a[q][k]=s*x+c*y
        a[p][p]=c*c*app-2*s*c*apq+s*s*aqq; a[q][q]=s*s*app+2*s*c*apq+c*c*aqq; a[p][q]=a[q][p]=0.0
    return [a[i][i] for i in range(n)]

def state(e,s):
    r=[[0.0]*8 for _ in range(8)]; r[0][0]=r[7][7]=(1-e)/2; r[0][7]=r[7][0]=(1-e)*s/2
    for i in (1,2,4):
        for j in (1,2,4): r[i][j]+=e/3
    return r

def ptA(r):
    z=[[0.0]*8 for _ in range(8)]
    for i in range(8):
        ai=(i>>2)&1; ri=i&3
        for j in range(8):
            aj=(j>>2)&1; rj=j&3; z[(aj<<2)|ri][(ai<<2)|rj]=r[i][j]
    return z

def main():
    assert 41*49-18*70+900-9*9==32*49
    cases=[(0.0,0.2),(0.1,0.8),(0.5,0.4),(0.99,0.7),(1.0,0.0),(1.0,1.0)]
    for e,s in cases:
        ev=jacobi(ptA(state(e,s))); num=sum(-x for x in ev if x<0); assert abs(num-formula(e,s))<2e-10
    for e,s in [(0.0,0.5),(0.2,0.3),(0.8,0.9),(0.99,0.2)]:
        den=math.sqrt(e*e+9*(1-e)*(1-e)*s*s); assert 3*(1-e)*(1-e)*s/(2*den)>0
    print('VERIFY_OK'); print('matrix_cases =',len(cases)); print('exact_sign_identity = 32*eta^2')
if __name__=='__main__': main()
