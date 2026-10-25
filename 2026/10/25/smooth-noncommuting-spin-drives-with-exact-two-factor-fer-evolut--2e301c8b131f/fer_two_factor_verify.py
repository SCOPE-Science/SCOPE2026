#!/usr/bin/env python3
"""Finite checks for an exact two-factor Fer expansion of smooth spin drives.

Use: python fer_two_factor_verify.py
Requires numpy and scipy; a numerical check is not a substitute for the proof.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm
from scipy.optimize import brentq

CHECKS = 0

def check(condition):
    global CHECKS
    CHECKS += 1
    assert bool(condition), 'check %d failed' % CHECKS


def spin_generators(j):
    dim = round(2*j)+1
    jp = np.zeros((dim, dim), dtype=complex)
    for i in range(1, dim):
        m = j-i
        jp[i-1, i] = math.sqrt((j-m)*(j+m+1))
    jm = jp.conjugate().T
    return np.array([jp+jm, (jp-jm)/1j, np.diag([2*(j-i) for i in range(dim)])])


def smoothstep(t):
    if t <= 0:
        return 0., 0.
    if t >= 1:
        return 1., 0.
    z = -1/t+1/(1-t)
    if z > 700:
        return 1., 0.
    if z < -700:
        return 0., 0.
    s = 1/(1+math.exp(-z))
    return s, s*(1-s)*(1/t**2+1/(1-t)**2)


def fer_weights(r):
    a = (1-math.cos(2*r))/(2*r*r)-math.sin(2*r)/r
    b = math.cos(2*r)/(r*r)-math.sin(2*r)/(2*r**3)
    return a,b


def resonance(n):
    x = brentq(lambda z: math.tan(z)-z, n*math.pi+1e-10,
               (n+.5)*math.pi-1e-10, xtol=5e-14)
    return x/2


def curve(t, r, theta):
    if t <= 1:
        s,ds = smoothstep(t)
        return np.array([r*s,0.,0.]),np.array([r*ds,0.,0.]),0.,0.
    s,ds=smoothstep(t-1)
    angle=theta*s
    rate=theta*ds
    return (r*np.array([math.cos(angle),math.sin(angle),0.]),
            r*rate*np.array([-math.sin(angle),math.cos(angle),0.]),
            angle,rate)


def mat(v, gen):
    return np.einsum('i,ijk->jk',v,gen)


def run_case(n, theta, j):
    r=resonance(n)
    alpha,beta=fer_weights(r)
    A=alpha*r*r
    check(abs(beta)<5e-13)
    check(abs(A-(1-(-1)**n*math.sqrt(1+4*r*r))/2)<1e-12)
    check(abs(2*r*math.cos(2*r)-math.sin(2*r))<1e-11)
    gen=spin_generators(j)
    dim=gen.shape[1]
    for t in np.linspace(0,2.9,161):
        f,h,angle,rate=curve(t,r,theta)
        if np.linalg.norm(f)>1e-7:
            a,b=fer_weights(np.linalg.norm(f))
            p=np.cross(f,h)
            q=np.cross(p,f)
            out=a*p+b*q
        else:
            out=np.zeros(3)
        check(np.linalg.norm(out-np.array([0.,0.,A*rate]))<2e-10)
    def rhs(t,y):
        _,h,_,_=curve(t,r,theta)
        return (-1j*mat(h,gen)@y.reshape(dim,dim)).reshape(dim*dim)
    sol=solve_ivp(rhs,[0,2.9],np.eye(dim,dtype=complex).reshape(dim*dim),
        rtol=1e-10,atol=3e-12,max_step=.008,dense_output=True)
    check(sol.success)
    max_err=0.
    for t in np.linspace(0,2.9,121):
        f,h,angle,rate=curve(t,r,theta)
        exact=expm(-1j*mat(f,gen))@expm(-1j*A*angle*gen[2])
        actual=sol.sol(t).reshape(dim,dim)
        err=np.linalg.norm(actual-exact,ord='fro')
        max_err=max(max_err,err)
        check(err<2e-8)
        check(np.linalg.norm(exact.conj().T@exact-np.eye(dim))<2e-12)
    return max_err


def main():
    for n in range(1,5):
        r=resonance(n)
        print('root',n,'r',format(r,'.14g'),'A',format(fer_weights(r)[0]*r*r,'.14g'))
    for n, theta, j in [(1,0.3,.5),(1,math.pi/2,.5),
                         (1,4*math.pi,.5),(2,1.2,.5),
                         (3,math.pi/2,.5),(1,math.pi/2,1.),
                         (2,math.pi/2,1.),(1,math.pi/2,1.5)]:
        e=run_case(n,theta,j)
        print('case',n,theta,j,'ODE matrix error',format(e,'.3g'))
    print('PASS',CHECKS,'numerical assertions')

if __name__=='__main__':
    main()
