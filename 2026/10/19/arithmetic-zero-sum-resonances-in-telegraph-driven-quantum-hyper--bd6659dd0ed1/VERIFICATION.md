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

The analytic statement follows from the telegraph forward generator, direct tensor-product propagation and finite-group Walsh inversion. The proof establishes every dimension and every positive real weight vector without relying on numerical searches.

The included standalone script `verify.py` constructs the exact two-condition density-operator Liouvillian of a common random telegraph fluctuator by Kronecker-product Hamiltonian matrices, propagates it using SciPy matrix exponentials, and compares its output site diagonal against a **separate** scalar telegraph-characteristic-function and Walsh calculation. Run `python verify.py` after installing the libraries listed in `requirements.txt`.

Observed output:

`VERIFY_OK dense_state_probabilities= 96 limit_profiles=5 slow_resonance=1 optimum_grid=7 max_error= 5.55e-16`

Checks span unequal and equal weights, three-site resonances, perturbed resonances, five exact limiting site distributions, the two-body-invisible parity law, a near-resonance asymptotic constant, and distinct trial switching rates on both sides of the optimal threshold. This is a reproducibility check, not infinite verification or independent validation. No claim of formal certification or external review is made. Critical analytic steps are given in `RESULT.md`; the local numerical and symbolic floating-point checks do not bound every parameter or prove publication priority.
