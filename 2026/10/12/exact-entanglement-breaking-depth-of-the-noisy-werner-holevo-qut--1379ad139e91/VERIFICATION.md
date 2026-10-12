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

# Reproduction and scope of checks

The included `verify.py` uses `numpy` and Python standard-library rational arithmetic, and is run with `python verify.py` after installing `requirements.txt` in an isolated environment. It directly reconstructs the Choi matrix of every tested power using repeated channel application on the nine matrix units, compares it with the exact three-coefficient expression and compares the resulting partial-transpose eigenvalues to the analytical inequalities. The grid contains 51 noise parameters and powers 1 through 12, totaling 612 state comparisons. Additional assertions check the four product-state twirling witnesses, exact rational spectra at noise 1/2 through the fourth power, the Werner endpoint, the absence of one-use breaking on a grid, and a numerical weak-noise sequence.

Expected final output: `VERIFY_OK 612 exact matrices + PPT + pure product corners; tau 1.463405430167`.

**Mathematical limits.** Neither the grid nor floating-point spectra prove universal separability or the sharp limit. The complete invariant-rectangle separability proof, analytic spectral decompositions, and threshold-bracketing argument in RESULT.md supply those infinite-domain facts. No stability to perturbations or independent external validation is asserted.
