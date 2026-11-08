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
# Verification of the triangular boundary diameter crossover

The theorem is proved using disjoint endpoint-arc avoidance, first-order Euclidean geometry and an exact conditional exponential integral; the computation is a reproducible crosscheck and not an infinite proof.

Run `python verify.py` with NumPy and SciPy. Actual execution returned:

`VERIFY_OK rate_identities=6 joint_law=6 correlation=3 onset=3 finite_sample_comparisons=9`

The checker verifies the two angular rates at three distinct base lengths, the dependent apex survivor at two threshold pairs per length, exact correlation against independent simulation, the single-edge CDF below the splitting threshold, quadratic onset via low-discrepancy quadrature, and nine direct finite-N diameter CDF comparisons.

The finite-N diameter routine evaluates the at-most-six edge-extremal sampled points (correct by convexity of Euclidean distance in each edge parameter). It does not exhaust all sample configurations or certify convergence uniformly. The analysis assumes fixed \(0<c<1\), and does not apply directly to the equilateral three-way case. No independent audit has been performed.
