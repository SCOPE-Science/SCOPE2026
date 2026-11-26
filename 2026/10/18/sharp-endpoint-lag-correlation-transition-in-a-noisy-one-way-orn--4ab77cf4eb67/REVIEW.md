# Independent mathematical audit

## correctness

PASS

For A=-aI+gL the nilpotent shift gives finite-chain stability and entrywise impulse responses exp(-as)(gs)^k/k!. Itô isometry adds the independent site contributions to the sink variance (D/a)S_m(h). Only source noise enters the endpoint cross-covariance: its forward lag integral is proportional to exp(-at) times the integral of exp(-2as)(s+t)^m over s>=0, yielding E_m(2at); the reverse replaces (s+t)^m by s^m. Differentiating the normalized profile gives the falling-factorial equation, whose ratio decreases strictly from infinity to zero, including m=1. Expanding at lambda=2m+c gives 1-(c+2)/m+O(m^-2), uniformly for c in a compact interval about -2: for ell<=m^(1/3) the term remainder is bounded by O((1+ell)^4 2^-ell/m^2) and the other terms are geometrically small. Evaluating at c=-2±C/m brackets the optimizer. At the root Stirling yields a peak asymptotic sqrt(2/(pi m))*h^m/sqrt(S_m(h)), with a relative error independent of h. Below one the generating function gives S_m→(1-h^2)^-1/2; at one S_m=(2m+1) binom(2m,m)/4^m; above one, the tail ratios are dominated by C sqrt(k+1)h^-2k and converge to h^-2k, giving the geometric multiplier. In the exp(theta/m) window, the first epsilon*m indices contribute O(sqrt(epsilon)) to the rescaled sum, so the bulk Riemann integral gives the stated crossover. The checks log and a separate root/recurrence calculation are consistent with the proof, not substitutes for it.

## originality

PASS

Pass for the sharp normalized OU peak law as a whole, especially the distinct dependence on coupling across the three regimes. The underlying OU model and exact covariance ingredients are covered by Pal–Gupta; the frozen relationship paragraph understates this because the relevant primary PDF is now available. A separate indexed resetting model gives the same time kernel, optimizer root and lag asymptotic, not a distinct scalar optimizer here. Another indexed paper yields the same OU critical variance integral and hence, with the peak numerator, the crossover constant. Neither states or supplies the full three-regime OU normalized endpoint-peak amplitudes: the supercritical and subcritical stationary normalizations differ in order as well as in coefficient, and neither follows from rescaling the resetting correlation or from the mesoscopic critical-window statement. The pass does not assert priority for the model, covariance formulas, scalar pulse, or the crossover denominator in isolation.

## value

PASS

The result separates a persistent directional delay from observability: the peak moves linearly with depth, yet normalized signal strength has three different attenuation rates despite unchanged finite-chain drift stability. The exact crossover and distinctions between m^-3/4 and m^-1/4 depend on local independent noise accumulated along the chain; the known scalar pulse or a calculation of total variance alone does not communicate that quantitative distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
