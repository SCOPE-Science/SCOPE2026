---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS: For k>=2 clique blocks, hub-to-leaf and within-block snowflake distances are 1, cross-block squared distances r=2^(2alpha). A positive weighted variance identity using p_i proportional to 1/b_i, b_i=(r-1+1/m_i)/2, proves c2^2>=R^2=r/2-1/sum_i 1/b_i, in addition to >=1. Orthogonal block simplices and a hub at (or perpendicular to) their common weighted circumcenter realize exactly max(1,R^2). Equality in the strictly positive weights determines all pair distances and congruence of optimum. The leaf affine rank is N-1, the hub adds one dimension iff R²<1. Strict monotonicity of the weighted-max expression and r=1/4 endpoint establish the unique alpha threshold, including the k=2 singleton endpoint. Independent Gram/PSD/distance checks covered 416 leaf pairs; finite tests are supplemental.

## originality

PASS

Best-knowledge PASS, qualified. General distorted negative type and complete-bipartite graph distortion are known, as are friendship-graph quadratic embedding constants, but the invariant there differs (unsquared distance conditional negativity versus squared-distance least Lipschitz distortion). No inspected theorem implies the variable-size bouquet harmonic law or the full snowflake-dependent affine dimension drop. Prior Euclidean distance matrix / minimum-enclosing-ball work might contain an equivalent characterization.

## value

PASS

PASS: The explicit harmonic block-size formula, rigidity and exact affine-dimension drop give a natural full classification of snowflake embedding behavior for a graph metric with one hub. The phase threshold is not a trivial consequence of an isometry test or a small fixed example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
