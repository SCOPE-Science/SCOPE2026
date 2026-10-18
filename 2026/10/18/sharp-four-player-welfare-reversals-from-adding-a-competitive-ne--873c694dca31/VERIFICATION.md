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

# Checks performed

`verify.py` is a standalone exact-arithmetic verifier. It checks every connected two-, three- and four-vertex graph in the NetworkX graph atlas for positive semidefiniteness of \(I+A/2\). It reconstructs all seven three/four-vertex graph-edge transition types by SymPy inversion and symbolic equality tests. It checks strict positivity of two lists of rational Bernstein coefficients, sign changes of the two threshold polynomials at rational endpoints, the exact derivative decomposition, and the rational four-player welfare witness.

To reproduce: install Python 3, SymPy and NetworkX, then execute `python verify.py`; it prints `All checks passed.` on success. This verifies algebra and finite structural coverage, not universal literature originality, external peer validation, larger graphs, or non-interior Nash equilibria.
