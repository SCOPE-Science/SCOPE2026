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

# Reproducibility and verified scope

Run `python3 check_beta_hausdorff.py` with Python 3 standard library; no external dependencies or numerical input files are required. The script performs 96 exact-rational row consistency/normalization checks, 25 comparisons of floating row recurrences with finite exact fractions, several illustrative critical-window calculations, and a finite Cesàro harmonic-identity check.

The proof does not infer uniform or infinite statements from these finite computations. The analytic certification steps are the exact gamma reduction, the three separate regularly varying convolution asymptotics, the hypergeometric endpoint series value, and the moving-parameter uniform `O_R(1/n)` row bound. The last has to be read with fixed `R>0` and `N` sufficiently large so both beta parameters remain positive. These computations do not verify bibliographic novelty or replace independent mathematical review.
