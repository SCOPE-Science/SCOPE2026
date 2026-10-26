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

The exact-arithmetic standalone verifier `verify.py` was run against the declared sumsets. It reported `CERTIFICATE_OK exact_constructions=30 exhaustive_small_h=9,21,33`. For each even integer \(t\) from \(2\) to \(60\), it directly computes the first missing nonnegative sum for the proposed basis and checks \(9t^2-2\). It also checks global optimality for the three smallest covered orders using the finite bounds on candidate three-stamp bases proved in the cited primary paper.

The infinite theorem is certified here by a written integer residue-progressions proof, not by extrapolating finite tests. The sharp universal upper bound invokes Theorem 4.1 and Stöhr's formula as reported in the cited paper. No other orders are verified as globally optimal, and no independent external audit has been conducted.
