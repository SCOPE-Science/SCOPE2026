# Independent audit — 2026-10-01

**Record:** Optimal shifted cyclic certificates for robust Chebyshev interpolation  
**Disposition:** passed

## Correctness — PASS

For even period, the shifted two-evaluation functional annihilates the one-dimensional sampling kernel and gives the displayed exact weights. Endpoint-singularity subtraction plus digamma sums yields \(W_k(a)=A(a)\log k+B(a)+o(1)\), while the nearest sampled point gives the exact maximum weight. Optimizing the resulting one-variable certificate at excess \(u=A(a)\) yields the displayed \(C(a)H^{-1}e^{-H/A(a)}\). Since \(A(a)=2\sin(\pi a)/\pi\), the half shift uniquely minimizes the exponent and its digamma value gives \(8e^{\gamma-1}/\pi\).

## Originality — PASS

The Euler prefactor, asymptotically optimal period, and fixed-phase exponent law require additional asymptotic and optimization work and are not stated by the source.

Equivalent-formulation search: No equivalent method-level asymptotic with the Euler-constant prefactor or phase classification was located.

Broader-coverage search: The audited claim deliberately does not assert an asymptotic equivalent for the true parameter; it exactly classifies a natural explicit obstruction family.

Exact-database/table check: There is no database lookup; the new implication is the optimized interpolation certificate.

## Scientific value — PASS

The theorem completely optimizes a natural explicit obstruction mechanism, improves its published leading coefficient substantially, and explains structurally why the half-period shift is uniquely exponent-optimal among fixed shifted two-point functionals.

## Source inspections

- https://arxiv.org/abs/2609.14769: Primary full text inspected through the Chebyshev-grid cyclic obstruction. The paper gives only the half-shift functional, the exact inequality before a coarse maximum-weight bound, and a nonoptimized explicit lower bound; it does not optimize the exact maximum coefficient or classify shifted phases.
- https://arxiv.org/abs/2407.19223: Classical/modern finite-cosecant-sum background. Standalone cosecant asymptotics are treated as prior mathematics, not as the contribution.

## Residual risks

- The asymptotic is for this explicit certificate family, not for the true obstruction parameter.
- It does not close the order-H gap for the true Chebyshev-grid obstruction parameter.
