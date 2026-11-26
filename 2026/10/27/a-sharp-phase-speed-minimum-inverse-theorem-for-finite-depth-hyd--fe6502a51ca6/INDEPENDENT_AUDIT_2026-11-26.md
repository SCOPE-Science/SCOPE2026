# Independent mathematical audit

## correctness

PASS

With p=T/(ρgh²), q=D/(ρgh⁴) and x=kh, the squared speed is f=(1/x+px+qx³)tanh x. Dividing its derivative by (x tanh x)' gives p+qG−A, with G=x²(3S+1)/(S+1) and A=(S−1)/(x²(S+1)). G increases from zero to infinity because S is strictly increasing. For A the derivative test reduces to S²−1>xS'. Setting t=2x gives (cosh(2t)−1)/(2t²)+sinh(t)/t−cosh(t)−1, whose constant and quadratic coefficients vanish and whose higher coefficients are (2^(2n+1)−4n(n+1))/(2n+2)!>0 for n≥2 (the exponential term grows by four, the quadratic term by less). Thus A decreases strictly from 1/3 to zero. The derivative has a unique negative-to-positive sign change exactly for 0<p<1/3; at equality p=1/3 it is positive for x>0, with only a long-wave infimum. The measured value and stationarity form a system in px²,qx⁴ with determinant 2S/(S+1)>0. Solving gives the displayed T,D; each open interval endpoint corresponds to vanishing of one modulus and the width is positive since S>1. Conversely a pair strictly inside gives positive moduli and satisfies stationarity, hence gives the unique global minimum. The Taylor coefficients A=1/3−2x²/45+O(x⁴) and G=2x²+O(x⁴) give the stated critical law; differentiating the strictly increasing stationarity factor gives both minimizer monotonicities. checker.py and VERIFICATION.md describe diagnostic sampled tests, not the proof of uniqueness or a new audit run.

## originality

PASS

The exact two-modulus inversion from a single minimum, with an open data interval and a converse global-minimum test, was not found implied by the closest inspected results. The combined-moduli dispersion, the capillary 1/3 threshold in the zero-bending case, and finite-depth pure-flexural minima are antecedents, not claimed novelties. This is a bounded comparison with a material full-text access limitation.

## value

PASS

The minimum is a physically meaningful feature beyond a generic sample of the curve. The interval is an exact data consistency test, and the no-hidden-extrema result makes the small linear inverse system globally meaningful. The conclusion is useful under the specified massless-sheet model and known g, ρ and h; it does not give stability under noisy minimum measurements or infer omitted effects.

The dated certificate retains the supplied scientific assessment, sources and limitations.
