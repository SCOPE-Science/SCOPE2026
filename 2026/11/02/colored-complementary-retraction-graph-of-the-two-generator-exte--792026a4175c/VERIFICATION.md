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

The standalone `verify_exterior.py` enumerates all unital algebra endomorphisms by mapping generators into the augmentation ideal and uses the exterior product to compute composite maps. It does not generate the idempotents or commuting graph from the target formula. The following full enumerations passed:

- \(q=2\): 64 endomorphisms, 14 idempotents, 3 components, 12 maximal families, 88 commuting ordered pairs.
- \(q=3\): 729 endomorphisms, 38 idempotents, 6 components, 54 maximal families, 292 commuting ordered pairs.
- \(q=4\): 4096 endomorphisms, 82 idempotents, 10 components, 160 maximal families, 724 commuting ordered pairs.
- \(q=5\): 15625 endomorphisms, 152 idempotents, 15 components, 375 maximal families, 1504 commuting ordered pairs.
- \(q=8\): 262144 endomorphisms, 578 idempotents, 36 components, 2304 maximal families, 7492 commuting ordered pairs.

Program completion: `VERIFY_OK exterior retraction commutation census`.

The proof of the general theorem is written in `RESULT.md`. The finite enumeration is corroborative and does not independently establish the result at untested prime powers. The program uses explicit binary polynomials to implement the two non-prime fields; their multiplication tables are checked by field assertions. The review is self-review only; no independent mathematical audit has been performed.
