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

The open common-neighbor facet criterion on the 21 unordered pairs generates exactly 18,495 augmented faces (18,494 nonempty) with the specified full 10-entry face vector. Independent reconstruction of greedy deterministic vertex toggles yielded 9,121 augmented matching pairs, including the empty-face match; after deleting it, exactly one critical vertex, 246 critical three-cells and seven critical four-cells survive. Independently built all 98,805 ordinary Hasse incidences and topologically sorted the reversed matching graph on all 18,494 ordinary faces. Signed integer gradient-path recursion on the critical 4-cell boundaries gave seven identically zero columns in the 246x7 Morse differential, not merely zero mod2. The 3-skeleton is a wedge of S3s; by pi3/H3 Hurewicz each 4-cell attaches nullhomotopically, so full integral wedge follows. Independent mod2 simplex-boundary ranks agree exactly (20,190,1000,2534,2646,1764,756,189,21). Pure dim9 with homology in dims3 and4 is non-shellable. This is an exact finite homotopy classification, not a theorem for all T_n.

## originality

PASS

The public exact T7 calculation gives precisely F2 Betti numbers 246 and 7, not integer attaching degrees or homotopy type. A zero integral signed Morse matrix genuinely adds information. Shukla treats max degree≤3 and 4-regular circulants (T7 is 10-regular); Braun–Vega treats Hajos operations; Goyal–Shukla–Singh considers clique rather than open-neighborhood complexes; Fröberg treats Stanley–Reisner rings of path/star/complete/multipartite graph neighborhoods, not T7 homotopy.

## value

PASS

T7 is the first natural triangular graph with established mod-two neighborhood homology in two degrees; earlier F2 data do not rule out integral 2-torsion, even attaching degrees or unstable higher structure. The full integral zero attachment matrix resolves the motivated homotopy question, yielding a complete two-dimensional sphere-wedge classification and concrete non-shellability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
