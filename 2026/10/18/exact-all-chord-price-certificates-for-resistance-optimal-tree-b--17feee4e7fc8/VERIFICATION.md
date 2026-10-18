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
# Reproducible checks and scope

Run \(\texttt{python3 verify_tree.py}\), using only the Python 3 standard library. The verifier enumerates path, star and eight seeded Prüfer-labeled trees for each size \(4\) through \(8\), generates nonuniform positive integer tree prices and exact rational optimal weights, independently computes the full pseudoinverse through exact fraction Gaussian elimination, and verifies the analytic chord marginal and cut-sum prices for every missing edge. It then constructs strictly improving budget-feasible allocations when a chord costs less than the threshold. The executed stdout is \(\texttt{VERIFY_OK exact_rational_assertions= 1900}\). Run and input are deterministic; the test checks finite cases and cannot establish the theorem for all sizes and prices. The exact general proof is in RESULT.md.

The source comparisons establish only a self-review. They do not certify novelty or provide independent verification. No independent audit or expert review has been performed.
