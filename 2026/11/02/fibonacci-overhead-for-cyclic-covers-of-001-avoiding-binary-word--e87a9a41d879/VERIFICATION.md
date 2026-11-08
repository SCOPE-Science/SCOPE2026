---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The required set comprises all FINITE length-n binary words without factor 001, not merely periodically admissible words. Counting no-00 words and terminal-zero suffix cases gives F_{n+3}−1 requirements. In the required-edge binary de Bruijn graph each of exactly F_{n−1} vertices starting 01 without 00 has excess outdegree one; matching deficit vertices end 00. Any augmenting flow for a circular covering walk decomposes into these many paths from deficits to surpluses; an overlap of ≥2 suffix/prefix bits is impossible because '00' cannot prefix a no-00 target. Thus each path needs n−2 edges. The last bit of each deficit is 0 and each surplus begins 0, so exactly n−2-edge connecting paths exist; the augmented balanced graph is strongly connected through 1^{n−1} and 0^{n−1} and hence Eulerian. This proves L_n=F_{n+3}−1+(n−2)F_{n−1} for all n≥3. Independent Euler constructions and coverage checks n=3..13 agree, and finite brute tests at n=3,4 corroborate minimality.

## originality

PASS

Best-of-knowledge comparison for Fibonacci overhead for cyclic covers of 001-avoiding binary words: four checks below distinguish exact claims from published stronger claims, related definitions, alternative expressions and available tables. No checked statement entails the entire result; inaccessible or unindexed possible coverage remains recorded, rather than being claimed disproved.

## value

PASS

The exact unavoidable linear-in-n cover overhead settles a natural finite-versus-periodic language distinction. The optimum is a concrete all-n invariant of a familiar forbidden-factor family and a tight directed-postman overlap bound useful in universal-cover and cyclic-superstring constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
