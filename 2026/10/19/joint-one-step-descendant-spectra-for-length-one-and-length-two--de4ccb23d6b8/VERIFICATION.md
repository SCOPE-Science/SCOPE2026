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

Run `python3 verify.py` with a standard Python 3 interpreter. The checker independently forms output sets by performing every legal tandem duplication of length one and length two, reducing those output lists to sets. It also counts all words by the transition-polynomial recurrence, tests binomial margins, zero covariance, exact conditional means by integer cross-products, sharp maximum values, and extremizer counts.

Test domain: labeled alphabets of sizes \(2,3,4,5\); respective inclusive upper source lengths \(12,8,6,5\), lower length \(2\); total 27381 source words. Expected stdout is `MIXED_TANDEM_SPHERE_PASS words=27381 q=2..5 n_max=(12,8,6,5) exhaustive=true`.

The proof in RESULT.md, not finite data, establishes the unlimited parameter claims. The verifier uses no external packages and does not access the network. Independent audit has not been performed.
