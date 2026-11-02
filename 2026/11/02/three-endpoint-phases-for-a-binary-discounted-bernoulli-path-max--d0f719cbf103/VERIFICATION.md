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

# Reproducibility and verification

The proof is a direct distributional calculation for an infinite binary-tree path maximum, independent of computer execution. `checker.py` can be run with `python3 checker.py` using only Python's standard library; its deterministic output is in `verification_output.txt`. The checker tests finite-depth exact-rational distributions against an independent three-mark enumeration; exact fixed-point, centering and dyadic recurrence identities; and a numerical critical-constant spot check. It does not enumerate infinite trees or certify uniqueness in the literature. The critical coefficient and both dyadic-amplitude limits follow from the displayed exact recursion and convergent products in RESULT.md.

The code's finite comparisons do not justify stronger results such as continuity of amplitude functions or all-real-scale ratio-one constants, none of which are claimed. Historical priority and independent mathematical audit remain unperformed.
