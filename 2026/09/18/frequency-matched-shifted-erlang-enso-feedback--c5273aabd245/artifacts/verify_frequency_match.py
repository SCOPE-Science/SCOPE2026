
import cmath
import math

def response(n, Delta, tau_m, omega):
    return cmath.exp(-1j*omega*tau_m) * (1+1j*omega*Delta)**(-n)

def hopf_frequency(n, Delta, loop_gain, tol=1e-14):
    # Solve w*(1+(w*Delta)^2)^(n/2)=loop_gain by bisection.
    lo, hi = 0.0, loop_gain
    for _ in range(200):
        mid=(lo+hi)/2
        val=mid*(1+(mid*Delta)**2)**(n/2)
        if val < loop_gain:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

n=3
omega_f=2*math.pi
for Delta in (1/15, 2/15):
    q=(1+(omega_f*Delta)**2)**(-n/2)
    alpha=1/q
    phase_extra=n*math.atan(omega_f*Delta)/omega_f
    mean_extra=n*Delta
    mismatch=mean_extra-phase_extra
    print(f"Delta={Delta:.12f}")
    print(f"  q={q:.12f}, alpha={alpha:.12f}")
    print(f"  source-scaled postfilter gain ratio q^2={q*q:.12f}")
    print(f"  corrected amplitude multiplier 1/q={alpha:.12f}")
    print(f"  mean-minus-phase delay={mismatch:.12f} yr = {365.25*mismatch:.6f} d")

a=1.0
kappa=11.0
for Delta in (0.0, 1/15, 2/15):
    w=hopf_frequency(n, Delta, a*kappa)
    q=(1+(w*Delta)**2)**(-n/2)
    print(f"Hopf Delta={Delta:.12f}: omega={w:.12f}, amplitude residual={abs(w-a*kappa*q):.3e}")
    for m in range(2):
        tau_m=(math.pi/2+2*math.pi*m-n*math.atan(w*Delta))/w
        tau_eff=tau_m+n*Delta
        G=response(n, Delta, tau_m, w)
        residual=abs(1j*w + a*kappa*G)
        print(f"  m={m}: tau_m={tau_m:.12f}, tau_eff={tau_eff:.12f}, characteristic residual={residual:.3e}")
