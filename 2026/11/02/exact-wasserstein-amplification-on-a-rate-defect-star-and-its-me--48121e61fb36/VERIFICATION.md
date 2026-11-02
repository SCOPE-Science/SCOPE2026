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

# Verification and reproducibility

The exact statement follows from the analytic two-block heat-gradient representation, comparison of the slow and ordinary row sums for both signs of \(H_{22}-e^{-t}\), and a unique critical point of a two-exponential profile. The full proof is in `RESULT.md`.

Execute `python CHECKER.py` with Python 3, NumPy, and SciPy. The script directly exponentiates the full vertex Markov generator, computes Wasserstein-one distances on the star by summing absolute differences of leaf masses, and checks the formula for each edge pair at multiple positive rates and times. It also compares the peak formula with independent scalar optimization and checks the fixed-degree logarithmic asymptotics.

The local replay passed 693 finite numerical assertions. These checks neither establish infinite-range validity independently nor constitute an external audit. In particular, the claimed analytic remainder is deduced from Taylor expansions of the exact spectral expressions, not extrapolated from samples.
