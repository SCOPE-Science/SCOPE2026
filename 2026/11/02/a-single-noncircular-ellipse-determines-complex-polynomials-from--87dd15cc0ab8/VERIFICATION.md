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
# Mathematical verification

The exact proof is contained in `RESULT.md`. The key implications are rational-function equalities, not numerical extrapolations. A nonzero rational \(h\) with both the ellipse deck identity and unimodular boundary identity satisfies \(h(v)=h(r^2v)\); expansion around zero proves it is constant. Sampling uses at most \(4n\) roots of a nonzero Laurent intensity difference. The circle counterexample is direct.

Run `python CHECK.py` for supplementary exact symbolic identities and numerical consistency tests. The finite tests do not prove the rational-function rigidity theorem or any optimality/stability assertion. No external independent audit has been conducted.
