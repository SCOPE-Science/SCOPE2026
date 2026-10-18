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

# Reproduction and verification

Run `python check.py` with a current Python 3 interpreter. The checker uses only the standard library; it implements its own field tables for the prime fields of orders three and five and the quadratic extension field of order nine. It independently evaluates square-zero equations and summand ranks by finite-field matrix arithmetic, and compares the complete observed rank spectra with the closed formula.

The ten fixed checks include the characteristic-three split hyperbolic and anisotropic zero-target cases, the nonzero paired-eigenspace obstruction, a mixed eigenvalue target, two four-dimensional orthogonal types, and cases over fields of orders five and nine. All ten cases returned matching full rank distributions. A supplementary exhaustive script checked all 258 diagonal symmetric-form and diagonal-target combinations in dimensions at most three over the field of order three. For the four-dimensional split form over the ternary field, the zero target has rank counts \(1,32,144\) and the mixed target with eigenvalues \(1,-1,0,0\) has rank counts \(2,8\) in ranks one and two.

These checks enumerate only bounded test families. The all-dimension statement rests on the operator normal form, anti-isometry correspondence, isotropic-flag count, and orthogonal-group orders proven in `RESULT.md`. Independent external audit has not been performed.
