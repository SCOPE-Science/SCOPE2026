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

Execute `python3 check.py` in an environment with NumPy and SciPy. The script uses a fixed pseudorandom seed and runs 443 tests across small Johnson networks, including exact expected Boolean inclusion ranks, eigenvalue classifications, projectors, nonuniform positive detector rates, long-time conditional propagators, coherent unmonitored inputs, and arbitrary Hermitian detector-sector perturbations.

The final output in the checked environment was:

`PASS 443 finite checks including arbitrary detector-side Hermitian perturbations; worst numerical error 2.226e-14`

The checker has no required file inputs and does not assert an infinite-dimensional or all-parameter computational certificate. The dimension-independent theorem is established in the analytical proof in `RESULT.md`; the finite tests can catch implementation, normalization and boundary errors, not prove universal quantifiers.
