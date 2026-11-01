# Scientific review: local stability of heterogeneous two-patch states

## Correctness — PASS
The migration equations reduce exactly to the displayed mean/contrast/chemical system. The strictly monotone equilibrium parameter \(X(t)\) supplies the negative fixed-sensitivity branch derivative \(G_t\). The full four-dimensional Jacobian contains an independent eigenvalue \(-\beta\). The remaining cubic satisfies each strict Routh–Hurwitz inequality because \(0<q<e\), \(D=ae+bd-aq>0\), and \(AB-C_0>0\). The symbolic checker verifies the nonobvious exact determinant identity and 164 parameter combinations corroborate the matrix sign calculation. The proof excludes the coalescing threshold and makes no global-attraction assertion.

## Originality — PASS under inspected evidence
The direct 2026 primary model and an earlier two-patch equilibrium enumeration account for the branch's existence, uniqueness, monotonicity and large-bias limits, not its spectrum along the entire branch. The present assertion requires a new, all-rate strict cubic Hurwitz certificate; a fold-free continuation alone cannot eliminate Hopf bifurcations. The nearest accessible metric-graph PDE results concern different edge-transport equations, and related research database searches returned no equivalent all-parameter spectral result. Unindexed or inaccessible specialized results remain a risk, so historical priority is provisional.

## Value — PASS
Numerical pattern emergence and a monotone equilibrium branch do not determine the fate of spatial patterns under further strengthening of taxis. This result rules out every secondary *local* destabilization of those patterns for arbitrary positive biochemical and population parameters, including the parameter region in which a key cross-derivative changes sign. It therefore completes a physically motivated local stability diagram rather than adding a routine special parameter evaluation. It is not a global dynamics theorem or an extension to general metapopulation graphs.

Self-review: passed. Independent audit: not yet performed.
