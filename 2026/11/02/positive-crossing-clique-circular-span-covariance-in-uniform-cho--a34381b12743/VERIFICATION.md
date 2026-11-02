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

The mathematical proof conditions on a marked matching chord and obtains the finite covariance sum from exactly one valid pairing per selected crossing-clique endpoint set. A monotone binomial-product kernel and the independent-copies covariance identity prove strict positivity for every permitted parameter, without computational extrapolation. The exact triangle rational formula uses a finite polynomial summation, verified in exact arithmetic.

To reproduce: run `python3 verify_clique.py` using Python 3 without third-party packages. The script enumerates all 15, 105, 945, and 10,395 perfect matchings at sizes 3 through 6 and directly computes chord lengths and all clique counts, then checks closed-form and positivity identities through size 64. These are finite cross-checks, not a separate infinite proof or an independent audit.
