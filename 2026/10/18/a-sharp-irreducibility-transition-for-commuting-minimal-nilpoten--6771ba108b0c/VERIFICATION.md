---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproduction scope

The companion `verify_rank_one.py` uses outer products to construct the finite-field rank-at-most-one, square-zero matrices on the tested instances, verifies commuting versus mutual annihilation by pair multiplication, and uses exact recursion to compare the number of ordered tuples with the Gaussian-binomial formula. It includes the cases \((n,r,q)=(4,2,2)\) and \((4,3,2)\), with expected counts 2836 and 38536; the formula is presented as a corollary of broader known coverage, not as the original contribution. The script also checks the index and dimension arithmetic on a finite parameter grid. Expected successful output ends with `VERIFY_OK_MINIMAL_NILPOTENT_TUPLES`.

The full reduced component classification is proved by the incidence construction and noncontainment witnesses in `RESULT.md`. Finite count or dimension-arithmetic tests do not establish this classification or any scheme-theoretic assertion.
