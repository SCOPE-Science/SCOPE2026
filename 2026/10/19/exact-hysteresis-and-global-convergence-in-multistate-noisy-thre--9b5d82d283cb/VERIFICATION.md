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
# Verification notes

`verify.py` requires Python 3 and SymPy. Run `python verify.py` from the folder containing the script. It tests 24 exact three-draw probability distributions against the closed-form update rule, 210 rational parametrized equilibria and all their simplex tangent Jacobian eigenvalue multiplicities, four symbolic gradient identities, 40 rational Lyapunov inequalities, and the exact three-opinion coexistence example. The executable checks passed at packaging. The quantified all-dimension argument, the nonhyperbolic endpoint conclusions, and global convergence rely on the written proof rather than finite tests. No external or independent audit has been performed.
