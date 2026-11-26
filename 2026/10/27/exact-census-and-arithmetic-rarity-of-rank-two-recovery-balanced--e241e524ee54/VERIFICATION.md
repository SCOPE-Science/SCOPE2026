---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A zero column is known before sampling and a nonzero column cannot be, so no balanced rank-two code has a zero column. For a nonzero target in direction i and t≥1 draws, recovery fails exactly when all t draws come from a single occupied direction j≠i: in dimension two two distinct nonzero directions already span. These events are disjoint and have probabilities (a_j/n)^t. Summing the discrete survival tail including time zero gives E_i=1+Σ_(j≠i) a_j/(n−a_j), agreeing with the source's Poissonized expression. Equality of expectations is precisely equality of the occupied multiplicities, so r|n with 2≤r≤q+1. Choosing directions, assigning the n labels in equal parts, and making q−1 independent scalar choices per column gives the numerator count. A full-rank generator's left GL₂ action is free and its orbits are exactly row spaces. For the nondegenerate denominator exclude one-direction lists from all nonzero columns; for the all-code denominator choose two independent rows. These steps work for every prime power, including n=2, and the numerator is zero if there is no eligible r. Stirling gives r^(n+r/2)/(2πn)^((r−1)/2) for the leading multinomial term, and each smaller candidate is exponentially dominated uniformly over the finite list of r at fixed q. The polynomial subsequence concerns the nondegenerate denominator only. The frozen exact-arithmetic verifier and its recorded prime-field results were inspected, not rerun; no extension-field computation is required by this proof.

## originality

PASS

Support is for the explicit census of distinct labeled subspaces over general finite fields and the exact divisor-sensitive rarity law. The recovery metric and the structural criterion's expectation-level derivation are not credited as new general results. The actual comparable sources inspect different populations or recovery objectives and do not establish the enumerated census or both probabilities.

## value

PASS

Recovery balance is a preexisting natural property; the result gives its exact frequency in two clearly defined code populations. The largest-divisor law resolves why lengths at the same fixed field size can have polynomial rarity, exponential rarity or exact absence, which a single typical-length bound would miss. This is useful information about the natural ensemble despite elementary proof methods and the rank-two restriction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
