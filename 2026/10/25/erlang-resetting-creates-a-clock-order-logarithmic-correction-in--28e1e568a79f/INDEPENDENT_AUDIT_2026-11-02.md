# Independent mathematical audit

## correctness

PASS

For x,D,r>0, v real and integer l≥2, solving D f″+v f′=r f with absorbing data at 0,m gives the stated F0 and Fm. The Erlang survival is exactly the finite sum of (-r)^j/j! derivatives of the exit Laplace transforms, so p_m and q_m are genuine mutually exclusive excursion probabilities, 0<p_m<p<1 and 0<q_m<q<1. IID renewal gives P(M<m,N=k)=p_m q_m^k, and p+q=1 ensures almost-sure finite N. Exact differences between the two-boundary and half-line transforms yield δp=T[C e^(-kappa m)/(1-e^(-kappa m))] and δq=T[C(e^(-alpha m)-e^(-kappa m))/(1-e^(-kappa m))]. The l−1 derivative dominates with alpha′=1/omega and kappa′=2/omega, yielding K and K0, while all subleading derivative terms are polynomially or exponentially smaller. Dividing the fixed-count joint tail by p q^k yields distinct k=0 vs k≥1 rates; summing all counts first gives the unconditional tail and tight size-biased geometric mass p² k q^(k−1). At m=(log k+(l−1)loglog k+log(K/[q alpha^(l−1)])+s)/alpha, k δq/q→e^(−s) and k(δq/q)²→0, proving the conditional Gumbel law for every real s. Independent stage-wise finite-difference boundary-value calculations at 12 configurations compared first-exit probabilities to exact transformed formulas with worst abs error 2.52e−6; 24 90-digit tail-ratio checks show convergence, 36 high-k CDF checks support Gumbel. Finite checks are corroborative only; no all-parameter conclusion is inferred from them.

## originality

PASS

The prior constant-rate stopped Brownian maximum results and count/splitting probability papers provide killed-hitting transforms and geometric restart identities but not the order-l≥2 joint barrier/count polynomial-times-exponential asymptotics. Fully read broad Gamma reset papers study FPT times or noninstantaneous return rather than the conditioned maximum; the 2026 Poisson fixed-window extremal analysis has a different horizon. The published 2026 count-conditioned splitting work is a close precursor but uses Poisson resets and does not visibly imply the Gamma polynomial factor. No matched published Resultary result or exact table surfaced. This is best-of-knowledge originality, not a guarantee that other derivations do not exist.

## value

PASS

The stopped spatial maximum (overshoot/overreach risk) and number of completed resets (restart budget) are jointly natural physical observables for search with non-memoryless Erlang clocks. The theorem supplies a single exact excursion kernel valid for every k and nontrivial separation between zero-reset and positive-reset barrier hazards, with explicit clock-shape dependent coefficients. It identifies how stage count l enters an order-(l−1) polynomial prefactor and thus a necessary (l−1) loglog k correction to conditional high-count extreme thresholds. These exact self-contained predictions are not a generic no-content normalization check, although renewal factorization and the Gumbel mechanism individually are classical. No claims beyond independent fresh clocks, fixed restart location, integer Erlang shape and one-dimensional drift diffusion are made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
