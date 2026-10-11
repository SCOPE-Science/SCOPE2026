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

The theorem is proved analytically in `RESULT.md`. The finite checker `verify.py` uses only Python 3 standard-library modules and reports `POLYGON_LINEAR_EXTENSION_VERIFY_OK` and 751 checks. It samples random Lipschitz data for \(3\le n\le18\), checks full pairwise quotients for an extension by averaging, and uses distance-to-vertex functions attaining the analytic upper bound. It also tests the chord-product identity, the exact unsnowflaked cotangent formula, closed triangle and square thresholds, and increasing large-polygon scaled roots converging toward \(2\sqrt6/\pi\).

To replay, execute `python3 verify.py` in a directory containing the standalone script. No external datasets, network calls, or installed packages are required.

The tests are neither exhaustive over real-valued functions nor a proof for every \(n\). The proof separately establishes the uniform derivative control needed for the limit; no finite cutoff is asserted as an infinite certificate. The implementation does not seek an independent audit.
