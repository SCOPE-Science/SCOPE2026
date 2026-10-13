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

# Reproducibility

Run `python3 verify_star.py` under Python 3. The executable is standalone, uses only standard-library `decimal`, `fractions`, `itertools`, and deterministic seeded data, and has no auxiliary file dependencies. It reproduces the exact conductance formulas, checks the unit budget and diameter, independently computes pairwise effective resistance by grounding the hub and solving the reduced Laplacian over the rational numbers, and checks a finite grid of positive feasible normalized resistances against the claimed optimum. Expected terminal line:

`VERIFY_OK 259 full-budget cases, 1225 grounded-network cases, 20277 exact dual-grid inequalities`

Analytically justified boundaries: every \(m\ge2\), every \(c_i>0\), both the no-majority and strict-majority branches, and their equality boundary. The finite checker does not establish the universal quantifiers, historical novelty, or independent validation. Uniqueness relies on strictness of \(\sum_i c_i/u_i\) and of the one-variable envelope in the proof; no solver status or failed search is used as proof. 
