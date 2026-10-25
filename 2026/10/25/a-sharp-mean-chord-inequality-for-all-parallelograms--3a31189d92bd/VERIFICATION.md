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

The complete analytical argument is in `RESULT.md`. To reproduce the key formulas, first use polar coordinates about an arbitrary point to convert angle-uniform chord averages into the inverse-distance potential divided by \(\pi\). Next apply layer cake and planar Brunn–Minkowski to the intersection of each centered disk with the symmetric parallelogram, which yields a strict maximum at its center. Horizontal interval rearrangement removes shearing while lowering perimeter. Verify the rectangle potential \(2[a\operatorname{arsinh}(h/a)+h\operatorname{arsinh}(a/h)]\) by differentiating the positive-quadrant integral formula. Weighted strict Jensen for \(\operatorname{arsinh}\) supplies the sharp square equality.

For an optional numerical check, run `python check_parallelogram.py` with NumPy and SciPy installed. The code quadratures sheared and rectangular examples and confirms the fixed-perimeter bound; it uses a cutoff near the integrable slice singularity and therefore is not a rigorous certificate. The proof itself is independent of finite experiments. These checks do not constitute independent auditing.
