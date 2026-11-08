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

On any labeled binary n-cycle n>=5 with 4 distinct neighbors ±1,±2, satisfaction means at least 2 agree. A singleton run can be happy only if both neighboring runs are singletons, forcing full alternating checkerboard; absent singletons any length-two run endpoint has at most one matching neighbor; every run>=3 is sufficient. Hence the exhaustive static class is constants, 2 even checkerboards, or alternating runs all length>=3. With k runs of each type, weak compositions after removing 3 from each yield binom(m-2k-1,k-1)binom(n-m-2k-1,k-1), weighted n/k for labeled positions. Summing m gives H_n=2+2[even]+sum_{k<=n/6}(n/k)binom(n-4k-1,2k-1). Six-state capped-run transfer has characteristic (t³-t²-1)(t³-t²+1) and primitive Perron root λ=1.465571..., so H_n~λ^n. Independent direct satisfaction predicate for all 16,352 words at n=5..13 exactly matches all S_{n,m}; check is finite and all-n run proof independent.

## originality

PASS

Long-run stability of majority cellular automata and structural short-run exceptions were known, including Nakar–Ron 2022 rank/radius general theory. The new mathematical object is the explicit population-resolved microcanonical census for every m and entropy for exactly the four-neighbor radius-two weak threshold model, not newly claiming the generic run dichotomy. Inspected original structural statements do not themselves state the binomial census. An older transfer-matrix/fixed-point table could overlap.

## value

PASS

Population count m is conserved under pair-swap Schelling dynamics, so S_{n,m} gives a natural exact fixed-composition invariant, not arbitrary sliced enumeration. The full microcanonical counts and exponential entropy quantify rarity of all-satisfied configurations at fixed m and under fair initialization without pretending to solve dynamic hitting probabilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
