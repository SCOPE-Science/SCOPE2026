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

The proof is uniform for all n≥7. After choosing two projected columns at distance two, the intersection of their closed cyclic radius-two neighborhoods is just the three-column interval. If the extreme columns are occupied, each must have the same single row and the possible middle vertices lie within one row step, giving a diamond. For two adjacent columns, a singleton yields a diamond; with at least two distinct rows in one column, their closed radius-one row neighborhoods have at least two common points only for an adjacent row pair, and then the intersection is precisely that pair. Applying the constraint in both directions gives a square. One column contributes the octahedral clique complex C6 squared, whose eight triangles consist of six consecutive ones and the two stated parity triangles. On the diamond/square base, an opposite arm pair has a unique midpoint and lies in no other generator. Matching its remaining cofaces with or without the center in descending cardinality proves freeness: four pairs for N–S and another three for W–E, after discarding cofaces already paired through N–S. The diamond remnants are faces of squares. Each square's two removals are then free because a chosen square diagonal lies in no other square, leaving the periodic diagonal triangulation of the torus. There are 54n pairs, all protecting nearest-neighbor meridian edges. Every parity triangle meets the base exactly along its boundary; replacing each length-two jump by two unit edges through its consecutive diamond triangle proves a single primitive meridional winding. After transporting these attachments along the base equivalence, choose the torus CW model and attach all 2n disks along its meridian edge. The meridian plus its first new disk is a contractible CW subcomplex; its quotient is a homotopy equivalence, leaves the other circle, and makes the old commutator cell and the remaining 2n−1 cells attach trivially. This proves the integral homotopy claim, not just the homology ranks. The inspected frozen verifier and verification_output.txt concern n=7,…,11 only; the local free-face and meridian arguments, not those finite checks, certify the infinite range. No other width, scale or continuum-torus model is implied.

## originality

PASS

Best-of-knowledge pass assessed for the frozen finding, not a claim that this result is absent from the present catalogue. The same theorem is now explicitly covered by a separately dated October 25 record and is also implied by a broader October 25 phase diagram. Neither inspected record demonstrates pre-existing coverage of the October 18 finding; independence, derivation, and priority beyond those displayed catalogue dates are not established. The strongest retrieved prior public sources treat squares or individual cycle factors, not this rectangular regime.

## value

PASS

At the first nontrivial graph-metric scale, width six is the last cycle width with nonconsecutive planar clique attachments. The structural proof explains why two exceptional triangles per column kill one of the two torus circles while making 2n two-spheres, a qualitative and integral statement not obtained from the nearest square case, factor alone, or computed Betti numbers. This is a natural infinite transition family with a reusable local description, not an isolated finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
