# Independent mathematical audit

## correctness

PASS

The critical Poisson(1) total progeny generating function obeys F(z)=z exp(F(z)-1). Lagrange inversion gives the exact Borel law P(N=n)=e^(-n)n^(n-1)/n!, whose Stirling expansion is comparable to n^(-3/2). The finite-variance conditioned Galton–Watson height-limit theorem implies a uniform positive probability of height >= a sqrt(n) for all sufficiently large n, and diameter d>=height. On any diameter path v_0,...,v_d, taking test function f(v_i)=i and extending constantly on attached branches has energy exactly d and variance at least d(d+1)(d+2)/12, hence lambda_2(Delta_T)<=12/((d+1)(d+2))<=12/d^2. Independently checked this exact Rayleigh certificate on all 94 unlabeled trees of orders 2 through 9. On the long-height event with n>=12/(a^2 E), there is at least one positive eigenvalue <=E, contributing >=1/n to the normalized trace. Thus E[spectral weight] >= p_0 sum_{n>=K/E}P(N=n)/n >= c E^(3/2). The power lower bound excludes an exp(-c_0 E^(-1/2)) upper tail for every positive c_0. This is a full all-E analytic proof, not an extrapolation from small trees; no exact asymptotic or matching upper bound is proved.

## originality

PASS

Best-of-knowledge new critical-parameter polynomial lower bound for the annealed normalized combinatorial-Laplacian spectral measure of critical Poisson(1) Galton–Watson trees. The closest full-text 2026 primary theorem treats strictly supercritical mean and explicitly says the critical case is not studied. The 2006 Lifshitz-tail theorem treats strictly subcritical mean. Kersting supplies the conditioned-tree height input, not the spectral-measure consequence. Potential implicit estimates in older conditioned-tree spectral literature are a residual priority risk; no exhaustive novelty guarantee is made.

## value

PASS

The critical mean 1 is a mathematically distinguished phase boundary separating the previously proved strictly subcritical and supercritical Lifshitz regimes. The explicit c E^(3/2) lower bound forces positive low-energy spectral weight far above exp(-c E^(-1/2)), ruling out an otherwise plausible critical extension of those theorems for precisely defined normalised-trace annealed tree-law measure. This is a motivated qualitative boundary obstruction, not a routine type check or a claim to the exact spectral exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
