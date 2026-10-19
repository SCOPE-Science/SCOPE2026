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

# Reproducibility

Run `python3 verify_fourier12.py` with a standard Python 3 interpreter and no external packages. The code constructs all 495 four-row sets and their 21 affine orbits. At each representative it enumerates all 495 four-column sets and compares two exact determinant tests: 24-term integral cyclotomic reduction and four independent determinant evaluations in the finite field of 61 elements. It verifies their equivalence for all 10,395 representative/column pairs, checks every reported orbit size and defect count, reconstructs the distribution and the exact total, and checks the occupancy counterexample.

The certificate is exhaustive for the stated finite domain; it cannot justify extrapolation to larger Fourier orders, and does not test matrix conditioning. The complete execution output is `verification_output.txt`, with the final marker `VERIFY_OK orbit_count=21 levels=20 singular_pairs=40608 total_pairs=245025 fraction=1504/9075`. No independent audit is asserted.
