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

The complete analytic proof is in `RESULT.md`. Execute `python verify_discord.py` with Python 3 and NumPy. The program derives actual \(4\times4\) density matrices, confirms trace one, strict positivity and second-subsystem PPT invariance, computes Bloch components by independent Pauli traces, diagonalizes the full \(3\times3\) Gram matrix and compares against the two exact closed forms. It checks small-\(\epsilon\) normalized slope values against the derived universal crossover profile.

Successful execution:

`VERIFY_OK direct_state_matrix=42 PPT_invariant=passed local_quadratic=passed correlation_linear=passed universal_slope=passed`

A supplementary direct check on five distinct parameter pairs satisfying \(0<b<a\), \(a+b<1\) agreed with both closed forms and scaled slopes. The tests sample finitely many states and times: neither a Monte Carlo test nor a finite parameter grid proves positivity or asymptotics for all allowed parameters. Those conclusions follow from the explicit operator norm and eigenvalue arguments, and the compact-uniform expansions documented in the proof.
