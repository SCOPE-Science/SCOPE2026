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

# Reproduction and limits

Run `python3 check.py` in a standard Python 3 environment. The checker evaluates the quintic polar-to-Cartesian polynomial identity at 243 parameter-point combinations; it verifies eight exact rational coefficients of the common local area series and 21 independent discrete angular moment checks against their exact limiting values. These finite checks do not establish the theorem. The proof in RESULT.md separately establishes all quantified infinite statements through analytic radial inversion, angular averaging, Hamiltonian coarea, and local saddle asymptotics. Full-text publication priority and independent proof review remain unperformed.
