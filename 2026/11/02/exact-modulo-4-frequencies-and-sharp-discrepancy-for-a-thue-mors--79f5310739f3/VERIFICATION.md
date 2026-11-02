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

# Reproducibility and limits

Execute `python checker.py` in the directory containing this document. It uses Python 3 standard-library integer and rational arithmetic only. The expected marker is `VERIFY_OK`.

The checker recomputes \(128\) complete signed-block count coordinates at each level, verifies the four-periodic transition matrices, tests four initial phases of a universal lag-\(16\) recurrence, and verifies the spectral projector for every primitive initial pair and both signs. It also tests four rational generating-function identities, exact denominator divisibility and the noncancellation remainder, then independently calculates the first \(2^{16}\) recurrence values modulo \(4\). The symbolic recurrence propagation and spectral argument in `RESULT.md`, not finite-index extrapolation, establish the unrestricted claim.

There is no claim of independent scientific audit, third-party certification, or exhaustive literature coverage. The method does not determine distributions for other moduli.
