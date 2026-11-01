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

Execute `python3 verify_triangle_moments.py` in this directory using Python 3.10 or newer. This script uses only Python standard-library modules. It independently expands the Dirichlet mixed-moment factorial sum as a polynomial in the squared side lengths, verifying the exact coefficients of the second, fourth and sixth distance moments over rational arithmetic; it also verifies inverse reconstruction on a strict scalene triangle and the two-moment counterexample with cubic separation. The script prints `ALL_CHECKS_PASSED` if every exact assertion succeeds.

The analytic proof in `RESULT.md` establishes arbitrary-triangle correctness and the uniform root-stability bound. Computational checks are finite exact algebra, not a stand-in for the complex-analytic Rouché argument. The inputs are independent area-uniform points, not chord samples; first moment \(m_1\) here means the second raw moment of Euclidean distance. This review is not independent certification, and historical-priority uncertainty concerning earlier chord-recognition literature remains.
