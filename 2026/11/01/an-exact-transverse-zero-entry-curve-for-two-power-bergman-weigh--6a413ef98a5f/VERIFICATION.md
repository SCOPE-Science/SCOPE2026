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

# Verification and reproducibility

The proof is analytic. The exact beta-function moments identify the scalar kernel, Euler's hypergeometric transformation produces a uniformly continuous zero-preserving numerator on the closed unit disk, and a polynomial root census at the critical parameter point allows Rouché's theorem to control *all* nearby zeros. The nonzero derivative with respect to the boundary exponent invokes the real analytic implicit-function theorem. The exact derivative coefficient follows from elementary integrals and sums; no numerical root search is used to establish existence, uniqueness or the zero counts.

Run `python CHECKER.py` using the dependencies named in `REQUIREMENTS.txt`. The checker verifies the base kernel numerator, all five root moduli, the two parameter derivatives, the radial crossing derivatives, and the exact tangent as symbolic identities. Separately, it checks a hypergeometric-versus-integral identity at three complex points, solves for unit-circle crossings at two nearby fractional origin exponents, and checks root-entry directions on both sides. These are finite reproducibility checks, not an infinite-dimensional proof or independent external certification.

The scalar zero count does not count pairs of points in the disk, and the quantitative radius of the permitted parameter neighborhood is not supplied. Nothing here establishes historical originality exhaustively. Independent mathematical audit has not been performed.
