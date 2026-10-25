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

# Reproducibility

`python3 verify_joint_protection.py` runs the exact finite certificate (Python 3.9+; standard library only). Its emitted canonical sorted-key JSON must equal `certificate.json` byte-for-byte. The enumeration covers all nonempty plant neighborhood multisets at each guild-size pair with at most nine total species. Breadth-first search retains only connected bipartite graphs, without quotienting pollinator labels. Each protection candidate is scored by exact integer counts of successful surviving subsets; every connected graph has a coefficientwise winner.

The checker reports 64,820 connected row-multiset representatives with zero exceptions, derives the ten-species witness coefficients, verifies coefficient differences symbolically through integer entries, and sums exact rational probabilities over all unprotected survival states at three independently chosen sample probabilities.

The *general* conclusion for real survival probabilities follows from nonnegative Bernstein weights for the coefficientwise part and exact factorization for the witness, not finite simulation. The code does not certify all ten-species networks, and the scientific review is not independent validation.
