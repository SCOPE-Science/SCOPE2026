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
Run `python3 verify.py` using Python 3.9 or later (standard library only) from the directory containing the attached files. Compare its stdout to `verify_output.txt`. The program constructs adjacency matrices directly from cycle and chord edges, independently counts characteristic-polynomial coefficients by matchings, computes ranks of successive matrix powers using binary elimination, and enumerates entire trajectory graphs for small orders. The actual recorded run printed `TRIANGLE_CHORD_XOR_VERIFY_OK`.

Checks: 1,071 matrix-power rank comparisons for \(4\le n\le150\); 18 matching-polynomial checks for \(4\le n\le21\); all 32,752 binary configurations across \(4\le n\le14\). These tests are finite, do not verify all \(n\), and do not individually enumerate nonbinary characteristic-two fields. The mathematical proof uses symbolic recurrence and Jordan arguments for all specified \(n\) and \(q\). The finite verifier is not an independent external audit.
