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

The bundled `verify.py` performs fresh direct Boolean-adjacency construction, rank reduction and full convolution-square checks at dimensions 3 through 12, with direct basis tests at dimensions 3 through 8. It evaluates both loop choices, with independent random-vector trajectory checks and a complete orbit enumeration at dimensions 3 and 4. The checks terminate with `VERIFY_OK`.

The verifier does not establish the infinite-dimensional family. The written group-algebra normal form, characteristic-two parity expansion, alternating quadratic rank calculation and Jordan arguments establish the all-dimension result. Historical priority has not been independently certified.
