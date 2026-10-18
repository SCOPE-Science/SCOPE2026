---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Fresh independently written Q(sqrt3) arithmetic rebuilt all twelve side lines, 66 seed intersection points, 913 candidate joins and exactly 49 richness>=4 lines. All 1176 pairs give char-zero histogram (204,96,6,24,6,12,1), total 349 and Σ choose(m,2)n_m=1176. Primitive integral triples have coordinate-norm gcd and pair-cross coordinate-norm gcd supported only at 2,3, ensuring line survival/distinctness at p>=5. Independently enumerated all 18424 unordered triples: 1120 zero determinants; 60 distinct nonzero determinant norms, max 1944, combined prime support {2,3,11,13}. Thus no new triple dependencies for p>=5 except 11,13; zero dependencies persist. Reductions at both roots sqrt3=±5 mod11 and ±4 mod13 give precisely the stated profiles, with 133 and 169 points and weighted pair counts 1176. p23 split-field control gives original profile. Exhaustiveness over determinant norms proves all p>=5, not sampled primes.

## originality

PASS

Pokora--Roulleau gives the arrangement and its characteristic-zero incidence; the same primary text does not compute bad primes. Exhaustive quadratic-integer determinant norm support and two different positive-characteristic multiplicity baskets are new arithmetic degeneration data for a canonical rigid configuration.

## value

PASS

Good/bad reduction of a rigid, well-studied 49-line arithmetic arrangement is a natural integral-matroid invariant. Determining precisely which two odd primes alter its geometric intersection lattice, with complete multiplicity distributions, is a mathematically useful exact arithmetic classification; it distinguishes modular degeneration from characteristic-zero freeness/rigidity. This involves a genuine all-primes finite determinant norm certificate, not arbitrary sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
