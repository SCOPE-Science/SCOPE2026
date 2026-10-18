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

# Reproduction and limits
Run `python verify.py` with Python 3 standard library. Expected line begins `VERIFY_OK`. The program checks the congruence exclusion for hyperelliptic Cartier coefficients for nine odd primes, the \(p+1\) order-\(p\) line subgroups and distinct-pair convolution for those primes, and representative trace point-count equalities over quadratic finite fields for five primes. Those are exact finite computations; they do not establish the theorem for infinitely many primes or parameters. The proof in RESULT.md proves the general assertion using ramification, quotient equations, correspondence vanishing, and the Ekedahl bound. No independent audit has been performed.
