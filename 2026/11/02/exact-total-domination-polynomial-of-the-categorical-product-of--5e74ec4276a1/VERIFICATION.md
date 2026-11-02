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

# Reproducible checks

The standalone Python 3 script `verify.py` uses standard-library integer arithmetic and contains no third-party dependencies. Execute `python3 verify.py` in this directory. It directly generates open-neighborhood bit masks from the categorical adjacency rule and checks every possible vertex subset for eleven graphs up to \(4\times5\). It then compares all coefficient counts with the symbolic expression implemented independently of graph adjacency. Separate subset checks compare the row-column-cross obstruction test against open-neighborhood coverage, and 625 parameter pairs undergo exact-arithmetic symmetry and boundary checks.

Expected completion markers include `DIRECT_SUBSETS_CHECKED 1173328`, `DIRECT_GRAPHS_CHECKED 11`, `EXACT_ARITHMETIC_PAIRS 625` and `VERIFY_OK`.

A finite verifier is not a proof for unbounded \(m,n\). The uniform proof is the disjoint active-support classification and unique-center argument in `RESULT.md`. No random sampling, numerical floating-point approximation, external solver or unverified certificate is required. Independent mathematical audit has not been performed.
