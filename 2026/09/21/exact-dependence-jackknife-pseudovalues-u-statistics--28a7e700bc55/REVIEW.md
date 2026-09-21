# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof reduces delete-one pseudo-values to the canonical Hoeffding components. For a component of order \(r\), the coefficient is \(r/{n-1\choose r-1}\) when the deleted index belongs to the component and \((1-r)/{n-1\choose r}\) otherwise. Orthogonality of canonical terms then gives the stated variance and cross-covariance after a complete subset count. The cross coefficient simplifies to \(-(r-1)/{n-1\choose r}\), making the negative-semidefinite sign immediate.

The iff-additive equality case follows because the cross covariance is a negative sum of positive multiples of positive-semidefinite matrices \(\Gamma_r\), \(r\ge2\). The scalar correlation bound is a weighted-average argument over the monotone sequence \((r-1)/(r(n-2)+1)\), and explicit first-order/fully-degenerate mixtures attain the entire interval. The jackknife-bias identity follows independently from exchangeability together with the exact pseudo-value mean identity. Exact-rational verification reproduces the coefficient algebra, the Rademacher counterexample, and the order-wise bias ratios.

Adversarial checks included the additive kernel, a completely degenerate degree-two kernel, the boundary \(n=m+1\), and the vector-valued positive-semidefinite ordering. No hidden nonsingularity assumption is needed except when a scalar correlation is written, where positive pseudo-value variance is stated explicitly.

## Originality

**PASS, to the best of our knowledge.** The classical ingredients are deliberately excluded from the originality claim: Hoeffding decomposition; Arvesen's jackknife theory for U-statistics; the approximate-iid pseudo-value heuristic in Miller's review; Hinkley--Wang's observation that pseudo-values are generally dependent; Efron--Stein's positive-bias theory for jackknife variance estimates; and later asymptotic pseudo-value independence results.

The checked literature did not reveal the explicit all-Hoeffding-order formula for cross-pseudo-value covariance, its negative-semidefinite sign with an iff-additive zero case, the sharp scalar correlation interval, or the exact identity identifying jackknife covariance bias with minus cross-pseudo-value covariance. A 2024 U-statistic testing paper states that the pseudo-values are “uncorrelated” as well as asymptotically independent; the present exact formula clarifies that finite-sample uncorrelatedness holds only in the additive-kernel case.

The principal residual risk is older specialized jackknife literature. The complete theorem text of Arvesen (1969) was not inspected, and the full text of Shi (1984) was not available for theorem-by-theorem comparison. Both are close enough in subject to remain explicit originality uncertainties. This is a residual risk, not evidence of prior coverage. Efron--Stein (1981) was inspected directly and supplies broad ANOVA/jackknife-bias context but not the specific package of claims asserted here.

## Value

**PASS.** The result gives a precise finite-sample correction to an independence heuristic that is still used in modern U-statistic pseudo-value methodology. The exact covariance decomposition identifies which Hoeffding orders create dependence, quantifies the strongest possible pairwise correlation at fixed \((m,n)\), and gives an interpretable exact source of jackknife variance inflation. The vector inequality also provides a dimension-free sharp covariance inflation factor.

## Scientific limitations

The theorem is restricted to complete one-sample U-statistics with square-integrable symmetric kernels and ordinary delete-one jackknifing. It does not claim analogous formulas for incomplete/two-sample U-statistics, delete-\(d\) jackknives, censored pseudo-observations, or arbitrary smooth statistics. It does not challenge asymptotic-independence results: the finite-sample correlations vanish for fixed degree as \(n\to\infty\). The uninspected full texts of Arvesen (1969) and Shi (1984) remain the main originality uncertainty.
