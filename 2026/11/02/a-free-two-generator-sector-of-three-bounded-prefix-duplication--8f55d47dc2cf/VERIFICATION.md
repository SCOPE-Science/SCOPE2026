---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Starting from 010, a length-one duplication introduces an absorbing 00 prefix. Any final 01-prefix path therefore uses only length-two 01 or length-three 010 prepends; both preserve 010. The successive gap lengths 2 or 3 between new 1 symbols before the fixed suffix uniquely decode all blocks and derivations, so every path has one step per new 1 and the exact (1-uz^2-uz^3)^(-1) series. The Fibonacci suffix recursion and avoidance of 000,11 establish the same-parity corollary. The two bound-four witnesses are valid. Independent full prefix-duplication enumerations for four seeds confirm finite cases, not the infinite proof.

## originality

PASS

The full all-seed regular sector and all-path uniqueness are not stated in the inspected companion implementation or the public abstract of Cabrera Salamanca–Smith. That companion README and derive.cpp do already claim an optimized shortest derivation for Fibonacci words; shortest-Fibonacci computation alone is not new. General prefix/suffix-duplication papers give closure and algorithms, but an inaccessible full text leaves an explicit risk of an implicit sector classification.

## value

PASS

Characterizing the entire naturally preserved 01-prefix sector and its length-distance enumerator explains a current bounded-duplication Fibonacci construction, as well as a sharp change at prefix length four. This is a structural result, not merely a new numeral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
