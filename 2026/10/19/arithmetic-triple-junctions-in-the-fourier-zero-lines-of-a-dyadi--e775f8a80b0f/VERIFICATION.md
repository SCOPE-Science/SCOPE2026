---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The compactly supported measure has a product of masks whose tail is nonvanishing and analytic locally: the translated compact complex neighborhoods have a summable bound on deviations from one. For the mask geometry, a nonzero sum of two unit vectors determines their unordered pair, since their product is the sum divided by its conjugate; a vanishing total of four unit vectors therefore pairs them antipodally. This yields the three known line families. At one scale two pivots occur only for the phases (−1,−1,+1); that fixes all coordinates to integers and yields exactly the equal-low-valuation condition. Across k<l, the higher pivot is +1 at k, forcing both others to be −1 there. The higher factor can thus vanish exactly when the nonzero high coordinate and the difference of the low coordinates have equal finite valuation; neither low coordinate can pivot again, and the high coordinate can pivot at only one scale. The three distinct directions are the permutations of (0,1,1), with absolute determinant 2. A pivot derivative of each vanishing factor is nonzero, so Taylor orders add exactly as one or two, even when the real zero lines of a single factor cross. For a specified high coordinate, the probability of a junction with low valuation a is 2^(−3a−3). For a triple the high valuation is a+j with j≥1, and the odd-part difference has valuation j with probability 2^(−j), giving weight 2^(−3a−2j−3). These sums, times three choices of high coordinate, give 3/7 and 1/7. Fixed moduli equidistribute in the centered cubes; discarded large-a or large-j cases require a coordinate in a high power-of-two divisibility class, bounding their upper density by a vanishing geometric tail. Zero high coordinate and coincident low coordinates do not create triples. A separate exact bounded modular recount (bounded_junction_check.py) reproduced (junctions, triples)=(1500,528) at R=7 and (108252,37200) at R=31. It corroborates the lattice arithmetic, not the unrestricted real geometry or the limiting densities. The supplied verify_tetra.py was inspected, not executed.

## originality

PASS

Credit the prior real zero-locus formulas to Dutkay–Jorgensen and Li. Also credit exact mathematical overlap of the indexed even-scale cancellation theorem at b=2: it covers both lattice densities and the at-most-two-level bound on the lattice, and its congruences recover the lattice two-scale test. This is genuine overlap regardless of catalogue date. The frozen junction-and-order theorem as a whole is distinct: it relates real line incidence, exclusions off the lattice, analytic Taylor order, and transversality to the arithmetic. The general index result does not address that real local classification, and the inspected earlier primary zero-locus passages do not resolve the cross-scale incidence analysis or census. This passes the combined theorem, not a standalone claim of originality for either density number, the factor count on the lattice, or the zero-line formula.

## value

PASS

The equal-weight dyadic tetrahedral measure is a standard affine self-similar object, and its known Fourier zero locus does not distinguish ordinary zeros from intersections or Taylor multiplicity. A complete real local classification explains why a two-line crossing can still be first order, identifies exactly where a second factor creates a transverse triple, and makes those singularities countable on the lattice. The geometry/order correspondence is the value beyond the already indexed lattice density calculation; a replay of those density numbers alone would not suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
