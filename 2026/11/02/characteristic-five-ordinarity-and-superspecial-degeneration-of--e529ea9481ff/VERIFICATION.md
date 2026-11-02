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

# Mathematical verification

Run `python3 verify_hesse_sextic.py` with a standard Python 3 interpreter. It uses only the standard library. The file is a self-contained exact checker, not a symbolic proof oracle.

The checker (i) expands \(F_t^4\) by both multinomial coefficients and independent repeated convolution over \(\mathbb F_5[t]\), (ii) evaluates the exact Čech coefficient rule for the full ten-by-ten Frobenius matrix, (iii) matches every coefficient with the ten-entry formula from the proof, and (iv) exhaustively checks the twenty-five parameters over \(\mathbb F_{25}=\mathbb F_5[\omega]/(\omega^2-3)\), including projective singular points and ranks of several Frobenius-twisted products. The expected positive marker is `CHAR5_HESSE_SEXTIC_FULL_HASSE_10X10_F25_SMOOTHNESS_AND_STABLE_RANK_PASS`.

The universal smoothness implication is proved by solving the geometric gradient equations; it is not an inference from the twenty-five-parameter enumeration. Likewise, the stable-rank classification uses the exact monomial block decomposition, not only matrix ranks in finite fields. The elliptic quotient and ordinary complementary factor are deduced from the explicit tame covering and the compatible Frobenius-invariant cohomology splitting.

Limits: the verification does not establish full Newton polygons or all automorphism groups, and it does not constitute independent external audit.
