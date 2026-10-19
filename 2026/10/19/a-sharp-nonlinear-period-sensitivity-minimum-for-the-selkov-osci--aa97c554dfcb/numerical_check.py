"""Optional numerical corroboration of local period coefficients.

Requires NumPy and SciPy; finite-offset quadrature is not a proof of the limit.
"""
import numpy as np
from scipy.integrate import solve_ivp
for gamma, delta in [(1.5, .02), (2., .02), (2., .01), (3., .02), (3., .01)]:
    k = np.sqrt(gamma-1)
    alpha = k**(-2)+delta
    def rhs(t,z):
        x,y = z
        flux = x*y**gamma
        return [1-flux,alpha*(flux-y)]
    def crossing(t,z):
        return z[0]-1
    crossing.direction = 1
    sol = solve_ivp(rhs,(0,3000 if gamma==2 else 2000),[1.2,1.],
                    rtol=2e-9,atol=2e-11,events=crossing,
                    dense_output=True,max_step=2.)
    assert sol.success
    crossings = sol.t_events[0]
    crossings = crossings[crossings>1000]
    assert len(crossings)>2
    period = crossings[-1]-crossings[-2]
    times = np.linspace(crossings[-2],crossings[-1],4097)
    x = sol.sol(times)[0]
    harmonic = np.exp(-2j*np.pi*(times-crossings[-2])/period)
    amplitude = 2*abs(np.trapezoid((x-1)*harmonic,times)/period)
    wlin = np.sqrt(alpha-((gamma-1)*delta)**2/4)
    measured = (period*wlin/(2*np.pi)-1)/amplitude**2
    limit = (2*k**4+k**2+2)/(48*k**2)
    print('gamma=%.1f delta=%.2f measured=%.8f predicted=%.8f' %
          (gamma,delta,measured,limit))
