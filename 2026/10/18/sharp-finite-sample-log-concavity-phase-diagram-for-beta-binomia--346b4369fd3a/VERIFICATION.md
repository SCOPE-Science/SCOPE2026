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

# Reproducibility and scope

Execute `python verify.py` using a standard Python installation. The script uses exact `fractions.Fraction` arithmetic and `math.comb` for finite samples; it asserts the theorem's ratio identity, all \(LC\) classifications on its stated grid, and the sharp equality and failure examples. It does not sample floating-point values and does not use external data.

The proof is analytic and covers every \(n\ge2\), \(\alpha,\beta>0\). The verifier exercises only finite rational selections and cannot certify the infinite theorem. The critical numerator identity and the monotonicity of the numerator in the mixed-shape cases provide the bridge to the quantified claim.

No independent audit has been performed. The review is the self-review reported separately in `REVIEW.md` and `AUDIT.json`.
