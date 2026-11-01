"""Numerical diagnostics for the annular active-Brownian weak-swimming theorem.

Requires Python 3, mpmath, numpy and scipy. These finite diagnostics supplement,
but do not replace, the analytic Bessel and perturbation arguments.
"""
import math
import mpmath as mp
import numpy as np
from scipy.integrate import solve_bvp

mp.mp.dps = 55
COUNT = 0

def check(cond, msg):
    global COUNT
    if not cond:
        raise AssertionError(msg)
    COUNT += 1

def exact(alpha, beta):
    alpha = mp.mpf(str(alpha)); beta = mp.mpf(str(beta))
    k = mp.sqrt(beta)
    L = mp.log(1 / alpha)
    c = (1 - alpha**2) / (4 * L)
    h = lambda r: c/r - r/2
    hi, ho = h(alpha), h(1)
    I = lambda r: mp.besseli(1, k*r)
    K = lambda r: mp.besselk(1, k*r)
    den = I(1)*K(alpha) - K(1)*I(alpha)
    def intI(s):
        return (mp.besseli(0, k) - mp.besseli(0, k*s))/k
    def intK(s):
        return (mp.besselk(0, k*s) - mp.besselk(0, k))/k
    def intw(s):
        ia = (I(1)*intK(s) - K(1)*intI(s))/den
        ib = (K(alpha)*intI(s) - I(alpha)*intK(s))/den
        return hi*ia + ho*ib
    C = -intw(alpha)/(2*L*beta)
    def B(s):
        s = mp.mpf(str(s))
        int_h = -(1-s**2)/4 + c*mp.log(1/s)
        return (int_h - intw(s))/(2*beta) + C*mp.log(s)
    S = hi + ho
    profile = lambda y: S*y/(2*L)+ho*y*y/4
    root = -2*S/(L*ho)
    return B,C,profile,root,hi,ho,S

def bvp(alpha, beta):
    c = (alpha**2-1)/(4*np.log(alpha))
    def fun(r, state):
        A,Ap,B,Bp = state
        h = -r/2+c/r
        return np.vstack((Ap, -Ap/r + (1/r**2+beta)*A - h,
                          Bp, -Bp/r-(Ap+A/r)/2))
    def bc(left,right):
        return np.array([left[0],right[0],left[2],right[2]])
    x = np.linspace(alpha,1,180)
    sol = solve_bvp(fun,bc,x,np.zeros((4,x.size)),tol=2e-10,max_nodes=25000)
    check(sol.success,'Boundary-value solver did not converge')
    return sol

for alpha in (0.1,0.25,0.5):
    for beta in (0.5,3,30,100):
        B,C,profile,root,hi,ho,S = exact(alpha,beta)
        sol = bvp(alpha,beta)
        check(hi>0 and ho<0 and S>0,'Boundary signs')
        check(root>0,'Layer root must be positive')
        for s in (alpha+(1-alpha)*.1,alpha+(1-alpha)*.5,alpha+(1-alpha)*.8):
            check(abs(float(B(s))-float(sol.sol(s)[2]))<3e-9,
                  f'Independent ODE disagreement: {alpha=}, {beta=}, {s=}')
        check(abs(float(C)-float(sol.sol(1)[3]))<3e-9,'Derivative disagreement')
        check(abs(float(B(alpha)))<2e-42 and abs(float(B(1)))<2e-42,
              'Dirichlet endpoints')

for alpha in (0.1,0.25,0.5):
    for beta in (400,1600,6400,25600):
        B,C,P,root,hi,ho,S = exact(alpha,beta)
        L=math.log(1/alpha)
        goalC=-float(S)/(2*L)
        scaledC=float(C)*beta**1.5
        check(C<0,'Wrong sign for large rotational diffusion')
        check(abs(scaledC-goalC)<0.09,'Boundary slope has incorrect limit')
        for y in (float(root)/3, float(root)*1.6):
            s=1-y/beta
            if y<float(root):
                check(B(s)>0,'Expected positive outer skin')
            else:
                check(B(s)<0,'Expected negative after skin')
            scaledB=float(B(s))*beta**2.5
            predicted=float(P(y))
            check(abs(scaledB-predicted)<.08,'Incorrect boundary-skin profile')
    B,C,P,root,hi,ho,S=exact(alpha,25600)
    check(abs(float(C)*25600**1.5+float(S)/(2*math.log(1/alpha)))<0.012,
          'Slow large-diffusion slope convergence')

print(f'PASS: {COUNT} independent finite diagnostic assertions')
