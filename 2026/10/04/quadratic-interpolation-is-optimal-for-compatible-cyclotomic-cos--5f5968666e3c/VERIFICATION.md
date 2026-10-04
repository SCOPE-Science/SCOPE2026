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

The symbolic proof uses only exact cosine values at levels \(2,3,4\) and compatibility of affine-linear polynomials. The included `verify.py` represents \(b_2,b_3,b_4\) as exact rational affine forms in \(c,a_1,a_2\), verifies \(2b_3-b_2-b_4=0\), reconstructs every tested triple on that plane, and verifies that \( (0,1,0)\) is excluded.

The script also checks, for a finite grid of prescribed low-level rational values, the explicit quadratic correction used in the source's exceptional \(2,3,4\) step. This finite replay is not used to prove the infinite upper bound. The universal degree-two construction is checked from the source proof: at the induction step the discrepancy belongs to \(K_{n+1}^+\); division by the nonzero \(\alpha_{n,n+1}\) stays in that field; and the standard cosine span of \(K_{n+1}^+\) provides a rational affine-linear \(L_n\), so adding \(x_nL_n\) preserves compatibility and total degree at most two while fitting the next target.

No numerical approximation enters the proof.
