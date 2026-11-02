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

# Finite reproducibility checks

Run `python3 verify_cubic.py` using only the standard Python library. The exact-rational test compares both presentations of the Walsh-kernel L1 norm for all dimensions from 3 through 400, including cases where the inner or outer root crosses the parity lattice. The second test uses the complete normalized binomial law in logarithmic arithmetic at 8 large even and odd dimensions and compares against the dimension-dependent predicted phase. Symbolic Gaussian integration was separately used to verify the continuum constants.

These are finite diagnostics. They cannot establish the all-dimensional telescoping identity or the asymptotic error bound, which are proved in RESULT.md. The phase asymptotic is established by a uniform Stirling/Edgeworth expansion, a cusp-aware Euler summation, and separate parity subsequence density. No independent audit is claimed.
