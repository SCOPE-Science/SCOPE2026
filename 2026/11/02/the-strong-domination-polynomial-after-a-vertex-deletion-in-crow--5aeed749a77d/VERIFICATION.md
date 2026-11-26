---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Deleting a₀ leaves b₀ and all aᵢ at degree n−1 and all other bⱼ at degree n−2. If b₀ is not selected, no selected B-neighbor can strongly dominate a missing aᵢ, so all of A′ is selected; that suffices, since n−1≥2 and a remaining bⱼ misses at most one member of A′. With b₀ selected, every missing aᵢ is covered, and respectively zero, one, or at least two selected aᵢ force all bⱼ, just the matching-index bᵢ, or none of the other B-vertices. The four disjoint contributions give the polynomial coefficientwise. At n=3 only A′ is minimum; for n≥4 the minimum is three, with (n−1)+C(n−1,2)+[n=4] possibilities. Substitution at z=1 gives the stated total. Direct independent enumeration over the residual adjacency and degree condition for n=3,…,7 matched every coefficient; for example n=4 gave (0,0,0,7,20,18,7,1) and the five totals were 13,53,225,945,3905.

## originality

PASS

The strongest inspected comparisons concern scalar stability, ordinary or other domination predicates, or different graph families. None evaluates or mechanically implies the all-size strong-domination polynomial of Kₙ,ₙ−M−v. This is a bounded best-of-knowledge assessment, not a priority guarantee.

## value

PASS

The crown is a natural matching-deleted complete bipartite family, and vertex deletion produces one high-degree B-vertex and asymmetric domination constraints. An exact all-cardinality polynomial answers more than scalar sensitivity, including the n=3 and n=4 boundary effects, the shapes and exact counts of minimum sets, and total-set counts. The elementary proof does not make the finer enumerator a substitution into a prior result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
