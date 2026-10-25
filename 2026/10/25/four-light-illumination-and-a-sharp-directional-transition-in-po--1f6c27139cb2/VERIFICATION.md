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

Run `python verify.py` with Python 3 in this directory. Only the standard-library `fractions` and `itertools` modules are needed.

The checker reconstructs all twelve exact supporting planes at nine rational parameters strictly between one and three. At every tested parameter, it certifies three contacts per plane, strict inequality at every other generating point, and positive signs consistent with vertex illumination. It computes the four explicit algebraic directions, checks their coverage of all eight vertices and their exact incident facets, and verifies the reciprocal-geometry endpoint algebra. It also samples 11,970 integer-profile candidates, separately marked as nonexhaustive; very close to the cube endpoint, tiny admissible cones need exact rational construction and cannot be discovered reliably from bounded grids.

The general proof does not depend on finite samples. Its decisive universal ingredients are the twelve-facet formula, the implication that at most one negative-orbit vertex can be illuminated, the strict symbolic four-direction covering, and the sign condition \((3s-1)T<0\) governing three positive-orbit illuminated vertices.

An independent external audit has not been performed. No formal theorem prover was used. The claim is restricted to the stated tetrahedral family and the finite-weight definition of fractional illumination.
