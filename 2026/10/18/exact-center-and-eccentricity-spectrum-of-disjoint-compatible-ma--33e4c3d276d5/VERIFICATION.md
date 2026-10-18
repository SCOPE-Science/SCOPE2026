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

# Reproducibility

Extract `verify_chord_masks.py`, `verify_dyck_dp.py`, `verify_chord_masks.stdout` and `verify_dyck_dp.stdout` from the same record. Run both Python programs without inputs or third-party packages. Their recorded outputs must match the new process outputs, including the terminal `VERIFY_OK`. Standard Python 3.11 or later suffices.

The first program enumerates all noncrossing perfect matchings by interval recurrence, constructs adjacency using full forbidden-chord bitmasks, and runs breadth-first search from every vertex of the largest component. The second independently enumerates Dyck words and generates neighbours by recurrence over all admissible replacement chords. The two source/adjacency constructions agree on \(4862\) total configurations, \(8677\) edges, the component-size distribution, the two ring centers, the six eccentricity counts, radius \(10\), diameter \(15\), and the exact canonical adjacency SHA-256 `81631930f2db82172b1509c4f558f1933749e4b263323c00c58fdcae6eed97cb`.

The independent enumeration mechanisms reduce the likelihood of common implementation mistakes. The mathematical certificate of completeness is the chord-splitting/Dyck-path bijection and the exact strict-interleaving crossing criterion given in `RESULT.md`; shortest-path correctness follows from exhaustive breadth-first search, not from the recorded output alone.

This finite verification does not establish any formula for \(k\ne9\), does not prove bibliographic priority, and is not an independent external scientific audit.
