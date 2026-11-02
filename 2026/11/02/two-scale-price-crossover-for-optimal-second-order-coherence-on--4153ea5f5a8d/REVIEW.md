# Self-review: price-dependent second-order coherence on stars

## Correctness — PASS

For every integer \(m\ge3\), positive price vector, and positive budget, the centered leaf cut-vector representation of the weighted Laplacian gives exactly
\[
\operatorname{tr}((L^\dagger)^2)=\frac{m-1}{m+1}\sum_iw_i^{-2}+\frac{1}{(m+1)^2}\left(\sum_iw_i^{-1}\right)^2.
\]
The expression is strictly convex in the positive conductances; it diverges at each zero-conductance boundary of the bounded feasible region and decreases under common conductance increases. Its unique minimizer is interior and exhausts the budget. Exact Lagrange stationarity gives the price-compression inequalities. For one premium-priced edge, permutation uniqueness reduces the full problem to the one-positive-root cubic; substitutions prove the two different joint limits. The included verifier replays exact rational trace identities and numerical comparisons, but finite checks do not establish the universal quantifiers.

## Originality — PASS on inspected sources, with residual risk

Patterson–Bamieh (arXiv:1310.2592v1, Section II-B, Eq. (6)) already prove the inverse-square spectral objective for noisy second-order consensus; this objective is not claimed as new. Bamieh–Jovanović–Mitra–Patterson (arXiv:1112.4011v1) analyze dimension-dependent coherence, principally on lattices. Xiao–Boyd–Kim (MTNS 2006) optimize discrete-time first-order averaging and Hassan-Moghaddam–Jovanović (arXiv:1506.03437) formulate first-order sparse topology design. Their objectives do not, on the inspected material, entail the all-positive-price star optimizer or its separate \(m^{3/2}\) budget-share and \(m^6\) conductance-ratio scales. Semantically searched published mathematical records yielded related spectral-gap and leader-allocation problems with different objective matrices. Title/keyword mismatch was not treated as sufficient; exact implications and reductions were compared. Unlocated older specialist results or implicit instances of general design theorems are possible, so this is a qualified self-review priority assessment, not independent originality certification.

## Value — PASS

The inverse-square Laplacian trace is a standard stochastic double-integrator network-coherence objective; pricing actual star edges is a natural resource-constrained design problem. The exact global optimizer, strict cube-root-versus-square-root price compression and two noncoincident asymptotic scales supply concrete allocation and size-scaling rules beyond textbook square-root allocation for first-order network coherence. The two scales identify distinct economic and spectral effects, not isolated arbitrary parameter samples.

## Scope, evidence and remaining risks

The claim covers all positive prices and conductances under a single linear budget; it does not cover general graphs, edge capacities, negative couplings, alternative controllers or transient convergence. The exact rational and numerical verifier is executable with Python 3, NumPy, SciPy and SymPy. Relevant published PDF material and a publicly accessible result-record search were compared; specialist overlap remains possible. The claim is not externally certified.

Self-review: passed. Independent audit: not yet performed.
