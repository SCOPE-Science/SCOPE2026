# Independent mathematical audit

## correctness

PASS

Resetting contracts differences of normalized states by e^(−rt) in trace norm, so the reset-age resolvent gives the unique stationary state. Site-projector dephasing gives Poisson position measurements at rate γ, not 2γ. The coherent interval kernel has characteristic function J₀(4ht sin(k/2)), so summing the measurement renewal series at reset Laplace rate r yields the stated normalized F. To check the split without a contour-sign convention, let W=(r+γ)²+8h²(1−cos k) and use 1/(√W+γ)=(1/π)∫₀^∞ √v/[(v+γ²)(v+W)] dv, which follows by setting v=x² and integrating partial fractions (with the equal-pole and γ=0 cases by limits). The coefficient of (W+v)⁻¹ is exp(−|m|y)/(8h² sinh y), where cosh y=cosh κ_b+v/(8h²). Its Jacobian cancels the sinh factor. Adding the simple pole from 2γ/(W−γ²) gives (1), including m=0, and the branch term is strictly positive. Expanding V=C_γ t+O(t²) gives the two fixed-rate branch exponents and constants. In the moving-rate window, V_γ(t)≥C_γ t gives the integrable rescaled majorant e^(−s)/√s. The branch limit is 1/√π−u e^(u²) erfc(u), while m(κ_b−κ)→u² and the scaled pole tends to 2u e^(u²), also at u=0. The Taylor coefficient of k² yields variance 4h²/[r(r+γ)]. Independent real-axis quadrature (`python3 review_checks/finite_checks.py 1`) compared 12 Fourier coefficients with the positive mixture (including m=0 and γ=0) with max error below 3×10⁻¹⁵ on the tested grid and checked three crossover points at m=10⁵; this corroborates but does not prove the limits.

## originality

PASS

The pass is for the positive-dephasing pole/continuum split, the change of spatial tail type and the joint weak-dephasing/large-distance crossover. The general reset resolvent, coherent Bessel kernel, and the exact single-site reset stationary law at γ=0 are prior. In particular Das–Dattagupta–Gupta give the full coherent stationary law as a Legendre Q function, not just its existence. No inspected same-model result supplies the positive-dephasing separation or its coalescence scale and profile.

## value

PASS

At every positive dephasing rate the exponential pole ultimately wins, but its residue vanishes as dephasing is removed. The model-derived C₀/γ² distance and the error-function profile quantify exactly when the coherent m^(−1/2) regime gives way to the pole contribution. This is a useful singular-limit benchmark for noise plus resetting and is not supplied by the coherent law, the variance, or a generic resolvent prescription.

The dated certificate retains the supplied scientific assessment, sources and limitations.
