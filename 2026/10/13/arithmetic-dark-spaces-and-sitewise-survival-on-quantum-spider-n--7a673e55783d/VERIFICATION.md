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

The analytic proof covers all integer arm lengths, all finite arm counts at least three, any real nonzero uniform hopping, and every strictly positive hub-loss strength. It uses exact open-path eigenvectors, one linear constraint at the hub, orthogonal projection, Ramanujan sums, and the dissipative spectral separation argument. No finite calculation substitutes for the proof.

`verify_spider.py` rebuilds the adjacency matrix directly and diagonalizes it; separately the exact formulas are evaluated using totients, divisors, and Ramanujan sums. The executable checks all \(182\) nondecreasing arm-length tuples for three or four arms, each arm having between one and six edges. Every one of \(2534\) sitewise comparisons, the complete dark-rank checks, and the arithmetic zero-site tests passed at the stated numerical tolerances. Install the dependency in `requirements.txt` and run `python3 verify_spider.py`.

The verifier's eigenspace grouping uses finite floating-point tolerances for only these small graphs. It does not certify all graph sizes or small complex spectral separations; the analytic proof controls those cases. Long-time loss behavior is established algebraically by the finite-dimensional dissipative argument, not by extrapolating simulated time traces.
