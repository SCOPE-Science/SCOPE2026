---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The seven-vertex graph has domination number at least three exactly when every pair has an outside vertex adjacent to neither member: an existing dominating singleton would extend to a pair. I independently enumerated all 2^21 edge masks by this common-nonneighbor test, formed every augmented simplicial boundary column by single-edge deletion, and reduced the original matrices by exact binary Gaussian elimination, without matching, Morse projection, or execution of the frozen verifier. The face counts for cardinalities 0–12 are 1,21,210,1330,5985,19782,47187,76590,76860,43330,13566,2310,105; all later counts vanish. The boundary ranks for cardinalities 1–12 are 1,20,190,1140,4845,14937,32250,44234,32003,11326,2205,105. The codomain for cardinality one includes the empty simplex, so rank-nullity with both adjacent boundaries gives exactly reduced mod-two Betti numbers 106,623,1,35 in dimensions 6–9 and zero elsewhere. This corroborates the frozen verifier’s homology output by an independent method, not merely by Euler characteristic. No inference about integral homology or homotopy type is made.

## originality

PASS

The inspected primary theorem and closest catalogue computations concern other thresholds or numbers of vertices. No equivalent exact seven-vertex no-dominating-pair computation was located. The pass is for the complete mod-two Betti vector at (7,3), not the introduction of the filtration or the use of existing homology methods.

## value

PASS

This is a natural term of a studied domination filtration, close to but outside its classified diagonal. Knowing that four adjacent reduced degrees survive, with a rank-one degree-eight term and the full exact ranks, is information unavailable from neighboring wedge classifications or Euler characteristic. It is a reproducible benchmark for future filtration and coefficient comparisons, without claiming a full census, persistence, or a homotopy classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
