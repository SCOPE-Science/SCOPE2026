---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and scope

Execute the unchanged `check.py` with `python3` in an environment with NumPy and SciPy. The script uses a fixed pseudorandom seed and runs 443 tests across small Johnson networks. These include numerical comparisons with the expected exact Boolean inclusion ranks, eigenvalue classifications, projectors, nonuniform positive detector rates, long-time conditional propagators, coherent unmonitored inputs, and sampled real-symmetric detector-sector perturbations. The checks do not cover all Hermitian perturbations or measure finite-time capture with every configuration monitored; those statements follow from the analytical argument in `RESULT.md`.

The final output in the checked environment was:

`PASS 443 finite checks including arbitrary detector-side Hermitian perturbations; worst numerical error 2.226e-14`

The checker has no required file inputs and does not assert an infinite-dimensional or all-parameter computational certificate. The dimension-independent theorem is established in the analytical proof in `RESULT.md`; the finite tests can catch implementation, normalization and boundary errors, not prove universal quantifiers.
