"""Finite arithmetic checks for angular optimization of two-orbit kernel Grams."""
import math
import numpy as np

passed = 0

def check(condition, label):
    global passed
    if not condition:
        raise AssertionError(label)
    passed += 1

def spectrum_blocks(power, m, r, s, phi):
    theta = m * phi
    t = (r*s)**m
    c = math.cos(theta)
    d = 1+t*t-2*t*c
    result = []
    for k in range(m):
        if power == 1:
            Sr = 1/(1-r**(2*m))
            Ss = 1/(1-s**(2*m))
            cross_sq = 1/d
        else:
            def S(z):
                return ((k+1)+(m-k-1)*z)/(1-z)**2
            Sr = S(r**(2*m))
            Ss = S(s**(2*m))
            a, b = k+1, m-k-1
            cross_sq = (a*a+b*b*t*t+2*a*b*t*c)/(d*d)
        A = m*(1-r*r)**power*r**(2*k)*Sr
        B = m*(1-s*s)**power*s**(2*k)*Ss
        C2 = m*m*((1-r*r)*(1-s*s))**power*(r*s)**(2*k)*cross_sq
        delta = math.sqrt((A-B)**2+4*C2)
        result += [(A+B+delta)/2,(A+B-delta)/2]
    return np.sort(np.array(result))

def gram(power,m,r,s,phi):
    z=np.array([r*np.exp(2j*np.pi*j/m) for j in range(m)]+[s*np.exp(1j*(phi+2*np.pi*j/m)) for j in range(m)])
    norm=(1-np.abs(z)**2)**(power/2)
    return norm[:,None]*norm[None,:]/(1-z[:,None]*np.conj(z[None,:]))**power

for power in [1,2]:
    for m in [2,3,4,5,6]:
        for r,s in [(0.23,0.54),(0.51,0.82),(0.12,0.91)]:
            star=np.pi/m
            star_spec=spectrum_blocks(power,m,r,s,star)
            for phi in [0.0, 0.13/m, 0.65/m, 1.7/m, star]:
                g=gram(power,m,r,s,phi)
                eig=np.linalg.eigvalsh(g)
                block=spectrum_blocks(power,m,r,s,phi)
                check(np.max(np.abs(eig-block)) < 2e-8, f'block spectrum p={power},m={m}')
                check(np.min(eig)>-1e-11, 'positive gram')
                check(eig[0] <= star_spec[0]+2e-9, 'sharp lower frame bound')
                check(eig[-1] >= star_spec[-1]-2e-9, 'sharp upper frame bound')
                check(np.sum(eig**2) >= np.sum(star_spec**2)-2e-8, 'convex t^2 spectral statistic')
                if np.min(eig)>1e-10 and np.min(star_spec)>1e-10:
                    check(np.sum(1/eig) >= np.sum(1/star_spec) - 1e-8*max(1.0,np.sum(1/star_spec)), f'inverse trace optimality p={power},m={m},r={r},s={s},phi={phi}: {np.sum(1/eig)} vs {np.sum(1/star_spec)}')
                if power==1:
                    u,v=r**m,s**m
                    c=np.cos(m*phi)
                    N=u*u+v*v-2*u*v*c
                    D=1+u*u*v*v-2*u*v*c
                    Nstar=(u+v)**2
                    Dstar=(1+u*v)**2
                    expected=(N/D * Dstar/Nstar)**m
                    actual=np.prod(eig)/np.prod(star_spec)
                    check(abs(actual-expected)<3e-6, 'Hardy determinant ratio')
                    q=2*u*v*(1+c)*(1-u*u)*(1-v*v)/(Dstar*N)
                    check(abs(expected*(1+q)**m-1)<3e-10,'exact Hardy phase deficit')

# Symbolic derivative identity for the Bergman off-diagonal squared modulus.
for m in range(2,13):
    for k in range(m):
        a,b=k+1,m-k-1
        for t in [0.01,0.25,0.75]:
            for c in [-1.0,-0.3,0.6,1.0]:
                D=1+t*t-2*t*c
                N=a*a+b*b*t*t+2*a*b*t*c
                deriv=(2*a*b*t*D+4*t*N)/D**3
                check(deriv>0, 'strict Bergman cross-correlation monotonicity')

print(f'PASS: {passed} finite checks of blocks, convex spectral order, Hardy determinant, Bergman monotonicity')
