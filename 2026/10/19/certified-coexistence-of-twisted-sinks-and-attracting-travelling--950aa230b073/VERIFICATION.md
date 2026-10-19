---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the travelling three-cycles

Run `python3 verify_triangle_cycle.py`. The supplied standalone Python file uses exact `fractions.Fraction` interval arithmetic for all theorem-critical inequalities: Machin-series bounds for pi, Taylor bounds for sine/cosine, the interval Newton contraction on an explicit box, and full-box trace/determinant Schur inequalities. Every proof-critical comparison is rational and checked by assertions. It independently verifies the non-singular rational approximate inverse, and tests the strict separation of the three coordinates.

A successful run reported: `PASS: exact rational interval Newton contraction and unique fixed point in box`; `center defect upper bound: 1e-12`; `contraction bound: 7.914e-08`; `trace enclosure: [-1.554694333705, -1.554694151305]`; `determinant enclosure: [0.705069729594, 0.705070150348]`; `PASS: all three strict quadratic Schur inequalities`. The decimal output is diagnostic formatting of exact rational inequalities, not floating-point evidence.

The analytical proof additionally checks that the edge-phase map is the quotient of the oscillator network, that the cyclic permutation commutes with the map, that the certified period divides three but is not one, that sign-reflected orbits are disjoint, and that the fixed twisted multipliers are strictly below unit modulus. The computation is finite but certifies a genuine real root and two-dimensional local stability by interval enclosure; it does not enumerate all possible attractors.

Independent audit: not performed.
