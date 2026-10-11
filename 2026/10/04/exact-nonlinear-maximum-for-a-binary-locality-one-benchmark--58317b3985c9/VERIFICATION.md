---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The eight-word construction has repair projections \(\{00,11\}\) inside each replication class and global minimum distance three. For the upper bound, every valid binary two-coordinate repair projection is contained in either \(\{00,11\}\) or \(\{01,10\}\), so helper-linked coordinate functions differ by a fixed bit. The transitive equivalence classes of coordinate functions all have size at least two and no coordinate is constant; representatives therefore embed the code into a weighted binary cube with class weights summing to nine. There are at most four classes. Three or fewer give at most eight words immediately. Four forces weights \(2,2,2,3\); slicing by the weight-three coordinate leaves two length-three binary codes of ordinary minimum distance at least two, each of size at most four. Thus the total is at most eight. The exhaustive weighted-quotient verifier reproduces the bound for every integer partition of nine, but the reduction and upper bound are proved symbolically.

## originality

PASS

Kang--Xiong's 2026 three-block LP treats the same nonlinear locality definition and the exact parameter row \((2,9,3,1,2)\), but its certified upper bound is \(64/5\) while its verified construction has size eight; the paper's exact-maximum theorem does not list this row. The closest Resultary exact-LRC finding resolves different locality-one parameter rows. The assigned equivalence-class reduction therefore closes a genuine benchmark left open by the strongest inspected source.

## value

PASS

The exact nonlinear maximum closes a named finite benchmark left unresolved by the strongest current LP bound and is supported by a reusable structural reduction specific to binary locality one. It is a motivated exact invariant rather than an arbitrary small-code census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
