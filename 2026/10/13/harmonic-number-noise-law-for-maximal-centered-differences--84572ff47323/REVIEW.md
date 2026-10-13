# Self-review

## Correctness
PASS. The proof reconstructs the centered weights from Lagrange interpolation, evaluates their complete absolute sum for every \(m\ge1\) by an exact beta-integral identity, and obtains the operator norm by finite-dimensional \(\ell_\infty\)-duality. A sign-matched perturbation proves sharpness. The exact-rational replay is supplementary rather than an extrapolation from finite cases.

## Originality
PASS, with residual risk. Full-text inspection of Fornberg's weight-generation paper and Sadiq–Viswanath's weight/superconvergence paper found the standard coefficient framework and numerical-stability discussions but not the exact harmonic-number data-perturbation norm. Published-finding-index searches using coefficient-norm, harmonic-number, condition-number, and noise-amplification aliases found no implication-equivalent statement. The main risk is older numerical-differentiation conditioning literature using different terminology.

## Value
PASS. The result evaluates a natural robustness invariant of a canonical high-order differentiation family. It gives a sharp worst-case error budget and a simple all-order law showing precisely how formal-order growth trades against bounded sample perturbations.

## Closest literature and limitations
Fornberg (1988) supplies general finite-difference weight recursions and centered equispaced tables. Sadiq and Viswanath analyze finite-difference weight computation, spectral differentiation, and superconvergence. Neither inspected source states the claimed \(H_m/h\) sample-noise norm. The finding is restricted to centered equispaced first-derivative formulas and deterministic componentwise perturbations; stochastic RMS behavior, weight-generation roundoff, nonuniform grids, boundaries, and higher derivatives are outside scope.

Self-review: passed. Independent audit: not yet performed.
