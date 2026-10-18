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

# Reproduction and boundaries

Run `python verification/check.py` with Python 3, SymPy, NumPy and SciPy. The code rederives the boundary gradient identity, the positive quartic certificates, the two-root sign pattern, the exact witness, and two formal limiting expressions. It reconstructs full graph Laplacians in finite dimensions and compares inverse traces and feasible nonsymmetric alternatives with the analytically reduced objective. The mathematical claims for every integer dimension and every real positive budget are derived in RESULT.md, not inferred from the finite checks. An independent audit has not been performed.
