"""Independent stationary-generator and beta-mixture checks for a two-state harmonic Langevin model."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import betaln, betaincc

def verify(a,b,u,w,D):
    alpha=u/(2*a); beta=w/(2*b); theta=beta-alpha
    assert theta>2.01
    pi=np.array([w/(u+w),u/(u+w)])
    L=D/a+D/b
    def bp_pdf(y,shape):
        return math.exp((shape-1)*math.log(y)+(theta-1)*math.log1p(-y)-betaln(shape,theta))
    moments=[pi]
    for k in range(1,3):
        vals=[]
        for j,shape in enumerate((alpha,alpha+1)):
            v_beta=quad(lambda y: ((D/a+D/b*y)/(1-y))**k*bp_pdf(y,shape),0,1,epsabs=1e-9)[0]
            vals.append(pi[j]*v_beta * math.prod(range(1,2*k,2)))
        M=np.array([[2*k*a+u,-w],[-u,w-2*k*b]])
        rhs=(2*k)*(2*k-1)*D*moments[-1]
        sol=np.linalg.solve(M,rhs)
        assert np.allclose(sol,vals,rtol=2e-8,atol=2e-8),(a,b,u,w,D,k,sol,vals)
        moments.append(sol)
    # Exact beta survival asymptotic and universal state-bias checks at large variance.
    lv=D/a+D/b
    ctail=lv**theta/theta*(pi[0]/math.exp(betaln(alpha,theta))+pi[1]/math.exp(betaln(alpha+1,theta)))
    for v0 in [1e4*max(D/a,D/b), 1e6*max(D/a,D/b)]:
        y0=(v0-D/a)/(v0+D/b)
        tails=np.array([pi[0]*betaincc(alpha,theta,y0),pi[1]*betaincc(alpha+1,theta,y0)])
        assert abs(tails.sum()*v0**theta/ctail-1)<.005
        assert abs(tails[1]/tails.sum()-a/(a+b))<.005
    # Marginal PDMP continuity and switching balance checked against analytic derivatives
    for y in np.linspace(.015,.985,29):
        v=(D/a+(D/b)*y)/(1-y)
        f_plus=2*(D-a*v); f_minus=2*(D+b*v)
        dy_dv=(L)/(v+D/b)**2
        pplus=pi[0]*bp_pdf(y,alpha)*dy_dv
        pminus=pi[1]*bp_pdf(y,alpha+1)*dy_dv
        assert abs(f_plus*pplus+f_minus*pminus)<5e-12
    return [float(sum(moments[k])) for k in (1,2)]

cases=[]
for a in [1.5,2.0,3.0]:
    for b in [.3,.6,1.0]:
        for u in [.6,1.4]:
            for D in [.7,2.0]:
                w=b*(u/a+5.0) # θ=2.5
                cases.append(verify(a,b,u,w,D))
print('PASS: 36 parameter sets, 72 generator/beta moment comparisons, 144 tail/bias comparisons and 1044 zero-flux checks')
print('representative E[X^2], E[X^4]:', cases[0])
