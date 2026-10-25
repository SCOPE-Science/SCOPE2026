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

# Verification of the triangle distance-moment inverse theorem

The mathematical proof is self-contained in `RESULT.md`. A reproducible exact check is available by running `python3 check_triangle_moments.py` with Python 3 and the standard library. The program expands barycentric difference moments using the complete Dirichlet factorial identity, derives every coefficient of the first three even-distance-moment polynomials over formal squared side variables, and asserts equality with the stated formulas.

It additionally checks the resulting moment-to-symmetric-polynomial inverse, Heron's area identity on five explicitly admissible triangles, and the precise sixth-moment separation \(4/2401\) for a pair with identical first two moments. All arithmetic in these checks is rational, with no floating-point tolerances, external symbolic engine, or stochastic enumeration. The sharp stability exponent follows instead from the analytic Rouché argument and explicit limiting family in the proof. The verification script does not certify historical priority or a broader theorem beyond the claimed domain.

Independent audit status: not performed.
