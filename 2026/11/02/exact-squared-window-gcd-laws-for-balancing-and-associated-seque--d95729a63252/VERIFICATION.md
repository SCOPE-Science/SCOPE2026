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

# Reproducible checks

Run `python3 verification/verify.py` using Python 3 and no third-party dependencies. The checker constructs all three coefficient-six recurrences and Pell recurrences from their initial terms and performs exact integer comparisons of 384 direct square-window gcds and 15,744 exact window identities. It also verifies 128 instances of each Pell representation and balancing doubling/tripling identity, plus 520 Pell difference identities.

Finite checks alone cannot prove formulas for arbitrarily large indices. The proof in `RESULT.md` reduces infinite gcds to two-integer computations and checks the relevant prime valuations. The gcd input indexes and all symbolic normalizations are defined there. Independent audit: not performed.
