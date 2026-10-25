---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For each perfect matching M of dodecahedron GP(10,2), deletion S subset E\M is uniquely anti-forcing iff it intersects N\M for every other perfect matching N: a complete exact hitting-set equivalence. Source orbits verifier enumerates 36 perfect matchings and 120 automorphisms, with orbit sizes 30 and 6, then every smaller subset and minimum witness. A different bitmask/LCF presentation checks all 36 matching cases independently. Crucially a separate independently implemented C++ exhaustive enumeration of every candidate 20-out-of-30 nonmatching-edge subset through cardinality eight recovered the complete profiles: (ordinary min 4, eight witnesses; disjoint min 8, four witnesses) for 30 matchings; (ordinary min 5, 22 witnesses; disjoint min 8, five witnesses) for six. This exhausts a finite object; 30t^4+6t^5 and 36t^8 and totals 372/150 follow. No extrapolation to fullerenes generally.

## originality

PASS

Primary evidence and published-record searches support best-of-knowledge originality of the precisely isolated mathematical contribution, not unconditional priority. Same graph and old parameter explicitly compared; no source inspected supplies required all-matchings constrained certificate counts. Strong prior partial coverage acknowledged; surviving claim requires true finer count and new constrained extremal size.

## value

PASS

The dodecahedral C20 graph is the smallest fullerene and canonical molecular perfect-matching model. Deletions constrained to be pairwise nonincident are a natural distinct intervention/observation rule. The sharp universal eight-deletion requirement is a substantive gap above previously known ordinary minima four/five and existing nonmatching-four restriction, and the full automorphism-resolved multiplicity census supplies a precise useful benchmark rather than only the already-known spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
