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

The accompanying executable `checker.py` uses arbitrary-precision `mpmath` arithmetic. Executing `python checker.py` returned `PASS 85 numerical assertions; finite evidence only`. It checks the exact frame-bound quotient, strict numerical optimizer order, the additive logarithmic offsets for six redundancies, the optimal-value expansions, a square-lattice comparison, and the three renormalized profiles at six critical-layer points.

The finite checks support algebra and numerical constants, but do not prove uniformity, infinite asymptotics, global optimizer uniqueness or literature originality. Those require, respectively, the expansion and sign argument in `RESULT.md` and the cited full primary text. No independent audit or validation has been performed.
