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

## Checks actually performed

The included `verify.py` reconstructs each information Gramian independently from exact integer observation trajectories of two positive-spectrum affine cycle evolutions. Its Bareiss determinant calculations check all distance choices on cycle sizes 3 through 14 for two shifts, 96 cases, including 40 equal-odd-order comparisons and 12 even-order strict-parity comparisons. It produces `verification_exact_output.txt`.

The included `verify_heat.py` uses `mpmath` with 80 decimal digits, constructs discrete heat trajectories at heat parameter \(\tau=0.3\), and checks the full determinant identities for cycles of order 3 through 12: 35 distances, including ten singular configurations. It produces `verification_heat_output.txt`.

Both scripts were executed successfully from their package directory. The universal identities and all-parameter optimizer classification follow from the analytic Fourier, Gram-complement, sine-product and Lagrange-sign proof; the finite tests are supplementary.

## Limits

No exact symbolic equality for transcendental heat parameters in arbitrary cycle order is inferred from the numeric tests. Full bibliographic uniqueness and independent audit remain unperformed. The scripts do not claim to certify arbitrary dynamical systems or observation horizons.
