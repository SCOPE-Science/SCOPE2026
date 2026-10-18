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

# Reproducible mathematical checks

Run `python3 verify_gp.py` to reconstruct the graph \(\overline{C_n}\) and independently search all shortest paths and subsets for \(5\le n\le14\). This validates the all-set and maximal-set formulas, including the \(n=6\) exceptional maximal pairs. The exact recorded stdout is `verification_output.txt`.

Run `python3 check_coefficients.py` to check integer strict log-concavity for every \(5\le n\le500\); recorded stdout is `coefficient_output.txt`. These are bounded cross-checks, while `RESULT.md` supplies the infinite-family proof. The tests do not establish uniqueness in the literature, independence of review, or a larger-scope conclusion.
