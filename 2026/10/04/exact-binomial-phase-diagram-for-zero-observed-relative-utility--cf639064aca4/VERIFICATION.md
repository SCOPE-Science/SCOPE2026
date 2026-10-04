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

The finalized `verify.py` uses exact rational arithmetic to reconstruct the model net benefit, the better-default net benefit, and the event of zero observed relative utility for every attainable count in representative rational cases. It independently computes the claimed binomial-tail event and checks equality of the exact probabilities for the \(q>t\), \(q<t\), and \(q=t\) branches.

It also evaluates finite-\(n\) binomial probabilities numerically for representative off-threshold and local-threshold sequences. Those numerical values are diagnostic only. The logarithmic and Gaussian limits in the finding are established analytically by Chernoff/Stirling and central-limit arguments, respectively; the script is not an infinite-proof certificate.

The script was executed from the finalized package path and returned `VERIFY_OK`.
