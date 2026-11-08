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

Lucas factorization of central trinomial coefficients gives T_n modulo 5 as the product of digit weights (1,1,3,2,4), all nonzero. Using the exact identity 2M_n=3T_n+2T_(n+1)-T_(n+2), the two consecutive Motzkin residues for n=5q+d equal U(q)(f_d(R(q)),g_d(R(q))) for twenty explicit d,R cells. Direct independent computation reproduced all twenty cells, the 80-point push-forward matrix and absence of (0,0), and matched direct Motzkin values for 700 n. For an aligned q interval of length 5^r the carry-run length h<r has one admissible prior digit for each ratio R; products of free digit weights give each U-value 5^(r-h-1)/4+O(1). Summing h yields the 5^r/16+O(r+1) joint equidistribution; h=r costs at most one endpoint. Disjoint base-five aligned blocks for arbitrary Q add O((log Q)^2) discrepancy. Hence each of the 25 pair frequencies has the claimed rational coefficient /80 for every cutoff N; the impossible (0,0) follows exactly and is not an asymptotic inference.

## originality

PASS

Existing work develops central-trinomial Lucas congruences, Motzkin automaticity, zero-position density 1/10 and explicit adjacency recurrences. Those ingredients are appropriately credited. The inspected primary theorems do not supply a complete 25-cell ordered-neighbor distribution together with a quantitative polylogarithmic all-cutoff discrepancy. Some zero-pair avoidance may be implicit in automatic presentations and is not individually relied on for priority.

## value

PASS

The full adjacent-residue correlation law determines dependence beyond known marginals for a classical combinatorial sequence. The exact forbidden pair and logarithm-squared uniform discrepancy are natural arithmetic refinements potentially usable in modular pattern questions; the result applies to every N, not just powers of five.

The dated certificate retains the supplied scientific assessment, sources and limitations.
