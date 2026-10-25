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

# Verification record

The proof for all integers \(\(p,q\ge2\)\) and all real parameters \(\(t\in[0,1]\)\) follows the exact vertex representation, squared-distance comparison, and variance/barycenter certificate. There is no finite-enumeration extrapolation to infinitely many parameter values.

Run `python3 verify.py` with Python 3, NumPy and SciPy. The executed standalone program returned `CHECK_OK {'exact_profiles': 126, 'vertices_checked': 81618, 'brute_profiles': 24, 'optimizer_profiles': 5}`. Its rational arithmetic verifies the proposed radii, all-vertex inequalities, contact counts and barycentric identities, across endpoints, interior values and plateau regimes. Its halfspace-intersection enumerator independently corroborates the vertex list in low dimensions. Its numerical epigraph optimizer independently corroborates five instances of the minimum-enclosing-ball calculation, subject to stated floating-point tolerances.

The independent audit is **not performed**. Numerical optimization does not prove global optimality for all dimensions; the analytic variance identity with a contact barycenter does. The mathematical limits of the theorem are stated under *Limitations* in `RESULT.md`.
