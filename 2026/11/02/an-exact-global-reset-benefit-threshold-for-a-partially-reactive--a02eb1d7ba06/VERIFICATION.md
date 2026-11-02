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
# Verification procedure

Run `python3 verify.py` in the same directory as this file. The checker requires SymPy, verifies exact expressions for the Taylor coefficients through order twelve and the crucial factorization, and conducts 600 deterministic numerical parameter trials of the mean-time inequality. The random seed is fixed. The code uses no network access, external files, or hidden inputs.

The proof in `RESULT.md` establishes the global sign of every coefficient for the entire parameter domain, not merely for the finitely many cases computed. The checker cannot by itself verify the infinite positivity argument or historical priority. Correctness and originality are assessed separately in `REVIEW.md`; no independent verification has been performed.
