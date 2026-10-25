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

# Checks and limits

The symbolic checker at `checks/pentagon_phase_checker.py` was run using Python 3 and SymPy on the complete code embedded in this record. It verified four algebraic factorization identities, the rational derivative formula, exact cubic discriminant signs and seven exact negative Bernstein coefficients; it also independently substituted two reflection-related supports for each of three representative rational parameters and reproduced the prescribed cone volumes. The checker output is `CONE_VOLUME_PENTAGON_OK endpoints 2.057628370579981 2.251826342639673 threshold 3.0852598169870777 branch_tests 6`. The analytical proof establishes all positive parameters, while the finite substitutions corroborate formula normalization only. Historical novelty remains subject to possible unindexed prior literature.
