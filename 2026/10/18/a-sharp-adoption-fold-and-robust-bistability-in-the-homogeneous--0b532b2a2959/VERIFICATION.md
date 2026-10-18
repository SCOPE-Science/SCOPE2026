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

# Exact arithmetic verification

Run `python verify.py` using Python 3. The standalone program uses only `fractions.Fraction` and checks the admissibility inequalities, the exact fold threshold, factor-root substitutions, the fixed-point equations, positivity of every state coordinate, independently constructed homogeneous and transverse Jacobians, their characteristic-polynomial coefficients, and strict rational endpoint sign changes.

The lower positive equilibrium has mean-mode roots in \((0,1/4)\), \((4/5,9/10)\), and \((1,21/20)\), and transverse nonzero roots in \((4/5,9/10)\) and \((19/20,1)\). The upper equilibrium has mean-mode roots in \((0,1/4)\), \((3/4,4/5)\), \((19/20,1)\), and transverse roots in \((3/4,4/5)\) and \((19/20,1)\). Degree bounds make these intervals exhaustive. Homogeneous/mean decomposition, the strict cubic maximum, and positive-baseline implicit-function continuation are proved in `RESULT.md` and are not established merely by these finite checks.

The calculation is deterministic and exact. No numerical tolerance, infinite-state enumeration, external formal verification, or independent audit is claimed. Novelty and physical relevance remain conditional on the research-specific assumptions and the cited literature comparison.
