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

Execute `python3 verification/verify.py` using Python 3 standard library. The program executes arithmetic in quadratic rings and checks the exact factorization, the identities required for the nonsquare lemma, root separation and genus consistency, printing `VERIFY_OK` on success.

Independent checks in the mathematical proof: quartic factors have simple roots by their quadratic-in-\(v^2\) discriminant and nonzero constant term; the field extension has total degree eight per component, and branch valuations are multiples of four. Global 96-node and 64-cusp completeness and remaining boundary smoothness are sourced from Burek Lemma 8.2. No computer experiment or numerical sample certifies an infinite claim. No independent audit is asserted.
