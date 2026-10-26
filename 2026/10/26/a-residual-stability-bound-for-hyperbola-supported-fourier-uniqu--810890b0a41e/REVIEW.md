# Scientific review

## Correctness — PASS

The sampling lemma is proved by piecewise-linear interpolation, an exact derivative bound using the positive minimum gap, and Poincare–Wirtinger on each interval. The first application to the reciprocal transform upgrades the initial \(\mathcal H_0\) assumptions to \(t\psi\in L^2\); the second application yields the estimate for \(\|\psi\|_2\). The Fourier normalization and reciprocal norm identities were checked explicitly. No finite computation is used as proof.

## Originality — PASS, with residual literature risk

The closest exact-geometry sources are Radchenko–Ramos (2024) and Hedenmalm–Montes-Rodríguez (2011). They prove uniqueness from exact vanishing, not the displayed \(\ell^2\)-residual bound. Yu–Townsend (2022) give nonuniform sampling stability for finite periodic trigonometric interpolation, which does not imply the reciprocal-transform estimate. Indexed comparisons returned other sampling and recurrence results, but no equivalent statement. An unindexed source may still exist.

## Value — PASS

The result turns qualitative uniqueness into a quantitative error-propagation estimate and derives the needed weighted \(L^2\) regularity from the residual data. The explicit dependence on the two gap bounds and on \(1-\alpha\beta\) is useful for understanding stability away from the critical threshold. Constants are not claimed optimal.

## Closest literature and limitations

The theorem is limited to the \(\mathcal H_0\) class, separated bi-infinite sequences with uniform lower and upper gap bounds, square-summable residuals, and \(\alpha\beta<1\). It makes no claim at or beyond the critical boundary.

Self-review: passed. Independent audit: not yet performed.
