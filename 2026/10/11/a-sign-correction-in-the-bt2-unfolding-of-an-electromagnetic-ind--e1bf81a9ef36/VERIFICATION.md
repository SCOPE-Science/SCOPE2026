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
The source-specific algebra is replayed by `verify.py` using decimal arithmetic on the constants displayed in the article. The script checks that the scaling factors are positive, that the first scaled unfolding coefficient is negative, that the displayed magnitudes are reproduced to rounding tolerance, and that the normalized saddle-node polynomial has linear part \(-\lambda_1+62.4500798\ldots\lambda_2\).

The verification proves only the internal sign correction from the published coefficients. It does not independently recompute the full center manifold from the four-dimensional neuron equations, establish the BT2 point from first principles, or certify hidden digits beyond those printed by the source.
