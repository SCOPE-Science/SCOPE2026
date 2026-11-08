---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For the four-simplex on five vertices, 31 nonempty faces, an optimal Morse matching uses 15 incidence pairs and leaves exactly one critical vertex (Euler/Morse constraints). Rooting that vertex at zero converts the full S5 orbit question to S4 orbits of perfect Hasse matchings of the remaining 30 faces. The least-unmatched-mask recurrence lists each perfect matching once and no others, giving exactly 117837 candidates; orient every Hasse cover upward except matched edges reversed, test the resulting full directed graph for acyclicity (equivalently no closed Forman V-path). An independent C++ enumeration and the pinned distinct Python method confirm 76025 acyclic rooted matchings and S4 fixed counts 76025, 243, 21, 8, 1 for cycle types 1^4, 2.1^2, 2^2, 3.1, 4. Burnside numerator 76025+6*243+3*21+8*8+6*1=77616 yields exactly 3234 orbits. Matching stabilizer counts 74568 trivial,1368 transposition,60 double transposition,28 S3,1 S4 sum to 76025 and give 3107+114+5+7+1=3234 orbits. The explicit S4-fixed cone pairing verifies the final singleton. This is an exhaustive finite certificate for the whole finite five-vertex simplex, not partial sampling.

## originality

PASS

PASS: primary Scoville 2026 gives 380125 *labelled* optimal matchings (five times 76025) and Lin–Scoville gives the automorphism group S5, but neither determines the nonidentity permutation fixed-point counts, stabilizer classes, or 3234 orbits. The new invariant is the full orbit/stabilizer refinement, not an independently novel labelled census.

## value

PASS

PASS: Exact classification up to the full automorphism group of a natural first large simplex provides a nontrivial fixed-point table and symmetry spectrum, refining an existing labelled census. The numbers cannot be recovered from only the group order and labelled count; a complete finite exhaustive classification is mathematically useful without an all-n family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
