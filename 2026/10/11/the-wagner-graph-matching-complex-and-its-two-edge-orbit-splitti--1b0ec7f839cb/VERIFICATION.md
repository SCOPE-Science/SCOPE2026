---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Independently constructed W as eight cycle edges plus four antipodal chords, and enumerated the full ordinary matching complex (12,42,44,7), 105 faces. Independently enumerated edge-deletion and endpoint-deletion complexes for cycle edge (0,1): (11,35,33,5), 84 faces and (7,11,2), 20 faces; for rung (0,4): (11,35,33,4), 83 faces and (7,11,3), 21 faces. Replayed exact five toggle orders from assigned verify_wagner_morse.py, obtaining pair counts 49,40,8,39,9, and complete Hasse cover counts 244,189,28,185,31. Exhaustive directed-DAG topological sorts passed for all five, with critical cells one 0+6 2, one 0+3 2, one 0+3 1, one 0+4 2, one 0+2 1, respectively. Forman gives all five integral homotopy types (no ambiguous attaching maps). Dihedral translations/reflections are transitive on each edge orbit. The matching-complex deletion-link vertex cofibration has inclusion wedge of circles -> simply connected wedge of 2-spheres, hence is nullhomotopic, giving both 3+3 and 4+2 splittings. Finite-field homology is only corroboration, not basis for torsion assertions.

## originality

PASS

The full-graph result M(W)≃wedge^6 S² is ALSO in a distinct indexed same-date SCOPE paper (Wagner-graph matching complex ... wedge 6 S²); that component is credited as prior coverage and not counted as new. The present claim adds a complete classification of both dihedral edge orbits, their deletion/link homotopy types and two distinct null-attaching decompositions. The published standalone full-graph theorem contains no such orbit data, so it does not imply these refinements. Agarwal–Basak arXiv:2608.30601v2 Main Theorem 1 and Theorem 21 compute Ind and perfect-matching (extendable) complexes, and Problem 26 p17 explicitly proposes ordinary matching complexes. Barmak gives general claw-free connectivity and Bayer–Jelić Milutinović–Vega’s outerplanar theorem excludes the nonplanar W. Searched line-graph independence and graph aliases plus Resultary; found no indexed complete orbit decomposition. Genuine residual unindexed-source risk remains.

## value

PASS

Two inequivalent natural edge orbits of a canonical nonplanar cubic graph have different exact deletion/link topology yet recover the same full six-sphere wedge in distinct ways. This is structural information useful for topological recurrences, edge-orbit comparisons and the open Möbius-ladder ordinary-matching program in Agarwal–Basak Problem 26, not just duplicating the previously published full-graph Betti number. No all-Möbius-ladder formula is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
