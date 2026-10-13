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

# Verification of the Haar amplitude-damping survival law

Execute `python3 verify.py` from the directory containing this document, after installing `requirements.txt`. The ordinary Python checker reconstructs the Kraus-operator output, evaluates concurrence directly from the spin-flip spectrum, and independently checks the sign of the least partial-transpose eigenvalue. It samples 400 Haar inputs across five visibilities, evaluates the two analytic forms of the exact one-dimensional integral at four points, compares predictions with three seeded large-Gaussian-ensemble frequencies, and checks both endpoint expansions.

Observed output from an execution of the embedded file:

`VERIFY_OK direct_concurrence_and_PPT=400 quadrature=4 Haar_ensemble=3 time_limits=4`

The nonstandard analytic steps needed for the universal statement are displayed in `RESULT.md`: the spin-flip singular-value reduction; the conditional complex-Gaussian law of the determinant; the gamma-two Laplace transform and independent uniform beta ratio; and explicit integration and Taylor expansions. The checker is finite numerical corroboration and does not certify equality for all states or all visibilities. Random-sampling failures or small numerical residuals cannot establish the absence of a theorem; neither literature discovery nor publication priority is assessed by this checker.

The limiting survival probability at positive visibility is deliberately distinguished from physical output entanglement at exactly zero visibility: the latter is identically zero. No external formal-proof certification, experiment, or independent audit has been performed.
