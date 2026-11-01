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

# Reproducible checks

Execute `python verify.py` using a standard Python 3 interpreter. The script checks the exact rational attention weights, normalization scale, Floquet blocks and threshold for a three-dimensional example; it evaluates the *original normalized residual update* at both labeled cycle states; compares the four tangent derivative columns with centered finite differences; and tests the scalar strict-stability equivalence over 750 exact rational parameter settings.

The script prints a `PASS` line or raises an assertion error. Exact arithmetic is used for the critical Floquet and threshold identities. Only the finite-difference diagnostics use standard floating point; none is treated as proof of the infinite parameter classification.

# Mathematical limits

The theorem follows from analytic block decomposition and strict inequalities. It is local, does not determine nonhyperbolic nonlinear behavior at equality, and does not establish global attraction, uniqueness of periodic dynamics, or historical priority. Independent audit has not been performed.
