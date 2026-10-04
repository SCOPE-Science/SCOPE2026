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

The equilibrium equations were reconstructed directly from the published vector field. Eliminating \(y,z,w\) yields the single exact condition
\[
x\left[(b-1)+\left(d-\frac1c\right)x^2\right]=0.
\]
The proof in `RESULT.md` performs the exhaustive real case split, including the singular case \(dc=1\).

`verify.py` is a dependency-free exact-rational replay. It checks the principal parameter set, a parameter set with two nonzero equilibria, and the degenerate one-dimensional equilibrium family. It also checks the structural reason that \(1\) is an eigenvalue of the origin Jacobian. The script is supporting computation only; the infinite classification rests on the displayed algebraic reduction.

Scientific limit: no numerical attractor, Lyapunov spectrum, or cryptographic experiment is reassessed here.
