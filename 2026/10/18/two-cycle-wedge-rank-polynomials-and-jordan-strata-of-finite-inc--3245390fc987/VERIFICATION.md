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

# Computational verification and reproducibility

Run `python3 figure_eight_checker.py` using Python 3 with no third-party packages. The checker independently enumerates each edge-weight specialization of the bipartite wedge and computes ordinary finite-field row reduction. The tested triples are `(n,m,q)=(2,2,2),(2,2,3),(2,2,4),(2,2,5),(2,3,2),(2,3,3),(3,3,2)`. The checker implements the extension field of order four directly, checks coefficient-by-coefficient against the rank-polynomial recurrence, and makes three additional polynomial total-mass checks. The observed terminal message was `ALL_FIGURE_EIGHT_RANK_CHECKS_PASSED`.

The general proof independently establishes forest rank from unique maximal-matching minors, the deleted-row path recurrence, the two-monomial cycle determinant, and the common-row direct-sum rowspace criterion. Exact finite cases cannot establish the general theorem or priority over unindexed literature. No external or independent audit was performed.
