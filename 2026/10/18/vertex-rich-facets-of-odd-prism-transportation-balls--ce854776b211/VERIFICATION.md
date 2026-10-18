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
# Reproducible checks

Run `python3 verify_odd_prism.py` with Python 3 and no optional dependencies. The script independently computes the coefficient of the explicit two-state matrix for odd \(n\) from 3 through 29, comparing it with \(2n\) times the central trinomial coefficient of order \(n-1\). Separately, it enumerates **every** integer edge-Lipschitz potential normalized at one vertex for \(n=3,5,7\), counts tight edges and verifies connectedness for every potential achieving \(3n-2\). The expected maximizing counts are \(18,190,1974\); the script raises on any discrepancy and prints `ALL INDEPENDENT CHECKS PASSED` on success.

The exhaustive checks are finite and do not establish the infinite assertion. The proof of the general result is the edge-parity, equality-classification, and transfer-matrix argument in `RESULT.md`. The asymptotic uses the standard local central limit theorem for steps \(-1,0,1\). No external independent audit is claimed.
