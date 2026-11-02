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

For p>=5 Fermat quartic is smooth; the 12 lines of coordinate-pair type X−αY, etc α^4=−1 and the 16 X+μY+νZ, μ^4=ν^4=1 have contact divisors respectively 4P or 2P+2Q, and exhaust the 28 geometric bitangents (odd theta-characteristic count in characteristic ≠2). Lifting all coefficients to Z[zeta8], independently enumerated all 3276 3×3 determinants and recomputed exact absolute norm histogram, with nonzero norms in {1,2,4,8,9,16,17,32,36,64,256,400} containing only prime divisors 2,3,5,17. A nonzero determinant cannot vanish after reduction at p>=5 except p=5,17, because its norm would be divisible by p. Every coefficient/root is defined over F_{p²}; independently enumerated all 378 line-pair projective intersections in exact F25,F49,F289 arithmetic, directly evaluated 28 incidences per point, and obtained p5 (240,16,15), p7 (288,0,15), p17 (144,48,15). The generic p7 pattern plus determinant invariance covers infinitely many nonexceptional p; finite field runs are exhaustive for exceptional models, not extrapolation across all primes. No >=5 concurrence; weighted pair identity 378 holds.

## originality

PASS

PASS best-of-knowledge for prime-dependent exceptional triple-concurrence of the Fermat/Dyck quartic bitangent arrangement. Janasz–Pokora–Zieliński Prop.3.2 explicitly gives over C 288 ordinary doubles and 15 quadruples; it supplies the generic baseline but does not imply that exactly p=5,17 produce triple points over algebraic closures. Ottaviani supplies classical 28-bitangent/theta background, not the cyclotomic integral determinant norm sieve in accessible material. No matching finite-field exceptional-prime incidence table appeared in Resultary or targeted published searches. Potential archival positive-characteristic arrangement computations remain a priority risk.

## value

PASS

The Fermat quartic with its 28 bitangents is a canonical classical plane-curve arrangement. Its characteristic-dependent singularity profile is a natural arithmetic invariant, and the complete determinant-norm sieve exactly locates the two bad primes instead of giving isolated finite-field examples. The resulting distinct (n2,n3,n4) profiles answer a meaningful reduction-of-incidence question and extend the known complex arrangement picture, without purporting to classify all quartics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
