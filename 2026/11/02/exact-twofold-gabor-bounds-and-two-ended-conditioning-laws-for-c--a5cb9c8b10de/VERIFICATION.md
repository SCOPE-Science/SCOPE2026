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

# Verification scope

The exact derivation in `RESULT.md` supplies the infinite-dimensional justification: Zak Parseval reduces the entire \(L^2(\mathbb R)\) frame problem to a continuous multiplier; strictly monotone frequency dependence gives the two boundary profiles; and a pair of quadratic derivative equations gives their global extrema. The resulting formulas hold for every \(a>0\), not just sampled parameters.

`erlang_gabor_check.py` uses only the Python standard library. Run `python3 erlang_gabor_check.py` from a folder containing the file to repeat the supplementary computation. At preparation, it printed `PASS 72421 assertions`, comparing the closed rational Zak expression against its defining series, checking the proposed optimal fibers and dense finite grids at eleven representative shape parameters, and checking both limiting regimes at finite samples.

These finite tests are not an exhaustive enumeration of all real parameters or frequencies, and their numerical tolerances cannot certify exact identities. The universal theorem depends on the written algebraic proof and its sign estimates. Source-access limitations and residual originality risks are disclosed in the scientific review and structured assessment. Independent mathematical validation has not been carried out.
