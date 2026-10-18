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

# Verification summary

Execute `python3 CHECK.py` with Python 3 and its standard library only. The checker enumerates exact rational outer and polar contact orbits for multiple cutoff parameters in dimensions two through seven, checks signed-permutation isotropic covariance, inverts exact nonscalar positive-definite matrices by rational Gaussian elimination, and verifies both supporting trace bounds. It checks sample branch monotonicity across cutoff breakpoints for dimensions two through 119 and the regular-octagon planar identity. The expected final line begins `VERIFY_OK`.

The executable check is supplementary. The infinite-dimensional-family claims follow from (i) the exact fractional-coordinate optimizer for the squared Euclidean radius, (ii) the normalized distances to the defining facets, (iii) signed-permutation orbit covariance identities, (iv) the exact positive-definite-matrix variational formula for Euclidean Banach–Mazur distance, and (v) a piecewise derivative sign with boundary continuity. The order-\(d^{1/4}\) asymptotic is a binomial expansion of the exact minimum.

Computations cannot establish absence of an older equivalent published theorem. The uniqueness of the optimal ellipsoidal shape concerns centered symmetric-norm embeddings; arbitrary affine translations can be removed for these origin-symmetric bodies.
