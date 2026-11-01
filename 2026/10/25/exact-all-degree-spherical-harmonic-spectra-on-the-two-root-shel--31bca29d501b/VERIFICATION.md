---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The normalized B_n root set has 2n² points in antipodal pairs; addition kernel is p_{n,l}(x·y) with p_n,l normalized at 1. Coordinate sign characters split the sample module, and Gegenbauer parity annihilates one n²-dimensional half. Odd surviving singleton-character blocks yield scalar 2−4v and 2x2 T_o eigenvalues; even surviving two-character blocks yield scalar 2(1−u), while trivial sign character block is decomposed using unsigned complete-graph incidence MM^T=(n−2)I+J into ker M scalar, n−1 standard T_s blocks, and constant T_c. Dimensions sum to 2n². Symbolic n-dependent Gegenbauer evaluations show degree5 all compatible branches positive and degree6 exactly one zero in T_c; independent direct full Gram numerical spectra checked n=3..6, l=0..8, with max discrepancy 4.5e−14. Universal result rests on representation/incidence decomposition and symbolic determinants.

## originality

PASS

Complete spectrum on the non-transitive union of short and long B_n root orbits, including cross-shell 2x2 blocks and all-n 5/6 rank anomaly. Established spherical addition formulas and invariant harmonic polynomial Gram determinants do not themselves state this mixed point-evaluation spectrum.

## value

PASS

Natural nontransitive two-shell root sampling problem. Gives entire exact-degree spectrum, optimal frame singular values, and an unexpected all-dimension parity-compatible rank drop between degrees 5 and 6. Cross-shell mixing is essential; no arbitrary slice or trivial substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
