#!/usr/bin/env python3
"""Independent finite checks of a row-Gram spectral theorem; not a proof."""
import numpy as np


def scaled_matrix(a, tau, sigma):
    n = len(a)
    d = np.diag(np.diag(a @ a.T))
    invd = np.linalg.inv(d)
    return np.block([
        [np.eye(n), tau * a.T],
        [-invd @ a / tau, np.eye(n)-2*invd @ a @ a.T],
    ])


def scaled_direct(a, x, y, b, c, tau, sigma):
    d = np.diag(np.diag(a @ a.T))
    xp = x - tau * (c - a.T @ y)
    yp = y + sigma * (b - a @ (2*xp - x))
    return xp, y + np.linalg.solve(d, (yp-y))/(tau*sigma)


def predicted(g):
    if g < 1:
        return np.sqrt(1-g)
    if g == 1:
        return 0.
    return g-1 + np.sqrt(g*(g-1))


checks=0
for rho in (0., .05, .21, .28, 1/3, .4, .5, .8):
    a = np.array([[1., 0.], [rho, np.sqrt(1-rho*rho)]])
    tau=sigma=.5
    k=scaled_matrix(a,tau,sigma)
    observed = max(abs(np.linalg.eigvals(k)))
    expected = rho+np.sqrt(rho*(1+rho))
    assert np.isclose(observed,expected,rtol=1e-11,atol=5e-14)
    assert (observed < 1-1e-8) == (rho<1/3-1e-8)
    if rho==0:
        assert np.linalg.norm(k @ k) < 1e-13
    xstar=np.array([2., 3.]);ystar=np.array([.7,-.4])
    b=a@xstar;c=a.T@ystar
    for j in range(15):
        x=np.array([.5+j/13, -.4+j/21]);y=np.array([j/17., -.8])
        xn,yn=scaled_direct(a,x,y,b,c,tau,sigma)
        truth = np.concatenate([xstar,ystar])+k@np.concatenate([x-xstar,y-ystar])
        assert np.allclose(np.concatenate([xn,yn]),truth,rtol=1e-11,atol=1e-12)
        checks+=1

rng=np.random.default_rng(20261016)
for n in (2,3,4,6):
    for j in range(100):
        a=rng.normal(size=(n,n))
        a+=.2*np.eye(n)
        if abs(np.linalg.det(a))<1e-6:
            continue
        d=np.diag(np.diag(a@a.T))
        g=np.linalg.eigvalsh(np.linalg.inv(np.sqrt(d))@a@a.T@np.linalg.inv(np.sqrt(d)))
        tau=sigma=.4/np.linalg.norm(a,2)
        k=scaled_matrix(a,tau,sigma)
        actual=max(abs(np.linalg.eigvals(k)))
        expect=max(predicted(float(t)) for t in g)
        assert np.isclose(actual,expect,rtol=1e-7,atol=1e-8),(g,actual,expect)
        checks+=1

# Two-step projected interior basin, independent actual projector implementation.
for n in (2,4):
    a=np.diag(np.arange(1.,n+1))
    tau=sigma=.05
    xs=np.arange(1.,n+1)
    ys=np.arange(1.,n+1)/3
    b=a@xs;c=a.T@ys
    for j in range(40):
        x=xs+rng.uniform(-.25,.25,n)
        y=ys+rng.uniform(-.1,.1,n)
        assert np.min(x+tau*a.T@(y-ys))>0
        for _ in range(2):
            xp=np.maximum(0,x-tau*(c-a.T@y))
            yp=y+sigma*(b-a@(2*xp-x))
            y=y+np.linalg.solve(np.diag(np.diag(a@a.T)),yp-y)/(tau*sigma)
            x=xp
        assert np.allclose(x,xs,atol=1e-12)
        assert np.allclose(y,ys,atol=1e-12)
        checks+=1

print(f'PASS: {checks} finite comparison cases')
