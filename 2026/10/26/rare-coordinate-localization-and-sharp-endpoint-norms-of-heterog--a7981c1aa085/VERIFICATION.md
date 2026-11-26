---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification summary

`python check.py` uses only the Python standard library and exact rational arithmetic. It reconstructs the projector by inverting the affine Gram matrix and evaluates complete weighted kernel rows and columns. In particular it checks the three four-bit values \(77/27\), \(371/128\), and \(6213/2048\), their signed differences, and equality of the endpoint norms. The included script also contains checks for the general affine endpoint formula, used here as prior work rather than claimed as new. Its recorded full run returned `PASS {'assertions': 4863, 'matrix_instances': 38, 'bias_comparisons': 500}`.

The proof in `RESULT.md` uses the established norm formula and identifies the two opposing strict inequalities with the two failures of Schur ordering. Finite exact arithmetic is corroboration of the witnesses, not a novelty determination or a general theorem about all bias vectors.
