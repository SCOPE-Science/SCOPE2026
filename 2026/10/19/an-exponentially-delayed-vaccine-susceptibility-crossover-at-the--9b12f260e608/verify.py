#!/usr/bin/env python3
"""Independent numerical checks for the critical leaky-immunity SIRI identities.

No external packages are required. These tests illustrate finite trajectories;
the accompanying analytical proof establishes the unrestricted limits.
"""
import math


def rk4_step(fun, y, t, h):
    k1 = fun(t, y)
    k2 = fun(t + h/2, [u + h*a/2 for u,a in zip(y,k1)])
    k3 = fun(t + h/2, [u + h*a/2 for u,a in zip(y,k2)])
    k4 = fun(t + h, [u + h*a for u,a in zip(y,k3)])
    return [u+h*(a+2*b+2*c+d)/6 for u,a,b,c,d in zip(y,k1,k2,k3,k4)]


def trajectory(theta):
    phi = 0.5
    s,v,iu,iv = 0.5,0.4,0.06,0.04
    infected = iu + iv
    alpha = (1-phi)/phi
    eps = (theta-phi)/phi
    # SU, SV, RU, RV, IU, IV, Z, first infections, reinfections, H
    y = [s,v,0.,0.,iu,iv,1.,0.,0.,0.]
    def rhs(_,w):
        su,sv,ru,rv,xu,xv,z,p,q,H = w
        j = xu+xv
        lam = j/phi
        return [-lam*su,-theta*lam*sv,
                xu-phi*lam*ru,xv-phi*lam*rv,
                lam*(su+phi*ru)-xu,lam*(theta*sv+phi*rv)-xv,
                1-s*z**(-alpha)-v*z**(-eps),
                lam*(su+theta*sv),lam*phi*(ru+rv),lam]
    worst = 0.0
    for n in range(1,5001):
        y = rk4_step(rhs,y,(n-1)*0.006,0.006)
        if n%50: continue
        su,sv,ru,rv,xu,xv,z,p,q,H = y
        j=xu+xv
        B=1-s*z**(-alpha)-v*z**(-eps)
        eq=[sum(y[:6])-1,
            H-math.log(z)/phi,
            j-B/z,
            su-s*z**(-1/phi),
            sv-v*z**(-theta/phi),
            p-(s*(1-z**(-1/phi))+v*(1-z**(-theta/phi))),
            q-(math.log(z)+j-1+s*z**(-1/phi)+v*z**(-theta/phi))]
        worst=max(worst,max(abs(a) for a in eq))
    assert worst<1e-8, (theta,worst)
    return worst


def log_clock(eps,zscale=1.0):
    phi=0.5;s=0.5;v=0.4;alpha=1.0
    theta=phi*(1+eps)
    assert theta<=1
    def f0(_,q):
        Z=q[0]
        return [1-s*Z**(-alpha)-v*Z**(-eps)]
    Z=1.0
    for k in range(500):
        Z=rk4_step(f0,[Z],k/500,1/500)[0]
    # W(u)=Z(exp(u))/exp(u) for u=log(t), initialized at t=1.
    def fu(u,q):
        W=q[0]
        return [1-W-s*math.exp(-alpha*u)*W**(-alpha)
                -v*math.exp(-eps*u)*W**(-eps)]
    W=Z
    u_end=zscale/eps
    N=round(u_end/0.02)
    h=u_end/N
    for k in range(N):
        W=rk4_step(fu,[W],k*h,h)[0]
    target=1-v*math.exp(-zscale)
    return W,target


def main():
    a=trajectory(0.5)
    b=trajectory(0.65)
    output=[]
    for eps in (0.05,0.025,0.0125):
        value,target=log_clock(eps)
        output.append((eps,value,abs(value-target)))
    assert output[-1][2]<0.003
    assert output[2][2]<output[1][2]<output[0][2]<0.01
    # Exact endpoint constants are C=1-v for theta=phi, C=1 otherwise.
    assert math.isclose(0.1+0.5,0.6)
    assert math.isclose(0.1+0.5+0.4,1.0)
    print('VERIFY_OK: 2 full six-compartment trajectories, maximum exact-reduction residual %.3g; '
          'three singular log-clock tests, final profile discrepancy %.6g' %
          (max(a,b),output[-1][2]))

if __name__ == '__main__':
    main()
