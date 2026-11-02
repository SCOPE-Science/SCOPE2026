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

The proof uses unique greedy embeddings to establish the exact per-word two-deletion count, a conditional binomial distribution for three-distinct-letter events, stars-and-bars summation, and an orthogonal Bernoulli expansion for the moments.

Execute `python3 verify.py` from this directory to check all enumerators against actual deletion-output sets and rational moments for 27 parameter pairs. The successful result is `VERIFY_OK cases= 27`. Execute `python3 crosscheck.py` for a separately implemented canonical-embedding count and the successful result `CROSSCHECK_OK`.

Finite enumerations are consistency checks only. The all-length and all-alphabet claims rely on the written combinatorial proof. Historical-priority searches do not constitute independent verification.
