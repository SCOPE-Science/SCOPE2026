# Scientific review

**Correctness (PASS).** The spectral radius follows from the positive Perron vector of the connected bipartite signless Laplacian. The exact two-color dynamics supplies the branch. Both period-two derivatives equal \(I-h\cos\delta L\), and the upper boundary has identity Jacobian. The reversed quadratic corrections compose to \(-\nabla W\), with \(W=\|Q\|^2/2\) positive definite on the mean-zero quotient by edge-weight positivity and connectivity; this gives two-sided quartic distance decrease and sharp \(\Theta(k^{-1/2})\) local convergence. A scalar expansion proves the nonzero \(\pi^{-2}\) leading squared-error coefficient. The packaged checker independently exercises finite instances only.

**Originality (PASS).** Buescu, D'Aniello, and Oliveira (arXiv:2610.10993v1) establish the underlying graph model and descent range \(h<2/\Lambda\). Buescu and Oliveira (arXiv:2610.19953v1) treat stationary twists and small-step almost-global behavior. A previously recorded symmetric-star calculation supplies the elementary two-color existence/hyperbolic window but leaves the upper all-unit-multiplier boundary unanalyzed. The distinguishing claim here is the positive-definite quartic return, rigorous nonlinear attraction at this fully parabolic endpoint, and sharp rate for every connected weighted-biregular bipartite graph. Equivalent and broader-coverage comparisons are in `AUDIT.json`.

**Mathematical value (PASS).** Exact nonlinear stability on a graph's fully neutral Floquet boundary is a substantive missing phase in the family, not just an extra small-parameter estimate. The quartic-gradient mechanism applies beyond rings and stars, giving a natural structural criterion and a sharp universal relaxation exponent.

**Limitations and risks.** Other periodic orbits and global basins are not classified. Arbitrary perturbations destroying biregularity may destroy the two-color branch. Some historical parabolic-gradient theorem may potentially imply the normal form; an independent priority check remains outstanding.

Self-review: passed. Independent audit: not yet performed.
