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

# Reproducibility and verification

Run `python verify.py` with Python 3 and SymPy. It checks the integral-to-characteristic-three polynomial reduction, the derivative-sum identity, the axis restriction, the exceptional-node transverse coefficient modulo the quadratic parameter relation, the local cusp quadratic and restricted cubic coefficients, and the six off-conic intersection points of the four lines. The packaged script returned `VERIFY_OK: characteristic-three identities, local cusp and node coefficients, four-point blowup, K5 geometry`.

The full geometric assertions also use (a) the four-base-point and axis case split, (b) the blowup smoothness criterion at a cusp and the ordinary-node quadratic tangent cone, (c) Bezout to exclude reducible fibres outside the explicit endpoints, and (d) elementary intersection computations on the blowup. These arguments are in RESULT.md. Finite point counts are not used to certify absence of other geometric singularities. No formal proof assistant or independent validation was used.
