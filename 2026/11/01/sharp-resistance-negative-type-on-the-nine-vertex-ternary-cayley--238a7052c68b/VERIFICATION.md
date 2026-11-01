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

# Reproducibility and limits

Execute `python3 verify_ternary_resistance.py` using Python 3 and its standard library. The implementation constructs the nine-by-nine weighted Laplacian, inverts its constant-mode-regularized version in exact rational arithmetic, computes every pairwise effective resistance, and verifies each of the four two-dimensional Fourier sectors of the powered-distance matrix at the integer exponents 1, 2 and 3. It verifies the sharp eigenvalue lower bound and the equality case for 16 explicit connected weight profiles, including zero and rational conductances. Its final lines read `ALL_TERNARY_RESISTANCE_CHECKS_OK profiles= 16` and `CARTESIAN_TORUS_OK exponents log(2)/log(5/4), endpoint_Gram_rank=4`.

The analytic argument in `RESULT.md`, not the enumeration, proves the universal inequalities for all nonnegative conductance profiles with at least two positive entries and all real exponents. The date and bibliographic comparisons are based on identifiable public records; full inspection of one particularly relevant 2011 paper remains unavailable. No independent mathematical validation has been performed.
