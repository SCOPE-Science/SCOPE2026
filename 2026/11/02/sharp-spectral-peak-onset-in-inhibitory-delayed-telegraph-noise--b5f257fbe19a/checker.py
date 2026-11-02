"""Numerical cross-checks for an inhibitory delayed two-state signal.

Requires NumPy and SciPy. Numerical experiments are not proofs of the
spectral global maximization theorem.
"""
import math
import numpy as np
from scipy.integrate import simpson
from scipy.optimize import minimize_scalar


def critical_delay(c, h):
    return 1.0 / (h + math.sqrt(h * (c + h)))


def denominator(w, c, h, T):
    return (c + h * math.cos(w * T)) ** 2 + (w - h * math.sin(w * T)) ** 2


def cov_delay(c, h, T):
    eta = math.sqrt(c * c - h * h)
    return (eta - h * math.sinh(eta * T)) / (eta * math.cosh(eta * T) + c * math.sinh(eta * T))


def spectral(w, c, h, T):
    A = 2 * (c + h * cov_delay(c, h, T))
    return A / denominator(w, c, h, T)


def best_frequency(c, h, T):
    # Scan multiple wells, including sidelobes, then refine each bracket.
    wmax = max(18.0, 20.0 / T, 10 * (c + h))
    grid = np.linspace(0.0, wmax, 18001)
    f = np.array([denominator(float(w), c, h, T) for w in grid])
    candidates = [(0.0, float(f[0]))]
    indices = [i for i in range(1, len(grid)-1) if f[i] < f[i-1] and f[i] < f[i+1]]
    for i in indices:
        res = minimize_scalar(lambda w: denominator(w, c, h, T),
                              bounds=(grid[i-1], grid[i+1]), method="bounded",
                              options={"xatol": 1e-14})
        candidates.append((float(res.x), float(res.fun)))
    return min(candidates, key=lambda a: a[1])


def run():
    count = 0
    for c,h in [(2.0,0.2),(2.0,1.0),(1.0,0.8)]:
        Tc = critical_delay(c,h)
        assert abs(1-2*h*Tc-c*h*Tc*Tc) < 2e-14
        count += 1
        for ratio in [0.4, 0.95, 1.0, 1.05, 1.5, 3.0]:
            T=ratio*Tc
            # Locate global minimum of the full spectral denominator.
            w, fmin = best_frequency(c,h,T)
            atzero = denominator(0.0,c,h,T)
            if ratio <= 1.0:
                assert fmin >= atzero-2e-9, (c,h,ratio,w,fmin,atzero)
                assert w < 0.001, (c,h,ratio,w)
            else:
                assert w > 1e-3 and fmin < atzero-1e-7, (c,h,ratio,w,fmin,atzero)
            count += 1
            # Independent Fourier-variance check.
            cutoff = 3000.0
            grid_int = np.linspace(0.0, cutoff, 600001)
            amplitude = 2 * (c + h * cov_delay(c,h,T))
            f_int = (c + h * np.cos(grid_int*T))**2 + (grid_int - h*np.sin(grid_int*T))**2
            integral = simpson(amplitude / f_int, x=grid_int) + amplitude / cutoff
            assert abs(integral/math.pi - 1.0) < 3e-6, (c,h,ratio,integral)
            count += 1
        # At onset, check the spectral minimizer's predicted square-root slope.
        K=12*(1+c*Tc)/(Tc**3*(4+c*Tc))
        for dt in [1e-2,1e-3,1e-4]:
            w, _=best_frequency(c,h,Tc+dt)
            assert 0.87 < w/math.sqrt(K*dt) < 1.04, (c,h,dt,w,math.sqrt(K*dt))
            count += 1
    print(f"PASS: {count} independent parameter and spectral checks")


if __name__ == "__main__":
    run()
