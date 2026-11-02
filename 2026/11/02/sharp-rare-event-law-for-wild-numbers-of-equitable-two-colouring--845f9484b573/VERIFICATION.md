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

The standalone `verify.py` program requires only the Python 3 standard library. Running `python verify.py` returned:

`VERIFY_OK exhaustive_colorings=359423 dimensions=4..7 exact_isolate_identities=4 numerical_ratio_cases=5`

The finite exact enumeration covers all \(\binom{\binom n2}{\lfloor\binom n2/2\rfloor}\) labelled red edge sets at \(n=4,5,6,7\), with blue the complementary set. It independently evaluates connected-component counts, the wild-number histogram and exact rational isolated-vertex expectations. Five larger input sizes support a numerical diagnostic of the leading asymptotic prefactor. These checks are not an infinite proof; the proof uses component decompositions, hypergeometric ratios and uniform cut sums.

No independent audit or external mathematical validation has been performed. The scientific limitations are specified in `RESULT.md`.
