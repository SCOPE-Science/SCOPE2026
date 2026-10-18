---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

The received ball B(x) contains x, all single deletion-of-0 outputs and all single swaps 01↔10, never an error composition. The compatibility graph on the 2^n words has edge iff balls disjoint, so its maximum clique is precisely the maximum code cardinality. Inspected packaged witnesses in artifacts/optimal_codes.json including 30 length-7 words; independent exhaustive graph construction and coloring branch-and-bound on 128 length-7 vertices established tuple 2,3,4,7,11,17,30, with 102,464 recursive calls; the package verifier has an independently checked coloring pruning lemma and a distinct explicit certificate path (recorded 100221 calls). Exact n=1..7, with no extrapolation.

## originality

PASS

Best-of-knowledge PASS: Wang/Vu/Tan full source defines exactly the channel but gives constructions; Ye/Ge Section VII supplies only n≥n0 asymptotic upper bounds; Gabrys et al. study a stronger arbitrary deletion alternative but only asymptotically. None imply (2,3,4,7,11,17,30). Exact-table discovery still uncertain due unavailable semantic index/unindexed sources.

## value

PASS

The exact finite capacity of a natural DNA/recording error channel, including 30 optimal length-7 codewords, is a useful and nonmechanical answer absent from the standard asymptotic constructions; naturally motivated finite cutoff and explicit upper certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
