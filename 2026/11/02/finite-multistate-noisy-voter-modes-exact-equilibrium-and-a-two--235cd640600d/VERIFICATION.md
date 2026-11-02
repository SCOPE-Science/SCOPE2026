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

# Reproducible checks and boundaries

Run `python check.py` with Python 3.9 or newer. The self-contained standard-library checker independently enumerates unordered two-neighbor opinion panels, evaluates all one-site transition probabilities as rational numbers, and verifies microscopic detailed balance across full small configuration spaces. It enumerates finite count compositions for sample populations and checks the one-leader reduction, the monotonic candidate modes, the six-voter weight formulas and the two isolated algebraic thresholds.

Observed execution: `PASS 16615 exact deterministic assertions`.

Finite exact checks cannot establish a statement quantified over every population size or all real noise parameters. The full proof in `RESULT.md` supplies those arguments through detailed balance, adjacent-ratio geometry and a majorization comparison. Historical-priority comparisons are necessarily incomplete. Independent mathematical validation has not been performed.
