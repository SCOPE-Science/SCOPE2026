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
# Verification

The analytic proof checks the full quantified domain: every finite simple complete multipartite graph with at least two parts and every \(0<\alpha,\beta\le1\). Its critical steps are the exact ordinary-zero-forcing lower bound \(N-2\) in the noncomplete case, the exhaustive two-unfilled-vertex transmission analysis, and the one-unfilled-vertex maximum-degree calculation.

The executable `verify_transmission_multipartite.py` independently implements the synchronous transmission rule using exact rational arithmetic. It enumerates every initial subset for every complete-multipartite isomorphism type of order at most \(8\) over the parameter grid \(\{1/4,1/3,1/2,2/3,3/4,1\}^2\), then compares the brute-force minimum with the theorem. It also compares the theorem directly with the published star and complete-bipartite formulas on the same grid.

Expected replay output:

`ALL CHECKS PASSED; multipartite_types=58; exhaustive_parameter_cases=2088; source_specializations=1332; max_order=8`

The finite replay is not an exhaustive proof for unbounded graph order or continuous parameters. It is a stress test of the independently stated analytic argument.
