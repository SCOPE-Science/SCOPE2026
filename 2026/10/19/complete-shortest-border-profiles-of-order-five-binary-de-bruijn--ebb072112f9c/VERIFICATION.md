---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A proper border of length at least five would give equal five-bit factors with distinct start positions, even if its two occurrences overlap. The length-one and shortest-length-two counts are forced by occurrence multiplicities of 00 and 11, and of 0101 and 1010, respectively. Rooting at the unique edge 00000 bijects rotation classes with rooted Euler tours in the four-bit vertex graph; exhaustive unused-edge DFS is complete, as is testing single cycles among all local incoming-to-outgoing bijections. Reversal and complementation preserve shortest borders and operate on the normalized rotation classes. Independent replay, using separately written code and not the supplied verifier, enumerated 2,048 tours and checked each proper border at all 65,536 cuts. It recovered the seven profile frequencies 48,64,256,448,48,384,800 in displayed order and the ordered size-2/size-4 orbit cells (4,10),(0,16),(4,62),(0,112),(4,10),(0,96),(20,190), with no other orbit sizes. The counts 48,768,1232 for 8,9,10 unbordered rotations yield mean 613/64 and variance 1191/4096, checked independently in exact arithmetic. Replay: python3 /workspace/branches/bc0ba784-7640-4f97-aae0-14da0a7c52d9/independent_border_census.py; SHA-256 8654ffece8b1bd049e3cb565cbe3af4a46918d37b099f737e8aeca1c391cfc8a. The supplied code and spectrum.csv were inspected; the independently reproduced data check the specific orbit cells, not merely their totals. This verifies order five only.

## originality

PASS

Pass for the complete shortest-border distribution and its cellwise orbit refinement. The cycle family, its total orbit counts, and its short-factor multiplicities are not credited as new. The strongest same-parameter earlier published SCOPE finding has a different run invariant, and two cycles identical in its reported numerical columns demonstrably have different shortest-border profiles.

## value

PASS

This enumerates an established word statistic on a canonical family and at a cutoff large enough for nontrivial profile and symmetry distinctions. The exact 8–10 rigidity and frequency distribution give concrete benchmarks for constructions or conjectures on border correlations of de Bruijn cycles, and the matched-run-data witness shows why a researcher cannot substitute the existing run profile. The finite scope is explicit; no general-order prediction or novelty of the known cycle list is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
