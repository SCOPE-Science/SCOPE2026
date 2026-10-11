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
# Verification

The proof certificate is `glp_octagon_verify.py`. It uses exact arithmetic in \(\mathbb Q(\sqrt2)\) implemented from Python's rational `Fraction` type.

A successful replay prints `VERIFY_OK` and the following structural counts: 48 feasible ordered edge-family intervals, 128 endpoint/support-breakpoint checks, and five distinct ordered shifted-norm pairs. It asserts that the maximum of each shifted norm is exactly \(2\sqrt2-1\), verifies the explicit equality pair, and asserts the exact five-pair set.

The finite computation is exhaustive because every point of the octagonal unit sphere lies on one of eight edges. For each ordered triple of edges containing \(x\), \(y\), and \(x-y\), the equilateral constraint is an affine system whose feasible portion is a closed interval. Along that interval the shifted vectors are affine and the octagonal norm is the maximum of eight affine support functionals. Thus the maxima relevant to the coordinatewise bound occur at interval endpoints; the additional support-change checks are redundant for the bound but provide an exact internal cross-check of the piecewise structure.

No floating-point approximation, random sampling, timeout inference, or unproved extrapolation is used in the certified inequalities. The verification does not address exponents \(p<1\), complex scalars, or other norms.
