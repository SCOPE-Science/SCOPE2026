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

The included `verify.py` checks the following without third-party dependencies: every strict input-order selector on cycles with 3–7 sites against cyclic-interval perturbations for all consecutive windows and the two-tap gapped window; explicit attaining pairs on cycles up to 100 sites; and reproducible random two-input checks. The reported tests execute against the files accompanying this result, not a log from another experiment.

These finite tests supplement, rather than replace, the all-dimensional selector, oscillation, and lattice inequalities proved in `RESULT.md`. Exhaustive finite cases do not certify arbitrary dimensions. There is no independent audit or independent validation.
