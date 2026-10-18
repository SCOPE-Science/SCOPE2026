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

# Verification of the fractional-threshold single-edge response theorem

The included `verify.py` was run with Python 3 and completed without assertion failures. It checked all connected labeled graphs on orders \(2\) through \(5\), every new nonedge, every single initiator and every rational threshold-critical cell, using exact integer comparisons. It recovered the expected connected-graph counts \(1,4,38,728\), exactly \(420\) reversal presentations at order five, and exactly five relabeling classes of sizes \(60,120,60,120,60\), all with identical three-step edge-response curves.

The program additionally evaluated the explicit construction at every order from \(5\) through \(40\) at thresholds \(1/2\) and \(2/3\). The unbounded family and its full threshold response are established analytically in `RESULT.md`; testing finitely many orders alone would not prove an all-order statement.

The standalone code uses only the Python standard library. No external data files, libraries, network connections or previously generated files are needed to reproduce the finite verification. Literature novelty remains subject to independent human bibliographic review.
