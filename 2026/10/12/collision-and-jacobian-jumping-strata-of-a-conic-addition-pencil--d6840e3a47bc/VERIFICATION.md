---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Frozen degree-seven f_t=(x²+y²−z²)(y−z)(x²−z²)(y²−txz) for all complex t≠0. Fixed conic Q has three tacnodes with line components; new C_t meets fixed lines and Q transversely generically, and Q∩C_t is governed by x²+t x−1 (discriminant t²+4). At t=±2i it has two additional A3 contacts; at t=±1 C_t passes an existing node creating one ordinary D4 triple. Bézout exhausts other potential collisions; Tjurina rows 22/23/24 follow. Source constructs exact Φ_r: S_r^3→S_{r+6}, r=3,4,5 with generic Q(t) ranks 30/43/56 and explicitly indexed minors; r3 pair gcd t^7 excludes nonzero t from lower syzygies, r4 pair gcd t^11(t²+4), r5 minor ∝t^15(t²−1)(t²+4)^2. Special ranks at t=±1 and ±2i as recorded. Independent exact SymPy reconstructions confirm at t=1 ranks 30,43,55; t=2 and3 ranks 30,43,56; t=2i over Q(i) ranks 30,42,54, so mdr=4 and dimAR4/5 correct in checked strata. Numeric samples are diagnostics; uniform no-other-parameter conclusion uses the source exact minor algebra and geometry, not samples.

## originality

PASS

Original Măcinic–Pokora Example 2.9 fixes only the single added conic t=1 and observes a four-syzygy result; its base curve already known free in Dimca–Pokora, neither is claimed new. The present exact complete complex t-stratification, two distinct collision mechanisms, and first graded syzygy jump loci are not stated or forced by those single-fiber examples. Search produced no matching full pencil theorem, but unindexed computations remain a risk.

## value

PASS

Varying the coefficient of the original conic added to a free conic–line arrangement is a canonical deformation, and fully locating geometric collision and Jacobian jumping values in the family is a worthwhile structural classification. The mdr=4 non-(nearly-)free obstruction on every smooth fiber and exact jump dimensions are potentially reusable boundary data, not an arbitrary finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
