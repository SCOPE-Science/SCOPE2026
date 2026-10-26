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

The standalone Python 3 file `verify.py` uses only the standard library. It exhaustively lists 46,232 uniform recursive trees for sizes 3 through 9. For adjacent root degrees it compares exact rational distributions on leaf masks for all principal upward events, all upper-count tails, and strict conditional leaf-count means. For sizes through six it checks every upward-closed event in the full leaf-mask poset. It also tests exact normalization for cardinality-conditioned product weights.

Observed execution: PASS: 2579 exact conditional-order checks; 46232 recursive trees enumerated (n=3..9).

The theorem for all tree sizes is proved by independent Bernoulli decomposition, positive-weight subset coupling from Newton log concavity, and pathwise parent reassignment. The finite checker is a consistency test, not exhaustive validation of unbounded sizes. Historical-priority comparisons are incomplete for the inaccessible complete Janson PDF; no independent audit has been performed.
