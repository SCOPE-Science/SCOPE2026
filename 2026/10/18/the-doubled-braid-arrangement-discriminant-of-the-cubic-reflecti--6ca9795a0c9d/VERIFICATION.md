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

The included standalone `verify.py` uses exact symbolic arithmetic and checks all displayed representative factorization, gradient and conic identities. It computes affine-chart Gröbner bases to confirm the chosen smooth cubic \(G_{1,2,3}\). The checker also enumerates the six parameter lines' seven intersections from their defining equations and verifies their factorizations. Run with `python verify.py` in an environment containing Python 3 and SymPy.

The parameter-uniform scheme-theoretic discriminant identity rests on the mathematical proof in `RESULT.md`: the degree-twelve property of the ternary-cubic discriminant and the independent local smoothing factors for each of two distinct ordinary nodes at a generic point of a parameter line. Neither finite symbolic samples nor search results replace that argument. An independent audit has not been performed; no independent certification is claimed.
