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

# Reproduction and mathematical limits

Use Python 3 and run `python3 check_backflow_exact.py`. No external packages, datasets, or unpublished files are needed. The checker evaluates the degree-79 Kummer polynomials at two specified complex rational arguments with exact rational real and imaginary parts. It also verifies a closed-form analytic tail bound based on \(|a|<1\) and \(|z|<11\). The resulting inequalities for the full Kummer function are strict, not statistical approximations.

The proof of positive trace-preserving non-divisibility additionally uses the standard contractivity of trace distance under positive trace-preserving maps, the trace-distance identity for two antipodal equatorial qubit states, and the pathwise accumulated-time bound yielding the uniform spectral-window extension. Both are reconstructed in `RESULT.md`; the executable certificate addresses the sole nontrivial numerical inequality in that proof.

The result does not establish the exact set of frequency ratios yielding backflow outside the certified band, the global supremum of distinguishability revival, or a property of arbitrary history kernels. Independence of the review has not been assessed.
