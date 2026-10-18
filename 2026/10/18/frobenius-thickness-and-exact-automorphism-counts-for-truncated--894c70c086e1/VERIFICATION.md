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

# Verification scope

Run `python3 verify.py` using Python 3 and no external packages. The checker constructs truncated polynomial multiplication independently and, for each candidate tuple of images, tests the exact nilpotency relations and the induced full-dimensional substitution matrix rank. Its five exhaustive prime-field checks yield respectively 1, 4, 6, 24, and 2048 automorphisms, agreeing with the formula. A further surviving-monomial test checks the three-generator exponent pattern \((1,1,2)\) in characteristic two. Expected terminator: `VERIFY_OK`.

The algebraic proof in RESULT.md covers all primes, arbitrary positive exponent tuples and coefficient fields. Enumeration covers only the listed finite cases; no claim of universal exhaustive computation or independent third-party review is made. The scheme factorization is as schemes, not generally as group objects.
