---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Connectedness and B>0 give positive definiteness throughout the unrestricted simplex. The logdet second variation in any nonzero diagonal direction is the negative squared Frobenius norm of the conjugated direction. Existence by compactness and strict uniqueness justify using the two induced automorphism orbits rather than imposing a symmetry constraint. The leaf-block Schur complement is L_H+(s−y+y/(1+y))I and the eliminated determinant contributes (1+y)^m. The derivative at y=0 is m; at y=s it is R_H(a)−m, a=s/(1+s), with the zero Laplacian eigenvalue included in deriving this identity. R_H decreases strictly from 2(m−1)>m to a value below m; strict concavity puts equality B=B_H in the unique leaf-only regime and gives a unique interior stationary point above it. The complement Laplacian bounds the core spectrum by m with at least one strict inequality unless the core is complete; the clique root is (m−2)/m. Strict edge inclusion gives a nonzero PSD difference of resolvents in the reverse Loewner order, hence strict growth of the trace defining R_H, and therefore of the root under the stated transitivity hypotheses. For C₄ the equation reduces to 3a²+8a−4=0, yielding B=8√7/7. The supplied verifier was inspected, not run; the stated finite verification is supplementary.

## originality

PASS

The inspected sources establish the determinant interpretation, graph-design framework, corona spectral reductions, and other grounding transitions. None of the compared statements reduces to the exact unrestricted vertex-conductance support threshold and its sharp core-graph comparison for the one-leaf corona.

## value

PASS

The theorem identifies when a continuous unrestricted design must assign exactly zero conductance to the whole core, and when gains must move to both orbits. The zero-set decision is exact at the boundary, not just numerical, and the sharp clique extremum and strict edge-addition law reveal how the core graph controls the budget range of the sparse optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
