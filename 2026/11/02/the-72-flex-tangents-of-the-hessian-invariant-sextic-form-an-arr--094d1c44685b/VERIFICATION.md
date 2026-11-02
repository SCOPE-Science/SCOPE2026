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

## Reproducible checks

Run `python3 verify_curvature.py` with SymPy installed. It verifies the Hessian determinant factorization, the slice equation and third-order tangent contact, the six distinct roots of the slice, and irreducibility of its defining sextic over \(\mathbb Q(\omega)\). The expected final line is `MASCHKE_HESSIAN_FACTOR_SMOOTH_SLICE_TANGENCY_IRREDUCIBILITY_PASS`.

Run `python3 verify_tangents.py` with Python 3 (no external Python dependencies). The program constructs all 72 orbit tangent vectors with coefficient pairs for \(\mathbb Z[\omega]\), checks 264 exact characteristic-zero concurrence identities, enumerates the distinct intersections after specialization \((\omega,r)\mapsto(14,29)\) modulo 211, and asserts the per-line local incidence counts. It prints `MASCHKE_72_TANGENTS_INCIDENCE_OVER_CHARACTERISTIC_ZERO_PASS`.

The modular enumeration by itself is **not** evidence for existence of the multiple incidences over \(\mathbb C\); the program separately verifies every required determinant identity symbolically in the integral coefficient ring. Modulo 211 is used to rule out *additional* coincidences. Distinctness after reduction likewise certifies distinctness in characteristic zero. The human-readable argument in `RESULT.md` verifies the smoothness and group-action premises. No independent external validation has been performed.
