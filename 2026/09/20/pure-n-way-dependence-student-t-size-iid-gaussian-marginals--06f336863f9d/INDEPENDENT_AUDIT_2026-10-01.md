# Independent mathematical audit — SCOPE-20260920-06f336863f9d

Final disposition: **PASS**.

## Correctness
**PASS** — Integrating any coordinate kills the centered sign interaction, so every proper subvector is exactly iid standard normal. For deterministic data with positive mean and at least one nonpositive coordinate, minimizing the centered sum of squares at fixed mean gives \(S^2\ge n\bar x^2/(n-1)^2\), hence \(T_n\le n-1\); sign reversal gives the lower-tail analogue. Therefore for \(c\ge n-1\) the upper tail lies wholly in the positive orthant, where the density is exactly multiplied by \(1+\theta\), and the lower tail is multiplied by \(1+(-1)^n\theta\). Under \(\theta=0\), \(T_n\sim t_{n-1}\), so the displayed formulas follow. Independently recomputing the \(t_3\) quantile gives \(t_{3,0.975}=3.182446305\ldots>3\), and \(2\Pr(t_3>3)=0.0576688856\ldots\), validating the four-observation 0-to-10-percent size range.

## Originality
**PASS** — The multiplicative centered-interaction family is a standard Sarmanov-type construction, and limited independence is known to alter other statistics. However, searches under Studentization, Sarmanov dependence, \((n-1)\)-wise independent Gaussian samples, and exact test size found no prior statement of the sharp deterministic threshold \(n-1\), the exact Student-tail multipliers, or the four-sample 5-percent-to-10-percent example. A full modern paper on pairwise-independent common-margin sequences concerns asymptotic sample-mean behavior rather than finite-sample Studentization. Originality therefore passes to the best of current knowledge.

### Equivalent formulations
Equivalent dependence-family and limited-independence formulations were searched; the audited contribution is the Student-specific orthant threshold and exact tail law.

### Broader coverage
These broader dependence results do not mechanically imply the threshold \(n-1\) or the exact tail rescaling.

### Exact database or table
No finite database is intrinsic; the database check targeted already-published equivalent theorems.

### Claim versus prior implication
The final claim is not a routine corollary of the inspected dependence literature.

## Value
**PASS** — The result isolates a concrete failure of a canonical exact finite-sample procedure under extremely strong local classicality: every proper subsample is exactly iid Gaussian, yet the conventional four-observation two-sided t-test can have any size from zero to twice nominal. The sharp threshold and exact multiplier make this a reusable finite-sample robustness boundary, not merely an existence counterexample.

## Source inspections
- **A counterexample to the central limit theorem for pairwise independent random variables having a common arbitrary margin** (https://arxiv.org/abs/2003.01350): full web article was available; introduction, construction, and scope statements were inspected Method: primary open full-text inspection. Assessment: BROADER_LIMITED_INDEPENDENCE_CONTEXT_NOT_STUDENT_COVERAGE. Evidence: The paper studies asymptotic sample-mean distributions under pairwise independence and does not provide the audited finite-sample Student-tail theorem.
- **Probability bounds for n random events under (n-1)-wise independence** (https://arxiv.org/abs/2211.01596): primary abstract and bibliographic record; verified full text was not available through the open route used Method: primary record inspection. Assessment: GENERAL_EVENT_BOUNDS_NOT_EXACT_STUDENT_THEOREM. Evidence: The work characterizes event probabilities under \((n-1)\)-wise independence rather than Studentization of Gaussian marginals.

## Checked sources
- https://arxiv.org/abs/2003.01350
- https://arxiv.org/abs/2211.01596

## Residual risks
- Equivalent older formulas could exist in Sarmanov, Lancaster, copula, or exact-robustness literature under different terminology.
- The theorem is an explicit family and does not prove a global extremal size distortion over all \((n-1)\)-wise independent Gaussian-marginal laws.
