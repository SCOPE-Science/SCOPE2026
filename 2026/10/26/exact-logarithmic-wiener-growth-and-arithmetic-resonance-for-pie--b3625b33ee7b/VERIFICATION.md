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

The analytic proof checks all frequencies: mutually separated integer-centered resonance windows, their complete complement at frequencies of size \(O(n)\), and the remote tail after cancellation of continuous endpoint terms. The formula \(|e^{-imb}-e^{-ima}|=2|\sin(m(b-a)/2)|\) fixes the normalization of the sharp constant; the other factor of two comes from positive and negative frequency offsets. The irrational case uses Weyl equidistribution and Abel summation rather than numerical sampling. Rational cases use one full residue period and the elementary sine-sum identity.

`check_wiener.py` uses standard Python only. It performs independent composite-midpoint checks for selected Fourier coefficients, verifies three explicit arithmetic means, and computes finite-frequency Wiener norms at sample powers. The script is a diagnostic complement, not a certificate of the infinite-frequency or infinite-exponent limits.

This verification does not assess originality beyond the literature comparisons recorded in the scientific review, and no independent audit has been performed.
