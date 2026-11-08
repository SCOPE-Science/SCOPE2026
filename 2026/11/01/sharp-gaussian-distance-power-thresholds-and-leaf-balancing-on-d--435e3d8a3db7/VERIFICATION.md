---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Eliminating both hub coordinates and zero-mean leaf fluctuations by completing squares yields the exact quadratic-form decomposition with Schur M_{a,b}=[[h−2^p/a,z],[z,h−2^p/b]]. Its normalized matrix M/2^p has positive definite derivative for p≥1 (the two eigenvalues y′±w′ are positive), so a unique first loss of negative type occurs between p=1 and p=2; the equality p=2 only at (1,1). On (1,2), 0<z<h; comparing determinant at the zero eigenvalue while fixing a+b proves strict increase with ab, not just numerical monotonicity. Equal-leaf root and its Taylor expansion yield the 1/m correction. The Schur nullity yields centered embedding dimensions. Independently checked full graph distance matrices against the 2×2 elimination in small asymmetric cases and strict ordering for totals 3..17.

## originality

PASS

Schoenberg and the classical finite-metric p-negative-type matrix criterion directly reduce all finite cases to matrix tests; Doust–Weston derive the exact single-star exponent, and Li–Weston the strict-lower-exponent principle. Sánchez computes graph metric of complete bipartite graphs, which are not the unweighted double-star tree metric. The inspected results do not give a strict all-partitions leaf-balancing law and explicit two-hub critical nullity. An unindexed earlier tree specialization could overlap.

## value

PASS

Double stars are the first diameter-three tree class with two branching hubs. Their negative-type exponent controls every-bandwidth Gaussian kernels and squared-Euclidean snowflake realizations. A sharp leaf-allocation extremal order, endpoint rank and large balanced-root law form a motivated infinite-family classification beyond repeating known star cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
