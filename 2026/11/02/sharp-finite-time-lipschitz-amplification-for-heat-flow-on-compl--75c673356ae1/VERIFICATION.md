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

The main claim is proved analytically in `RESULT.md`. The reproduction script `verify_heat_lipschitz.py` requires Python 3 and its standard library only. Run `python3 verify_heat_lipschitz.py`; a successful run prints `CHECK_OK exact_integer_potentials_and_spectral_matrices= 50`.

The script forms exact heat matrices at two times whose spectral multipliers are rational, independently maximizes the relevant graph-Lipschitz linear functional over integral vertices of the network-constraint polytope, and checks the closed formula in 50 cases. A separate check directly compared floating-point matrix exponentials to independent linear programs in 245 instances. Neither finite experiment establishes the infinite-dimensional-parameter result: the decomposition and upper/attainment argument in the proof does.

The normalization is essential: every incident edge has rate one, not rate reciprocal to degree. The literature coverage is assessed as qualified, and no independent scientific audit is asserted.
