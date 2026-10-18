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

# Verification of the orientation-rigidity theorem

Run `python verify.py` with Python 3, NumPy, and SymPy. The standalone script proves no statement by sampling: it tests exact symbolic formulas and uses numerical cases only to compare the first-order limits against direct symmetric eigensolvers.

Observed successful replay: balanced compression and orthogonal leakage squared formulas are exact symbolic identities; coordinate-probe residual identities are exact; there are 288 direct perturbation comparisons across balanced, unbalanced, and coordinate normals, two small amplitudes and fixed random diagonals; five independent-seed Monte Carlo CDF comparisons each use 600,000 samples and satisfy tolerance 0.004. The analytic proof in RESULT.md alone addresses all normals and all permitted perturbations and supplies the cube-volume calculation.

Critical assumptions: the perturbed top eigenvector is spectrally isolated by the unit unperturbed gap; the two smaller eigenvalues may coincide. The finite-amplitude comparisons test only the expected \(O(\varepsilon)\) normalized error, not exact finite-amplitude equality. The known marginal CDF holds on the stated lower branch only. No independent mathematical audit has been performed.
