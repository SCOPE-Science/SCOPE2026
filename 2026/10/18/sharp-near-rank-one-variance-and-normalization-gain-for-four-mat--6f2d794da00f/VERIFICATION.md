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

# Reproducible checks and limits

The executable `verify.py` uses only Python, NumPy and SciPy. From the directory containing the file, run `python verify.py`; versions and minimal dependencies are specified in `requirements.txt`. The saved output is `verification_output.txt`.

The checker reconstructs the two original XTrace trace estimates using direct vectors, orthogonal projections and quadratic forms, rather than evaluating only the asymptotic formulas. It also computes the independent one-probe conditional-variance integrals through the beta distribution \(X^2/(X^2+R^2)\sim\operatorname{Beta}(1/2,(n-1)/2)\), checks the \(\varepsilon\)-scaled singular coefficient, and computes rare-event probabilities from the exact folded-Gaussian interval condition. The tested dimensions are \(2,3,4,6\), with positive \(\varepsilon\) values down to \(0.001\); six simulation configurations use 600,000 paired Gaussian samples each, with seeded random generation. All programmed assertions passed in the recorded execution.

**Interpretation:** Finite quadrature and Monte Carlo corroborate the derived finite-parameter identities. They do not prove the \(\varepsilon\downarrow0\) limit or exclude all alternative literary sources. The proof in `RESULT.md` supplies dominated convergence, the exact spherical conditional variance, and an analytic bound on the dependence of the two leave-one-out terms. No separate expert or independent audit has been performed. Numerical values may vary slightly with the installed floating-point library and random generator, within the stated assertion tolerances.
