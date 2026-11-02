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

Run `python3 verify.py` in the directory holding the extracted files. It uses only Python's standard library and checks separately implemented gap-by-gap enumeration of all increasing ordered labeled trees through size eight, exact integer state recursion through size sixty, all conditional means and bias signs on their full finite support, the adjacent-regression identity, tree counts, moments, covariance, and variances. The extracted checker completed 7,374 exact assertions with output `VERIFICATION_OK exact assertions= 7374`.

The coefficient proof, conditional covariance recurrence and positivity checks in `RESULT.md` establish the claims for arbitrary integer \(n\ge3\); the finite checker cannot substitute for these steps. Relevant marginal results and first public source date are documented by identified literature. No independent scientific audit or external proof verification was performed.
