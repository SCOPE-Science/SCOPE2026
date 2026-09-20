# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The proposed density is nonnegative for \(|\theta|\le1\), integrates
to one, and integrating out any coordinate annihilates the sole
highest-order interaction because the standard-normal sign has mean zero.
Thus every proper subvector is exactly an iid standard-normal vector.

The deterministic Student-statistic lemma was checked algebraically. If
the sample mean is positive and at least one observation is nonpositive,
convex minimization of the residual sum of squares at fixed mean gives
\[
\sum_i(x_i-\bar x)^2\ge \frac{n}{n-1}\bar x^2,
\]
which implies \(T_n\le n-1\). Sign reversal gives the lower-tail analogue.
Consequently, above this threshold each relevant one-sided rejection event
lies entirely in one same-sign orthant, where the density ratio
\(f_\theta/f_0\) is constant. This proves the exact tail multipliers.

For \(n=4\), the closed-form \(t_3\) CDF gives
\[
2\Pr(t_3>3)=\frac13-\frac{\sqrt3}{2\pi}
=0.057668885622\ldots>0.05,
\]
so the ordinary two-sided 5% critical value lies in the proven regime.
The resulting size is exactly \(0.05(1+\theta)\), ranging from 0 to 0.10.

A standalone verification script independently checks the endpoint sign
laws, a finite-grid stress test of the geometric implication, the
closed-form tail threshold, and the numerical 5% critical value.

## Originality

PASS, to the best of our knowledge. Student (1908) supplies the classical
iid-normal reference law. The multivariate Sarmanov literature already
contains higher-order product interactions, so the density construction
itself is not treated as novel. Natarajan, Ramachandra and Tan (2023)
characterize \((n-1)\)-wise independence for events, providing relevant
limited-independence context. Schaufele (1975) is especially relevant
statistically: it shows that pairwise-but-not-joint independence can change
exact regression testing error probabilities.

Searches for combinations of “Student t”, “t-test”, “studentized mean”,
“pairwise independent”, “(n-1)-wise independent”, “normal marginals”,
“Sarmanov”, and “higher-order interaction” did not locate the theorem
stated here: exact Student-tail rescaling above \(n-1\), or the concrete
four-observation result in which every triple is iid standard normal while
the ordinary two-sided 5% t-test has size anywhere from 0 to 10%.

The main residual originality risk is terminology mismatch. A mathematically
equivalent calculation could be embedded in older exact-distribution,
Sarmanov, copula, or robustness literature without being indexed under
limited independence or Student-test calibration. The inspected Lee (1996)
material establishes Sarmanov structure and multivariate extensions, but
the accessible abstract does not establish coverage of this Student-tail
calculation. No concrete source implying the stated formula was found.

## Value

PASS. The result isolates a pure higher-order dependence failure in a
foundational exact test. It is stronger than merely keeping univariate
normality, pairwise independence, or zero correlations: with four
observations, every three-observation marginal is exactly the classical iid
Gaussian model. Despite that, the conventional 5% two-sided t-test can have
exact size 0%, 5%, 10%, or any intermediate value in a one-parameter
absolutely continuous family. The proof is short, exact, and identifies
the deterministic threshold responsible for the phenomenon.

## Scientific limitations

No global extremal claim is made over all \((n-1)\)-wise independent
Gaussian-marginal laws. The two-sided distortion produced by this pure
sign interaction cancels for odd \(n\) in the high-threshold regime. The
result concerns exact small-sample calibration, not asymptotic behavior
under general dependent sequences. Equivalent older formulations under
different dependence terminology remain a residual originality risk.
