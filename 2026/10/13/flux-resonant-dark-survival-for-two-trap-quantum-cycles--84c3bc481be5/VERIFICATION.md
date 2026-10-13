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
# Reproducibility and scope

The analytical proof establishes the result for every integer cycle size \(n\ge3\), integer separation \(1\le d<n\), every real flux modulo one, every initial site, and all strictly positive absorption strengths. The attached `verify.py` is a finite independent implementation for identifying errors in the eigenmode classification or normalization. It is not an infinite proof or independent scientific audit.

Run `python3 verify.py` using Python 3 with NumPy and SciPy. The verifier constructs the matrix \(H_\alpha\) in the site basis, diagonalizes it numerically, obtains the subspace annihilated by the two sink-site amplitude maps via numerical null spaces, and tests dimensions and all diagonal projector elements. It covers 825 parameter triples with \(3\le n\le24\), all separations, and \(\alpha\in\{0,\tfrac12,0.113\}\). Seven tests independently propagate the full dissipative \(K_\alpha\) for long finite times with different positive sink rates, comparing the measured survival to the predicted limit.

The observed output is:

```
VERIFY_OK independent_eigenspaces= 825 matrix_semigroups= 7 trapping_formula=passed
```

Numerical eigenspace tolerances are finite and can be unreliable at sizes or fluxes too close to the exact degeneracy boundaries. The theorem does not infer uniform convergence rates from any finite-time check. The proof's exact integer divisibility and finite Fourier sums are the sufficient basis for its global assertion.
