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

# Reproduction and limits

Run `python verify.py` in the directory containing this file and `verify.py`, with Python 3, NumPy, and SciPy installed. The program independently integrates finite-dimensional survival using a complex Lyapunov solver and compares against the closed formulas for multiple odd rings and parameter values, including both orientations of flux, every source site, and the optimizing-flux transition. It also checks the discrete Fourier identity underlying the exact coefficient.

These are finite numerical checks, **not** a substitute for the full arbitrary-odd-size proof in `RESULT.md`. The computation does not establish historical originality and is not an independent audit. Fluxes at integer multiples of \(\pi\) and even ring orders are expressly outside the theorem.
