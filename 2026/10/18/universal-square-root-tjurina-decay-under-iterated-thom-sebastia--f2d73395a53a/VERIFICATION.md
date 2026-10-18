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
# Verification record

The complete proof is in RESULT.md, Steps 1–5. The attached `verify.py` is standalone Python 3 code using only the standard library and finite modular linear algebra. It constructs direct Kronecker-sum matrices for five small Jordan configurations, checks ranks against the exact formula, checks the published \(\tau(F_2)=226\) and \(\tau(F_3)=1363\) benchmarks, and measures convergence toward the proved leading asymptotic. Successful execution prints `VERIFY_OK`. Matrix tests are finite corroboration; the infinite statement is proved symbolically, and no independent audit is claimed. The boundary \(c=0\) and the possible second saddle \(s=0\) are addressed explicitly in the proof.
