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

Run `python3 artifacts/verify.py`. The code computes CRT divisor weights and exact cyclic independent-set optima from prime-power formulas without floating-point arithmetic. All \(m\in[1,90]\) are checked; a separate exhaustive direct subset search corroborates \(1\le m\le15\). The complete integer certificate is `artifacts/values_through_90.tsv` and its actual run output is `artifacts/verification_output.txt`. The DP recurrence is proved in RESULT.md and is exhaustive by induction. The asymptotic for fixed residue classes relies on the independent analytic proof in RESULT.md; finite samples are not substituted for that proof. Independent validation has not been performed.
