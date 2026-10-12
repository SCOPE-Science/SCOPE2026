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
The analytic proof uses only the exact fold formulas of Bogachev and Rozikov. The packaged `verify.py` independently re-evaluates those formulas numerically for representative \((k,q)\), checks positivity of the critical derivative pattern for \(2\le k\le100\), and verifies convergence of
\[
\frac{\alpha_+(\theta)-\alpha_-(\theta)}{(\theta-\theta_c)^{3/2}}
\]
toward the stated coefficient. A successful replay prints `VERIFY_OK`.

The finite replay does not certify the all-integer theorem. The all-parameter conclusion rests on the displayed exact algebra and Taylor expansion in `RESULT.md`. The verification does not test other boundary-law branches, global monotonicity of \(\alpha_\pm\), extremality, or the total number of Gibbs measures.
