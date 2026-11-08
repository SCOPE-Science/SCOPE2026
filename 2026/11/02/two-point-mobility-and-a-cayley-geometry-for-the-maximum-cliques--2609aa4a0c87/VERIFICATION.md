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

For residues modulo 41 form Q as all 20 nonzero squares and exhaustively enumerate increasing five-cliques (the source second verifier iterates all C(41,5)=749398 five-subsets). Exactly 205 five-cliques are found, none extendable to six. Independently constructed all 205 five-cliques by growing common neighbor sets and confirmed no six extension. The affine subgroup with multipliers {1,10,16,18,37} maps B={0,1,2,10,33} to 205 distinct cliques, proving regular action. For each pair, no intersection of size 4, and exactly 820 edges at intersection size 3; all degrees 8. The eight displayed affine generators are inverse closed. Independent BFS on the actual exchange adjacency yields (1,8,36,98,62) from B; regular Cayley symmetry yields that shell count from every clique and exact radius/diameter 4. This is a finite complete proof backed by exhaustive enumeration, not a finite sample of an infinite family.

## originality

PASS

Best-of-knowledge distinct claim after comparison with directly relevant primary sources and published mathematical findings. Prior special cases and baseline formulas are explicitly credited. Complete historical originality is not certified.

## value

PASS

Paley(41) is the first standard prime-order Paley example with maximum clique size five, so its optimal-clique reconfiguration under a minimal simultaneous exchange is a natural finite graph problem. A sharp local mobility transition from 205 isolated vertices under one exchange to a connected vertex-transitive Cayley geometry under two exchanges, with full metric shells, gives a structural benchmark. Does not falsely claim a general Paley theorem or novelty of clique number five.

The dated certificate retains the supplied scientific assessment, sources and limitations.
