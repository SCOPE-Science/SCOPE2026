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
# Reproducibility and verification

The included `verify.py` uses only Python standard-library modules. Run `python verify.py`; successful execution ends with `VERIFICATION_OK`. It enumerates both shear propagators over all selection strings of lengths \(0\) through \(7\), using \(z\in\{0,1/2,2,5/3\}\) and initial vectors \((1,0)\), \((1,2)\), and \((3,-4)\). For each string, both exact rational mean-square norm and mean-vector norm are calculated without any Monte Carlo approximation. All \(192\) expected identities passed. It also checks the critical transcendental root numerically and the explicit exact comparison \(2/e<1<3/e\). The damping factor is symbolically factored out of the exact rational checks.

The **infinite-horizon argument is analytic**, not a numerical extrapolation: direct matrix multiplication gives the conditional quadratic factor for every state; induction gives the identity for all integers \(k\ge0\). The derivative of \(\log(1+z^2/2)/z\) determines the unique global extremum, and comparison with the damping line gives the full classification for all positive steps and all positive shear/damping ratios. The numeric approximations to the critical ratio do not certify an isolated root on their own; uniqueness follows instead from the displayed exact derivative sign.

Known limits: no independent audit, no computer-assisted infinite proof, no stochastic-path Lyapunov exponent, and no claim of useful accuracy on the coarse stable branch. The explicit analytic source and complete matrix conventions appear in `RESULT.md`.
