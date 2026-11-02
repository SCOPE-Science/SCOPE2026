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

# Verification notes

The analytic proof is in `RESULT.md`. The standalone `check_fpfm2.py` requires Python 3 and `mpmath`; run `python check_fpfm2.py` from the directory containing the extracted files. In the supplied environment it printed `PASS 882 high-precision conditions` and the high-precision critical parameter. It constructs each allowed two-cycle from a unique scalar root, checks its direct two-step return, and recomputes smooth return Jacobians rather than trusting a tabulated result.

The count is not inferred from the finite tests. The independent analytic implication \(|v|+|v+u|=\ell_\beta\), followed by its three exhaustive sign cases and monotone scalar root equations, supplies global completeness and exact boundary counting. Schur inequalities are checked symbolically in the proof. Numerical root tolerances only affect the reproducibility tests, not the theorem.

The public source is Almatroud–Pham (2023), Section 4, Equation (8), doi:10.3390/math11061319. The closely related Ramadoss et al. (2022) NFP2 formula uses constant forcing. The principal scientific limits are longer periods, nonsmooth-boundary derivative claims, publication-priority risk, and absent independent mathematical validation.
