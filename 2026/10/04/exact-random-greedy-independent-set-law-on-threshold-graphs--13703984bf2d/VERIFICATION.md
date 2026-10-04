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
# Checks performed
The recursive proof was replayed from the threshold creation operations. The isolated case was checked to append the new vertex without altering earlier greedy decisions. The dominating case was checked to split exactly on whether the universal new vertex is first in the uniform permutation, producing the recurrence used for every product probability.

The standalone script `artifacts/verify_threshold_rgmIS.py` was executed from its package path. It enumerates all threshold creation sequences of orders one through seven with first bit zero, exhaustively enumerates every vertex permutation, computes the greedy maximal independent set directly, and compares the exact rational empirical law to the theorem. It also checks the probability-generating-function recurrence and the closed maximum-success probability. The observed output was `VERIFY_OK sequences=127 permutation_checks=347741`.

# Limits
The finite exhaustive computation checks edge cases and arithmetic only; it is not the proof of the infinite theorem. The theorem itself follows from the exact isolated/universal recursion. The literature comparison is targeted rather than exhaustive over all historical terminology. No independent external audit has been performed.
