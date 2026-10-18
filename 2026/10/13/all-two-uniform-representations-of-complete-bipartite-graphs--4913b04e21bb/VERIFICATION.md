---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Take an X-letter x0 and rotate between its occurrences: each Y-letter must appear once in each interval by cross-part alternation; every other X-letter must occur twice together in one interval, enclosing that interval’s Y-occurrences, and nested X-intervals give P B P^R; the opposite interval similarly Q C Q^R. Y nonalternation forces C=B^R; rotation produces A B A^R B^R. Reverse construction verifies alternation for every cross edge and nonalternation within each part. Parameter pairs (A,B) and (A^R,B^R) give the sole cyclic duplication when N=m+n>=3, with 2N distinct rotations; count follows. Graph is connected and not complete for N>=3, so published square-free theorem applies. Independently enumerated all 2N-letter double-occurrence words through N=5 (113400 at N=5), for every bipartition, and matched the classification and counts. Infinite all-m,n proof is the nesting argument.

## originality

PASS

Circle graphs and double-occurrence words supply equivalent objects, but general 2-word representability only guarantees existence, not all labeled double-occurrence words or enumeration. The foundational Das–Hariharasubramanian paper proves k-uniform square-freeness and counts complete-graph K_n words, not all K_mn words. No covering all-m,n count was found in the inspected literature, though older chord-diagram enumeration remains possible.

## value

PASS

This classifies an entire representation-number-minimal word layer for the fundamental connected noncomplete family K_mn and counts labeled linear and cyclic words. The exact classification is a natural answer to the original source’s word-counting direction and a usable reference for double-occurrence word enumeration, not an arbitrary small parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
