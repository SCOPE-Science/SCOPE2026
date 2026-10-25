---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The actual RESULT.md argument factors the characteristic-function Fourier transform into radial Bessel factors and achieves the first real zero along the top left singular vector of a minimizing block. With D=diag(j_i I), T=rho A D^{-1}, each block operator norm is <=1, so Hadamard gives |det T|<=1 and equality exactly T orthogonal, with no omitted skew or mixed block. The positive-definite Gram matrix G=T^T T has tr G<=d; the scalar inequality (sqrt(lambda)-1)^2 <=lambda-1-log lambda yields min_U ||T-U||_F^2 <= -log det G=2delta, and an explicit two-block epsilon shear has squared gap and deficit both epsilon^2/2+O(epsilon^4), proving the sharp 1/2 exponent. Stirling and j_{q/2,1}=(q/2)(1+O(q^{-2/3})) prove the fixed-m entropy limit. Independent 100 random full-rank matrices satisfy the inequality with separately computed Bessel zeros, determinant and polar factor. These finite tests corroborate, not replace, the general inequalities.

## originality

PASS

Benguria--Levitin--Parnovski 2009 Example 3.5 contains the exact individual-ball Bessel zero and Example 3.6 the cuboid special case, both credited; their main work does not state all affine products of higher-dimensional balls with sharp orthogonal equality and uniform Procrustes stability plus proportional-dimension entropy limit. Gómez-Serrano et al. 2026 disprove a global equal-volume ball optimizer in unrestricted convex bodies; no implication contradicts or covers this restricted sharp theorem. A general determinant inequality is used, but obtaining exact radius and rigidity in this class is an additional statement; best-of-knowledge only.

## value

PASS

The structured class of affine products of Euclidean balls includes skewed, anisotropic and mutually mixed blocks, and its exact normalized optimum/equality set and dimension-free distance-to-optimizer estimate supply a natural structural geometric extremum. The entropy deficit isolates a meaningful fixed-proportion high-dimensional loss. Though the cuboid endpoint and elementary Bessel steps are known, the mixed-block all-partition stability and entropy classification are not a bare recomputation of a known numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
