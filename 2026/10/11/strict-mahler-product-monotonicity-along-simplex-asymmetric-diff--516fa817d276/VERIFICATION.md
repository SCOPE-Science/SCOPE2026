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

The accompanying `verify.py` requires Python 3, SymPy, NumPy and SciPy. Invoke `python3 verify.py` in the directory containing the script; the observed output for this package was `VERIFY_OK 2292`.

Exact symbolic tests cover dimensions \(2\) through \(12\), proving the identities for those specified finite dimensions by rational-polynomial arithmetic; the root inequalities are checked numerically through dimension \(64\), and direct convex-hull and halfspace calculations test the two volume formulas through dimension \(4\). No finite run proves the all-dimensional assertion; the analytic proof in `RESULT.md` uses the already established Stieltjes zero-comparison theorem (Marcus–Spielman–Srivastava, *Finite free convolutions of polynomials*, Theorem 4.22), positive-Jacobian chamber integration and a pairwise logarithmic-derivative sign comparison.

Independent validation has not been performed. Reproduction requires the stated ordinary open-source mathematical libraries; the script makes no network requests and needs no external data.
