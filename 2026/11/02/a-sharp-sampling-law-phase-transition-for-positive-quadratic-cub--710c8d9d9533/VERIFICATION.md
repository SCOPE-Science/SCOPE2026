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

# Verification of the arcsine-node quadratic cubature law

The theorem is proved analytically in `RESULT.md`. The independently structured numerical checks in `verify.py` require Python 3.10+, NumPy and SciPy (`scipy.integrate.quad`, `scipy.optimize.linprog`). Run `python verify.py` in a directory containing the extracted files. This verifier makes no network calls and uses a fixed random seed `20261031`.

The verifier passed **1,257 checks**: 45 probability-integral range tests for distinct sample counts and target second moments, 10 sharp-rate coefficient checks, 1,200 independent finite-node linear-program feasibility comparisons against the geometric criterion, and 2 critical-identity/sample-budget checks. For each finite-node comparison, the target moment constraints \((1,0,q)\) are submitted directly to a linear-program solver, with a small positive lower bound on every weight and explicit residual validation. Computations used double precision; proximity to a positivity boundary could affect feasibility in other samples. The analytical criterion avoids this numerical qualification.

Additional separate double integrations for \(q\in\{1/5,1/3,7/10\}\), sample counts \(m\in\{2,3,4,5\}\), and the pair-extremum formula agreed with the two one-dimensional failure integrals to within \(3\times10^{-14}\). At the uniform target, the predicted sharp constants are \(r_*=0.6081734479693928\ldots\) and \(C_*=0.8804063044373697\ldots\). For \(m=240\), the computed failure divided by \(\sqrt m r_*^m\) was \(1.011889629465945\ldots\), approaching the predicted constant; this finite result by itself would not prove convergence.

Limits: no proof assistant, interval-certified numerical integration, independent expert audit, floating-point stability guarantee, or claim for degree greater than two is supplied. The derivation of the constants, probability formulas and phase transition must be evaluated from the written proof; the executable tests are supplementary.
