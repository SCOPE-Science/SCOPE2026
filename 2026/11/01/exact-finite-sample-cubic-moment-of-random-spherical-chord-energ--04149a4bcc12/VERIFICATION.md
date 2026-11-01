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

# Verification record

Run `python verify.py` with Python 3, SymPy, and NumPy. Its finite symbolic computation checks the first eleven Funk--Hecke eigenvalues by exact Legendre-polynomial integration, the single-chord moments, the full rational partial-fraction identity, and the numerically independently truncated cubic trace. The separate Monte Carlo uses 500,000 independently generated three-point configurations on the unit sphere and checks the triangular centered chord product and pairwise covariance with stated tolerances. Results should print `ALL_CHECKS_PASSED`.

The proof for arbitrary \(n\) uses forest independence and combinatorial enumeration, not enumeration up to a finite cutoff. The infinite chi-square limit was previously established by Bakshaev (2010); the independent derivation here checks normalization through the harmonic addition theorem, finite-dimensional central limit theorem, and a uniform expected-tail estimate. It is not claimed as new. No finite trial or approximate sum is used as an infinite proof; the explicit rational partial-fraction identity supplies an analytic summation certificate. A successful script run does not imply independent verification or historical novelty.
