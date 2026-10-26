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

# Reproducibility

Run `python verify.py` using Python 3 with SymPy. The program evaluates symbolic normal-form derivatives, cross-checks the coefficient through independently averaged polar equations, proves the algebraic parameter identity, and certifies a counterexample using an explicit rational interval for \(\log5\). It does not infer bifurcation from finite trajectories or claim that interval arithmetic checks every possible parameter; the general theorem follows from the analytic derivation in `RESULT.md`.

The positive Hopf crossing uses \(pM/2>0\). The sign of the radial coefficient controls the local cycle type only away from the vanishing-coefficient case. No higher-order coefficient, global cycle uniqueness, or independent third-party validation was performed.
