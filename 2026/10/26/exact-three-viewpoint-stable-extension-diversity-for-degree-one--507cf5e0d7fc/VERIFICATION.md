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

# Verification of the stated theorem

**Logical verification.** Directed paths have a forced alternating stable extension. Even directed cycles have two complementary stable phases; odd directed cycles have none. Stable extensions factor over components. The triple-coordinate argument converts pairwise distances to total cycle weight minus the loads of three bins, and each bin partition is realized by explicit phase choices.

**Computation.** Run `python3 verify.py` with Python 3.8 or later and no external packages. The script enumerates all vertex-subset candidates and their attack/stability conditions for 35 small cases and independently checks the three-bin dynamic program. The executed test returned `PASS 35 exact stable-extension/three-diversity tests`.

**Boundary checks.** Tests include odd-cycle obstruction, path-only cases with fewer than three stable extensions, mixed paths and even cycles, and uneven cycle lengths. For arbitrary sizes the proof, not the finite tests, establishes the exact formula. No external independent validation has been performed.
