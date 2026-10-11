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

The proof was reconstructed from the primary-source normalization and standard fixed-point formulas. The source gives a genus-\(19\) invariant fiber, an order-three automorphism with three fixed points of tangent multiplier \(\omega^2\), quotient genus \(6\), and the independent ordinary-Lefschetz trace \(-1\) on first homology.

The critical calculation is exact:
\[
\frac{3}{1-\omega^2}=1-\omega,
\qquad
1-\overline{\operatorname{tr}(S^*|H^{1,0})}=1-\omega,
\]
so \(\operatorname{tr}(S^*|H^{1,0})=\omega^2\). With invariant dimension \(6\) and total holomorphic dimension \(19\), the only nonnegative eigenspace dimensions are \(6,6,7\). Complex conjugation then yields \(12,13,13\) on complexified first homology.

Boundary checks: the characteristic polynomial has degree \(38\), its trace is \(-1\), and Riemann–Hurwitz gives quotient genus \(6\) from the stated three totally ramified points.

No computation log or finite experiment is used as proof. The integral \(\mathbb Z[C_3]\)-lattice and Prym polarization are not verified or claimed.
