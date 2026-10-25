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
The proof works over \(\overline{\mathbb F}_2\) and for every \(q=2^n\) with \(n\ge2\). It depends on the original curve's affine normalization and unique singular point, checked in Kollár's full text, and on the displayed polynomial coefficient comparison. Distinctness of the five relevant exponents is essential; the exceptional case \(q=2\) is not covered. The ordinary geometric stabilizer, not the stabilizer group scheme, is classified.

The bundled `verify.py` checks the characteristic-two binomial exponents for \(q=4,8,16,32,64\). Run `python3 verify.py`; expected final marker is `VERIFY_OK characteristic_two_projective_stabilizer_polynomial_pattern`. Finite checks corroborate the formula but are not the reason the infinite family is proved. No external independent audit has been performed.
