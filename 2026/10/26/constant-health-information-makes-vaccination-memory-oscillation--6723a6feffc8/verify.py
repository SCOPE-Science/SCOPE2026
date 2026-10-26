"""Reproduce the campaign-prevalence identities in a vaccination-memory SIR model.

Requires Python 3 with numpy, scipy and sympy. The periodic-looking
trajectory is used only as a numerical diagnostic, not a proof of an orbit.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks
from sympy import symbols, factor

mu, delta, alpha, eta, q, x, r, y = symbols('mu delta alpha eta q x r y', nonzero=True)
# The equilibrium identity lets us eliminate q.
q_from_equilibrium = ((mu + delta*alpha)*r**2 - delta*eta)/(mu*r)
# The first-moment identity gives I = (mu/delta)(q-x),
# and logit balance gives I = alpha*x-eta*y.
# Here y is E[1/p], and V=y-1/x.
V = y - 1/x
moment_residual = (mu/delta)*(q_from_equilibrium-x)-alpha*x+eta*y
claimed_residual = -((alpha+mu/delta+eta/(r*x))*(x-r)-eta*V)
assert factor(moment_residual-claimed_residual)==0
print('symbolic elimination: PASS')

# Independent numerical integration of the normalized Erlang-2 memory kernel.
mu=1/(70*365); nu=1/7; delta=mu+nu
beta=10*delta; alpha=.002; eta=1e-6; k=400; sigma=2/150
q=1-delta/beta
A=alpha+mu/delta; B=mu*q/delta
r=(B+np.sqrt(B*B+4*A*eta))/(2*A)
Istar=(mu/delta)*(q-r); Sstar=delta/beta

def rhs(t,state):
    S,I,p,m1,m2=state
    return [mu*(1-p)-beta*S*I-mu*S,
            I*(beta*S-delta),
            k*(1-p)*(p*(I-alpha*m2)+eta),
            sigma*(p-m1), sigma*(m1-m2)]
initial=[1.01*Sstar,1.02*Istar,.98*r,r,r]
sol=solve_ivp(rhs, (0,55000),initial,method='DOP853',rtol=5e-9,atol=1e-12,dense_output=True)
assert sol.success
rough_t=np.linspace(35000,55000,50001)
rough_p=sol.sol(rough_t)[2]
peaks,_=find_peaks(rough_p,distance=350)
assert len(peaks)>=10, len(peaks)
start,end=rough_t[peaks[-11]],rough_t[peaks[-1]]
t=np.linspace(start,end,100001)
S,I,p,m1,m2=sol.sol(t)
assert np.min(p)>0 and np.max(p)<1 and np.min(I)>0
span=t[-1]-t[0]
avg=lambda y: np.trapezoid(y,t)/span
x=avg(p); im=avg(I); V=avg(1/p)-1/x
V2=avg((p-x)**2/p)/x**2
assert np.isclose(V,V2,rtol=1e-8,atol=1e-10)
pred=(mu/delta)*eta*V/(alpha+mu/delta+eta/(r*x))
observed=Istar-im
assert observed>0 and pred>0 and abs(observed-pred)/pred<2e-4, (observed,pred)
assert abs(avg(S)-Sstar)<1e-6
assert abs(avg(S*I)-avg(S)*avg(I))<1e-7
print('numerical Erlang-2 diagnostic: PASS')
print(f'period_window=[{start:.2f},{end:.2f}], mean_p={x:.12g}, mean_I={im:.12g}')
print(f'equilibrium_I={Istar:.12g}, observed_discount={observed:.12g}, predicted_discount={pred:.12g}, relative_error={(observed-pred)/pred:.3g}')
print('No computational claim of rigorous periodic orbit existence.')
