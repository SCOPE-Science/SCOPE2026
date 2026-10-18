"""Exact arithmetic and numerical spot checks for critical reward-boundary asymptotics.
Requires Python 3.10+, scipy. This numerical checker supplements the analytical proof.
"""
from fractions import Fraction as Q
from math import isfinite, log
from scipy.integrate import solve_ivp

G0, GP, GPP = Q(7,4), Q(-2), Q(2)
ALPHA, BETA = Q(1,2), Q(2)
L= BETA-ALPHA
COUNT=0

def ck(cond, what):
    global COUNT
    assert cond, what
    COUNT +=1

for side, delta, expected_q, expected_q1, expected_A, expected_B in (
    (1,Q(8,21),ALPHA,Q(4,7),Q(21,4),Q(160,3)),
    (-1,Q(2,21),BETA,Q(16,7),Q(21,16),Q(643,48)),
):
    q0=Q(1,3)/(delta*G0)
    q1=q0*(-GP/G0)
    q2=q0*(2*(GP/G0)**2-GPP/G0)
    F0=delta*Q(1,4)*G0
    c0=2*L
    A=c0/q1
    B=c0/(F0*q1*q1)-side*q2/(2*q1*q1)-Q(1,1)/L
    for got,expected in ((q0,expected_q),(q1,expected_q1),(A,expected_A),(B,expected_B)):
        ck(got==expected,('symbolic',side,got,expected))
    ck(F0*q1==Q(2,21),('fast eigenvalue',side))
    ck(q1>0 and F0>0 and A>0,('positivity',side))
    ck(q2>0,('curvature',side))
    k=1/q1
    ell=c0/(F0*q1**3)-side*q2/(2*q1**3)
    ck(c0*ell-2*k==A*B,('second-order drift',side))
    # An exact identity for the Lyapunov derivative at rational test states.
    for xx in (Q(1,5),Q(2,5),Q(3,5),Q(4,5)):
        gg=1+(1-xx)+(1-xx)**2
        ff=delta*xx*(1-xx)*gg
        qq=Q(1,3)/(delta*gg)
        for aa in (Q(3,5),Q(4,5),Q(6,5),Q(9,5)):
            xp=ff*(aa-qq)
            ap=(aa-ALPHA)*(BETA-aa)*(1-2*xx)
            vd=(xx-Q(1,2))/ff*xp+(aa-q0)/(2*(aa-ALPHA)*(BETA-aa))*ap
            ck(vd==-(xx-Q(1,2))*(qq-q0),('Lyapunov identity',side,xx,aa))
    def rhs(t,state):
        x,a=state
        g=1+(1-x)+(1-x)**2
        return [x*(1-x)*(-1/3+float(delta)*a*g),
                (a-float(ALPHA))*(float(BETA)-a)*(1-2*x)]
    xstart=0.5
    ystart=0.6 if side==1 else 1.8
    sol=solve_ivp(rhs,(0,10000),[xstart,ystart],rtol=3e-12,atol=1e-14,method='LSODA',dense_output=True)
    ck(sol.success,('solver',side,sol.message))
    residuals = {}
    for t in (1000,3000,10000):
        x,a=sol.sol(t)
        y=(a-float(ALPHA)) if side==1 else (float(BETA)-a)
        z=side*(x-0.5)
        ck(y>0 and z>0 and isfinite(y) and isfinite(z),('sign',side,t,y,z))
        ck(abs(t*y-float(1/A))<0.25,('leading reward',side,t,t*y,float(1/A)))
        ck(abs(t*z-float(Q(1,3)))<0.05,('leading cooperation',side,t,t*z))
        ck(abs(z/y-float(Q(1,1)/q1))<0.05,('slow tracking',side,t,z/y,float(1/q1)))
        residuals[t] = 1/y-float(A)*t
    log_slope=(residuals[10000]-residuals[3000])/log(10000/3000)
    ck(abs(log_slope-float(B))<3,('logarithmic coefficient',side,log_slope,float(B)))
    print('critical side',side,'root',q0,'leading inverse reward',A,'log coefficient',B,
          'last trajectory',sol.y[:,-1],'last time',sol.t[-1], 'function_evals',sol.nfev)
print(f'{COUNT} checks passed')
