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

# Verification of the geometric claims

Execute `python3 verify_parallelotope.py` with stock Python 3. The script uses a direct Gaussian-correlation/arcsine computation and a separate independently constructed spherical solid-angle calculation of all eight cones, and independently counts plane-cube edge intersections under Gaussian normal sampling. The checks cover seven valid equiangular parameters, one nonequiangular matrix, and numerical comparisons of the analytic derivative. The last line on successful execution is `VERIFY_OK`.

Finite random sampling and finite arithmetic comparisons are consistency checks only, not an infinite-domain proof. The proof in RESULT.md establishes the full exact formula and the monotonicity sign without sampling. The independent scientific review and final historical-priority assessment have not been performed. Voss (1982) could not be accessed in full and remains a material originality qualification.
