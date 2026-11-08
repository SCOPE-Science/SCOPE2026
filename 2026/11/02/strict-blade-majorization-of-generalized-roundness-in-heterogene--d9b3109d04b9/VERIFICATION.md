---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the unit-edge vertex metric on K_1 joined to m>=2 disjoint cliques (N>=m+2 peripheral vertices), reconstructing the hub zero-sum coefficient gives exactly Q_p=-sum_{peripheral}z_v^2+(1-2^p)sum_i s_i^2+(2^p-2)(sum_i s_i)^2. Within-blade and weighted Cauchy-Schwarz are simultaneously sharp, yielding necessary-and-sufficient (q-2)sum k_i/(1+(q-1)k_i)<=1. The left side increases from zero to m, so its unique root q>2 sets critical p=log_2 q. Cauchy-Schwarz equality gives one-dimensional null space at criticality; Schoenberg centering gives minimal Euclidean snowflake embedding dimension N-1 at critical and N below. Strict concavity of h_q(k)=k/(1+(q-1)k), combined with integer Robin-Hood transfers, proves strict root increase under non-permutation majorization and the unique balanced/unbalanced fixed-budget extrema. Independently calculated full zero-sum distance-powered matrix eigenvalues for k=(2,2,2),(1,2,3),(1,1,4),(1,3),(2,2), checking critical zero and negative other eigenvalues; finite tests only corroborate the universal proof.

## originality

PASS

Best-of-knowledge source comparison of exact mathematical implications, not merely titles; published SCOPE/Resultary semantic corpus queried and primary source material inspected as specifically recorded. No inspected stronger prior result covers the distinctive final claim, subject to explicitly named access and priority limitations.

## value

PASS

Motivated exact generalization of a one-point clique union's negative-type exponent and endpoint equality dimension, including a genuinely nontrivial heterogeneous redistribution law and complete fixed-size optimization. The monotonicity direction and unique extremizers are not routine consequences of computing an equal-blade windmill value; researchers working on finite metric embeddings can use exact thresholds and strictness. Not a claim for other graph metrics or arbitrary weighted bouquets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
