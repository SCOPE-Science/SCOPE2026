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

The analytic derivation is self-contained in `RESULT.md`: the monomial basis and weight identity give exact orthogonal columns, the gamma asymptotics and boundary-ray control justify the global maximization, and Perron–Frobenius estimates plus infinitely many weighted-shift chains give the Fredholm conclusions.

Run the standalone numerical diagnostic with `python3 CHECK.py`. It checks 3,203 finite test cases and prints `PASS: 3203 finite diagnostic checks; no infinite-proof certification.` The samples cover several positive nonsingular exponent matrices, multiple Bergman exponents and the Hardy endpoint, iterated weights and the Fibonacci matrix identity.

The script tests only finitely many columns and powers. It does not by itself prove asymptotic uniformity, Calkin equalities, or the full essential spectrum. Those statements require the analytic proof and standard Perron and weighted-shift results. Independent audit has not been performed.
