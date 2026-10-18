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

The analytical proof uses the exact free two-convex norm and Hilbert operator/nuclear duality, concavity of trace square root, a complete weighted-Laplacian eigenspace decomposition, strict concavity and exact scalar inequalities. It works for every integer \(a\ge2\) and \(b\ge1\).

The standalone `verify.py` separately assembled incidence-vector outer products and passed 36 rational eigenspectral tests, 13 unrestricted SLSQP edge-probability optimizations, and 15 polar-factor witnesses admissible in the defining lattice norm. Run `python3 verify.py` with NumPy, SciPy and SymPy installed. The optimizers use floating-point tolerances and do not certify universal optimality; the exact finite tests are not a replacement for the general argument.

Uniqueness applies to the averaged one-dimensional mass parameter only. Independent mathematical audit and external certificate are not available.
