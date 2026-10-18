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

# Reproducibility checks

Execute `python3 verify.py` using Python 3.10 or later and the standard library only. The script independently constructs all \((n-1)!\) uniform recursive parent assignments for each \(3\le n\le8\) and recomputes exact leaf covariance entries. It then constructs weighted-orthogonal polynomial values over every interior lattice from \(N=2\) to \(N=15\) by rational Gram--Schmidt, checking the finite difference eigen-equation and its Green-kernel counterpart. The actual execution outcome was:

`VERIFY_OK assertions= 2617 recursive_trees_through_n=8 polynomial_spectra_through_N=15`

The exact finite checks corroborate the calculations only for the enumerated sizes. The proof in `RESULT.md` supplies the unrestricted self-contained argument and the continuum Riemann-sum justification. The comparison with earlier literature is a self-review rather than independent historical-priority certification.
