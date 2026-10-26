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

Run \(\texttt{python3 VERIFY.py}\) using Python 3 and only its standard library. The program verifies exact rational row normalization, signed projection identities, the three displayed rational angle pairs, exact stationary detailed balance and normalization for five integer residual powers, equality of edge-average and row-average rates, and approximate endpoint/monotonicity identities. It also compares long simulated Markov paths with analytic rates at four positive powers and at iid uniform sampling (750,000 transitions total). Recorded execution: \(\texttt{VERIFY_OK}\).

The proof, not simulation, establishes the almost-sure infinite-time claims. The key independently inspectable mathematical steps are: (1) collapse of a planar projection onto its selected perpendicular line, (2) cancellation of the current amplitude from residual probabilities, (3) symmetric-edge detailed balance with stationary flux \(s_{ij}^p/(2Z_p)\), (4) finite-state ergodic theorem for the log norm, (5) covariance monotonicity, and (6) distinct self-loop kernels at exactly zero versus positive exponent. The finite tests cover a particular rational three-row example, not the entire parameter family. No external scientific validation is claimed.
