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

The source distribution and parameter convention are those of arXiv:2207.10445v2, Eq. (23). The exact beta convolution, exterior hypergeometric expression, strict monotonicity via positive-coefficient tilted variance, and endpoint limits are proved in RESULT.md. Running `python CHECK.py` requires Python, SciPy and NumPy and checks direct convolution against hypergeometric evaluations at independent parameter choices, monotonicity, roots and a critical scaling limit. The executed local checker reported `PASS: 120 direct-convolution, root, monotonicity and critical-scaling checks`. These are finite tests, not a comprehensive symbolic proof; no independent review has been performed.
