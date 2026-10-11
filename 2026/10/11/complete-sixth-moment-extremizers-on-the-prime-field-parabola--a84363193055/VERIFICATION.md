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

# Verification of complete prime-field parabola sixth-moment extremizers

The general proof is contained in `RESULT.md`; `checker.py` is a standalone Python 3 exact-integer reproducibility check (standard library only). Run with `python3 checker.py`. No third-party data files or network access are required.

The checker enumerates all ordered triple fibers for primes \(5,7,11,13,17,19,23\), verifies \(\sum_{s,r}R_{s,r}^2=p^4+p^3-p^2\), checks the translated equal-sum/equal-square triple identity, and establishes constant fiber products for each of the \(p^2\) candidate quadratic phases. It additionally finds a fiber inconsistency for a genuinely cubic phase in each tested prime. The intended final output is `EXACT_CHECKS_PASS` with the actual tally printed in the preceding line.

The *general* constant-modulus premise is verified from the published Theorem 1.3 and proof §6 of arXiv:2405.16647. The new phase proof uses an exact identity, telescoping over the cyclic field, and elementary root counting; no infinite-domain conclusion is based on finite enumeration. The projective optimizer count is valid only for prime \(p\ge5\). There is no independent audit or external formal certification.
