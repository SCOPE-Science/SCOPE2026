# Scientific review: effective semi-best stopping threshold

## Correctness

PASS. The source's exact threshold property for the state with one unit of drawdown is used with its correct quantifiers. The proof of the new finite-horizon certificate independently reconstructs the tail-event split for the optimal Bellman values, and the first-hitting probability change of measure has the exact factor \((p/q)^2\). Hoeffding's exponent is \(-u^2/(2m)\) for \(m\) increments in \([-1,1]\), and the deviation thresholds are applied only when positive. For \(n\ge32\), the chosen \(\delta\) lies in \((0,1)\), the concentration prerequisites hold, and the error is strictly below the drift margin. The finite checker passed 24,257 assertions. The proof, not those assertions, establishes all integers \(n\ge32\).

## Originality

PASS, with historical-priority uncertainty. The closest primary source, Islas (2026), proves convergence of the critical probabilities but explicitly leaves their rate unspecified. Allaart (2010) establishes the threshold structure and oscillations; Islas (2017/2024) establishes additional oscillation properties and small-index bounds. None of these inspected sources states the effective \(\sqrt{\log n/n}\) bound or the explicit concentration certificate. Published-record searches for the exact model, drift window, threshold and equivalent rate found only unrelated Bernoulli stopping and concentration results. Existing general concentration inequalities are ingredients, not prior quantitative statements for this stopping threshold. The later journal version of the 2017 preprint was not accessible for full-text comparison; other optimal-stopping literature may contain a stronger bound.

## Mathematical value

PASS. Quantifying the approach to the critical fair-walk probability is a natural next question after the newly resolved convergence conjecture. The inequality supplies a certified stopping region for every horizon beyond a finite explicit cutoff and an effective convergence rate, avoiding evaluation of high-degree critical polynomials. Its logarithmic overhead and loose finite-size constants are material limitations; the result is not a sharp asymptotic determination. This is not a numerical re-tabulation or a parameter substitution: the proof makes the prior qualitative long-horizon comparison uniform in the vanishing drift.

## Closest literature and limitations

The main input is J. A. Islas, arXiv:2610.26670v1 (19 October 2026), particularly Proposition 2.1, Theorem 3.1 and Remark 3.3. Historical comparators are P. C. Allaart, RIMS 1682 (2010), and J. A. Islas, arXiv:1711.08857v1 (2017). This result is deliberately one-sided: it does not show a matching lower bound for the threshold deficit or identify its sharp constant.

Self-review: passed. Independent audit: not yet performed.
