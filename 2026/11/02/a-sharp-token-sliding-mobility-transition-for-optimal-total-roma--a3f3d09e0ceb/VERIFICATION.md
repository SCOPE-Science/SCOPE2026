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

The previously known domination minimum 2(k+1) comes from k+1 disjoint Kneser vertices. The inspected proof counts k-set hitting witnesses to exclude label-2 family sizes 0..k and weights beyond k+1, then uses the Roman domination property to force disjointness at equality. Exactly (k+1) disjoint blocks plus s unused elements yields the quotient factorial vertex count, and replacement by a k-block from the unused set gives degree (k+1)binom(s,k). For s<k no move exists; for s=k each state belongs to an immutable partition of n into k+2 k-blocks, with all choices of unused block adjacent. For s>=k+1, occupied/free element swaps connect token-jump configurations, and an auxiliary KG(n-k^2,k) on >=2k+1 available elements implements exchanges as genuine disjoint slides. Exhaustive k=2 state graph checks n=6..9 give 15,105,105,1 components respectively. The infinite theorem follows from exchange connectivity and the constructive Kneser path lemma, not the finite enumeration.

## originality

PASS

Zec–Grbić (2023) Theorem 2 proves the minimum total Roman number and a disjoint-block construction, explicitly credited. Clique and matching reconfiguration references address generic slides/jumps but do not evaluate the exact component transition of the minimum total Roman Kneser configurations in inspected materials. This classification is not merely recomputing the old minimum weight; the new object is the entire graph of optimum labelings.

## value

PASS

Reconfiguration mobility is a natural independent structural question after characterizing optimal Roman labelings. The theorem gives the first nonzero-mobility point, complete partition-clique critical layer, exact connectedness threshold and degree for the entire natural integer family. This is a meaningful phase transition, not an arbitrary tiny census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
