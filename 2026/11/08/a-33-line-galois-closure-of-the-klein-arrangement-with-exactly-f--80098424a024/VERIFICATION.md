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

Run `python3 verify.py` with Python 3 standard library. The verifier constructs the 21 line vectors in the quadratic integer ring, adjoins their Galois conjugates to obtain 33 projective lines, checks every \(\binom{33}{2}=528\) pair and \(\binom{33}{3}=5456\) triple, and confirms that every determinant norm and pair-minor norm gcd has prime support in \(\{2,3,7,11\}\). It then computes the generic intersection-class partition and the complete exceptional profiles at characteristics 2, 3, 7, and 11. The output includes `VERIFY_KLEIN_GALOIS_CLOSURE_OK`.

Exact arithmetic certificates plus the algebraic-norm invertibility lemma prove the all-good-characteristics assertion; enumerations of only finitely many fields would not suffice. The verifier does not establish any unclaimed higher-dimensional, representation-theoretic, rational-point-count, or symbolic-power assertion. Independent audit status: not performed.
