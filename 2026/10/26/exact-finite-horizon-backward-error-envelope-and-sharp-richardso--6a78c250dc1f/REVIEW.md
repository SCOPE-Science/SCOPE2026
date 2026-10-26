# Self-review

## Correctness

**PASS.** The eigendecomposition of a nonzero real PSD matrix reduces the matrix-only residual/iterate quotient to a maximum of scalar multipliers. The geometric-sum solution denominator remains strictly positive for every \(0<\alpha<2\). The scalar multiplier decreases from the null-mode limit to zero on \(0<\beta\le1\) and increases from zero to the spectral endpoint on \(1<\beta<2\). Two explicit matrices attain the two branches of the claimed exact envelope. A decreasing/increasing crossing proves the finite-horizon optimizer; quadratic and parity inequalities prove the universal \(1/k\) interval, sharply. Numerical tests are checks, not universal certificates.

## Originality

**PASS on best accessible evidence, with explicit historical risk.** The motivating arXiv manuscript establishes the PSD Richardson universal backward-error bound using \(\eta\|A\|_2\le1\), not the exact overrelaxed envelope or the horizon-optimal step, and Cornell stationary-iteration notes optimize the distinct forward spectral radius for fixed SPD endpoints. Dedicated published-finding corpus searches for the matrix-only backward-error objective returned related Richardson claims about spectral contraction, positivity, and non-Richardson iterations but no statement implying the two-branch envelope. A publication search for the exact overrelaxation threshold and aliases found no directly covering work. This is not a proof of historical uniqueness; specialized unindexed work could exist.

## Value

**PASS.** The source's condition-number-free \(1/k\) guarantee is used to choose a stopping iteration; its stepsize was restricted to the nonoscillatory range. The exact worst-case calculation quantifies the safe cost of relaxing that conservative restriction, establishes the largest all-horizon safe overstep (\(1+1/\sqrt3\)), and gives a unique finite-budget optimal step with an asymptotically almost twofold decrease in the worst-case coefficient. This matters precisely because backward error, unlike forward contraction, includes inconsistent singular systems and two competing spectral mechanisms.

## Closest literature and residual risk

The closest manuscript is Dereziński–Nakatsukasa–Rebrova, arXiv:2604.16075, Sections 3.1–3.2 (source date 17 April 2026). Classical Richardson SPD tuning is summarized by Bindel (2025), but concerns an interval-dependent spectral radius, not universal matrix-only backward error. published-finding corpus's *Sharp stagewise-safe Richardson frontier and a no-acceleration barrier* addresses individually nonexpansive two-step error polynomials over SPD spectral intervals, not the present fixed-step backward-error supremum. The published-finding corpus comparator was available as an indexed title/summary, not a complete inspected manuscript. Specialized pre-2026 analyses could contain a mathematically equivalent inequality; independent literature audit remains outstanding. The mathematically relevant definition and Richardson theorem/proof sections were read in accessible arXiv HTML, not inferred from an abstract.

Self-review: passed. Independent audit: not yet performed.
