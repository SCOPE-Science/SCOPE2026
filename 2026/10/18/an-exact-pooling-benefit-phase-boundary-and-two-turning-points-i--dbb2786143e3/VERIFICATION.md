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

The symbolic checks in RESULT.md are exact algebraic identities, not estimated coefficients. `python3 check_exact.py` runs from the containing directory using only Python 3 and its standard library; it independently sums beta-binomial probabilities, checks cost differences and ratios with rational arithmetic, and reports the two-turn witness. A completed execution reported 14,520 exact identities and the displayed rational inequalities. The executable does not certify the infinite quantifiers; those are supported by the sign analysis and gamma-ratio asymptotics in the proof.

Only fixed-sensitivity, perfectly accurate two-stage Dorfman testing is considered. Independent validation has not been performed.
