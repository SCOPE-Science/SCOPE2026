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

The proof reduces the exact one-exception criterion at dimension \(3\) to rational points on
\[
E:Y^2=X^3+13X^2-32X.
\]
The critical mathematical check is a standard two-isogeny descent. For \(E\), the square classes \(-1\) and \(2\) are excluded modulo \(3\), while \(1\) and \(-2\) are represented. For the two-isogenous curve \(E':Y^2=X^3-26X^2+297X\), all negative square classes are excluded over \(\mathbb R\), and the remaining classes \(3\) and \(11\) are excluded modulo \(16\), leaving only \(1\) and \(33\). The standard rank formula therefore gives rank zero.

The included `verify.py` independently checks these curve-specific local obstructions, verifies all displayed rational points, computes \(|E(\mathbb F_5)|=|E(\mathbb F_7)|=6\), and checks that both allowed nonzero \(X\)-coordinates map to \(t=1\). Its captured output is in `verification_output.txt` and ends with `CHECK_OK`.

The checker does not attempt to re-prove the general two-isogeny descent theorem or the good-reduction torsion theorem. Those are standard external results used transparently in the proof. No finite search is used to assert completeness of \(E(\mathbb Q)\).
