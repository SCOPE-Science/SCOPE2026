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

A direct equality-case certificate, without even requiring the symmetry averaging for the lower bound, confirms the proof. Let A be the total hub-edge weight, X the total weight from L to R, s=1−A/(2m), y=X/m, and U the classwise zero-sum subspace. The normalized trace of the compression to U is the mean peripheral diagonal s−y (each class diagonal contributes the same factor 1−1/m). The unit vector contrasting L and R has Rayleigh quotient s−2y. Consequently μ≥max(s−y,|s−2y|)≥s/3≥(2m−1)/(6m), since A≤1. At the proposed kernel the nontrivial eigenvalues are −1/(2m), −μ*, and +μ* of multiplicity 2m−2, so the bound is attained, also at m=2 where the two negative eigenvalues coincide. Equality forces A=1 and y=2s/3. The PSD operator μ*I−P+J has zero compressed trace on U, so it annihilates all of U. Testing classwise coordinate differences then forces the hub vector constant on each class, the cross block to have equal rows and columns, and every peripheral diagonal to equal μ*. Row sums identify the two constants on the hub edges and recover the claimed matrix exactly. The no-hub calculation is the same with s=1 and gives SLEM 1/3, attainable by edge weight 2/(3m). For m=1, J is feasible on K3 and is the unique zero-objective point; the U argument is not used. No sample of kernels substitutes for equality-case rigidity.

## originality

PASS

Credit the established complete-multipartite reduction and the complete-bipartite baseline, and give little novelty weight to solving the reduced two-weight optimum. What survives the prior comparison is the characterization of every optimal kernel on K_(1,m,m), including equality forcing zero hub holding and the loss of all asymmetric degrees of freedom. An earlier catalogued uniqueness theorem treats a different graph; a later weighted three-part result formally reproduces the explicit value outside its stated parameter range and does not resolve the unrestricted equality case.

## value

PASS

The principal value is equality-case rigidity in a natural multipartite FMMC problem: every optimizer, not just an orbit average, has identical weights, every allowed edge is active and the hub holding constraint saturates. These conclusions do not follow from existence of a symmetric optimum and clarify the degeneracy of the convex problem. The small numerical improvement over K_(m,m) alone would not justify the finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
