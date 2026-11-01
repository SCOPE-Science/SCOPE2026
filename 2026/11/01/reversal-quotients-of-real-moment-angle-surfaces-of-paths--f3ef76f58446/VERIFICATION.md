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

# Reproducibility and limits
Execute `python3 verify_path_angle.py` in a directory containing the embedded program. The expected output is embedded as `verify_path_angle.out`, and the final line is `VERIFY_OK`.

The checker constructs all sign vertices of the n-cube for n=3,...,11, computes components of the induced graph on nonpalindromic corners, enumerates all fixed proper arc endpoints, identifies the parallel-arc pairing of palindromic boundary circles, computes the signed Lefschetz trace on cubical cells, and compares its quotient Euler characteristic and nonorientable genus with the symbolic formulas. All arithmetic uses integers; there are no random samples or symbolic-precision approximations.

Limit: these finite enumerations do not establish the all-length theorem. The proof uses an explicit connectivity argument for arbitrary length, geometric half-disk and quotient-boundary analysis, and compact-surface classification. The verifier is not an independent audit or external certification.
