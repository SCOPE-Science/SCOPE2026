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
Run `python3 verify.py` with Python 3 standard library; no third-party dependencies. The tool enumerates all binary outer-layer words at periods 1, 2, 5, 10 (at most 1024), computes uniquely forced inner-layer indicators and checks every adjacency-kernel and independence equation, giving period-10 sizes \((0:1,4:10,6:20,8:5)\). The separate graph enumeration reconstructs every edge for \(n=7,8,9,10\), searches independent low-vertex sets and directly tests the original perfect-edge condition, returning precisely the same polynomial coefficients. `VERIFY_OK` reports completion. These finite checks constitute a complete certificate only after the algebraic period-10 reduction, not by extrapolation. No independent scientific assessment has been performed.
