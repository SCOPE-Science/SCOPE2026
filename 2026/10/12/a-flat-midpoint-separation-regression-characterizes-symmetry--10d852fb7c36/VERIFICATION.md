---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The theorem is proved analytically in `RESULT.md`.

The accompanying checker performs a supplementary exact-rational finite census. It takes every strictly increasing support of size two through five from
\[
\{-3,-2,-1,0,1,2,3\}
\]
and every positive integer mass vector with entries in \(\{1,2,3\}\), normalized to probabilities.

For each law it enumerates every ordered iid pair, groups the pair sum by the attained absolute difference, and verifies whether the conditional pair-sum mean is constant. It independently tests central symmetry of support and probability mass about the exact rational mean.

The replay covers \(9072\) laws. Exactly \(396\) have flat conditional pair-sum mean, and exactly the same \(396\) are centrally symmetric.

The finite census is not used as an infinite proof. The universal claim relies on the conditional-expectation, exchangeability, independence, and moment-generating-function uniqueness argument.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK laws=9072 flat=396 symmetric=396`.
