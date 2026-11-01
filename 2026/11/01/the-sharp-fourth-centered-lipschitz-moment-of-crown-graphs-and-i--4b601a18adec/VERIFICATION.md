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

# Reproducibility and boundaries

With Python 3 and no third-party dependencies, run `python3 verify_crown_fourth.py`. The checker uses `fractions.Fraction`, verifies all endpoint assignments modulo simultaneous permutations of matched graph indices for graph sizes from three to thirty-six, independently enumerates all labelled endpoint assignments for sizes three through six, checks the two exact witness functions and their strict branch crossover, and checks the elementary three-level fourth-moment identity using rational arithmetic.

Expected final line: `ALL_CROWN_FOURTH_MOMENT_CHECKS_OK`.

The mathematical proof in RESULT.md is general and independent of the finite range. Finite exhaustive checks establish only their finite scopes. The prior crown polar-vertex classification is acknowledged as prior art; the claimed new invariant is the fourth centered moment and its threshold.
