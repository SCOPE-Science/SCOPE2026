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

The self-contained `verify.py` uses NumPy and SciPy. Run from its directory with `python3 verify.py`.

Observed output from execution of the package source:

```text
PASS: 182 checks; exact compact modes and independently reconstructed finite graph spectra.
```

Checks include direct sparse-matrix construction for seven distinct combinations of wire number and separation, comparison of positive and negative exterior eigenvalues against analytical scalar-root solutions, exact compact-eigenstate residuals for the finite paths, and broad monotonicity stress tests. The truncation has 80 outer vertices per ray and is a numerical approximation for exterior eigenvalues, not an infinite-volume spectrum certificate. The exact enumeration and threshold conclusions rest instead on the Dirichlet recurrence and increasing Schur-complement proof in `RESULT.md`.

Scientific limits: the operator is the discrete adjacency Hamiltonian on the precisely defined two-junction infinite graph. The source-priority comparison remains subject to a relevant inaccessible waveguide paper and possible implicit consequences of general graph spectral theory. There is no independent mathematical audit or external validation.
