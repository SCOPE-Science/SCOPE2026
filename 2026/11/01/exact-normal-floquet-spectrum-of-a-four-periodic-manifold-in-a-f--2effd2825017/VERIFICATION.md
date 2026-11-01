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

# Mathematical verification

The 20-dimensional history-map derivative was reconstructed independently in the variables of logarithmic perturbation. The four output recurrences and the sixteen history shifts uniquely determine its sparse matrix. All four coefficients are identical on each positive four-periodic state because the product constraint forces denominator one.

To reproduce, run `python verification/check_floquet.py` from the package root with SymPy installed. The checker verifies the full one-step characteristic polynomial, the fourth-iterate characteristic polynomial, the exact two-eigenvalue annihilator, trace and rank, and two parameter specializations. The executed checker printed all five PASS lines and raised no assertion.

The matrix calculation is an exact symbolic certificate for the derivative. Completeness of the periodic manifold, semisimplicity for all admissible parameters, and nonlinear local attraction/instability depend on the separate analytic proof in RESULT.md. Symbolic checks do not replace a proof of convergence for the nonlinear system. The excluded value \(p=1\) is a true spectral degeneracy, not a proved dynamical boundary classification. No independent audit has been performed.
