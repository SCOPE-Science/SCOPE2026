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

# Reproducibility and mathematical limits
The accompanying `artifacts/verify.py` uses only the Python standard library. Execute `python3 artifacts/verify.py` from the extracted package directory. It checks the four Hilbert–Burch maximal minors, the tensor-product Betti numerator, Hilbert coefficients through degree 23, the degree and arithmetic-genus formulas, all 36 coordinate-component ideals and every projective point over finite fields of orders two and three. The expected final line is `VERIFY_OK K4 singular scheme / Hilbert / resolution / finite fields`.

The symbolic proof, not finite samples, establishes the claimed result in every characteristic. The principal residual scientific risk is an unlocated equivalent description in general binomial-hypersurface or monomial-ideal literature. These verifications are self-review; independent audit has not been performed.
