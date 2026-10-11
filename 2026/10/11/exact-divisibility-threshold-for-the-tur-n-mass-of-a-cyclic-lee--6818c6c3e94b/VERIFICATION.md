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

# Reproducible verification

Run `python checker.py` from the directory containing the file, using Python 3 and only its standard library. The expected final line begins `CHECKER_PASS`.

The script directly enumerates exact integer cyclic difference multiplicities for the five-point cross on all orders \(5\) through \(40\); verifies its thirteen-point difference support and autocorrelation values; checks the sharp algebraic pentagonal contact identities numerically; tests the predicted cyclotomic Fourier-zero coordinates and explicit positivity-preserving perturbations for all orders \(5\) through \(240\); and verifies by `fractions.Fraction` every Fourier inequality at the sixteen ordered cosine pairs for the exact \(n=6\) witness \((a,b,c)=(3/7,2/7,3/7)\), whose counting mass is \(39/7\).

The infinite proof instead follows the Fourier identity, exact sampled dual inequalities, the full published Lam–Leung short vanishing-root-sum theorem (Theorem 3.3, Corollary 3.4, Theorem 4.8), and strict finite-grid perturbation arguments. Numerical tolerances in grid tests are never substituted for those analytic arguments. Reproduction does not establish bibliographic uniqueness or independent validation.
