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

The proof is analytic. The accompanying checker uses exact rational arithmetic.

It exhaustively enumerates every permutation through \(n=7\), reconstructs the full covariance matrix from the sample space, and checks it against
\[
C=\frac1{12}(I+B^\top B).
\]

For dimensions through \(n=14\), it independently verifies
\[
(B^\top B)^2=nB^\top B,
\]
multiplies the proposed inverse factor by \(I+B^\top B\), checks the determinant from the two spectral multiplicities, and checks every pairwise marginal and full-order linear partial-correlation class.

The finite replay is supplementary. The universal theorem is the exact rank-probability and incidence-matrix argument in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK permutations_checked=5912 covariance_entries=812 q_square_entries=26663 inverse_entries=26663 pair_class_checks=13104 determinant_checks=13`.
