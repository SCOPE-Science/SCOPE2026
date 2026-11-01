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

# Reproduction and verification

Run `python3 verify.py` with Python 3. No nonstandard modules, external files, network access, numerical optimization packages, or random seeds are required.

The actual packaged code was run successfully with output:

```
PASS: 675 dimension/radius/separation configurations.
PASS: quadratic containment maxima and isotropic contact moments.
PASS: all three geometric regimes including both sides of transition.
Finite diagnostics are not a proof of the all-dimensional theorem.
```

The diagnostic computes the candidate formulas, checks the maximum squared distance to each ball center by **analytically maximizing the exact concave quadratic** over the entire ellipsoid boundary parameter \([-1,1]\), and checks the proposed normalized contact means and covariance identities numerically. It varies the dimension, radius ratio, and separation, including positions around the transition. Its numerical tolerances are not error bounds for all real inputs.

The independent mathematical checks required for the general result are given as identities in `RESULT.md`: in the one-pole phase, an exact negative square for the smaller sphere and an endpoint maximum for the larger sphere; in the two-latitude phase, one exact negative square for each sphere; and in both phases, exact zero-mean and isotropic contact weights. Strict monotonicity of each scalar equation proves the existence and uniqueness needed by the formulas. John's characterization proves global optimality and uniqueness. Those derivations apply without numerical approximation to every stated dimension and separation.

The proof does not cover the tangent endpoint \(L=1+q\), equal-radius balls, or intersections of more than two balls. The document does not assert independent verification or historical-priority certification.
