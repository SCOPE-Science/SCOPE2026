# Review

## Correctness

PASS. Both statistics are written as quadratic forms of the same centered uniform empirical-process sum. The exact finite-sample decomposition separates diagonal one-observation terms from the degenerate two-observation kernel. Conditional centering makes the mixed diagonal/off-diagonal terms vanish.

The diagonal functions are explicitly
\[
q_W(u)=u^2-u+\frac13
\]
and
\[
q_A(u)=-1-\log(u(1-u)).
\]
Their variances and covariance are elementary beta-logarithmic integrals. The off-diagonal terms reduce to squared Brownian-bridge covariance-kernel integrals. Substitution gives the exact covariance and both exact marginal variances, with no asymptotic approximation.

A standalone checker recomputes the integral identities numerically at high precision and checks the finite formulas over one hundred sample sizes.

## Originality

PASS, with a residual generic-weight risk. The strongest full source inspected, Hwang--Kuriki, treats generalized Anderson--Darling and generalized Cramér--von Mises statistics in one framework and gives their separate covariance kernels and eigenstructures, but no cross-statistic covariance was found. Laio likewise treats both statistics side by side and computes marginal moments separately from empirical-process covariance kernels; targeted full-text searches found no joint covariance or correlation.

The closest own-ledger finding pairs Cramér--von Mises with Watson, not Anderson--Darling. Its stated claim does not imply the present weighted cross-covariance or the Anderson--Darling variance correction.

The residual risk is that a sufficiently general published joint-moment theorem for two weighted Cramér--von Mises functionals could imply the result as a specialization even if the explicit formula was not recorded.

## Value

PASS. Cramér--von Mises and Anderson--Darling are canonical goodness-of-fit tests that differ mainly in tail weighting. Their very high exact and limiting correlation directly measures how much information their null fluctuations share.

The result is more informative than separate marginal moments: the asymptotic correlation is about \(0.979\), while the finite-sample correction is explicit for every \(n\). This is useful when interpreting agreement, redundancy, or combined use of the two tests.

Self-review: passed. Independent audit: not yet performed.


Deterministic replay: `VERIFY_OK integral_checks=8 finite_formula_checks=400 limit=0.9789229548736679`.
