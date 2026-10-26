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

# Reproducibility and verification

Run `python3 verify.py` in a directory containing that file. `verification_output.txt` records the actual results. These checks require only the Python standard library. Exact rational operations tested negative and positive covariance examples for every integer from 2 through 20; a separate integer-composition dynamic program approximated uniform circular spacings for sizes 3, 4, 5 at two lattice resolutions; numerical roots for sizes 2, 3, 4, 5, 10, 25, 50, 100 were checked against the exact formula and the asymptotic prediction.

The executable computations **do not certify infinitely many cases**. The analytic proof in RESULT.md establishes the universal strict one-zero classification through a derivative sign factorization and establishes critical-size asymptotics by a uniform expansion and simple-root perturbation. There is no independent audit or external theorem certification.
