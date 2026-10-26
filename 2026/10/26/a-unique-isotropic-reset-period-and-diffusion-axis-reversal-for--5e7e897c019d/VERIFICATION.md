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

# Reproducible checks and limits

Run `python verify.py` using Python 3 with NumPy and SymPy. The finite verification covers symbolic harmonic identities, trace and diffusion-axis algebra, numerical SPD positivity and limiting regimes, three separate Itô-SDE Monte Carlo experiments using the original correlated rotational noise (rather than directly generating from the proved endpoint-covariance formula), and an exact finite-period isotropization witness. In the completed check the program reported **96 passed assertion groups**. Its Monte Carlo runs use 24,000 cycles and 400 steps per cycle for each of three parameter choices, with fixed seeds. Numerical tolerances reflect time discretization and sampling error; they are not substitutes for the analytical proof.

The central-limit assertion is justified by the independent finite-variance cycle displacement decomposition proved in `RESULT.md`, and is not claimed to have been checked computationally for all times. Model sources and scientific originality limitations are listed in `RESULT.md` and `REVIEW.md`.
