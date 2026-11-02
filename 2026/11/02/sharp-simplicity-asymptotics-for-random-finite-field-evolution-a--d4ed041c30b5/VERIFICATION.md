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

# Verification scope

The standalone file `verify.py` runs using Python 3 and its standard library. It evaluates five complete small-field matrix spaces, keeps exactly the invertible matrices, checks strong connectivity by both closed-subset search and directed reachability, and verifies exact block-cut counts for every nontrivial coordinate subset. It checks the nonasymptotic error bound for dimensions at least three. The verified cases are \((n,q)=(2,2),(2,3),(3,2),(3,3),(4,2)\), with respective simple-matrix counts \(3,28,80,7504,11658\). The verifier terminates with `VERIFY_OK`.

The all-dimensional theorem is proved symbolically in `RESULT.md`. Finite enumeration is not a proof over all prime powers, dimensions, or extension fields. The error term is for fixed finite-field size. Source priority is not independently certified.
