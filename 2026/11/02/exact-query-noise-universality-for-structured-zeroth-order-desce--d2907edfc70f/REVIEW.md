# Scientific review

## Correctness — PASS

The conditional mean identity follows from \(\mathbb E[PP^\top]=I_d\) and \(\mathbb E[P\mathbf1_\ell]=0\). Orthogonality gives \((PP^\top)^2=(d/\ell)PP^\top\) and exact control of the curvature and oracle-noise squares. All cross terms vanish under the stated independence and sign-balance assumptions. Iterated conditional expectation proves the finite-horizon recursion; a nonnegative scalar contraction factor gives both sides of the sharp stability boundary. Strict positivity of the two terms in \(Ah^2+B/h^2\) gives unique radius minimization; direct substitution proves the direction-count cancellation. The independent-baseline comparison follows from two different noise covariance matrices having equal trace after multiplication by the orthogonal frame. Exact finite-branch and symbolic checks are supplied, not used as an infinite proof.

## Originality — PASS (qualified)

The 2022 structured stochastic zeroth-order method employs one stochastic input for all evaluations in a finite-difference step and reports convergence rates, not the new independent per-evaluation noise model's exact all-horizon quadratic risk. The 2021 orthogonal random-direction analysis treats an exact function oracle; its known \(\ell\)-dependent contraction geometry alone does not determine the fresh-query noise law or unique radius. The 2019 approximation comparison treats bounded errors and generic estimation bounds rather than the joint iterative stationary error and shared-baseline equivalence. We checked source statements and proof/appendix sections where accessible; no identified source states the specific present classification or a stronger statement that subsumes it. Standard bias-variance balancing is not claimed independently original. Risk remains from specialized stochastic-approximation results, older common-baseline methods and uninspected sources.

## Value — PASS

Independent noise is amplified by shrinking the finite-difference radius, while curvature bias increases as the radius grows. The theorem makes the full sharp tradeoff exact at *every* iteration, rather than merely providing an asymptotic approximation. The surprising equality of shared-baseline versus per-direction-baseline mean-square risk shows that orthogonality permits a strict oracle-call saving for multiple directions. The direction-count-invariant floor at the fastest contraction step clarifies an otherwise misleading expectation that extra directions must always improve stationary error, and distinguishes an iteration-speed criterion from a noise-floor criterion. These are useful structural benchmarks for derivative-free algorithm design, even though the quadratic model is deliberately limited.

## Closest literature and limits

- Rando, Molinari, Villa and Rosasco, *Stochastic Zeroth Order Descent with Structured Directions* (2022), https://arxiv.org/abs/2206.05124. Main algorithm, assumptions and appendices examined. Its within-step noise mechanism is materially different.
- Kozak, Molinari, Rosasco, Tenorio and Villa, *Zeroth order optimization with orthogonal random directions* (2021), https://arxiv.org/abs/2107.03941. The framework and main analysis were inspected; functions are evaluated exactly in the modeled recursion.
- Berahas, Cao, Choromanski and Scheinberg, *A Theoretical and Empirical Comparison of Gradient Approximations in Derivative-Free Optimization* (2019), https://arxiv.org/abs/1905.01332. The introduction, noise assumptions and error analysis were inspected; its bound-based statements do not imply the exact dynamic identities.

The proof only supplies mean-square information, not higher moments or an invariant distribution; it does not compare oracle methods under a common global call budget. Publication priority beyond the inspected sources is not certified.

Self-review: passed. Independent audit: not yet performed.
