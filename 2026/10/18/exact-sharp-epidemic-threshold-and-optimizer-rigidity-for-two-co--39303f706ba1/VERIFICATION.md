---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: For each n≥3 with nonempty A,B, strictly positive normalized fractions π and positive class row rates a,b, the detailed-balance similarity makes M self-adjoint in weighted L2(π). Its class-constant Rayleigh compression equals H(t)=diag(a,b)−t vv^T, v=(P^{-1/2},−Q^{-1/2}), where reciprocal cross flux 0≤t≤min(Pa,Qb). The largest eigenvalue L(t) decreases strictly for a≠b by equality characterization of the rank-one Loewner perturbation. Every matrix therefore has ρ(M)≥L(t*). The explicit bipartite-positive, within-class-diagonal M* obeys row sums, weighted reciprocity, is irreducible, and has an everywhere positive lifted quotient eigenvector realizing L(t*). Equality of the global and compressed Rayleigh maxima forces the lifted eigenvector to be an M eigenvector; x≠y implies all cross-class row totals constant at t*/P and t*/Q; conversely these totals give an everywhere positive Perron eigenvector. For a=b, constant row sums force ρ=a. Independent rational four-type witness and numerical symmetric eigenvalue checks support finite instances, not infinity.

## originality

PASS

PASS best of knowledge: the relevant 2026 Bizzotto–Ball–Britton paper already formulates reciprocal contact-rate optimization for arbitrary types by SDP and gives a sharp two-type formula, but the audited theorem is an all-n two-rate-per-individual-family closed-form reduction, irreducible attainability and NECESSARY-and-sufficient lumpability of every minimizer. The general SDP encodes but does not state/automatically imply this rigidity theorem. The antecedent rank-one Rayleigh bound and equitable partition are not claimed new. Read the paper's Theorems 3.2 and 3.6 and arbitrary-type optimization section, and distinguish result-level implications; residual risk of an unindexed matrix reduction remains.

## value

PASS

PASS: exact epidemic threshold under unequal population fractions and fine class subdivision solves a motivated spectral extremal problem, and classification of all extremizers is structurally stronger than the previously known two-type computation. It is useful for checking whether group refinement affects attainable epidemic thresholds; not merely rewriting a 2×2 formula because lumpability is proved compulsory across all n≥3.

The dated certificate retains the supplied scientific assessment, sources and limitations.
