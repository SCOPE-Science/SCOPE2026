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

# Reproduction and evidence

## Analytical checks

The pivotal identity \(p^2(1+t^2)-(1+(t+\varepsilon)^2)=\varepsilon p(t-p^{-1})^2\) for \(p-p^{-1}=\varepsilon\) was simplified symbolically to an identically zero remainder. It gives both Rayleigh inequalities after interchange of the true and approximate factors. The explicit diagonal \(2\times2\) matrices attain both endpoints and the sharp condition-number ratio simultaneously. An exact SPD similarity provides the induced energy-norm contraction. The scalar right-hand side \((-aR,R)\) is an inconsistent system with minimizer zero, and an exact quadratic objective expansion verifies ascent for every strictly positive step along the mismatched correction for suitable arbitrarily small starting error.

## Executable checks

The standalone `verify_row_split.py` program depends on Python 3 and NumPy. Run it from this package's directory using `python3 verify_row_split.py`. It executes deterministic trials over four upper-block sizes, three trailing-block sizes, six perturbation magnitudes and 70 random trials per configuration. It checks the generalized eigenvalue interval and fixed-step worst-case bound, then tests the exact two-dimensional extremizer for six errors and nine scalar biased-residual examples. The run executed successfully and printed `PASSED 15198 checks`.

## Limitations of verification

The finite random experiments are not an exhaustive proof, and numerical eigenvalue computations have floating-point tolerances. The symbolic step checks one algebraic identity, not all quantifiers. All universal conclusions are proved in RESULT.md. No external or independent audit, code certification, or experimental evaluation of incomplete-factorization applications has been performed.
