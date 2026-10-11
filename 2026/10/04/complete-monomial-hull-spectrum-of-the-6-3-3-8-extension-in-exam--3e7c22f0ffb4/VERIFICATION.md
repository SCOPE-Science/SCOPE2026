---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The exact GF(8) arithmetic and generator matrix were independently reconstructed using the polynomial relation defining the field. The baseline code has rank 3 and hull dimension 1. For a monomial transform, the Gram rank depends only on diagonal coordinate squares, and a common nonzero scalar can be normalized away, leaving exactly \(7^5=16807\) scalings. Independent exhaustive Gram-rank enumeration reproduced hull counts 14685, 2091, 31, 0 in dimensions 0,1,2,3 respectively, so the attainable spectrum is exactly {0,1,2}, the maximum is 2, and no monomially equivalent code is self-dual.

## originality

PASS

The primary construction paper gives the exact Example 5.6 generator and certifies only the displayed representative's one-dimensional hull. Chen introduces maximal hull dimension and general hull-variation methods, but those general results do not determine the attainable hull dimensions of this particular code. The exact 16807-scaling profile, maximal hull dimension 2, and impossibility of a self-dual monomial equivalent were not found in the checked sources.

## value

PASS

Maximal hull dimension is an explicitly motivated invariant in the equivalent-code literature, and this source paper presents the code as a concrete worked example. Determining the full attainable spectrum and proving that self-duality is impossible in its monomial class is a natural exact invariant of that named object, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
