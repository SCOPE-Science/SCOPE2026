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

The proof uses exact finite-isometry quotient distances, Haar pushforward under a surjective sum–difference endomorphism of a torus, Prékopa's marginal log-concavity theorem, strict Karamata majorization, planar circular-segment area, and a local simplex limit at the corners of a rectangular nearest-lattice-point cell. These are analytic arguments for the stated all-dimensional quantifiers, not extrapolations of finite tests.

The bundled `verify.py` was run with Python 3, NumPy, and SciPy. All 2,241 deterministic threshold checks passed, and four 150,000-pair ensembles matched the predicted CDF and integrated second moment within the stated tolerances. The test covers sample dimensions and parameters only. It cannot certify historical novelty or the analytic prerequisites.

For the upper tail, the verifier computes the square of the torus survival directly. Subtracting the already-near-one quotient CDF from one would lose relative accuracy, and such cancellation must not be mistaken for disagreement with the asymptotic formula.

The 1973 Prékopa source has a year-level bibliographic date; no exact original day is asserted. The arXiv first-public source used for the reproducible day-resolution archive metadata is 2005-05-25. Independent audit remains unperformed.
