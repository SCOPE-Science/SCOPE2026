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

# Reproducible checks and proof boundaries

Run `python check_quantization.py` with Python 3 and NumPy. The checker directly tests seven gap parameters, 3,500 arbitrary competing four-level outcome supports, and 450 randomized positive-operator measurements with generally noncommuting effects, for 3,957 grouped test cases. Execution passed all grouped cases. It verifies formula identities, exact first-moment reconstruction for finite diagonal observables, and finite-matrix Loewner inequalities used in the proof.

The proof for any bounded self-adjoint operator with the stated full two-band spectrum relies on functional calculus, adjacent-node nonnegative polynomial certificates, and elementary four-node minimax inequalities. No finite numerical experiment is used as a substitute for that infinite-dimensional argument. The program is not an exhaustive search of all supports and does not independently validate publication priority or certify external mathematical correctness.
