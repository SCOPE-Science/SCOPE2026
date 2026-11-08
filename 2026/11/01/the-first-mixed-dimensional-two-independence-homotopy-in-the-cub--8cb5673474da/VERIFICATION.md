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

Two exactly equivalent membership predicates (maximum induced degree <=1, forbidden center-with-two-neighbors triple) exhaust each of 2^(2^d) vertex subsets through d4. Independent enumeration reproduced d4 3054 nonempty faces and dimension f-vector (16,120,464,964,960,440,80,10). The inspected complete verify.py constructs an acyclic discrete Morse matching, checks all 13568 directed Hasse incidences via topological sort, leaves 1 zero-cell, 16 three-cells and a single four-cell. Signed exact integral projection of the single critical 4-cell 0x4a30 to 16 critical 3-cells is identically zero. Its 3-skeleton is wedge^16 S3 and Hurewicz gives pi3~=H3, making the attaching map null and proving the asserted integral mixed wedge, not merely mod2 Betti agreement. Our independent bounded computation fully enumerated faces but the complete supplied Morse projection was source-inspected rather than separately run.

## originality

PASS

Taylan P3-devoid paper classifies paths, cycles and forests, not Q4; Deshpande–Singh higher-independence formulas cover complete multipartite, fully whiskered, path/cycle/tree graphs, none the four-cube; chordal theorem cannot apply since Q4 has induced squares. Q4 ordinary independence, Čech and Rips complexes have different face rules, so even same graph and homological dimensions do not imply present two-independence result. Search included dissociation and induced-P3-devoid synonyms. No known exact same-complex Q4 homotopy statement identified.

## value

PASS

Q4 is a canonical graph, and dimensions d1-d4 form a natural ascending sequence; the first occurrence of genuinely mixed homotopy in d4 is a motivated structural cutoff, not an arbitrary combinatorial slice. An explicit exact finite integral homotopy type of the natural dissociation complex can be useful without an all-dimensional theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
