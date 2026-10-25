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

The enclosed `checker.py` uses exact rational arithmetic and can be run with `python3 checker.py`. It checks the Parseval convolution identity at eight rational coefficient choices, isolates the only real stationary point by exact sign tests, and checks the global curvature certificate and strict gap. Output: `PASS: exact convolution, derivative root isolation, strong convexity, strictly positive contraction gap`.

The mathematical proof of the full statement additionally uses strict convexity in complex polynomial coefficient space and Haar-preserving reversal, conjugation, and rotation. Those infinite-dimensional integral identities are proved in RESULT.md, not inferred from the finite rational tests. No external independent audit has been performed.
