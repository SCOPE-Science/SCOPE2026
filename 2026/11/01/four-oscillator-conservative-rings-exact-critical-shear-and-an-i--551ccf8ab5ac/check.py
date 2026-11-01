"""Independent finite diagnostics for the finite four-ring quadrature model.
The exact global theorem follows from the analytic reduction, not these tests.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp


def original_theta_rhs(theta, c, d):
    t=np.asarray(theta,float)
    yp=np.roll(t,-1)-t
    ym=t-np.roll(t,1)
    return c*(np.cos(yp)+np.cos(ym))+d*(np.sin(yp)+np.sin(ym))


def explicit_reduced(theta,c,d):
    y=np.roll(theta,-1)-theta
    a=y[0]+y[2]
    u=(y[0]-y[2])/2
    v=(y[1]-y[3])/2
    A=2*(c*np.sin(a/2)+d*np.cos(a/2))
    B=2*(c*np.sin(a/2)-d*np.cos(a/2))
    return a,u,v,A,B


def check():
    rng=np.random.default_rng(20261031)
    trials=0
    for j in range(2000):
        theta=rng.uniform(-7,7,4)
        c,d=rng.uniform(.1,4,2)
        thdot=original_theta_rhs(theta,c,d)
        ydot=np.roll(thdot,-1)-thdot
        a,u,v,A,B=explicit_reduced(theta,c,d)
        assert abs(ydot[0]+ydot[2])<2e-13
        assert abs(ydot[1]+ydot[3])<2e-13
        assert abs((ydot[0]-ydot[2])/2-A*np.sin(v))<2e-13
        assert abs((ydot[1]-ydot[3])/2-B*np.sin(u))<2e-13
        # Hamiltonian derivative must vanish identically.
        assert abs(-B*np.sin(u)*A*np.sin(v)+A*np.sin(v)*B*np.sin(u))<2e-13
        trials+=1
    # Direct original phase integration conserves first integrals.
    for c,d in [(1.0,1.0),(.5,2.0),(2.3,.7)]:
        for a,u,v in [(.3,.71,-.44),(1.1,.8,1.7),(2.7,.5,-.3),(4.3,-.4,1.5)]:
            y=np.array([a/2+u,-a/2+v,a/2-u,-a/2-v])
            theta=np.array([0.,y[0],y[0]+y[1],y[0]+y[1]+y[2]])
            a0,u0,v0,A,B=explicit_reduced(theta,c,d)
            H0=B*np.cos(u0)-A*np.cos(v0)
            sol=solve_ivp(lambda t,x:original_theta_rhs(x,c,d),(0,15),theta,
                         rtol=1e-10,atol=1e-11,dense_output=False,max_step=.02)
            assert sol.success
            worst_a=0.; worst_h=0.
            for col in sol.y.T[::10]:
                aa,uu,vv,AA,BB=explicit_reduced(col,c,d)
                worst_a=max(worst_a,abs(aa-a0))
                worst_h=max(worst_h,abs(BB*np.cos(uu)-AA*np.cos(vv)-H0))
            assert worst_a<1e-7,(worst_a,c,d,a)
            assert worst_h<1e-7,(worst_h,c,d,a)
    # Algebraic critical-fiber identities and square-root constant.
    for c,d in [(.4,2.1),(1.,1.),(3.2,.7)]:
        amin=2*math.atan(d/c)
        amax=2*math.pi-amin
        kap=4*c*d/math.hypot(c,d)
        for a in (amin,amax):
            A=2*(c*math.sin(a/2)+d*math.cos(a/2))
            B=2*(c*math.sin(a/2)-d*math.cos(a/2))
            assert min(abs(A),abs(B))<5e-15
            assert abs(max(abs(A),abs(B))-kap)<1e-13
        for ac in [amin,amax]:
            for e in [1e-4,1e-6,1e-8]:
                a=ac+e
                A=2*(c*math.sin(a/2)+d*math.cos(a/2))
                B=2*(c*math.sin(a/2)-d*math.cos(a/2))
                omega=math.sqrt(abs(A*B))
                # predicted omega ~= 2 sqrt(c d epsilon).
                assert abs(omega/(2*math.sqrt(c*d*e))-1)<.002
    # Exact tail identity via quadrature: critical v is Haar uniform.
    for z in [.1,.25,.4,.7,.95]:
        grid=(np.arange(300000)+.5)*2*math.pi/300000
        empirical=np.mean(np.abs(np.sin(grid))<z)
        expected=(2/math.pi)*math.asin(z)
        assert abs(empirical-expected)<1e-5, (empirical,expected)
    print('PASS: 2000 direct four-phase/reduced-vector comparisons; 12 trajectory first-integral checks; critical coefficients and sqrt-law checks; five Haar-tail tests.')

if __name__=='__main__': check()
