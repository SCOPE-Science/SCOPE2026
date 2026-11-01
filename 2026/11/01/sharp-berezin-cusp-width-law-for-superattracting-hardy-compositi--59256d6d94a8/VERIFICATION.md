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

# Verification record

**Analytical checks.** The closed-disk estimate \(|\varphi(z)|\le|z|^m\) follows from repeated Schwarz lemma. The radial bound has uniform gap from one on every exterior annulus, including its \(2/(m+1)\) endpoint. The polar expansion is differentiable uniformly in angle on a small fixed disk, so the radial level derivative is \(2r+O(r^m)\), and no extraneous distant preimages contribute to a near-\(1\) vertical section. The compact interval and both endpoints are obtained by continuous angular images and uniform error control, not merely sampled values.

**Supplementary computation.** Run `python verify_cusp.py` with Python 3, NumPy and SciPy installed. It evaluates nonmonomial disk selfmaps of orders \(2\) through \(5\) at five positive section deficits using a radial root solver and a finite angular mesh; 44 assertions passed. These checks do not certify global maxima over all angles, exact small-deficit limits, or untested symbols.

**Scientific limits.** There is no independent audit. The phase and higher coefficients cannot be reconstructed from this theorem. Publication priority against all older equivalent terminology is not certified.
