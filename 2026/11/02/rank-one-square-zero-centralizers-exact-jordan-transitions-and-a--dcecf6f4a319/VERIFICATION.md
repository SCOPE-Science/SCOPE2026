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

## Reproduction
Run `python verify.py` and `python verify_ambient.py` in the same folder using Python 3.8 or newer. Both are standard-library-only scripts. The first runs 90 exhaustive tensor-parameter cases over fields of sizes 2, 3, 4 and 5; the field of size four is implemented as a quadratic extension. It reconstructs Jordan matrices and all candidate rank-one operators, checks operator multiplication and ranks directly, and compares three rank-change counts to the closed formulas. The second checks eight complete ambient matrix spaces (not just the tensor-parameter locus) over fields of sizes two and three.

The expected final markers are `RANK_ONE_NILPOTENT_PERTURBATION_OK 90_EXHAUSTIVE_PARAMETER_CASES` and `AMBIENT_RANK_ONE_SQUAREZERO_CENTRALIZERS_OK 8_COMPLETE_MATRIX_SPACES`. The exact observed outputs are embedded as `verification_output.txt` and `ambient_output.txt`. Checks were executed from these accompanying scripts.

## Scope of evidence
The finite tests do not establish the infinite family of formulas or the algebraic-geometric irreducibility statements. These follow from the rank-one update criterion and the incidence-cone proof given in `RESULT.md`. The experiment also does not establish publication priority. No independent mathematical audit has been performed.
