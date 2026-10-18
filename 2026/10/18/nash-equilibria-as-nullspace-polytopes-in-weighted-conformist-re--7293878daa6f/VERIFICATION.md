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

The result is established by a complete analytical proof. For every weighted edge, the conformist and rebel obtain complementary payoffs, and the sum of best-response regrets is exactly half the sum of the two absolute residuals. Hence all Nash equilibria satisfy both homogeneous kernel equations, including boundary mixed actions. Standard determinant-monomial reasoning and independent atomless edge weights establish the generic matching-rank claim. A single nontrivial vertex-balance equation proves almost-sure absence of pure equilibria.

Reproduce the exact finite checks with `python3 verify.py` in the same directory. The script uses only the Python standard library (`fractions` and `itertools`). Observed output: `VERIFY_OK: 9 game instances, 1953 exact profile checks, 256 positive weighted 2x2 matrices` plus three example statements. Tests use exact rational arithmetic, not floating point. They are not substitutes for the infinite-graph-size and almost-sure proof.

Only self-review has been carried out; independent audit and external validation have not been performed. Historical priority beyond the explicitly compared accessible works is not independently established.
