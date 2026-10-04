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
The proof is symbolic and covers all nonempty finite \(T_0\)-spaces. The accompanying `verify.py` is a dependency-free finite stress test, not a substitute for the proof.

It constructs every labeled poset on one through four points, obtaining counts 1, 3, 19, and 219. It then checks the stated up-beat and down-beat equivalences for all pairs with both factors of size at most three, and for every four-point factor paired in both orders with every factor of size at most two. The replay covers 2,281 product pairs, performs 32,720 pointwise beat-characterization checks, and separately checks minimality equivalence for all 2,281 products.

A successful replay prints `VERIFY_OK`. The stored `verification_output.txt` records the expected successful output. The computation does not establish the general theorem by exhaustion; its role is to detect normalization mistakes and small boundary counterexamples to the symbolic argument.
