# Independent audit — 2026-10-01

**Record:** Critical-scale phase transition in logarithmically monotone Marcinkiewicz renormings  
**Disposition:** passed

## Correctness — PASS

The arbitrary-moment construction is bounded by the Marcinkiewicz norm via Jensen, inherits logarithmic-submajorization monotonicity from the power-integral inequality, and its quasi-triangle constant tends to one. When \(\delta_nL_n\to0\), the lower moment bound using the essential supremum matches the Jensen upper bound and yields exactly the tail seminorm. Direct evaluation on Huang's pair gives \(\Phi_\delta(g)=1\) and \(\Phi_\delta(f)=(1-e^{-c})/c\) when \(\delta_nL_n\to c\), with the stated endpoint regimes.

## Originality — PASS

The final theorem strictly extends the parameter domain and identifies the exact critical response, so it is not merely a restatement of those special cases.

Equivalent-formulation search: No equivalent statement of the arbitrary-delta response function or subcritical collapse was found.

Broader-coverage search: The audited theorem combines a precise new limit calculation with an exact order-structure consequence not supplied by the primary source.

Exact-database/table check: Not applicable.

## Scientific value — PASS

It gives a natural complete phase diagram for the governing dimensionless scale, including an exact response function and the previously untreated return to full symmetry for alpha>1. This resolves the structural boundary of the source construction.

## Source inspections

- https://arxiv.org/abs/2609.20270: Complete 11-page primary full text inspected. It defines the same Marcinkiewicz construction for the power family with \(0<lpha\le1\), proves the \(lpha=1\) values \(\Phi(f)=1-e^{-1}\), \(\Phi(g)=1\), and the \(lpha=1/2\) values \(\Phi(f)=0\), \(\Phi(g)=1\), but does not state the arbitrary-delta phase diagram or the alpha>1 fully symmetric regime.
- https://arxiv.org/abs/1910.10874: Background source for logarithmic submajorization and power-integral monotonicity; no covering phase diagram identified.

## Residual risks

- No claim is made for genuinely oscillatory sequences outside the stated limit regimes.
- Generality is limited to Huang's sparse Marcinkiewicz scales.
