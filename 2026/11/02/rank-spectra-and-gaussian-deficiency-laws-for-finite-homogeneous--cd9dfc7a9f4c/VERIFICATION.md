---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

By the finite homogeneous graph classification, a graph or complement is t disjoint equal-sized cliques or an exceptional C5 or 3×3 rook graph. Occupied cliques inject into distinct target cliques; this yields R=Σ_s binom(t,s)(t)_s(B_n(z)−1)^s with B_n=Σ_j binom(n,j)^2 j! z^j. Complement induces identical partial isomorphism monoid. For exceptions, orbit-stabilizer counts each induced-domain isomorphism: C5 coefficients [1,25,100,100,50,10], rook [1,81,1296,5616,9072,9072,6048,2592,648,72], total 34,498, independently verified by explicit group actions on all subsets. For fixed t, s=t dominates as T_n=n!L_n(−1)→∞; local deficiency weights binom(n,j)/j! have ratios (n−j)/(j+1)^2, yielding (J_n−sqrt(n))/n^(1/4)⇒N(0,1/2). Independence of t components implies total variance t/2. Classical Laguerre asymptotic gives stated total-size factor t!(n!)^t e^(2t√n−t/2)/(2√π)^t n^(t/4).

## originality

PASS

Finite homogeneous graph classification, partial permutation rank counts/laguerre asymptotic, and C5 values are prior work. Full primary paper on general graph-partial-automorphism inverse monoids was inspected; its focus is monoid structure and Green classes, not the complete homogeneous graph rank polynomial and Gaussian deficiency. The combined all-homogeneous rank enumerator and fixed-t limit appear new at best knowledge; potential equivalent PAut enumeration remains a priority risk.

## value

PASS

A complete rank spectrum for every finite homogeneous graph, including the nontrivial nine-vertex rook exception, is a natural complete inverse-monoid classification. The Gaussian deficiency law links these exact finite counts with a nondegenerate asymptotic invariant; not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
