# Assessment of critical exclusion for the planar Ricker map

## Correctness
**PASS.** All parameter inequalities are explicitly checked against the global-attraction theorem of Baigent et al. (2023), Theorem 3.6 R3. In the exact transformed recurrence, the transverse multiplier \(1-r\) has modulus strictly below one and the neutral population satisfies \(y_{n+1}/y_n\to1\). The proved stable-filter lemma then supplies \(q_n=-\alpha(1-\alpha\beta)y_n^2/r+O(y_n^3)\) without assuming an unproved rate. Reciprocal expansion yields a summably accurate logarithmic law, so the finite orbit-dependent constant exists. A standalone standard-library checker independently tests exact rational coefficients and four trajectories, including both signs and zero of the logarithmic coefficient. Simulations are confirmatory, not an infinite proof.

## Originality
**PASS subject to explicit priority risk.** The 2023 primary source proves convergence and describes invariant manifolds; it does not specify the asymptotic logarithmic coefficient, finite affine correction, or its cancellation locus. Luís–Elaydi–Oliveira (2011) treat the very same map and center manifolds, but their full PDF was not accessible, so a possibly implicit earlier calculation cannot be excluded. Kulakov–Neverova–Frisman (2022) analyze bifurcation modes, not a reciprocal critical-rate law in the consulted sections. Related logarithmic-relaxation records concern different dynamical systems and do not entail this Ricker law. Published-result searches are useful overlap checks but cannot prove uniqueness.

## Mathematical value
**PASS.** At the invasion-neutral boundary, the missing quantitative invariant is not whether the second species disappears, but *how fast* it does so. The leading \(1/n\) law, signed logarithmic correction, and exact cancellation hypersurface supply a parameter-sensitive sharp physical-time extinction profile for all positive initial conditions in a nontrivial global regime, improving mere asymptotic convergence without requiring a new general center-manifold theorem. The cancellation is a natural dynamical transition because it separates opposite directions of unbounded reciprocal drift.

## Nearest literature and limits
Baigent et al., *Journal of Difference Equations and Applications* 29 (2023), 575–591, Theorem 3.6 R3, https://doi.org/10.1080/10236198.2023.2222855; Luís et al., *Journal of Biological Dynamics* 5 (2011), 636–660, https://doi.org/10.1080/17513758.2011.581764; Kulakov et al., *Mathematics* 10 (2022), 1076, https://doi.org/10.3390/math10071076. No uniform-in-parameter or off-threshold assertion is made; the finite offset has no claimed elementary form. The 2011 full-text access gap is unresolved, and no independent audit was conducted.

Self-review: passed. Independent audit: not yet performed.
