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
# Reproducibility

Run `python3 check.py` with Python 3 (standard library only). It prints the exact rational cut-permutation coefficients for seven specified graphs, checks rational transient-generator moment systems for rates \(10\), \(20\) and \(40\), and verifies the complete-graph formula for \(n=2,\ldots,6\). The executable's success message is `PASS: all seven graphs and all five complete-graph constants`.

The proof in `RESULT.md`, not these tests, establishes the stated infinite family of fixed connected graphs. In particular, finite positive-rate checks alone do not certify the asymptotic remainder or generality.
