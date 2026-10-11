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

The analytic proof is primary. The exact checks are:

1. Parseval applied to \(F_c^2\) gives the ordered pair-sum-fiber identity
\[
\|F_c\|_4^4=\sum_s\left|\sum_{a+b=s}c_ac_b\right|^2.
\]
2. Under the one-collision hypothesis, every fiber except one contributes exactly the generic term \(2S^2-\sum_a|c_a|^4\).
3. For a disjoint-pair collision, the exceptional cross term is bounded by \(8\sqrt{x_ax_bx_cx_d}\), and AM-GM yields the sharp value \(9/4\).
4. For a three-term progression, the exceptional cross term is bounded by \(4y\sqrt{xz}\). With \(p=x+z\), the inequalities \(\sqrt{xz}\le p/2\) and \(x^2+z^2\ge p^2/2\) reduce the defect to
\[
2yp-y^2-\frac{p^2}{2}
=(p+y)^2\left(\frac17-\frac{(7y/(p+y)-3)^2}{14}\right),
\]
which gives the sharp value \(15/7\).
5. Equality in the scalar inequalities and phase bounds yields exactly the extremizer classes stated in `RESULT.md`.

`artifacts/verify.py` reconstructs ordered pair-sum fibers directly, verifies exact witnesses for both constants, exhaustively finds single-collision supports in a bounded integer census, and stress-tests the corresponding upper bounds with a fixed random seed. `artifacts/verification_output.txt` records the replay result.

Finite enumeration does not prove the arbitrary-group theorem. Unproved limits are multiple collisions, torsion, other exponents, stability, and finite cyclic sampling. Literature search can miss an older equivalent result expressed under substantially different terminology.
