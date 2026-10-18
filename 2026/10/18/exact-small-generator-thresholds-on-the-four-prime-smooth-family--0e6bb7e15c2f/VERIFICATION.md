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

Run `python3 code/verify.py` under Python 3 (standard library only). The program constructs primitive-root discrete logarithm tables mod \(9,25,49\) using modular exponentiation and checks that each table has the expected full size. It computes all elementary-quotient rank certificates for the \(24\) corner exponent patterns and independently enumerates the subgroups generated below and at the proposed thresholds in the six arithmetic model moduli \(210,420,840,22050,44100,88200\). The output ends in `VERIFY_OK` and includes exact subgroup orders. Computations are deterministic and use only integer arithmetic.

The infinite assertion for arbitrary exponents is proven by the Frattini-kernel lifting argument in RESULT.md, not by extrapolating the finite checks. Literature comparison was based on a full accessible motivating paper and other relevant bibliographic/abstract material and searches; the Bach–Huelsbergen full text remained unavailable. An independent review and external mathematical validation have not been performed.
