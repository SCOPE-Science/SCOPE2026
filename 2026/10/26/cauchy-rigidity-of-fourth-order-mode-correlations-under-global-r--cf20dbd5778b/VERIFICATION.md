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

The proof is analytic. Its essential steps are (1) exponential stationary age for a common Poisson reset; (2) conditionally independent centered Gaussian modes; (3) the Laplace transform of each conditional variance; (4) the Cauchy determinant identity; (5) the explicit positive-parameter inverse construction. These steps apply to every finite number of real nonzero modes, without sampling-based extrapolation.

Run `python3 verify.py` with the standard Python library. The provided `verify_output.txt` records exact-fraction matches for three chosen positive parameter sets, including repeated relaxation rates. The checker independently evaluates conditional variance products, single-mode fourth cumulants, cross-mode fourth cumulants, the inverse ratios, all square minors, and the determinant formula; it makes no claims about an infinite parameter enumeration. The embedded source paths are relative and self-contained.

Residual scientific limitations: no claim about independent audit, non-Poisson resetting, correlated forcing, nonlinear interfaces, or a uniform infinite-mode determinant. A general preexisting full-configuration renewal formula remains relevant to the literature-priority assessment.
