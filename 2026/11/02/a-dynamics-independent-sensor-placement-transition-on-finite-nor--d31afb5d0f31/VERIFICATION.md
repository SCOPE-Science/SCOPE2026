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

The finite-path eigenvectors, spectral transfer identity, determinant comparison and analytic cutoff are derived directly in `RESULT.md`. Under equal sensor weights, the spectral parity blocks have enough independent time rows when \(K\ge\lceil m/2\rceil\); distinct selected evolution eigenvalues guarantee each block has full rank. Both \(G_E\) and the column-congruence calculation use the same orthonormal signal coordinates.

Run the included checker with `python3 verify_two_sensor.py`. It uses only the Python standard library and checks eigenvector normalizations and eigen-equations, column transfer, Gram congruences for injective spectral nodes, finite determinant comparisons, strict-win intervals across paths through 500 vertices, numerical quadrature for the critical fraction, and the finite-size correction. The checker was actually executed from the complete new package and reported:

`TWO_SENSOR_CHECK_OK 132643 alpha 0.409581086749 delta 0.687239309064`

This finite numerical suite does not certify the infinite family. The infinite-dimensional-as-N-grows claims are established by the Riemann-sum limit and Euler–Maclaurin analysis in the mathematical proof. There is no external expert, formal machine-proof or independent audit claim. Numerical decimal displays are approximations to uniquely specified exact mathematical quantities.
