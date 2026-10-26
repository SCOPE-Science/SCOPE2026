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
# Verification

The differential-equation model is completely specified in `RESULT.md`. For every \(5\le N\le42\), `verify.py` computes the unique stationary point of the scalar branch function, compares it with the right-angle endpoint, and samples three values strictly inside the stable-obtuse window. Both fold-side solutions are reconstructed from the actual current and tested using a directly assembled matrix Laplacian. The predicted stable branch has one zero eigenvalue and all other Laplacian eigenvalues positive; the opposite fold branch has a negative Laplacian eigenvalue. The right-angle endpoint is tested as a path of positive conductances. Three large sizes test convergence to the stated transcendental constant. The observed output is:

```text
VERIFY_OK n_range=5..42 checks= 1447 constant= 4.603338848751704
```

The tests are floating-point, finite and dependent on NumPy. They are not exhaustive over all phase configurations, and neither they nor an unverified publication search independently certify correctness or historical originality. The mathematical proof is the cycle-current reduction, signed quadratic-form analysis, strict log-convexity and winding exclusions in `RESULT.md`. Independent audit remains unperformed.
