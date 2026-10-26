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

# Verification and reproducibility

Run `python verify.py` with Python 3 standard library. On the tested package the output was:

```text
POLYNOMIAL_IDENTITY_PASS 15 nonzero monomials
EVENT_EXACT_PROBABILITY_PASS 70 strata
EXHAUSTIVE_DIGRAPHS_PASS 20 strata
VERIFY_OK
```

The first check expands the algebraic identity for the three nontrivial reciprocal-pair/directed-cycle intersection classes as a three-variable integer polynomial. The second enumerates each possible directed cycle and reciprocal vertex pair and independently calculates the probability of their joint requirements using uniform-subset combinatorics over all rows for \(3\le n\le7\). The third enumerates entire directed graphs with a uniform \(k\)-subset in each row for \(3\le n\le5\), then computes all admissible mixed covariances by independent count accumulation. All calculations use integers or exact rational numbers.

No finite enumeration is invoked as an infinite proof. The theorem in `RESULT.md` supplies a complete analytic event classification, factorial count, polynomial simplification, strict sign argument and limiting calculations. The scope excludes independently prescribed indegrees and with-replacement models.
