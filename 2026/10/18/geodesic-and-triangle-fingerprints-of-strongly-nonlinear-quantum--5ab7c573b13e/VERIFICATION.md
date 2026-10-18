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

The following independent finite computations were executed from the embedded `verify_strong_kerr.py` script using Python 3's standard library. The output was: `PASS 117 standalone finite numerical checks; no infinite family is inferred from them.` Five graph families were used: a path, a two-geodesic diamond, a star, a triangle with a tail, and a square, at couplings \(100\), \(300\), and \(900\). Assertions check mass conservation, the Hamiltonian energy, leading root leakage, next-order triangle leakage, and vertexwise geodesic amplitude limits.

The analytical proof in RESULT.md—not the finite integrations—establishes the statements for all finite connected simple graphs and all sufficiently large couplings. The numerical solver is fourth-order Runge–Kutta with fixed finite step size; no interval arithmetic or computer-assisted infinite certification is claimed. The asymptotic remainder constants are graph dependent and are not estimated uniformly over increasing graph size. No independent audit was performed.

Reproduce with `python3 verify_strong_kerr.py`.
