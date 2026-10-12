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

The analytic proof establishes the theorem for every integer \(n\ge1\). The finite checker is an independent consistency test of the displayed identities, not an exhaustive proof over all \(n\).

`checker.py` enumerates every sign path for \(1\le n\le9\) and uses exact rational arithmetic. It checks the discrete last-zero mass function, all conditional occupation means, the coefficient identities for the return-probability sums, both required marginal means, and the final covariance.

The largest exhaustive case contains \(2^{18}=262144\) paths. `CHECKER_OUTPUT.txt` records successful completion of 153 exact assertions.

No statement is made for biased walks, non-nearest-neighbor increments, odd horizons under a redefined endpoint convention, or occupation conventions that count zeros.
