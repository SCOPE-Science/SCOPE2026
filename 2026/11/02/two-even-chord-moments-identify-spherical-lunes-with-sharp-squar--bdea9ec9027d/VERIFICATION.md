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

# Verification and limits

Run `python verify.py` in the same directory, with Python 3, `sympy` and `numpy` installed. The program constructs a degree-35 exact rational polynomial, converts it to degree-35 Bernstein coefficients on \([0,(11/7)^2]\), and asserts that all 36 are greater than \(1/10\). A separately bounded Taylor/trigonometric approximation error is strictly less than \(1/10000\). Thus the derivative's sign is proved everywhere, including parameters near either endpoint. The \(\pi\) bound is derived from two rational arctangent series and Machin's identity, not a floating-point assumption.

The program also checks the two endpoint expansions symbolically and independently integrates the two distance moments by four-dimensional tensor-product quadrature for three nontrivial angles. Quadrature is only a consistency check; all universal statements use exact integrations and the rational certificate.

The reconstruction uses exact population moments and a unique scalar inversion; no finite-sample estimation guarantees are proved. Independent external audit has not occurred.
