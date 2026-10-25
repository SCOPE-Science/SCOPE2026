---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The cited WHB duality sends an expansion of the fixed product ∏C_(n_i+1) to independent monotone Ferrers blocks on disjoint dual chains. Nonzero block endpoints u,v have exactly binom(u+v−2,u−1) interior threshold fillings. The active graph within one block is connected through the first source and final target point, even in diagonal blocks; the overlap graph H of endpoint supports therefore gives its union-components. Remaining uncovered dual vertices number Σ_i max(0,n_i−U_i−V_i), proving Boolean congruence rank I+κ(H) via Theorem 5.10. Direct independent enumeration of all relations on (1,1) gives {1:12,2:4} and on (2,2) gives {1:1213,2:70,3:12,4:1}; these agree with the formula but are not proof for all vectors. For uniformly random s×t Ferrers blocks, the binomial ratio for at least half zero rows is at most exp[−min(s,t)/4]; similarly for target columns. Union bound over both tails in k² blocks ensures overlapping longer-than-half prefixes and suffixes, no isolates, and connected H, hence simplicity probability ≥1−2k² exp(−m/4). Boundary k≥2,n_i≥1, named operations and fixed-k complexity are respected.

## originality

PASS

PASS on a qualified best-of-knowledge comparison: Celani–Nagy–Zuluaga Botero cover general duality and congruence representation, but the all-factor-size weighted overlap rank polynomial and uniform generic-simplicity tail law are separately derived. Finite Ferrers counts alone are old, and the 2015 one-connective count is not claimed absent from literature without reading the full paper.

## value

PASS

Simplicity and full congruence-rank spectra are intrinsic algebraic invariants for subdirect decomposition. A compact exact endpoint-weight generating function replaces an enormous enumeration of operations for any fixed factor count and yields quantitative generic simplicity across a natural infinite class of distributive lattice reducts; these are mathematically motivated objects, not arbitrary tiny tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
