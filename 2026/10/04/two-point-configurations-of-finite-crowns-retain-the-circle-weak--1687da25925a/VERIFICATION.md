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
The universal theorem is verified by a symbolic proof: each inverse image of a minimal open set under the first projection is contractible by an explicit beat-point reduction, so McCord's theorem applies.

The included `verify.py` is an independent finite stress test for \(2\le n\le12\). It reconstructs the order relation, the deleted product, all projection fibers, and their beat-point cores. It also computes the order-complex mod-two Betti vector. A successful replay prints `VERIFY_OK` followed by one line for each tested \(n\).

The computation does not certify the universal quantifier by enumeration; the proof in `RESULT.md` does. No claim is made beyond ordered two-point configurations of finite crowns.
