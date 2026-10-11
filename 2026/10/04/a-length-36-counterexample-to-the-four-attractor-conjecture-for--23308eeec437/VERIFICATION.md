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

The directive prefixes reconstruct exactly to the stated length-36 palindrome. The seven displayed factors give a transparent lower bound: three eligible-position sets inside positions 0–14 have empty common intersection and require at least two points, one factor forces a point in the disjoint range 15–20, and three sets inside 21–35 likewise require at least two, totaling five. Independent replay enumerated all 500 distinct nonempty factors, verified the attractor {3,7,15,21,25}, and exhaustively rejected all 58,905 four-position sets.

## originality

PASS

The primary paper explicitly conjectures that every pseudopalindromic prefix of every binary generalized pseudostandard sequence has minimum attractor size at most four, while proving smaller bounds only for special subclasses. Exact-word, directive-pair, conjecture and Resultary searches found no earlier size-five counterexample or correction. The explicit mixed-directive witness is therefore best-of-knowledge new.

## value

PASS

A short exact counterexample that falsifies the main universal attractor conjecture of the source paper is a motivated combinatorics-on-words result. The certificate is transparent and independently replayable, and the witness narrows the search for the true universal behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
