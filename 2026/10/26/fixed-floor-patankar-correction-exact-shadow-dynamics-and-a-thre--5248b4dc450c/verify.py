from fractions import Fraction as F
import math
import numpy as np

def src_check():
    alpha,beta,m,eps=F(4),F(1),F(1),F(2)
    x=m*beta/(alpha+beta); z=m-x
    for h in (F(1,1000),F(1,2),F(1),F(10)):
        true_delta=h*(beta*z*z-alpha*x*x)/(eps+h*(alpha*x+beta*z))
        new=x+true_delta
        assert true_delta>0 and x<new<m
        assert true_delta==h*F(12,25)/(2+h*F(8,5))
    # factor theta always >0

def step_sdirk(y,h,alpha=4.,beta=1.,epsilon=2.):
    G=np.array([[-alpha,beta],[alpha,-beta]],float)
    gamma=1-1/math.sqrt(2)
    I=np.eye(2)
    Y1=np.linalg.solve(I-h*gamma*G,y)
    Y2=np.linalg.solve(I-h*gamma*G,y+h*(1-gamma)*G@Y1)
    pred=Y2
    scale=(1-gamma)*np.maximum(Y1,0)/np.maximum(pred,epsilon)+gamma*np.maximum(Y2,0)/np.maximum(pred,epsilon)
    B=G@np.diag(scale)
    out=np.linalg.solve(I-h*B,y)
    assert min(out)>=-1e-12
    assert abs(sum(out)-sum(y))<2e-12
    return out

def reference(T):
    E=math.exp(2*T)
    return (3*E-1)/(9*E+1)

def tests():
    src_check()
    y0=np.array([0.2,0.8])
    for h in (1.,.5,.25,.1,.05,.025,.0125,.00625,.003125):
        n=round(1/h); y=y0.copy()
        for _ in range(n): y=step_sdirk(y,h)
        err=abs(y[0]-reference(1))
        print(f'{h:8.6f} {y[0]:.13f} error_to_shadow {err:.8g} error_to_true {y[0]-y0[0]:.8g}')
    assert abs(y[0]-reference(1)) < .0004
    for alpha,beta in [(10,1),(4,1),(2,1),(3,2)]:
        r=beta/alpha
        e=1
        for m in (.25,.5,1.,1.5,2.,2.5,4.,10):
            if m<= e*(1+math.sqrt(r)):
                x=m*math.sqrt(r)/(1+math.sqrt(r))
            elif m<e*(1+1/r):
                x=(-r*e+math.sqrt(r*r*e*e+4*r*e*m))/2
            else: x=m*r/(1+r)
            g=lambda z:z*z/max(z,e)
            assert 0<x<m and abs(alpha*g(x)-beta*g(m-x))<1e-10
            assert x+1e-12>=m*r/(1+r)
    print('finite checks: PASS')
if __name__=='__main__':tests()
