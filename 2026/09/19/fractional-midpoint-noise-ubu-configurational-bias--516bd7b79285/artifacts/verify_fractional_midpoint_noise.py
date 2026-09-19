#!/usr/bin/env python3
"""Direct Lyapunov checks for fractional-midpoint UBU covariance formulas."""
import math
import numpy as np


def cov(h, gamma, alpha, lam, theta):
    k = alpha * lam
    q = math.exp(-gamma*h/2)
    A = np.array([[1-k*h*(1-q)/gamma,
                   (1-q*q)/gamma-k*h*(1-q)**2/gamma**2],
                  [-k*h*q, q*q-k*h*q*(1-q)/gamma]])
    Q0 = np.array([[2*alpha/gamma*(h-2*(1-q*q)/gamma+(1-q**4)/(2*gamma)),
                    alpha/gamma*(1-q*q)**2],
                   [alpha/gamma*(1-q*q)**2, alpha*(1-q**4)]])
    vm = 2*alpha/gamma*(h/2-2*(1-q)/gamma+(1-q*q)/(2*gamma))
    r = np.array([2*alpha/gamma*(h/2-(1-q*q)*(1-q/2)/gamma),
                  alpha*q*(1-q)**2/gamma])
    c = np.array([-k*h*(1-q)/gamma, -k*h*q])
    Q = Q0 + theta*(np.outer(c,r)+np.outer(r,c)) + theta**2*vm*np.outer(c,c)
    S = np.linalg.solve(np.eye(4)-np.kron(A,A), Q.reshape(-1)).reshape(2,2)
    return A, S


def root(h, gamma=3.0, alpha=1.0, lam=1.0):
    y = [cov(h,gamma,alpha,lam,t)[1][0,0]-1/lam for t in (0,.5,1)]
    a = 2*(y[2]-2*(y[1]-y[0])-y[0]); b = y[2]-y[0]-a; c = y[0]
    rr = np.roots([a,b,c])
    return [z.real for z in rr if abs(z.imag)<1e-10 and 0<z.real<1][0]


def main():
    g=a=l=1.0
    g=3.0
    print('gamma=3 alpha=lambda=1')
    for h in (.1,.05,.025):
        vals=[]
        for name,t,p in [('LC',0,2),('1/3',1/3,3),('UBU',1,2),('corr',1/3-g*h/9,4)]:
            A,S=cov(h,g,a,l,t); err=S[0,0]-1
            vals.append((name,t,float(max(abs(np.linalg.eigvals(A)))),float(err/h**p)))
        print('h=',h,vals,'root=',root(h))
    print('predicted:',1/12,-1/12,-1/6,(23*g*g-80)/8640)
    for h in (.1,.05,.025):
        t=1/3-g*h/9
        errs=[abs(cov(h,g,a,L,t)[1][0,0]-1/L) for L in (.5,1,3)]
        print('anisotropic',h,float(max(errs)/h**4))

if __name__ == '__main__':
    main()
