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

# Reproducibility and limits

Run `python3 checker.py` using Python 3 and its standard library. The standalone file checks exact-rational instances of the proposed spectral-gap optimum and its dual witness for integers \(1\le\ell\le k\le7\) and a set of rational \(q=\sqrt t\), including values on both sides of the predicted phase boundary. It verifies the exact Gram matrices, edge costs, centered geometry, rate budget, \(L_0G=G\), and eigenvalue-one multiplicity. Recorded local outcome: `VERIFY_OK 299 exact rational cases; 97 low-price and 202 high-price; Gram eigenrelations, budgets, ranks and Schur certificates`.

In the mathematical proof in `RESULT.md`, the low-price principal minor/interlacing step and high-price signed Schur complement establish the spectral-ordering fact for every positive real bridge price. The finite test suite is a consistency check, not a certificate of the universal quantifiers. The originality comparison is based on publicly inspectable primary text and expressly discloses inaccessible full-text sources. Independent audit has not been performed.
