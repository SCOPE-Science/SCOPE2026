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
Analytical proof: reconstruct the equilateral billiard's period-two and period-three rays; differentiate the local ellipsoid graph and specular reflection; use the \(2\times2\) symplectic free-flight/reflection block to obtain an exact expanding eigenvalue; compare scalar traces and check the strict derivative at critical flattening. The norm-normalization and collision-versus-flow time distinction are explicit in `RESULT.md`.

Reproducible finite diagnostics: execute `python check.py` with SymPy. `checker_output.txt` contains the exact output of that execution. It checks the curvature Hessian, three ray reflections and cosine identities, monodromy traces, the algebraic critical parameter and seven sample spectral comparisons. The open-set perturbation statement rests on hyperbolic continuation, not numerical enumeration. Independent audit: not performed.
