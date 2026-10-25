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
# Reproducibility and limits

Run `python work_variance_checker.py` with Python 3, NumPy and SciPy (SymPy optional). A direct run produced `PASS: 648 independent-generator cases, 3889 checks` with SymPy installed. The checker constructs the full polynomial-generator matrix separately from the closed-form claimed variance; it checks mean, variance, stationary moments, independent energy-martingale covariance and positivity at 648 parameter configurations including full resets and the exact critical factor. It uses `scipy.linalg.expm`, not Monte Carlo.

The proof in RESULT.md establishes the theorem for every \(D,r,\kappa>0\), every \(q\in[0,1)\), and every finite \(T\ge0\); finite checks cannot certify a universal theorem. The central-limit and infinite-positive-moment statements are analytically proved, not inferred from the finite computation. Independent audit and independent mathematical validation have not been performed.
