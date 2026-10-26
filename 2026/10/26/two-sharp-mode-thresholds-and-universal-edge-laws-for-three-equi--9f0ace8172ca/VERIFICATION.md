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
The principal analytical checks are the exact free resolvent for the discrete Laplacian, the three eigenvalues of the mass-defect Green matrix, strict monotonicity of \(\lambda(\lambda-L)^{-1}\) outside the host band, and the second-order threshold expansions. No finite computation replaces those arguments.

Run `python3 verify.py` from the package directory with the Python 3 standard library. It uses a Dirichlet-chain Sturm inertia count at 1,201 sites for each tested parameter triple, and evaluates the two independent edge coefficients using bisection. The script prints PASS only if all specified checks succeed. At criticality a finite chain cannot by itself decide the infinite-chain square-summability question; this follows from the external recurrence in the proof.

Independent audit has not been performed.
