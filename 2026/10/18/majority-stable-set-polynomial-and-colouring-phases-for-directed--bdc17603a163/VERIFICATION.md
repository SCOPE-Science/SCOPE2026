---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

A selected vertex of layer i sees exactly x_(i+1) selected successors, hence admissibility is x_i=0 or x_(i+1)≤floor(m/2). Empty/nonempty weighted transition M=[[1,(1+z)^m−1],[1,B(z)−1]] counts cyclic layer words exactly once and Cayley–Hamilton yields recurrence. Each heavy layer forces empty predecessor; disjoint pairs bound selected total by floor(dm/2). Equality classifies cyclic matchings, yielding stated leading coefficients. Vertex-transitive averaging gives χ*=dm/floor(dm/2). Two colours are either everywhere balanced for even m or alternate monochromatic layers for even d; otherwise three suffice. Independent exhaustive subset-vs-occupancy comparisons covered 12 small (d,m) instances and their maximum coefficients; finite checks only corroborate unrestricted proof.

## originality

PASS

Previous general majority colouring results provide bounds and even-cycle existence, not the exact transfer-matrix polynomial, extremizer counts, or named-colour census on these cyclic complete-layer blowups.

## value

PASS

Complete natural family classification: enumeration of all stable sets, sharp fractional-integral gap, and combinatorially interpretable extremizer coefficients, beyond standard existence bounds. Valuable for testing majority colouring bounds on vertex-transitive digraphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
