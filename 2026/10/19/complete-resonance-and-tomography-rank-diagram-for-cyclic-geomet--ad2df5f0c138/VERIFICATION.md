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

Run `python3 verify.py` using Python 3 and its standard library. The checker uses independent direct summation of cyclic ambiguity coefficients and the algebraic closed form at \(N=3,\ldots,14\), including seven nonzero geometric ratios of different modulus and phase type per dimension. It checks all 7,070 resulting coefficient comparisons, every predicted zero/no-zero decision, the gcd-rank counts, and 12 explicit pairs of inequivalent equal-intensity signals.

Observed execution: `VERIFY_OK 7070 direct-vs-formula / zero-pattern comparisons; 12 independent ambiguity witnesses; N=3..14`.

Finite floating-point checks are supplementary. The proof for every cyclic dimension and every nonzero complex ratio is the exact argument in `RESULT.md`: finite sums, modulus/phase rigidity, integer divisibility, and Weyl character orthogonality. No independent audit or proof-assistant certificate is claimed.
