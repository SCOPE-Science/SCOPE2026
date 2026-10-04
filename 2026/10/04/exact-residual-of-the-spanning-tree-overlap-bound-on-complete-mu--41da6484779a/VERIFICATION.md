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

The analytic proof is the primary evidence. It derives the closed-neighborhood avoidance sets part by part, proves the exact maximum-spanning-tree value, counts non-dominating sets directly, and reduces the gap to a binomial identity.

The included `verify.py` independently reconstructs every complete multipartite graph through order \(11\). For each \(1\le k\le N\), it evaluates \(\sigma_k\) from closed neighborhoods, computes \(\tau_k\) by Kruskal's maximum-spanning-tree algorithm on the complete weighted vertex graph, enumerates all \(k\)-subsets to test domination from adjacency, and checks the three formulas, the exact residual, and the sharpness criterion.

Expected output:

`ALL CHECKS PASSED; multipartite_types=183; parameter_cases=1656; subsets=177373; max_order=11`

The exhaustive test is finite and does not constitute a proof for unbounded order. No independent audit has been performed.
