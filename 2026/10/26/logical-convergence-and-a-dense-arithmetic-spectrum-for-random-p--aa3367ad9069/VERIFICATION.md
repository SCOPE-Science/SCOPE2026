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
# Verification and proof boundary

The standalone program `verify_partial_injection.py` uses only Python 3 standard-library modules. From the directory containing this file, run `python verify_partial_injection.py`. Its output begins `PARTIAL_INJECTION_EXACT_OK 15126 12`. It exhaustively checks all labelled partial injections up to six vertices and twelve exact mixed-factorial-moment identities, along with auxiliary coefficient ratios computed by exact rational arithmetic. The proof of first-order convergence depends instead on the separately documented coefficient asymptotic, growth of the number of long paths, and the bounded-degree Hanf theorem. The finite checks are not substituted for those results. No independent external audit has occurred.
