---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

The inspected Black–De Loera primary text gives Q vertices exactly the signed permutations (2,1,…,1), and Q facets exactly <s,x>≤k+1 for sign s∈{−1,0,1}^d, k=|supp s|≥1. Thus every Q vertex has squared norm d+3, yielding Q minimum covering radius √(d+3), and every facet has origin-distance (k+1)/√k with binom(d,k)2^k faces and minimum2. By polarity, each Σ facet corresponding to a Q vertex has origin-distance 1/√(d+3), all d2^d touch the same ball; each Σ vertex is s/(k+1), norm √k/(k+1) and max1/2 at support1. Differences of squared shell radii show strict increase/decrease. Opposite supporting facets and antipodal extreme vertices show the origin is the unique relevant Euclidean extremal center in both bodies. Every dimension d≥2 follows symbolically; inspected verify.py enumerates d=2..7 and LP facets only corroboratively.

## originality

PASS

Black–De Loera give full vertex/facet coordinate descriptions and combinatorial equivalence for the canonical signohedron, which imply the metric identities after normalization, but do not directly state the exact d-shell metrics, universal all-facet tangency, their multiplicities as metric shells, or uniqueness of the Euclidean centers. Other Resultary radial-shell work is for signed Birkhoff and symmetric edge polytopes; these differ from the cube-plus-cross-polytope Minkowski sum and its polar. Thus the contribution is an explicit metric package derived from known combinatorial data, not a claimed new polytope realization.

## value

PASS

The canonical signohedron is a natural high-dimensional combinatorial polytope; exact in/circum-radii, simultaneous tangentiality of all exponentially many facets, multiplicity-resolved shells and center uniqueness provide a complete Euclidean geometric invariant in its canonical realization. These formulas are short once the parent vertex/facet structures are known but organize nontrivial uniform geometric information of a natural object, rather than an arbitrary isolated small numerical case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
