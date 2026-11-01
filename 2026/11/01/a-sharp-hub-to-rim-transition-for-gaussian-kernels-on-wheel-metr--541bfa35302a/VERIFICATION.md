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

# Verification record

The complete graph distances and the full Fourier/block decomposition are reproduced explicitly in `RESULT.md`. All-order correctness rests on the spectral identities, the unique-root arguments, the rational sign comparisons, and the implicit-function calculation, not on the checker output.

Run `python check.py` with Python 3, NumPy and SciPy. The checker exercises orders \(4\) through \(120\), confirms semidefinite/indefinite separation at nearby parameters and critical nullity, and checks exact rational inequalities. It also samples the cubic root expansion at three large orders. The observed run passed 351 symmetric-eigenvalue tests and the rational certificates.

Limitations: finite tests do not enumerate all orders, and floating eigenvalues have finite precision. The independent audit status is not performed.
