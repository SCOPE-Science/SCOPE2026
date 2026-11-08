# Independent mathematical audit

## correctness

PASS

For dX=Vdt, dV=-gamma Vdt+sqrt(2Dv)dB, independent Poisson full position reset with velocity redrawn N(0,epsilon²), renewal gives stationary p_epsilon(x)=r∫exp(-rt) N(0,W_epsilon(t))(x)dt, W=epsilon²h(t)²+2Dv∫h² and h=(1-exp(-gamma t))/gamma. W=epsilon² t²+c t³+O(epsilon²t³+t4), c=2Dv/3; t=epsilon²u/c and x=epsilon³y/c yield the universal profile (2pi)^(-1/2)∫exp[-y²/(2u²(1+u))]/[u sqrt(1+u)]du. On compact y away from 0, short-time variance comparison provides an integrable small-u exponential and u^(-3/2) tail, with older ages contributing O(epsilon); dominated convergence proves locally uniform limit. As y->0, exponential-integral asymptotics plus ∫delta^infty (u sqrt(1+u))^(-1)du=log(4/delta)+o(1) give log4+(log2-gamma_E)/2. Substitution u=|y|^(2/3)v yields |y|^(-1/3) gamma constant 2^(1/6) Gamma(1/6)/(3sqrt(2pi)); fixed epsilon>0 gives r/(epsilon sqrt(2pi)) logarithmic origin singularity and epsilon=0 gives r c^(-1/3) times the same power-law constant. All bounds require r,gamma,Dv>0 and fixed physical parameters; no claim at y=0.

## originality

PASS

The established 2026 Franke–Sokolov article proves endpoint logarithmic and inverse-cubic stationary singularities for two resetting rules in essentially the same inertial process. The inspected new claim is the small independently redrawable Gaussian velocity variance crossover, its universal integral, precise epsilon³/c spatial scale and matching constants. The full closest article compares the two endpoint protocols and time-dependent kurtosis; it does not present the inspected singular perturbation regime. Singh and Gupta examine related but different reset mechanisms. Historical priority for general Gaussian-mixture crossover theorems remains provisional.

## value

PASS

The two qualitatively different singular stationary densities are established for physically important velocity resetting protocols; the small-variance limit is a natural stability/singular-perturbation question. A nontrivial parameter-free crossover on the epsilon³ spatial scale with both exact asymptotic constants quantifies the noncommuting limits and is a meaningful sharp classification, not merely recomputation of known endpoint exponents.

The dated certificate retains the supplied scientific assessment, sources and limitations.
