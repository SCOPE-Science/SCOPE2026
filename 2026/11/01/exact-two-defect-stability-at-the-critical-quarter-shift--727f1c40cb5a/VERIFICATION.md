---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Choose the positive-shift Fourier columns as an orthonormal basis and replace exactly two by corresponding negative-shift columns. The Gram matrix is an identity block plus a 2-column cross block L, hence its minimum is 1−||L||=1−sqrt(1−s_min(K)^2) for the two removed reference coordinates K. Geometric-sum evaluation yields |K| entries d,b,c and negative off-diagonal phase product, so s_min(K)=[sqrt(4d²+(b+c)²)−|b−c|]/2. For p=3, L has one row; the same singular-value identity still applies. With y=sin²g and v=y/(sin²β−y), the derivative F_y′(v)<0 follows from a positive quadratic with negative discriminant; v decreases as shorter separation grows, proving unique adjacency minimizer. d=1/(p sin g) and q=1/(3−4sin²g) increase with g, giving strict decrease of the adjacent lower bound as p increases and stated limit. Independent direct eigenspectrum computations for all separations p=3..30 matched the formula. Finite matrices corroborate, not prove, all-p claims.

## originality

PASS

Vellucci–Samad arXiv:2610.31956 introduces the auxiliary periodic shifted-sinc Fourier reduction and states an adjacent/contiguous-block minimizer as Conjecture 7.4, with a special p=3 calculation. The current proof resolves exactly the two-minority case at all p and an exact uniform lower constant, not their general conjecture. Pan and Batenkov et al conditioning papers concern broader matrices but do not give the identical finite sign-specific exact minimax theorem in inspected sources.

## value

PASS

The fixed-two-defect subclass is the first natural nontrivial geometry-dependent slice of a declared contiguous-block conditioning conjecture. The explicit separation profile proves a sharp defect count/stability boundary: two minority classes remain uniformly stable at the critical quarter shift even though unrestricted patterns can collapse. It is an all-period structural classification, not an arbitrary instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
