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

The proof is symbolic and uses exact rational expressions. Run `python verification.py` to reproduce exact-arithmetic checks for probability normalization, nonnegativity, first and second moments, variance, and representative parameter points. These finite checks supplement but do not replace the interval proof in `RESULT.md`.

The two boundary equalities are exact: at \(t=1/50\), \(b/L=\Pr(\Theta_t=1)\); at \(t=7/75\), \(b/L=\Pr(\Theta_t=2)\). The full interval classification follows from the symbolic inequalities in the proof. The closest 2017 paper’s full text was unavailable, so originality retains that access limitation.
