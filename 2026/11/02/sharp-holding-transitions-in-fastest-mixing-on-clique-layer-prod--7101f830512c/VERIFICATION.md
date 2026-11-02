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

# Reproduction and scope

Run `python fmmc_clique_layers_verify.py` using the dependency versions or compatible versions listed in `requirements.txt`. The program executes the full transition-matrix eigenvalue checks, a separate linear-programming optimizer, feasible asymmetric perturbation checks, independent Johnson graph construction, and exact symbolic rational inequalities.

Successful local execution reported `PASS {'matrix_spectra': 95, 'linear_programs': 126, 'asymmetric_tests': 504, 'cycle_parity_tests': 91, 'johnson_spectra': 20, 'exact_rational': 90}`.

All comparisons use finite instances or exact identities restricted to selected integer parameters. The universal claim is proved by convex symmetry averaging, the product spectrum, and the minimax lower bounds in RESULT.md. The program does not certify uniqueness of unrestricted global optimizers or exhaust all finite graphs.
