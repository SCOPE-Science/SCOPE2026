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

For open Johnson rank-two neighborhoods the positive fiber after a first pair e splits, under a second adjacent f, into a punctured star plus one exceptional pair; any further query leaves one child with at most two centers. Disjoint e,f leave exactly four hypotheses. Thus Ldim of each first-positive class is <=3 and the full class <=4. n=2 gives 0, n=3,4 gives 1 (for n=4 complementary center pairs have identical neighborhoods), and n=5,6 cannot reach 4 by hypothesis-count. The actual 8-leaf J(5,2) and 16-leaf J(7,2) certificates in lower_certificates.json realize depths 3 and 4 and embed into larger n. Independently recomputed exact adaptive recurrence for n=2..9 and checked finite certificate structure; it returned 0,1,1,3,3,4,4,4. Restriction to induced subgraphs only carries upper bound, not claimed exact Ldim.

## originality

PASS

The source Adler–Benediktsson–Macpherson determines VC dimension/density of this same Johnson/line-graph adjacency concept family, but that static shattering statement does not determine the complete adaptive Littlestone profile or its threshold n=7. Checked paper sections and terms for online dimension. Best-of-knowledge original online classification, residual alias/undiscovered priority risk.

## value

PASS

Exact, sharp adaptive learnability invariant for all n>=2 in an unbounded, highly symmetric family; identifies exceptional n=3,4 and n=5,6 and first depth four at seven. Different from textbook static VC bounds and gives nontrivial constant dimension for every induced subgraph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
