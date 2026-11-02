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

Run `python verify_bad_wiman.py`. The program uses only the Python standard library and evaluates exact integral polynomial coefficients before reducing them. It verifies all three factorization identities, computes the quadratic tangent cone and its nonsquare discriminant at a characteristic-five node, verifies that the four intrinsic marked points form projective frames in characteristics three and five, enumerates rational points of the original homogeneous sextic over \(\mathbb F_2,\mathbb F_4,\mathbb F_3,\mathbb F_9,\mathbb F_5,\mathbb F_{25}\), and enumerates the ten rational singular support points in characteristics three and five. The observed point counts are, in that order, \(7,13,10,40,10,22\).

The expected final program output is `WIMAN_BAD_PRIME_EXACT_CHECKS_PASS`, which was obtained on the packaged program. The algebraic argument in `RESULT.md` proves the point-count identities for every positive extension degree. Finite point enumeration by itself cannot prove that infinite assertion. The program does not purport to independently certify geometric irreducibility or completeness of the classification over algebraic closures; these are proved from the derivative equations, Bézout's theorem, and the genus calculation.

No independent audit has been conducted.
