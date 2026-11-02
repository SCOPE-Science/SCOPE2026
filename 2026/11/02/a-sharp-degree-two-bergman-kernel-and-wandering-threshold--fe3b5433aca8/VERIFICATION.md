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

The proof determines all scalar zeros by the exact even-part binomial identity and the Cayley transform, then transfers the sharp zero-free threshold to cyclicity of the wandering vector in the original weighted Bergman norm. All quantifiers \(\alpha>-1\) and \(0\le a<1\), including equality and boundary zeros, are addressed analytically in `RESULT.md`.

Reproduction: run `python CHECK.py` with SymPy and mpmath available. The bundled arithmetic checker returned `PASS: 271 finite exact/numerical assertions`. The SymPy assertions reconstruct exact rational numerator polynomials and count negative roots at integer weights; the high-precision calculations corroborate the even-binomial closed form and negative roots at noninteger weights. They are **supplemental checks**, not infinite certifications or independent review.

The earliest motivating source was first public September 29, 2026. Its complete full text could not be inspected; only publicly indexed metadata and abstract were accessible. A subsequent October 27, 2026 paper was examined for potentially dominating statements but was not treated as the eligible motivating source. No independent mathematical audit has been performed.
