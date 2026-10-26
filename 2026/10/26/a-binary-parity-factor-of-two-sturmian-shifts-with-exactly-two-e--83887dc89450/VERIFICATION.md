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

# Verification and limits

The unrestricted result is proved symbolically in `RESULT.md`, not extrapolated from finite experiments. The proof's critical external input is Kronecker equidistribution on the two-torus under the explicit rational-independence hypothesis. Its critical local input, checked directly from the mechanical floor formula, is that the two extensions of a singular Sturmian phase differ at exactly two adjacent coordinates.

Running `python3 verify.py` checks both same-parity exceptional identities and the distinct mixed-parity branch for all 101 tested positions from \(-50\) through \(50\), using the explicit example \(\alpha=\sqrt2-1\), \(\beta=\sqrt3-1\). It also computes 30,000-term weighted binary-symbol averages to corroborate recovery of both phases, observing errors below \(0.006\) from their target unit complex numbers. These numerical checks do not certify asymptotic convergence, general uniqueness, or any untested irrational pair; those statements are established analytically.

Scientific scope is the noiseless bilateral subshift with known slopes and independent \(1,\alpha,\beta\). It does not cover rationally dependent rotations, finite-sample optimal recovery, robust decoding under symbol errors, or a conjectural exact word-complexity expression. Independent audit has not been performed.
