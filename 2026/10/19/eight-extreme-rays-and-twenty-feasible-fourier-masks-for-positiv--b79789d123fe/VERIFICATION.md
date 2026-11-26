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

Restriction to H is onto with fibers of size 2^(d-3); the transform of a zero extension is the pullback of the local transform. Locally the three independent equality rows are Walsh rows 0, 1, 2, fixing the sum and two spatial zeros. The polytope is compact and has relative dimension five (the strict full-mask witness). At a vertex five independent inequalities must be active modulo those three rows; the supplied exact certificate exhausts the possible five-element active sets. Nonnegative coordinates cannot cancel under convex combinations, in either domain, so a mask and strict positivity throughout the prescribed spatial support occur precisely as the unions of the supports of a nonempty subset of vertices. An independent exact calculation agrees on all eight normalized vertex vectors, not just masks, and the full twenty-mask table. The eight rays are of the relaxed nonnegative cone with the two specified zeros, not of a closed cone requiring all six other sites to be positive.

## originality

PASS

The inspected strongest sources give support-size bounds and diagrams, general dual-cone language, or indicator magnitudes for the same geometry. They do not give the normalized primal vertices or the attainable positional masks when positive weights vary subject to both constraints. No exact matching record was found in the bounded comparison.

## value

PASS

Two simultaneous positivity constraints make this a natural exact support problem; cardinality bounds cannot tell which spectral zeros may coexist. The full classification for the six-point Boolean orbit gives reproducible witnesses and obstructions for positional deletion patterns. The eight normalized vertices are enough to decide any candidate pattern for the entire lifted family, so the result contains more structure than a finite minimum or a list of example spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
