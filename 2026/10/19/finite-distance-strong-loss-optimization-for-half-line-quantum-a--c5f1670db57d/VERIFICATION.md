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

# Reproducibility of the half-line absorption optimum

The included `verification.py` independently evaluates the stated integrals and their first derivatives by high-precision adaptive numerical quadrature. It compares the reciprocal-asymmetry identity, calculates finite-distance optimal rates with scalar root-finding, checks the leading \(3/4\) coefficient, and reconstructs the survival amplitude from the finite-truncation non-Hermitian Hamiltonian using sparse matrix exponentiation.

Dependencies are listed in `requirements.txt`; run `python verification.py` with numpy and scipy installed. An actual execution returned:

`VERIFY_OK 244 direct integral, derivative, asymptotic and time-domain comparisons`

The finite-truncation flux integral agrees closely with, but does not exhaust, the exact infinite-time probability; its remaining positive tail is not certified by the experiment. Numerical data provide consistency checks only. The proof of the exact all-distance and asymptotic statements appears in `RESULT.md`.
