---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The source definitions and proof steps were checked in the arXiv HTML full text. Equation (3) has input dimension \(d_x+d_y\) and output dimension \(d_y\); equation (7) uses the predictor on the current coupled predicted state; equation (8) writes powers of this non-self-map; Appendix B equation (29) requires a bound on the actual coupled nodal differences.

For the explicit RBF family, the proof was checked algebraically. The Gram matrix satisfies \(K_h=I+E_h\) with \(\|E_h\|_\infty\le2h^{-1}e^{-h^{-8}}\), so its KRR coefficients satisfy \(A_h={\bf1}+O(h^5)+o(h^r)\) for every fixed \(r>0\). The exact normal equations give true-center error \(h^5(A_h)_j\). The first coupled state is at squared distance \(h^{10}(1+o(1))\) from the next true center, hence the self-kernel tends to \(e^{-1}\) while all other kernel contributions vanish super-polynomially. Therefore \(\widehat y_2\to e^{-1}\). The endpoint second-order update then gives the exact resolved error \(h(3-2\widehat y_1-\widehat y_2)/2\), asymptotic to \((1-e^{-1})h/2\).

No computation is required for the proof. The result does not claim failure when the theorem's hypothesis is strengthened to bound the actual coupled unresolved rollout directly, and it does not claim the weakest possible sufficient stability condition.
