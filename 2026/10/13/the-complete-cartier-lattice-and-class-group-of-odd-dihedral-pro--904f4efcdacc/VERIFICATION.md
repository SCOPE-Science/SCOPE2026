---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For this complex action all nonidentity rotations fix exactly the four corners because 2 is invertible modulo n. Each reflection fixes four noncorner points; no two distinct reflections can fix the same point since their product is a nonidentity rotation. There are two corner orbits and four reflection orbits, each reflection tangent action being (−1,−1). Removing the nonfree points gives an étale torsor. Removing finitely many points preserves the class group on the normal quotient and the equivariant Picard group upstairs (line bundles and their equivariance extend uniquely on the smooth surface). Hence Cl is the equivariant Picard group. The lifts diag(ζ^h,ζ^(−h)) and diag(ζ,ζ^(−1)), h=(n+1)/2, with the swap, give the degree-one generators; the kernel is the character group C₂ of odd D_n. For the Cartier subgroup one must kill inertia on every fiber. The corner congruences ha±b=0, along with their negatives modulo n, imply n divides both a and b. The reflection eigenline pairs (+,+), (−,+), (+,−), (−,−) force ε=0 and a,b even. Conversely these conditions kill every stabilizer, so descent is sufficient and the sublattice is (2nZ)² with zero torsion coordinate. The sign twist has precisely the asserted local obstructions. The invariant functions on each factor have degree 2n, so the two descended ruling line bundles give the basis and (n−4,1) is primitive.

## originality

PASS

Prior statements located for this exact quotient describe its construction, local singularities, ruling maps, polarization or joint branch geometry. They do not give the global integral Weil group, the exact embedded Cartier lattice, or the sign twist's descent behavior. The general equivariant class group theorem does not turn those geometric data into the stated answer without the splitting and simultaneous local restrictions computed here.

## value

PASS

This is the full integral Cartier obstruction for a naturally occurring family of Seshadri-constant examples. In particular the result determines which Weil classes are honest line bundles and distinguishes the reflection obstructions from the cyclic ones. It identifies all polarization divisibilities in the two ruling coordinates, rather than just producing known Cartier classes or recomputing the singularity types. The local-to-global character computation is substantive for this exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
