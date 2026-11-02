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

Execute `python3 verify_humbert_char5.py` with Python 3 standard library. All \(25\) field elements in \(\mathbb F_{25}=\mathbb F_5[t]/(t^2-2)\) are handled as coefficient pairs modulo five. The script enumerates all \(506\) ordered pairs satisfying the smoothness inequality and tests the exact five homogeneous equianharmonic polynomials.

Observed check: 20 parameters satisfy exactly two tests, 180 satisfy exactly one, and 306 satisfy none; each of five divisors contains 44 points, each pair has two intersections, no three meet, and the 20 special points comprise ten fifth-power-Frobenius conjugate pairs. Over \(\mathbb F_5\), all six parameters satisfy none. The verifier exits successfully with `VERIFY_OK`.

The script does **not** itself establish the global geometric completeness, the prime-to-five isogeny, or point counts for arbitrary extensions. These depend on the mathematical proof in RESULT.md; the verifier is an independent exact check of its finite-field specialization. Independent audit has not been performed.
