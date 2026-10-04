#!/usr/bin/env python3
import math

PI=math.pi

def coeffs_gamma0(k,t,theta,l1,l2,l3,ell):
    c=math.cos(PI*t/3.0)
    su=math.sin(PI*t/3.0)
    s1=math.sin(k*l1); s2=math.sin(k*l2); s3=math.sin(k*l3)
    B4=(-4.0*s1 + 3.0*math.sin(k*(l1+l2+l3))
        + math.sin(k*(l1+l2-l3))
        + math.sin(k*(l2+l3-l1))
        + math.sin(k*(l3+l1-l2)))
    B2=(8.0*s1 - 9.0*math.sin(k*(l1+l2+l3))
        + math.sin(k*(l1+l2-l3))
        + math.sin(k*(l2+l3-l1))
        + math.sin(k*(l3+l1-l2)))
    P6=72.0*ell**6*(c-1.0)**2*s1*s2*s3
    P4=12.0*ell**4*(c-1.0)*(c+1.0)*B4
    P2=2.0*ell**2*(c+1.0)**2*B2
    Pc=-16.0*ell**2*(c+1.0)*(3.0*k*k*ell**2*(c-1.0)-(c+1.0))*(s2+s3)
    Ps=32.0*k*ell**3*math.sqrt(3.0)*su*(c+1.0)*(math.cos(k*l3)-math.cos(k*l2))
    return P6,P4,P2,Pc,Ps

def secular(k,t,theta,l1,l2,l3,ell):
    P6,P4,P2,Pc,Ps=coeffs_gamma0(k,t,theta,l1,l2,l3,ell)
    return k**6*P6+k**4*P4+k**2*P2+k**2*(math.sin(theta)*Ps+math.cos(theta)*Pc)

def x_limit(tau,theta,eps,a,b,l1,ell):
    return (24.0*l1/(PI**4*ell**2*tau**2)
            *(math.sin(a+b)-eps*(math.sin(a)+math.sin(b))*math.cos(theta))
            /(math.sin(a)*math.sin(b)))

def bisect_x(m,t,theta,x0,l1,l2,l3,ell):
    k0=m*PI/l1
    # Find the sign-changing root nearest the predicted branch.
    step=0.10
    radius=10.0
    xs=[x0-radius+i*step for i in range(int(2*radius/step)+1)]
    vals=[secular(k0+x/m,t,theta,l1,l2,l3,ell) for x in xs]
    brackets=[]
    for xa,xb,fa,fb in zip(xs,xs[1:],vals,vals[1:]):
        if fa==0.0:
            brackets.append((xa,xa))
        elif fa*fb<0.0:
            brackets.append((xa,xb))
    if not brackets:
        raise AssertionError('no sign-changing root found')
    a0,b0=min(brackets,key=lambda ab:abs(0.5*(ab[0]+ab[1])-x0))
    if a0==b0:
        return a0
    fa=secular(k0+a0/m,t,theta,l1,l2,l3,ell)
    fb=secular(k0+b0/m,t,theta,l1,l2,l3,ell)
    for _ in range(90):
        mid=0.5*(a0+b0)
        fm=secular(k0+mid/m,t,theta,l1,l2,l3,ell)
        if fa*fm<=0.0:
            b0,fb=mid,fm
        else:
            a0,fa=mid,fm
    return 0.5*(a0+b0)

def main():
    # A commensurate test subsequence chosen only for replay: l2+l3=2pi,
    # l1=2pi, m=1 mod 6. Then a=pi/3, b=2pi/3, epsilon=-1.
    l1=2.0*PI; l2=2.0*PI/3.0; l3=4.0*PI/3.0; ell=1.0
    tau=1.4; eps=-1; a=PI/3.0; b=2.0*PI/3.0
    predicted_width=96.0/(PI**3*ell**2*tau**2)*abs((math.sin(a)+math.sin(b))/(math.sin(a)*math.sin(b)))
    errors=[]
    for m in (121,241,481,961):
        assert m%6==1 and m%2==1
        t=tau/math.sqrt(m)
        roots=[]
        for theta in (0.0,PI):
            xp=x_limit(tau,theta,eps,a,b,l1,ell)
            xr=bisect_x(m,t,theta,xp,l1,l2,l3,ell)
            roots.append(xr)
        k0=m*PI/l1
        energies=[(k0+x/m)**2-k0**2 for x in roots]
        width=abs(energies[0]-energies[1])
        errors.append(abs(width-predicted_width))
    # The exact secular equation converges monotonically here toward the predicted finite width.
    assert all(errors[i+1] < errors[i] for i in range(len(errors)-1)), errors
    assert errors[-1] < 0.05, (predicted_width, errors[-1])

    # Check the scaled exact secular function against the derived limiting affine function
    # for a nontrivial Bloch phase. Only convergence is asserted, not exact equality at finite m.
    theta=0.73
    target=x_limit(tau,theta,eps,a,b,l1,ell)
    scaled=[]
    for m in (241,481,961,1921):
        t=tau/math.sqrt(m); k0=m*PI/l1
        scaled.append(abs(secular(k0+target/m,t,theta,l1,l2,l3,ell))/m**3)
    assert scaled[-1] < scaled[0]
    assert scaled[-1] < 0.40, scaled
    print('VERIFY_OK')
    print('predicted_width=%.15f' % predicted_width)
    print('width_errors=' + ','.join('%.6g'%e for e in errors))
    print('scaled_residuals=' + ','.join('%.6g'%e for e in scaled))

if __name__=='__main__':
    main()
