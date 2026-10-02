# Independent scientific audit — SCOPE-20260919-9b3127a8a223

Audited at: 2026-10-01T12:12:53.903497Z

Disposition: **passed**

## Correctness — PASS

The source certificate is reconstructed from the roots of the Chebyshev combination and its positive weights. The logarithmic-derivative identities give exact normalization and the exact objective moment. Under the boundary scaling, the exterior root converges to the unique positive solution of \(a\tanh a=1\), while fixed interior roots converge to the positive solutions of \(z\tan z=-1\). The even entire characteristic function has one imaginary pair and the positive real pairs; its genus-zero product gives the two trace identities needed to show that the limiting masses sum to one and have the asserted first moment. Independent numerical reconstruction at moderate orders reproduces unit mass, the exact objective, and convergence of the exterior mass to approximately \(0.9655400431\).

## Originality — PASS

The primary moment-SOS paper supplies the sharp atomic certificate and the exact relaxation gap, but not the boundary-layer scaling law, persistent infeasible mass, weak limiting law, or Sturm-Liouville trace explanation. The semantic research index returned the audited record as the exact match and no earlier stronger record.

### Equivalent formulations

No equivalent published formulation of the full limiting atomic law was located.

### Broader coverage

The broader moment-SOS results do not dominate the audited asymptotic certificate theorem.

### Exact database or table

This is an asymptotic theorem rather than a tabulated invariant; database absence is secondary evidence only.

### Claim versus prior implication

The final boundary-layer statement is not mechanically implied by the source theorem alone.

## Value — PASS

The theorem explains the mechanism behind a sharp relaxation-rate example: almost all dual mass remains on a single infeasible atom whose distance to the feasible endpoint is exactly on the sharp order scale. The full limiting law and trace identities are a motivated structural analysis of the extremal certificate rather than a finite numerical refinement.

## Sources inspected

- Convergence rate of the moment-SOS hierarchy for univariate polynomial optimization — https://arxiv.org/abs/2609.20544. NOT_COVERING: The paper proves the exact gap and supplies the certificate but does not state its scaled boundary-layer law or limiting mass distribution.

## Checked sources

- https://arxiv.org/abs/2609.20544
- https://arxiv.org/abs/2512.19141
- https://arxiv.org/abs/2509.01382
- semantic research-index search

## Residual risks

- Classical asymptotics for zeros and Christoffel-type weights may contain component formulas in different notation, but no source-specific theorem implying the complete limiting law was located.

## Limitations

- The result concerns one explicit optimal certificate and does not prove uniqueness of the SDP optimizer.
- It does not establish a general boundary-leakage theorem for moment-SOS hierarchies.
- The numerical checks corroborate, but do not replace, the analytic proof.
