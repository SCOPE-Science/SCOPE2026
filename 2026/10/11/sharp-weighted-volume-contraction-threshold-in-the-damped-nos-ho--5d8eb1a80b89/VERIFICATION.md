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

# Reproducibility and verification
The standalone symbolic test `proof_check.py` uses SymPy and can be executed with `python proof_check.py` in the package directory. It verifies the vector-field divergence, exact quadratic coboundary, weighted-divergence residual, nonzero-equilibrium coordinates and characteristic polynomial with exact symbolic operations. The script was actually executed; it does not certify invariant measures, general trajectory existence, Oseledets hypotheses, or bibliographic exhaustiveness.

The analytic proof in `RESULT.md` establishes the required non-algebraic statements: Liouville's flow-Jacobian identity, the compact-set bound on the coboundary, the invariant-integral cancellation, the orbitwise equality rigidity, and the ergodic Lyapunov-sum formula. These are mathematically distinct from the checked symbolic identities and do not follow merely from executing the script. The finite-time identities hold on existing solution intervals; noncompact initial data are not assumed to have global solutions.

The originality comparison uses the full-text 2014 and 2015 primary accounts of the same damped oscillator as well as a related 2022 quadratic-oscillator paper. An equivalent overlooked source remains a residual risk. Independent audit has not been performed.
