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

# Reproducibility checks

Run `python verify.py` in an environment with the stated SymPy requirement. The verifier expands the full Jacobian derivatives of \(f=H(H-z^4)\), checks both homogeneous syzygies vanish, and confirms that their vector cross product equals minus the entire gradient. It checks the Euler identity for \(H\), the six rational transformations of the anharmonic invariant \(j\), the orbit-derived projected stabilizer orders \(4,8,12\) for exact sample parameters, and the numerical Tjurina equality \(37=(8-1)^2-3\cdot4\).

Execution result: `VERIFY_OK: exact Saito syzygies (degrees 3,4), anharmonic j invariance, sample stabilizers 4/8/12, Tjurina 37`.

The finite sample subgroup counts do not constitute proof for every parameter. The universal proof of completeness is the block-matrix coefficient comparison, classical four-point orbit classification, and fourth-root lifting argument in the main result. The singularities are verified by analytic local forms. No independent validation has been performed.
