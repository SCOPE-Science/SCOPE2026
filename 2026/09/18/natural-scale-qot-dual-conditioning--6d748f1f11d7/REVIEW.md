# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The central estimate is reduced to a positive-slack core with row and column degrees comparable to \(\ell^d\) and overlap of nearby sections comparable to \(\ell^d\). Those properties follow from the inner positive-slack balls and the nearby-row overlap argument proved in arXiv:2609.20400. Conditioning on one endpoint converts the signless bipartite quadratic form into a within-section variance; the overlap cancellation leaves a finite-range difference energy, and the standard convex-domain nonlocal Poincare estimate contributes exactly \(\ell^{d+2}=\varepsilon\). The remaining mean component is controlled by the normalized edge measure, whose marginal densities are uniformly bounded. This gives the claimed \(c\varepsilon\) core coercivity.

The local strong-concavity statement does not assume Hessian continuity. Along any segment in the stated \(L^\infty\) ball, the one-dimensional second derivative of the negative dual exists almost everywhere and is the active-set quadratic form already used in arXiv:2605.27175. The fixed positive-slack core remains active throughout the segment, so integration yields strong concavity. Uniform convexity of the transformed optimal potentials confines all slightly enlarged active sections to radius \(O(\ell)\), giving the \(O(\ell^{-2})\) local smoothness bound. The PL and quadratic-growth inequalities are standard consequences of strong concavity.

The extremal Hessian scales are independently checked in both directions: the constant direct-sum direction forces an \(\Omega(\ell^{-2})\) top eigenvalue, while a Brenier-graph anti-mode has Rayleigh quotient \(O(1)\), matching the core lower bound on the bottom eigenvalue. The exact periodic Fourier model gives the compatible limits \(\lambda_{\min}\to1/2\) and \(\lambda_{\max}r^2\to6\).

## Originality

**PASS, to the best of our knowledge.** Three closely related primary sources were inspected in detail. arXiv:2509.08547 proves strict positive definiteness of the linearized curvature for each fixed regularization parameter and explicitly says that a rigorous quadratic-growth statement in an \(L^\infty\) neighborhood is future work. arXiv:2605.27175 proves a general PL inequality, but its explicit localization and constants use the smaller \(O(\varepsilon)\) scale and do not yield an epsilon-uniform modulus in the smooth quadratic-cost regime. arXiv:2609.20400 proves the sharp support and potential geometry and explicitly notes that the results can upgrade the PL and algorithmic analysis, but its accessible Part I does not state the core-coercivity estimate, the epsilon-uniform strong-concavity theorem, or the sharp dual-Hessian condition number proved here.

Searches for combinations of quadratically regularized optimal transport with uniform/local strong concavity, Hessian conditioning, and epsilon-dependent PL constants did not locate an inspected source containing these statements. Older QOT work develops duality and numerical methods but does not supply the present small-regularization spectral scaling.

The main residual originality risk is unusually concrete: arXiv:2609.20400 is very recent and explicitly flags PL/algorithmic upgrades as a consequence of its geometry. Its bibliography also lists González-Sanz--Nutz, *Geometry and Convergence of Quadratically Regularized Optimal Transport II*, as a 2026 working paper, with no public identifier or accessible text found in the literature search. Because Part I describes that companion as developing further consequences of the same geometry, it is the inaccessible source most likely to overlap this result. No accessible statement inspected here establishes such coverage. Accordingly the claim is limited to “to the best of our knowledge.”

## Value

**PASS.** The result identifies the correct optimization scale behind the new support geometry. Under smooth marginals, the previously certified PL curvature can be replaced by an epsilon-independent constant on a neighborhood that is parametrically larger, \(O(\varepsilon^{2/(d+2)})\) instead of \(O(\varepsilon)\). It also separates two effects of weak regularization: the smallest local curvature does not vanish, while the largest grows like the inverse squared support thickness. The resulting condition number \(\Theta(\varepsilon^{-2/(d+2)})\) gives a concrete local step-size and stiffness law for first-order and second-order algorithm design.

## Scope and limitations

The theorem requires the smooth uniformly convex continuous setting of arXiv:2609.20400. It does not supersede the weaker-assumption PL theorem for semi-discrete or rough marginals. The certified basin is an \(L^\infty\) direct-sum neighborhood; no basin-entry theorem is claimed. The local spectral step-size statement is not a global nonlinear convergence theorem. The periodic calculation is only a reproducibility check. No independent audit has been performed.
