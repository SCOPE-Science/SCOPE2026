# Independent scientific audit — 2026-10-01

**Disposition:** passed

**Final claim:** For the positive-parameter classical Rössler flow, compact invariant dynamics exist exactly when the equilibrium discriminant is nonnegative; every compact invariant probability measure satisfies the stated variance-gap, covariance, and arithmetic–harmonic height laws, with critical statistical rigidity.

## C — PASS

Direct generator identities give the first and second moment balances and the variance factorization. The support argument puts every compact invariant measure in \(z\ge0\), regularized logarithms yield the reciprocal-height identity, and standard invariant-measure existence on compact invariant sets yields the dynamical obstruction. At the double-root threshold, zero variance forces equilibrium support.

## O — PASS

Kontorovich et al. (2009) is close prior art, but full-text inspection shows its displayed stationary y-variance approximation omits the \(b/a\) term and is reported with a 5.8% discrepancy; the paper later states that exact variance evaluation is not obtained by that approach. The audited theorem supplies the exact invariant-measure relation with the missing term, derives the sharp discriminant threshold for all compact invariant dynamics, and adds the reciprocal-height identity and critical rigidity. Starkov–Starkov covers a weaker no-periodic-orbit/localization consequence when equilibria are absent, not the full compact-invariant-measure theorem.

## V — PASS

The result replaces an earlier approximate Rössler variance relation by an exact parameter-uniform invariant-measure law, identifies the equilibrium discriminant as the exact threshold for any compact invariant dynamics, and proves a reciprocal-height defect identity and critical statistical rigidity. These are motivated structural constraints on a canonical chaotic flow, not a routine finite calculation.

## Source inspections

- **Cumulant Analysis of Rössler Attractor and its Applications** (https://doi.org/10.2174/1874110X00903020029): PARTIAL_COVERAGE. The paper derives a close but approximate y-variance relation; its displayed formula omits the b/a term, and the numerical section reports a 5.8% discrepancy.
- **Localization of periodic orbits of the Rössler system under variation of its parameters** (https://doi.org/10.1016/j.chaos.2006.02.011): PARTIAL_COVERAGE. It predates the record and links absence of equilibria to exclusion/localization of periodic dynamics, but does not state the exact compact-invariant-measure laws.

## Residual risks

- Older Rössler localization or statistical-moment literature could contain an equivalent exact invariant-measure formulation under different notation; the inspected 2009 primary source does not.
