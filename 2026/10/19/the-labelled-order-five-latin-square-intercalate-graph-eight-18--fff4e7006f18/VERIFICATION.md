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

Independently enumerated the 56 reduced squares by cell-level row/column bitmasks. Each labelled square has a unique normalization (symbol-normalize row zero and sort the remaining rows by column zero), so expansion by 24 row orders and 120 symbol bijections is exhaustive and injective. Intercalates are exactly the 2-cycles of the relative symbol permutation for a pair of rows. Using this switch generator, BFS found 17,280 isolated squares and eight 18,000-square components, each of degree four, giving 288,000 edges. The parity triple is invariant because each move transposes two permutations in each coordinate's collection; direct counting gives 4,320 isolates and two mobile components in each of the four listed parity classes. Normalizing all choices of first row and column permutation from one representative of each type gives exactly the 6 and 50 reduced-square orbits. Isotopy acts by graph automorphisms and is transitive on all mobile states, hence the stabilizer of each component is transitive within it. Independent BFS from one root per component gives the claimed 14 coefficients with final nonempty shell 13, establishing both radius and diameter for each such component. Independently reconstructed every certificate byte and matched the frozen SHA-256 ce71d8163426d2c0d139614f33225224948d267553e76aa2ff6cda7bc5c556f6.

## originality

PASS

Credit the known square and isotopy counts, parity invariance and parity constraint, and the known four intercalates on the non-group type. The inspected primary switching paper addresses the quotient and does not give the labelled reachability census or sharp metric profile. Two distinct catalogued records reproduce core numerics, but their recorded dates are later; these are genuine equivalences or reuse, not demonstrated earlier coverage. Pass the labelled component structure and distances, not the precursor results.

## value

PASS

This is the first order singled out in the classical switching study where a class can self-switch by an intercalate but the order-five quotient on distinct classes is edgeless. The labelled problem is therefore substantive: even with a single mobile isotopy orbit, the moves split every allowed parity into two distinct mobile components, and the sharp worst-case switch count between reachable mobile states is 13. These are useful reference data for testing proposed reachability invariants and comparing enlarged move sets; the later chamber study uses the intercalate-only census as just such a baseline.

The dated certificate retains the supplied scientific assessment, sources and limitations.
