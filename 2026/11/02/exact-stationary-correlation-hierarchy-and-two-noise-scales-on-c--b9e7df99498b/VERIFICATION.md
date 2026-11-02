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

# Verification performed

Run `python3 verify.py` using Python 3 (standard library only). The expected success output is `VERIFY_OK 512`.

The program verifies three linear stationary pair-balance equations by exact rational Gaussian elimination, compares the solution against the explicit closed form and checks the inequalities for \(6\cdot5\cdot5=150\) distinct parameter triples. It constructs a finite-state one-vertex-update transition kernel directly, iterates stationary distributions for four graphs of up to seven vertices and compares pair correlations with the formula. Additional large-parameter numerical checks cover the two critical scales and the intermediate regime. The program is not a formal proof of arbitrary graph sizes or an external audit; the infinite quantifiers and limit laws are justified analytically in `RESULT.md`.

The first-public preprint date and the source scope were checked against bibliographic records and accessible primary text. Exact historical priority is not independently validated. No Lean or external expert certification was performed.
