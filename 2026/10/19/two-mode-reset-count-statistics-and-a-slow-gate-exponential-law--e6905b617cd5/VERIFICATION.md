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

# Mathematical and computational verification

The analytic argument directly solves the pair of backward boundary-value equations, checks \(F_A(1)=F_I(1)=1\), proves positive distinct characteristic roots below one, and proves that numerator-denominator cancellation is impossible in the stated open parameter domain. The slow-gate Laplace convergence follows from first-order expansions of the exact rational generating function and uniqueness of the Laplace limit.

To reproduce numerical cross-checks with NumPy and SciPy, run `python verify.py`. The script independently approximates the coupled absorbed Markov generator using centered finite differences, checks the generating function at 12 test points, verifies three discriminant identities and ordered roots, and reports fast- and slow-gating convergence. Finite spatial cutoffs and discretization are not proofs; all-parametric assertions are justified analytically in the accompanying result. No independent external audit or formal proof certification is claimed.
