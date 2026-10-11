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

Fresh exhaustive construction of all 120 permutations gave the exact compatibility graph with 2520 edges and degree 42. An independent Bron-Kerbosch enumeration returned maximal-clique histogram 60 of size 2, 120 of size 3 and 4020 of size 4, with no larger clique. Every one of the 4020 maxima had six pairwise distances exactly three. Explicit construction of all 240 stated isometries verified distance preservation and yielded orbit-size distribution 60x5, 120x7, 240x12. This is exhaustive over the finite graph, not a timeout/sample.

## originality

PASS

The exact optimum \(A(5,3)=4\) is prior art and is not claimed as new. The 2015 primary paper's Example III.1 explicitly records that value after deriving an integer-programming upper bound of five, but it does not enumerate all extremizers. No inspected source or Resultary record gives 4020 labeled maxima, universal pairwise distance three, or the 24-orbit decomposition under the stated 240-element isometry subgroup.

## value

PASS

The parameter cell is a standard small Ulam-code benchmark whose optimum size was known but whose full optimizer landscape was not. A complete exact extremizer census, universal equidistance phenomenon, and symmetry quotient are natural finite classification data that a future coding-theory comparison can directly use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
