---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For every m>=2 with n=2^m and fixed cyclic truth-table coordinate ordering 0..n-1, each nonconstant affine truth table is balanced with n/2 ones, giving cyclic pair weight n/2+T/2. Binary addition transitions occur with frequency 2^(m-t-1) by trailing-ones count plus two all-bit carry transitions. Invertible prefix-parity transformation yields T/2 as subset sum of coefficients {1,1,2,4,...,2^(m-2)}; generating polynomial gives pair enumerator 1+4 sum_{j=1}^{n/2-1} z^(n/2+j)+3 z^n, accounting separately for zero and all-one constants. Selected nonzero low-weight codewords span constant b direction plus exactly the prefix-parity unit axes whose positive coefficient <=j=alpha-n/2. Thus gamma=0 for alpha<=n/2 and 1+min(m,2+floor(log2 j)) above, components 2^(m+1-gamma), connected first at 3n/4 versus Hamming n/2. Fresh independent enumeration of every affine word at m=2..8 checked all coefficients and rank at every integer threshold. Finite checks supplement the all-m proof, not stand in for it.

## originality

PASS

Best-of-knowledge original complete pair-weight distribution and intermediate generation-rank phases for canonical binary lexicographic RM(1,m) truth tables; general symbol-pair generation profiles and minimum b-symbol distances are prior work. Highly relevant Singh–Singh full manuscript unavailable, explicitly recorded as material originality risk, not treated as proof of noncoverage.

## value

PASS

Complete profile of a natural infinite code family gives every symbol-pair weight, exact component count for each threshold and an n/4 gap between Hamming and pair connectivity. Such precise thresholds are natural parameters in protection against localized adjacent errors and cannot be obtained from only the minimum distance; an all-m result is substantially stronger than an arbitrary finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
