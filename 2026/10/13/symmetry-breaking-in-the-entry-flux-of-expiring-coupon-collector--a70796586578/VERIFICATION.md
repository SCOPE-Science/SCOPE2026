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

# Reproduction and limits

Run `python3 check_flux.py` in the folder containing this document, the proof and the checker. The checker has no non-standard dependencies; its actual replay returned `PASS: 234 exact checks; 30 direct window enumerations; n<=8 Hessian coefficients`.

The direct check constructs full length-\(M+1\) iid words and counts transitions from incomplete to complete windows, independently of the inclusion-exclusion identity. Other checks reproduce the two shortest-window product expressions, the exact binary transition polynomial, the \(M=4\) square certificate, and the exact Taylor coefficient computed by both inclusion-exclusion polynomial expansion and counting formulas.

These tests concern finite samples of alphabet sizes, window lengths and rational probabilities only. They do not prove the global or infinite-window assertions. Those follow from the algebra, calculus, symmetry and fixed-alphabet asymptotics in `RESULT.md`. No independent external scientific audit or validation has been performed. The result does not establish a comparison of nonuniform first-hitting-time laws.
