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

The supplementary script `verify.py` uses Python 3 and SymPy. Execute `python3 verify.py` with SymPy installed. It checks exact polynomial radial factorization, equilibrium equation, reciprocal-radius Dulac divergence and square completion, the divergence for every radial power, the derivative of the radial-power minimum, the saddle/sink Jacobian determinant and trace identities, and the exact endpoint ratio. Successful execution emits one `PASS` line.

The full proof additionally requires the standard Bendixson–Dulac/Green, Poincaré–Bendixson, stable-manifold and Poincaré recurrence theorems, which are applied to the analytically bounded polynomial field and proved sign identity. Finite or sampled computations do not replace those infinite-dimensional quantifiers. The restriction to globally nonpositive radial-power divergences is not a claim of a globally sharp absence-of-cycles threshold. No independent verification or separate audit has been conducted.
