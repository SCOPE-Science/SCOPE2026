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

# Verification and limits

The standalone `verify.py` runs with Python 3 and no third-party modules. It contains all 57 defining linear forms as exact integer coefficient pairs in \(\mathbb Z[\epsilon]\), performs exhaustive arithmetic on 1,596 pairs and 29,260 triples, and tests both embeddings at each of the three exceptional odd primes. Replaying the actual packaged file must return `VERIFY_OK`.

The proof that no other primes at least five are exceptional follows from exhaustive norm factorization of *all nonzero* triple determinants, not finite sampling. Rational-point counts over every good prime follow from the proved fixed-point counts for conjugation combined with the quadratic-field splitting rule; checks at primes five, eleven, seventeen, twenty-three, and thirty-one are useful independent arithmetic spot checks but do not replace that deduction. The characteristic-seven Moore identity follows from the exact equality of all 57 reduced coefficient classes with the 57 elements of the dual finite plane.

Excluded characteristics: two and three. Other limitations: no claim about freeness in positive characteristic or about unspecified integral presentations. Independent audit: not performed.
