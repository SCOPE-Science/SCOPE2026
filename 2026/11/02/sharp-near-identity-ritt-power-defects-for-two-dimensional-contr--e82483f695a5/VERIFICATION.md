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
Execute `python3 check_ritt.py` in an ordinary Python 3 installation. The checker contains the exact finite-power formula and a separate direct triangular-matrix singular-value calculation, comparisons for five gap sizes and five couplings, stationary-equation tests, dense finite envelope samples, the quartic special case, and the weak/strong coupling checks. It reports `CHECK_OK 154820 finite assertions`, `sharp_contracting_boundary= 0.6794006077854641`, `peak_scaled_time= 2.395336994467073`, and `large_c_slope= 0.3090047859876757`.

The proof in `RESULT.md` supplies the exact global optimization and uniform infinite-horizon bounds. The finite computations cannot establish a global maximum or certify originality. No external independent mathematical audit is represented by this file.
