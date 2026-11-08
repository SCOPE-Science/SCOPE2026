---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Each strict order and its reversal induce one ternary betweenness concept, so there are n!/2 concepts and each fixed middle-label query is positive for exactly n!/6. Any depth-d complete online mistake tree must have at least 2^(d−1) concepts at its positive root, yielding d≤1+floor(log2(n!/6)). Fetched the ACTUAL 78,165-byte certificate JSON (Git blob 80733f0b8c1c2032b59cfef5a3f5e715cd6bac96), independently enumerated lexicographic orders modulo reversal, evaluated all questions on all leaf paths in a separate JavaScript evaluator and verified distinct leaf witnesses at depths 1,3,5,7,10,13 for n=3..8, i.e. 2,8,32,128,1024,8192 leaves respectively. Independently implemented exhaustive monotone-prefix VC-support DFS for n=3..6; observed VC dimensions 1,2,4,6 (n=6 tested 558,091 retained support nodes). Thus finite exact values and universal root bound are supported. No exact values for n≥9 or VC n≥7 are claimed.

## originality

PASS

Best-of-knowledge PASS as an exact finite-range adaptive and static shattering census for ternary betweenness predicates on total orders, including the first cardinality-bound deficit and first VC/Ldim gap. General dimension definitions and reversal uniqueness are prior work.

## value

PASS

This is a natural complete finite classification to eight labelled elements, with exact first thresholds and large independently checkable exhaustive lower-bound certificates. Ternary midpoint questions have a different learning complexity from pairwise order comparisons; exact finite cutoffs are substantive even without an all-n formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
