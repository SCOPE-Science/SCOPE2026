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

Run `python verify.py` with the Python standard library only; successful output terminates in `VERIFY_OK`. For each field and dimension, the program constructs all candidate first-vector images, recursively squares them, directly enforces all mixed-product relations, and computes the linear rank. In addition to the count and rank polynomial, it tests the set of actual idempotents by composing the full image matrices. The inspected configuration list is \(q=2\), \(2\le n\le8\); \(q=3\), \(2\le n\le6\); \(q=4\), \(2\le n\le5\); and \(q=5\), \(2\le n\le4\), a total of 19 cases. The order-four field is represented by characteristic-two arithmetic on a multiplicative group of order three.

As sample reproducibility anchors, the program reports eight endomorphisms of \(E_4(\mathbb F_2)\), 21 of \(E_4(\mathbb F_3)\), and 52 of \(E_5(\mathbb F_4)\). Finite enumeration cannot establish a theorem for all field sizes and dimensions. The general proof is symbolic and derives all multiplication constraints, flags, and sharpness without assuming empirical extrapolation. Independent mathematical audit has not been performed.
