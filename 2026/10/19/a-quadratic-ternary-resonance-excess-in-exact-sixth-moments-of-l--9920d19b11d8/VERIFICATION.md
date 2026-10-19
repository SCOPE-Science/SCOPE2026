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

The symbolic proof uses the precise finite support of Laurent powers and an exhaustive classification of five-term carries. The source code `verify.py` is standalone Python using the standard library. To run: `python3 verify.py`.

The program checks the exact sixth moments, intermediate fourth moments, second moments, and target coefficients at the first omitted frequency for integral bases \(q=3,4,5,6\) and eight truncation lengths, plus bases seven and eight through five truncations. Independent root-of-unity quadrature checks selected small cases. It exits nonzero on the first mismatch.

No external certification was performed. A finite computation is not a proof for arbitrarily large truncation length; that conclusion is supplied by the explicit recurrences and carry classification in RESULT.md. The verification does not inspect or decide the full weighted Bessel-extension inequality.
