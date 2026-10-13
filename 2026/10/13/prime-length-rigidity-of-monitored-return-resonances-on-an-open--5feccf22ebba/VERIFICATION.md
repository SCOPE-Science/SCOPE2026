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

# Reproducibility and scientific limits

Run `python verify.py` in the directory containing the standalone script, after installing NumPy and SciPy as in `requirements.txt`. The verifier reconstructs all sampled eigenvalues and endpoint weights for seven prime sizes, checks the collision multiplicities on 220 resonance ladders, and solves a discrete Lyapunov equation for 43 small-system return means. Recorded result:

`VERIFY_OK distinct_resonance_ladders=220 pair_collisions=406 direct_lyapunov_means=43`

The analytic proof, not these finite tests, proves rational independence and ladder nonoverlap for every odd prime and arbitrary positive sampling interval. Floating-point phase partitioning has an explicit tolerance and cannot certify irrationality or infinitely many intervals. Verification does not include an independent audit, an external priority check, or a check of noisy implementations.
