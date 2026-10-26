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

# Computational verification

`verify_rook.py` is a standalone Python 3 standard-library script. Its `F_vote` directly tallies the \(n\) graph neighbors of each individual vertex and implements strict voting plus tie retention. Its separate `F_sets` implements the symbolic set update from row cardinalities. Those functions are independently compared on every one of the \(\sum_{n=3}^{9}4^n=349504\) labelled initial configurations.

For each state the script checks its trajectory to five updates, computes its first entry into period one or two, and compares period and transient-depth histograms with the binomial formulas. It verifies that \(F^5=F^3\), and for even \(n\), \(F^4=F^2\). Formula integrality, nonnegativity and conservation are also checked for sizes \(3\) through \(400\). The exact captured output is `verification_output.txt`, ending with `EXHAUSTIVE_VOTE_AND_ORBIT_OK` and `FORMULA_INTEGRITY_OK`.

These finite computations are not a proof of the claims for all graph sizes. The all-size proof is the explicit population-type analysis in `RESULT.md`. No independent external review or audit has been performed.
