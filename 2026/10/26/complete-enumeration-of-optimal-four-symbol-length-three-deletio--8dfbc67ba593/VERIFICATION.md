---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For q=4 and three transmitted symbols, each 3-word has at most three distinct length-2 deletion descendants, so five words cannot cover all 16 ordered received pairs. The displayed six-word code gives a partition. Directly inspected exact mask representation M(a,b,c) and complete six-subset DP (64 possible triples), and independently implemented capacity-pruned increasing-sextuple and 24 global symbol permutations times reversal; found 644 optimal covers, 120 disjoint-shadow, 524 overlapping, and 21 orbits: 8*1 + 12*3 + 24*9 + 48*8 = 644. The capacity bound at depths 3,4,5 is 16-3(6-k), so pruning is exhaustive. Every counted codebook is an unordered set with distinct words; duplicate deletion positions are collapsed. This is a finite exhaustive proof only for q=4,n=3, not a general alphabet formula.

## originality

PASS

Known lower bound/minimum size and existence of perfect six-word deletion codes are explicitly not new. The tested new final claim is the 644/120/524 labeled-codebook census, incidence profiles and 21 symmetry orbits. No inspected stronger theorem or published record was shown to imply the complete counting statistics; residual unindexed directed-covering-design risk remains.

## value

PASS

A natural DNA-sized four-symbol deletion-covering problem has many inequivalent minimal covers; determining all 644, including 524 non-perfect overlap-bearing ones, resolves a complete finite classification beyond a known optimum size. Exact orbit and incidence profiles are usable structural benchmarks, not a routine substitution of a previously published count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
