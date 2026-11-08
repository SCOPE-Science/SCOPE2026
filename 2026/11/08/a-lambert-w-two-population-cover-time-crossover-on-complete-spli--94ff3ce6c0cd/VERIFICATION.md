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

# Verification notes

The proof derives the exact killed two-state transition matrix for avoidance of an arbitrary fixed set of vertices. Direct characteristic polynomial algebra and derivatives at zero deletion identify the two rare-hit intensities. The factorial-moment argument proves the infinite-family statement; finite computation alone cannot prove the limit.

Run `python verify_cover_crossover.py` from the file directory with Python 3, SymPy, and mpmath installed. The observed complete replay output was `VERIFY_OK 1087 assertions`. The checker compares the exact full-graph rational walk with the two-state matrix, verifies the symbolic derivatives and identity, and stress-tests finite-size Lambert-scale factorial moments. All required checker code is included in this package.

The claim assumes \(a\to\infty\), \(b\to\infty\), \(b/a\to0\), and a finite limit of \(\log a-(1+b/a)\log b\). Convergence is for every fixed centered time and arbitrary deterministic starts. No uniform rate or historical-priority certificate is asserted.
