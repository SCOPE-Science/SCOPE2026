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

The included `verify.py` uses standard-library integer arithmetic only. It was executed from the actual saved source directory and returned `VERIFY_OK`. Two different exhaustive implementations agree on all six factor-product triples. The product-first algorithm examines all 231 possible odd products of binary weight three under the bound \(2^{23}\) and 5473 admissible trial divisors. The factor-first algorithm evaluates all 3672 unordered odd three-bit factor pairs whose product lies under the same bound. It asserts the exact witnesses and sharp maximum product of 1029.

The finite certificate requires the separately established theorem of Kaneko and Stoll (arXiv:2112.03077v1, Theorem 2.2) to reduce the unbounded integer problem to products below \(2^{23}\). This verification does not independently prove that published theorem, establish novelty, or constitute an independent audit.
