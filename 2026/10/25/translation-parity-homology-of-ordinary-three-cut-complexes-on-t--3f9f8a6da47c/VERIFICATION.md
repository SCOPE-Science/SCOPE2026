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

The source file `check_torus_translation.py` uses only the Python standard library. Execute `python check_torus_translation.py`. It enumerates the Alexander-dual faces, constructs the invariant chain complex under coordinate translations, repeats with the ground-set sign twist, and uses exact rational elimination to compute boundary ranks. It checks the chain identity \(\partial^2=0\) and verifies the predicted quotient-homology ranks for \((5,5),(5,6),(5,8),(6,6),(6,7)\). The reported success marker is `TOROIDAL_CUT_TRANSLATION_INVARIANTS_OK`.

The all-length conclusion follows separately from the elementary collapses, the explicit translation-fixed torus generator, the Hopf trace formula, the sign in equivariant Alexander duality, and averaging. The checker is finite and cannot by itself establish that theorem. Only the displayed cases have been computationally examined; integral quotient torsion and symmetry actions outside translations have not been determined.
