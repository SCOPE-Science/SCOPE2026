# Review

## Correctness

PASS. The component offsets cancel exactly from the variance-reduced estimator. In the state \(e_k=x_k-w_k\), direct conditioning on the sampled component and the independent refresh coin gives a closed three-dimensional recursion for \(\mathbb E[x_k^2]\), \(\mathbb E[x_ke_k]\), and \(\mathbb E[e_k^2]\). Its characteristic polynomial satisfies
\[
P(1)=\frac{\alpha}{4}\left[2+\alpha-(1+4h^2)\alpha^2\right].
\]
Applying the complete cubic Jury test shows that the other three inequalities remain strict until this factor vanishes. The proof supplies explicit endpoint and monotonicity arguments for each nonbinding condition. At the claimed boundary the moment operator has eigenvalue \(1\); beyond it the necessary Jury condition \(P(1)>0\) fails.

Risk: the theorem is specific to the original pre-step snapshot refresh and \(p=1/2\). It is not transferred by analogy to other loopless conventions.

## Originality

PASS. The original Loopless SVRG paper was inspected at the algorithm, convergence theorem, and proof-development level; it supplies the pre-step refresh rule, the standard choice \(p=1/n\), and a sufficient \(\eta\le1/(6L)\) condition, but not an exact scalar second-moment phase boundary. The later arbitrary-sampling paper was also inspected through its algorithm and strongly convex theorem; it retains the same refresh convention and gives expected-smoothness-based sufficient stepsizes rather than the present closed frontier.

Focused searches covered the method name, two-component and scalar quadratics, second moments, Schur/Jury stability, snapshot staleness, and the derived radical expression. No inspected source or database record stated or implied the complete claim. The main residual risk is an equivalent result in older stochastic-approximation or jump-linear-system language.

## Value

PASS. Snapshot staleness and curvature heterogeneity are the two mechanisms that remain after reducing Loopless SVRG to its smallest nontrivial finite sum. The exact formula quantifies their joint stability cost and cleanly separates it from noninterpolation noise, which cancels from the control variate. It also turns the source paper's conservative general sufficient stepsize into a sharp benchmark for a natural \(n=2\), \(p=1/n\) model. This is a motivated boundary result rather than a routine recomputation of a known table.

Same-model review: passed. Independent audit: not yet performed.
