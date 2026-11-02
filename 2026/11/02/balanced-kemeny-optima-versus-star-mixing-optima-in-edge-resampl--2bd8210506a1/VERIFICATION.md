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

The exact finite-state verifier is `verify.py`; run `python3 verify.py`. It requires only Python's standard library. Its independent rational first-hitting-time computations and transition-power comparisons agree with the stated closed formulas, and it reports 12,354 checked exact-rational comparison units.

The all-size result is proved analytically in `RESULT.md` through a block-spectrum decomposition, a strict derivative comparison, and monotone crossover branches. Finite grid checks do not establish the continuum claim by themselves. A separate expert or independent mathematical audit has not been performed. No claims concerning temporally correlated edge states or exact mixing-time optimality beyond the displayed cases were checked.
