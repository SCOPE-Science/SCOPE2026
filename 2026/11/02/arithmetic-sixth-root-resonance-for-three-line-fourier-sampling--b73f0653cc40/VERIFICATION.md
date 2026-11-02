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

# Verification evidence

The all-prime-power proof decomposes the (three-line)-indexed Fourier operator into a four-dimensional constant sector and three-dimensional multiplicative-character sectors. Direct elimination proves the constant sector nonsingular. In nontrivial sectors the character Gauss factor is nonzero with squared modulus equal to the field order, so rank is governed by an explicit three-by-three matrix with a two-by-two identity leading block. Its determinant is zero exactly at the claimed odd-characteristic isotropic obstruction or at the unit-circle equation that forces two conjugate sixth-root character prescriptions. Characters of the generated subgroup have exactly the stated number of extensions. These deductions are algebraic and do not rely on machine experiments.

The standalone `three_line_rank_checker.py` requires Python and NumPy. Run `python three_line_rank_checker.py` to construct every principal Fourier matrix for nonzero slopes over 17 finite fields, compare numerical singular values to the exact discrete-log congruence nullity formula, and assert equality. The recorded execution passed 232 slope tests, including 36 singular cases and fields of characteristics 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 and 31. The script explicitly defines extension fields of degrees 2, 3 and 4; numerical tolerance is relative to the largest singular value. Finite numeric ranks corroborate but do not prove the universal result.

The scientific scope is the normalized three-line set with standard dot product. Originality review inspected finite-field spectral/tiling papers and cyclic principal-minor theory; possible older equivalent results remain a risk. Independent validation has not been performed.
