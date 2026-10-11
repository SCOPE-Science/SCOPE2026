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

# Reproducibility and proof bounds

The equations, Hamiltonian derivatives, quadrant level sets, two-traversal radial quadrature and elliptic-modulus convention are stated in `RESULT.md`. The essential universal step is differentiating the positive angular integral on compact energy subintervals; its sign proves all derivative orders by ordinary dominated differentiation. The complementary-modulus asymptotic supplies the precise logarithmic constant, with fixed positive parameters.

The standalone `verify_period.py` has no dependencies beyond the Python 3 standard library. It checks the angular quadrature against arithmetic–geometric-mean evaluation of the complete elliptic integral, samples several anisotropy scalings, checks first/second derivative signs on a finite mesh, and probes both endpoints. Replay with `python verify_period.py` should print `CHECK_OK`. This finite test is not an infinite proof and does not certify originality, independent validation or behavior outside the stated family.
